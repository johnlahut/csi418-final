from django.shortcuts import render
from django.http import HttpResponse

from .forms import MakeMultipleChoiceQuestionForm, MakeTrueFalseQuestionForm

# Create your views here.

def make_mulitple_choice_question_view(request):
    form = MakeMultipleChoiceQuestionForm()
    return render(request, 'make_multiple_choice_question.html', {'form': form})

def make_true_false_question_view(request):
    form = MakeTrueFalseQuestionForm()
    return render(request, 'make_true_false_question.html', {'form': form})

def make_home_view(request):
    return render(request, 'make_home.html')