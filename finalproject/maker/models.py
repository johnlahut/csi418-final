# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class QuestionCategory(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class QuestionModel(models.Model):

    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=256)
    answer = models.IntegerField()
    answer_text = models.CharField(max_length=256, default='')
    choice_1 = models.CharField(max_length=256, default='True')
    choice_2 = models.CharField(max_length=256, default='False')
    choice_3 = models.CharField(max_length=256, null=True, default=None)
    choice_4 = models.CharField(max_length=256, null=True, default=None)
    choice_5 = models.CharField(max_length=256, null=True, default=None)
    choice_6 = models.CharField(max_length=256, null=True, default=None)
    image = models.ImageField(default=None)
    category = models.ForeignKey(QuestionCategory, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class TestModel(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ManyToManyField(QuestionModel)
    createdDate = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=256, default=None)

    def __str__(self):
        return self.name

class GradedQuestionModel(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    correct = models.BooleanField()


class GradedTestModel(models.Model):
    id = models.AutoField(primary_key=True)
    test = models.ForeignKey(TestModel, default=1, on_delete=models.CASCADE)
    score = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.ManyToManyField(GradedQuestionModel)


