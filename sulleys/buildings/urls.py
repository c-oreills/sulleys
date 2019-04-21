from django.urls import path

from buildings import views

urlpatterns = [
    path('', views.BuildingList.as_view(), name='index'),
    path('<int:pk>/', views.BuildingDetail.as_view(), name='detail'),
]
