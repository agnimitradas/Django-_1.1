from django.contrib import admin
from .models import ChoiceModel,QuestionsModel


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question', {'fields': ['question_text']}),
        ('Date information', {'fields': ['created_date']}),
    ]
admin.site.register(QuestionsModel,QuestionAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Choice Text',{'fields':['choice_text']}),
        ('Choice For',{'fields':['question']}),
        ('Votes',{'fields':['votes']}),
    ]
admin.site.register(ChoiceModel,ChoiceAdmin)

