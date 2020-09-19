from django.urls import path
from . import views
urlpatterns = [
    path('feedback', views.feedback, name='feedbac')
]