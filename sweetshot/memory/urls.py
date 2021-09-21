from django.urls import path
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('memory/', views.MemoryList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)