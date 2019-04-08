from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from .forms import MakeMultipleChoiceQuestionForm, MakeTrueFalseQuestionForm, MakeTestForm
from .models import QuestionModel, Test

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


def delete_popup(request, id):

    q = QuestionModel.objects.get(id=id)

    return render(request, 'delete_popup.html', {'q': q})


def make_home_view(request):

    t = Test.objects.all()

    q = QuestionModel.objects.all()

    return render(request, 'make_home.html', context =  {'q': q, 't': t})


def multiple_choice_preview_view(request):

    return render(request, 'view_multiple_choice.html')


def make_test_view(request):

    if request.method == 'POST':
        form = MakeTestForm(request.POST)

        if form.is_valid():
            test = form.cleaned_data
            test.save()

    test = MakeTestForm()

    return render(request, 'make_test.html', {'form': test})
