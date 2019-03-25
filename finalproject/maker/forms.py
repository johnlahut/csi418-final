from django import forms
from . import models
class QuestionForm(forms.Form):
    title = forms.CharField(max_length=256)
    image = forms.ImageField()


class MakeMultipleChoiceQuestionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MakeMultipleChoiceQuestionForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False

    class Meta:
        model = models.QuestionModel
        fields = ['question', 'choice_1', 'choice_2', 'choice_3', 'choice_4', 'image', 'category']

    choices = (
        (1, 'Answer 1'),
        (2, 'Answer 2'),
        (3, 'Answer 3'),
        (4, 'Answer 4')
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