from django.urls import path
from .import views

urlpatterns = [
    path('', views.LibraryDetails.as_view()),
    
]