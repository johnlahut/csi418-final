from django.shortcuts import render

from .forms import MakeMultipleChoiceQuestionForm, MakeTrueFalseQuestionForm
from .models import QuestionModel

# Create your views here.

def make_mulitple_choice_question_view(request):

    if request.method == 'POST':
        form = MakeMultipleChoiceQuestionForm(request.POST)

        if form.is_valid():

            cd = form.cleaned_data
            question = form.save(commit=False)
            question.answer = int(cd['answer'])
            question.save()

    question = MakeMultipleChoiceQuestionForm()

    return render(request, 'make_multiple_choice_question.html', {'form': question})

def make_true_false_question_view(request):
    form = MakeTrueFalseQuestionForm()
    return render(request, 'make_true_false_question.html', {'form': form})

def make_home_view(request):

    q = QuestionModel.objects.all()
    return render(request, 'make_home.html', {'q': q})

def multiple_choice_preview_view(request):
    return render(request, 'view_multiple_choice.html')