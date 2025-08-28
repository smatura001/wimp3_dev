from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from agro.views import CommodityTypeViewSet

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("pest-risk-list/", views.pest_risk_list, name="pest_risk_list"), 
    path("pest-risk-entry/start/", views.pest_risk_entry_start_view, name="pest_risk_entry_start_view"), 
    path("pest-risk-entry/add/", views.pest_risk_entry_start_add_view, name="pest_risk_entry_start_add_view"), 
    path('pest-risk-entry/<int:entry_id>/', views.pest_risk_entry_details, name='pest_risk_entry_details'),
    path('pest-risk-entry/<int:entry_id>/add/', views.pest_risk_entry_add_details, name='pest_risk_entry_add_details'),
    
    #path("add-pest-risk-entry/add/", views.add_pest_risk_entry_add, name="add_pest_risk_entry_add"), 
    path("livestock-entry/", views.livestock_entry, name="livestock_entry"),
    path('admin/', admin.site.urls),
]