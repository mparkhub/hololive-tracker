from django.urls import path
from . import views

app_name = 'streams'

urlpatterns = [
    path('upcoming/', views.upcoming, name='upcoming')
]
