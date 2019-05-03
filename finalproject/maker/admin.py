from django.contrib import admin

# Register your models here.
from .models import QuestionCategory, QuestionModel, TestModel

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class MultipleChoiceAdmin(admin.ModelAdmin):

    list_display = ('question', 'answer', 'image', 'category')

class TestAdmin(admin.ModelAdmin):

    list_display = ('name', 'id',)


admin.site.register(QuestionCategory, QuestionAdmin)
admin.site.register(QuestionModel, MultipleChoiceAdmin)
admin.site.register(TestModel, TestAdmin)