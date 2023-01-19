from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuizCategory(models.Model):
    title=models.CharField(max_length=100)
    details=models.TextField()
    image=models.ImageField(upload_to="cate_image")
    
        
    def __str__(self):
        return self.title
class QuizQuestion(models.Model):
    category =models.ForeignKey(QuizCategory,on_delete=models.CASCADE)
    question=models.TextField()
    opt_1=models.CharField(max_length=100)
    opt_2=models.CharField(max_length=100)
    opt_3=models.CharField(max_length=100)
    opt_4=models.CharField(max_length=100)
    level=models.CharField(max_length=100)
    time_limit=models.IntegerField()
    right_opt=models.CharField(max_length=100)
 
    def __str__(self):
        return self.question
class UserSubmitAnswer(models.Model):
    question=models.ForeignKey(QuizQuestion,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    right_opt=models.CharField(max_length=100)
    
    