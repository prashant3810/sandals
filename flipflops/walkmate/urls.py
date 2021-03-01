from . import views
from django.urls import path

urlpatterns = [
    path('shoe/', views.shoes),
    ]
