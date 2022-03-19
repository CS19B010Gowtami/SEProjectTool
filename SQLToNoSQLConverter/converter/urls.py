from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.frontend, name='frontend'),
    # path('result/',views.result,name="result"),
]