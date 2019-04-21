from django.urls import path

from buildings import views

urlpatterns = [
    path('', views.BuildingList.as_view(), name='index'),
    path('tags/<str:tag>', views.BuildingListByTag.as_view(), name='list_by_tag'),
    path('<str:slug>/', views.BuildingDetail.as_view(), name='detail'),
]
