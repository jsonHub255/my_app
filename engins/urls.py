from django.urls import path
from . import views

app_name = 'engins'
urlpatterns = [
    path('', views.engin_list_view, name="engin_list_view"),
    path('<int:id>/', views.engin_single_view, name="engin_single_view"),
    path('create/', views.engin_create_view, name="engin_create_view"),
    path('update/<int:id>/', views.engin_update_view, name="engin_update_view"),
    path('delete/<int:id>', views.engin_del_view, name="engin_del_view"),
    path('drivers/', views.drivers_list_view, name="drivers_list_view"),
    path('drivers/create/', views.create_driver_view, name="create_driver_view"),
]
