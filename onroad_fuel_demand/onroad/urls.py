"""
URL configuration for onroad_fuel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home),
    path('login',views.login),
    path('admin_home',views.admin_home),
    path('admin_manage_fuel_type',views.admin_manage_fuel_type),
    path('update_fueltype/<fuel_type_id>',views.update_fueltype),
    path('delete_fuel_type/<fuel_type_id>',views.delete_fuel_type),
    path('admin_manage_vehicle',views.admin_manage_vehicle),
    path('update_vehicle/<vehicles_id>',views.update_vehicle),
    path('delete_vehicle/<vehicles_id>',views.delete_vehicle),
    path('admin_manage_drivers',views.admin_manage_drivers),
    path('update_driver/<login_id>',views.update_driver),
    path('delete_driver/<login_id>',views.delete_driver),
    path('admin_assign_vehicle/<driver_id>/<d_first_name>',views.admin_assign_vehicle),
    path('admin_view_users',views.admin_view_users),
    path('admin_view_rating_ad_riew',views.admin_view_rating_ad_riew),
    path('admin_view_booking',views.admin_view_booking),
    path('admin_view_payment',views.admin_view_payment),
    path('admin_view_complaints',views.admin_view_complaints),
    path('admin_view_report',views.viewreport),
    
    
    # -----------------------------------android start---------------------------------------
   
    path('views/andro_login', views.andro_login, name='andro_login'),
    path('views/userregister', views.userregister, name='userregister'),
    path('views/user_view_nearest_vehicle', views.user_view_nearest_vehicle, name='user_view_nearest_vehicle'),
    path('views/user_send_complaints', views.user_send_complaints, name='user_send_complaints'),
    path('views/user_view_complaints', views.user_view_complaints, name='user_view_complaints'),
    path('views/user_view_request', views.user_view_request, name='user_view_request'),
    path('views/user_payment', views.user_payment, name='user_payment'),
    path('views/user_rate_fuel', views.user_rate_fuel, name='user_rate_fuel'),
    path('views/user_view_rated', views.user_view_rated, name='user_view_rated'),
    path('views/user_send_fuel_request', views.user_send_fuel_request, name='user_send_fuel_request'),
    path('views/viewspinner', views.viewspinner, name='viewspinner'),
    
    
    
    
    

    
    # -----------------------------drivermodule------------------------------------------------------------------
    path('views/driver_view_assigned_vehicle', views.driver_view_assigned_vehicle, name='driver_view_assigned_vehicle'),
    path('views/driver_update_stock', views.driver_update_stock, name='driver_update_stock'),
    path('views/driver_view_stock', views.driver_view_stock, name='driver_view_stock'),
    path('views/driver_view_request', views.driver_view_request, name='driver_view_stock'),
    path('views/driver_accept_request', views.driver_accept_request, name='driver_view_stock'),
    path('views/driver_accept_payment', views.driver_accept_payment, name='driver_accept_payment'),
    path('views/driver_view_ratings', views.driver_view_ratings, name='driver_view_ratings'),
    path('views/updatepasslocation', views.updatepasslocation, name='driver_view_ratings'),
    
    
    
    
   
]
