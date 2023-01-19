from django.contrib import admin
from . import models

admin.site.register(models.QuizCategory)

class QuizQuestionAdmin(admin.ModelAdmin):
    list_display= ['question','level' ]
admin.site.register(models.QuizQuestion,QuizQuestionAdmin)


class UserSubmitAnswerAdmin(admin.ModelAdmin):
    list_display= ['id','question','user','right_opt' ]
admin.site.register(models.UserSubmitAnswer,UserSubmitAnswerAdmin)


# Register your models here.
# username admin
# password 123456
