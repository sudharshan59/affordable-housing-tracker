from django.urls import path
from . import views

app_name = 'housing'

urlpatterns = [
    path('', views.house_list, name='house_list'),
    path('house/<int:pk>/', views.house_detail, name='house_detail'),
    path('apply/<int:pk>/', views.apply_for_house, name='apply_for_house'),
    path('application/<int:applicant_id>/', views.application_status, name='application_status'),
]