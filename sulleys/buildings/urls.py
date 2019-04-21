from django.urls import path

from buildings import views

urlpatterns = [
    path('', views.BuildingList.as_view(), name='index'),
    path('<str:slug>/', views.BuildingDetail.as_view(), name='detail'),
]
