from django.urls import path
from .views import Home, Page1, Page2

urlpatterns = [
    path('', Home.as_view()),
    path('page1', Page1.as_view()),
    path('page2', Page2.as_view()),
]