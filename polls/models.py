import datetime
from django.db import models
from django.utils import timezone

#�e�t�B�[���h�ɂǂ̂悤�ȃf�[�^�^���L�������邩�������B

#Question�e�[�u��
class Question(models.Model):
    question_text = models.CharField(max_length=200) #char�^
    pub_date = models.DateTimeField('date published') #date�^

    #str(question)�ȂǂƌĂяo���ꂽ�Ƃ�
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#Choice�e�[�u��
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #�O���L�[
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) #Integer�^

    def __str__(self):
        return self.choice_text
