from django import forms


class MakeMultipleChoiceQuestionForm(forms.ModelForm):

    choices = (
        ('choice_1', 'Answer 1'),
        ('choice_2', 'Answer 2'),
        ('choice_3', 'Answer 3'),
        ('choice_4', 'Answer 4')
    )

    title = forms.CharField(max_length=256)
    questions = forms.ChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple)
    image = forms.ImageField()


class MakeTrueFalseQuestionForm(forms.Form):
    choices = (
        ('choice_1', 'False'),
        ('choice_2', 'True')
    )

    title = forms.CharField(max_length=256)
    questions = forms.ChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple)
    image = forms.ImageField()