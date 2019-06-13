import datetime
from django.db import models
from django.utils import timezone

#Question
class Question(models.Model):
    question_text = models.CharField(max_length=200) #char
    pub_date = models.DateTimeField('date published') #date

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)

#Choice
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #äOïîÉLÅ[
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) #Integer

    def __str__(self):
        return self.choice_text
