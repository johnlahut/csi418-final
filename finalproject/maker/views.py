from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from .forms import MakeMultipleChoiceQuestionForm, MakeTrueFalseQuestionForm
from .models import QuestionModel

# Create your views here.

def make_mulitple_choice_question_view(request, id=None):

    if request.method == 'POST':
        form = MakeMultipleChoiceQuestionForm(request.POST)

        if form.is_valid():

            cd = form.cleaned_data
            question = form.save(commit=False)
            question.answer = int(cd['answer'])
            question.save()

            return HttpResponseRedirect(reverse('maker:home'))

    else:
        form = MakeMultipleChoiceQuestionForm()

        # trying to look up a specific question
        if id is not None:
            question = QuestionModel.objects.get(id=id)
            form.fields['question'].initial = question.question
            form.fields['choice_1'].initial = question.choice_1
            form.fields['choice_2'].initial = question.choice_2
            form.fields['choice_3'].initial = question.choice_3
            form.fields['choice_4'].initial = question.choice_4
            form.fields['choice_5'].initial = question.choice_5
            form.fields['choice_6'].initial = question.choice_6



    return render(request, 'make_multiple_choice_question.html', {'form': form})

def make_true_false_question_view(request, id=None):

    if request.method == 'POST':
        form = MakeTrueFalseQuestionForm(request.POST)

        if form.is_valid():

            cd = form.cleaned_data
            question = form.save(commit=False)
            question.answer = int(cd['answer'])
            question.save()

            return HttpResponseRedirect(reverse('maker:home'))

    else:
        form = MakeTrueFalseQuestionForm()

        if id is not None:
            question = QuestionModel.objects.get(id=id)
            form.fields['question'].initial = question.question


    return render(request, 'make_true_false_question.html', {'form': form})

def delete_question(request, id):

    q = QuestionModel.objects.get(id=id)
    q.delete()
    return HttpResponseRedirect(reverse('maker:home'))

def make_home_view(request):

    q = QuestionModel.objects.all()
    return render(request, 'make_home.html', {'q': q})

def multiple_choice_preview_view(request):
    return render(request, 'view_multiple_choice.html')