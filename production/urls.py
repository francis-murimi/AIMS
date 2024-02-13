from django.urls import path
from . import views
#from .farm_dash import app as FarmDash

urlpatterns = [
    path('farming-journey/create/', views.farming_journey_create_update, name='farming_journey_create'),
    path('farming-journey/update/<int:farming_journey_id>/', views.farming_journey_create_update, name='farming_journey_update'),
    path('farming-journey/list/', views.farming_journey_list, name='farming_journey_list'),
    path('farming-journey/detail/<int:farming_journey_id>/', views.farming_journey_detail, name='farming_journey_detail'),
    #path('farm/dash/', views.farm_dashboard, name='farm_dashboard'),
]
