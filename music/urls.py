from django.urls import path
from .import views

urlpatterns = [
    path('', views.LibraryList.as_view()),
    path('<int:pk>/',views.LibraryDetails.as_view()),
    
]