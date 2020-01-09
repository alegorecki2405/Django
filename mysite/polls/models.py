from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date_published')
    def __str__(self):
        return self.question_text
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
