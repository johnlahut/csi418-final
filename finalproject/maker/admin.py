from django.contrib import admin

# Register your models here.
from .models import QuestionCategory, QuestionModel

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class MultipleChoiceAdmin(admin.ModelAdmin):

    list_display = ('question', 'answer', 'image', 'category')

admin.site.register(QuestionCategory, QuestionAdmin)
admin.site.register(QuestionModel, MultipleChoiceAdmin)