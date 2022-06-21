from django.urls import path
from cleebweb_app import views

urlpatterns = [
    path('', views.testv, name='a'),
    path('legion/', views.region_list, name='list'),
    path('legion/add', views.add, name='add'),
    path('legion/del', views.delete, name='delete'),
    path('', views.region_list, name='home'),
]
