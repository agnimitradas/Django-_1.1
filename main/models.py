from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import datetime


class QuestionsModel(models.Model):
    question_text = models.CharField("Question Asked",max_length=200)
    created_date = models.DateField("Creation Date",auto_now=False)

    def was_published_recently(self):
        print("TimeZone Now")
        print(timezone.now())
        print(self.created_date)
        return self.created_date > timezone.now()

    def __str__(self):
        return self.question_text


class ChoiceModel(models.Model):
    question = models.ForeignKey(QuestionsModel, on_delete=models.CASCADE)
    choice_text = models.CharField("Options / Choice",max_length=200)
    votes = models.IntegerField("Total Votes",default=0,help_text="Total Votes")

    def __str__(self):
        return self.choice_text

