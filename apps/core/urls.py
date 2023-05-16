from . import views
from django.urls import path

urlpatterns = [
    path('', views.DashboardIndex.as_view(), name='dashboard'),
]
