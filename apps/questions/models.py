from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Choice(models.Model):

    choice = models.CharField(max_length=200)
    question = models.ForeignKey(
        'questions.Question',
        on_delete=models.CASCADE,
    )
    is_correct = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        exist_true = Choice.objects.filter(
            question=self.question,
            is_correct=True).exists()
        if exist_true:
            correct = Choice.objects.get(
                question=self.question,
                is_correct=True)
            if self.is_correct and self.id != correct.id:
                raise ValidationError('Already exist a correct choice for this question')
        super(Choice, self).save(*args, **kwargs)

class Question(models.Model):

    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question

    def exist_correct_response(self):
        choices = Choice.objects.filter(
            question=self.id,
            is_correct=True)
        return choices.count() > 0

class Response(models.Model):

    choices = models.ForeignKey(
        Choice,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return 'User: {} choice:{}'.format(self.user.username, self.choices.id)

    class Meta:
        unique_together = ('choices', 'user')
