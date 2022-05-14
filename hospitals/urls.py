from django.urls import path
from . import views
urlpatterns = [
    path('<int:hospital_id>/', views.hospital, name='hospital'),
    path('all/', views.hospitals, name='hospitals'),
]
