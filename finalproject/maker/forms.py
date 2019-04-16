from django import forms
from . import models


class QuestionForm(forms.Form):

    title = forms.CharField(max_length=256)
    image = forms.ImageField()


class MakeMultipleChoiceQuestionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MakeMultipleChoiceQuestionForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
        self.fields['choice_1'].initial = ''
        self.fields['choice_2'].initial = ''
        self.fields['choice_5'].required = False
        self.fields['choice_6'].required = False

    class Meta:
        model = models.QuestionModel
        fields = ['question', 'choice_1', 'choice_2', 'choice_3', 'choice_4', 'choice_5', 'choice_6', 'image', 'category']

    choices = (
        (1, 'Answer 1'),
        (2, 'Answer 2'),
        (3, 'Answer 3'),
        (4, 'Answer 4'),
        (5, 'Answer 5'),
        (6, 'Answer 6')
    )

    answer = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)


class MakeTrueFalseQuestionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MakeTrueFalseQuestionForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False

    class Meta:
        model = models.QuestionModel
        fields = ['question', 'image', 'category']

    choices = (
        (1, 'True'),
        (2, 'False')
    )

    answer = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)


class MakeTestForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MakeTestForm, self).__init__(*args, **kwargs)

    class Meta:
        model = models.Test
        fields = ['question']




