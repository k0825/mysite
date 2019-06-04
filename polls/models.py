import datetime
from django.db import models
from django.utils import timezone

#各フィールドにどのようなデータ型を記憶させるかを書く。

#Questionテーブル
class Question(models.Model):
    question_text = models.CharField(max_length=200) #char型
    pub_date = models.DateTimeField('date published') #date型

    #str(question)などと呼び出されたとき
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#Choiceテーブル
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #外部キー
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) #Integer型

    def __str__(self):
        return self.choice_text
