from django.urls import path
from newapp.views import index, details, create

urlpatterns = [
    path('', index),
    path('create/', create),
    path('<int:id>/', details)
]
k