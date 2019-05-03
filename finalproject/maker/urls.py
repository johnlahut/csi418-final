"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'maker'

urlpatterns = [
    path('', views.make_home_view, name='home'),
    path('mc/', views.make_mulitple_choice_question_view, name='multiple_choice'),
    path('mc/<int:id>/', views.make_mulitple_choice_question_view, name='multiple_choice_edit'),
    path('tf/', views.make_true_false_question_view, name='true_false'),
    path('tf/<int:id>/', views.make_true_false_question_view, name='true_false_edit'),
    path('preview/', views.multiple_choice_preview_view, name='multiple_choice_preview'),
    path('delete/<int:id>/', views.delete_question, name='delete_question'),
    path('test_maker/', views.make_test_view, name='test_maker'),
    path('get_question/<int:id>/', views.get_question, name='get_question'),
    path('make_test/', views.make_test, name='make_test'),
    path('upload/', views.upload, name='upload'),
    path('take_test_view/<int:id>/', views.take_test_view, name='take_test_view'),
    path('user_home/', views.user_home_view, name='user_home_view'),
    path('view_test/', views.view_test_view, name='view_test_view')
]
