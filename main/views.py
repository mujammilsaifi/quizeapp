from django.shortcuts import render
from . import forms
from . import models
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 

# Create your views here.
def home(request):
    return render(request,'home.html')

def Register(request): 
    mag=None
    form=forms.RegisterUser(request.POST) 
    if request.method=='POST':
        if form.is_valid():
            form.save() 
            mag='Form is successfully added'
    return render(request,'register.html',{'form':form,'mag':mag} )

def all_category(request):
    catData=models.QuizCategory.objects.all()
    return render(request,'all-category.html',{'data':catData})

# question fetch according to category
@login_required
def allQuestion(request,cat_id):
    category=models.QuizCategory.objects.get(id=cat_id)
    question=models.QuizQuestion.objects.filter(category=category).order_by('id').first()
    return render(request,'category-questions.html',{'question':question,'category':category})

@login_required
def submit_answer(request,cat_id,quest_id):
    if request.method=='POST':
        category=models.QuizCategory.objects.get(id=cat_id)
        question=models.QuizQuestion.objects.filter(category=category,id__gt=quest_id).exclude(id=quest_id).order_by('id').first()
        if 'skip' in request.POST:
                quest=models.QuizQuestion.objects.get(id=quest_id)
                user=request.user
                answer="Not submitted"
                models.UserSubmitAnswer.objects.create(user=user,question=quest,right_opt=answer)
                
        else:
            quest=models.QuizQuestion.objects.get(id=quest_id)
            user=request.user
            answer=request.POST['option']
            models.UserSubmitAnswer.objects.create(user=user,question=quest,right_opt=answer)
            
        if question :
            return render(request,'category-questions.html',{'question':question,'category':category})
        else:
            result=models.UserSubmitAnswer.objects.filter(user=request.user) # showing the result here
            skiped=models.UserSubmitAnswer.objects.filter(user=request.user,right_opt='Not submitted').count()
            attempt=models.UserSubmitAnswer.objects.filter(user=request.user).exclude(right_opt='Not submitted').count()
            rightans=0
            percentage=0
            for row in result:
                if row.question.right_opt == row.right_opt:
                    rightans+=1
            percentage=(rightans*100)/result.count()
            return render(request,'result.html',{'result':result,'skiped':skiped,'attempt':attempt,'rightans':rightans,'percentage':percentage}) 
    else:
        return HttpResponse("method not allowed!!")