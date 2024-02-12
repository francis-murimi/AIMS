from django.urls import path
from . import views
from .farm_dash import app as FarmDash

urlpatterns = [
    path('farm/create/', views.farm_create_update, name='farm_create'),
    path('farm/update/<int:farm_id>/', views.farm_create_update, name='farm_update'),
    path('farm/list/', views.farm_list, name='farm_list'),
    path('farm/detail/<int:farm_id>/', views.farm_detail, name='farm_detail'),
    path('farm/dash/', views.farm_dashboard, name='farm_dashboard'),
]
