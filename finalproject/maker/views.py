from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.core import serializers

from .forms import MakeMultipleChoiceQuestionForm, MakeTrueFalseQuestionForm, MakeTestForm
from .models import QuestionModel, QuestionCategory, Test

import json

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

    q = QuestionModel.objects.all()


    return render(request, 'make_test.html', {'q': q})

@require_GET
def get_question(request, id):
    # serialize requires iterator even though get returns a single object always
    # serializer returns an array but we always will return a single question, so return dict instead
    q = json.loads(serializers.serialize('json', [QuestionModel.objects.get(id=id)]))[0]

    # look up category to return as string, and return all the fields of the model
    q['fields']['category'] = QuestionCategory.objects.get(id=q['fields']['category']).name
    q['fields']['id'] = q['pk']
    return JsonResponse(q['fields'])

@require_POST
def make_test(request):

    q_ids = json.loads(request.POST.get('questions'))
    name = request.POST.get('name')

    questions = QuestionModel.objects.filter(id__in=q_ids)

    # error says ID is not getting set, but it saves into the DB with a value
    # and auto populate is set to true on id

    test = Test(name=name)
    test.save()
    test.question.set(questions)
    test.save()

    return HttpResponse('Success')
