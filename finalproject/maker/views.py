from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import render, reverse
from django.core import serializers
from io import StringIO

from .forms import MakeMultipleChoiceQuestionForm, MakeTrueFalseQuestionForm, UploadForm
from .models import QuestionModel, QuestionCategory, TestModel

import json
import csv
# Create your views here.


def make_mulitple_choice_question_view(request, id=None):

    if request.method == 'POST':

        # check to see if we are editing an existing model
        if id:
            form = MakeMultipleChoiceQuestionForm(request.POST, instance=QuestionModel.objects.get(id=id))

        # new
        else:
            form = MakeMultipleChoiceQuestionForm(request.POST)

        if form.is_valid():

            cd = form.cleaned_data
            question = form.save(commit=False)
            question.answer = int(cd['answer'])
            question.answer_text = cd[f'choice_{question.answer}']
            question.save()

            return HttpResponseRedirect(reverse('maker:home'))


    else:
        form = MakeMultipleChoiceQuestionForm()

        # render form with fields if editing a model
        if id is not None:
            question = QuestionModel.objects.get(id=id)
            form.fields['question'].initial = question.question
            form.fields['answer'].initial = question.answer
            form.fields['choice_1'].initial = question.choice_1
            form.fields['choice_2'].initial = question.choice_2
            form.fields['choice_3'].initial = question.choice_3
            form.fields['choice_4'].initial = question.choice_4
            form.fields['choice_5'].initial = question.choice_5
            form.fields['choice_6'].initial = question.choice_6
            form.fields['category'].initial = question.category_id

    if id: edit=True
    else: edit=False

    return render(request, 'make_multiple_choice_question.html', {'form': form, 'edit': edit})


def make_true_false_question_view(request, id=None):

    if request.method == 'POST':

        # check to see if we are editing an existing model
        if id:
            form = MakeTrueFalseQuestionForm(request.POST, instance=QuestionModel.objects.get(id=id))
        else:
            form = MakeTrueFalseQuestionForm(request.POST)

        if form.is_valid():

            cd = form.cleaned_data
            question = form.save(commit=False)
            question.answer = int(cd['answer'])
            if question.answer == 1:
                question.answer_text = 'True'
            else:
                question.answer_text = 'False'
            question.save()

            return HttpResponseRedirect(reverse('maker:home'))

    else:
        form = MakeTrueFalseQuestionForm()

        # edit an existing model
        if id is not None:
            question = QuestionModel.objects.get(id=id)
            form.fields['question'].initial = question.question
            form.fields['answer'].initial = question.answer

    if id: edit=True
    else: edit=False


    return render(request, 'make_true_false_question.html', {'form': form, 'edit': edit})


def delete_question(request, id):

    q = QuestionModel.objects.get(id=id)
    q.delete()
    return HttpResponseRedirect(reverse('maker:home'))


def delete_popup(request, id):

    q = QuestionModel.objects.get(id=id)

    return render(request, 'delete_popup.html', {'q': q})

def delete_test(request, id):

    t = TestModel.objects.get(id=id)
    t.delete()
    return HttpResponseRedirect(reverse('maker:home'))


def delete_test_popup(request, id):

    t = TestModel.objects.get(id=id)

    return render(request, 'delete_popup.html', {'t': t})


def make_home_view(request):

    t = TestModel.objects.all()
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

    # TODO: check for no questions sent in
    # JavaScript is sending in an array of question IDs and name of test
    q_ids = json.loads(request.POST.get('questions'))
    name = request.POST.get('name')

    # get questions user selected by ID
    questions = QuestionModel.objects.filter(id__in=q_ids)

    # create test model, save, associate questions, save  <-- needs to be done in this order, how Django works i guess
    test = TestModel(name=name)
    test.save()
    test.question.set(questions)
    test.save()

    # go back to create home
    return HttpResponse()


def upload(request):


    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():

            bad = []

            answer_map = {
                'A': 1,
                'B': 2,
                'C': 3,
                'D': 4
            }

            f = request.FILES['file'].read().decode('utf-8')
            reader = csv.reader(StringIO(f), delimiter=',')

            for row in reader:
                row = [s.strip() for s in row]

                if len(row) < 10 or len(row) > 11:
                    bad.append(row)
                    continue

                try:
                    answer = [index for index, string in enumerate(row) if '*' in string][0]
                except IndexError:
                    bad.append(row)
                    continue


                q = QuestionModel()

                q.question = row[1]
                q.choice_1 = row[3]
                q.choice_2 = row[5]
                q.choice_3 = row[7]
                q.choice_4 = row[9]
                q.image = row[10]

                row[answer] = row[answer].replace('*', '').upper()

                if row[answer].upper() in answer_map:
                    q.answer = answer_map[row[answer]]
                    q.answer_text = row[answer+1]
                else:
                    q.answer = int(row[answer])
                    q.answer_text = row[answer+1]


                q.save()
            return render(request, 'upload.html', {'form': form, 'bad': bad, 'finished': True})
        return render(request, 'upload.html', {'form': form, 'finished': False})
    else:
        form = UploadForm()
        return render(request, 'upload.html', {'form': form})


@require_GET
def edit_test_view(request, id):

    q = TestModel.objects.get(id=id).question.all()
    d = json.loads(serializers.serialize('json', q))
    return JsonResponse(d, safe=False)



