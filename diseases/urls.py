from django.urls import path
from . import views
urlpatterns = [
    path('<int:disease_id>/', views.disease, name='disease'),
    path('all/', views.diseases, name='diseases'),
]
