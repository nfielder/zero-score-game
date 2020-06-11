from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('quiz/<int:pk>/', views.QuizView.as_view(), name='quiz'),
    path('question/<int:pk>/', views.QuestionView.as_view(), name='question'),
    path('question/<int:question_id>/outcome', views.outcome, name='outcome'),
]
