from django.db import models

# Create your models here.
class Choice(models.Model):

    choice = models.CharField(max_length=200)
    question = models.ForeignKey(
        'questions.Question',
        on_delete=models.CASCADE,
    )
    is_correct = models.BooleanField(default=False)


class Question(models.Model):

    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question

    def exist_correct_response():
        pass
