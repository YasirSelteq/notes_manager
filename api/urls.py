from django.urls import path
from api import views

urlpatterns = [
    path('notes/', views.TaskApi.as_view()),
]
