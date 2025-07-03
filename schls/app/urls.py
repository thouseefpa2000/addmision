"""
URL configuration for clg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views
from django.urls import path,include


urlpatterns = [
    
    path('',views.home,name='home'),
    path('createcourse',views.createcourse,name='createcourse'),
    path('table',views.table,name='table'),
    path('course',views.course,name='course'),
    
    path('logout',views.logout_views,name='logout'),
    path('login',views.login_views,name='login'),
    path('register',views.register_views,name='register_views'),
    
    path('stdapply',views.stdapply,name='stdapply'),
    path('success',views.success,name='success'),
    path('delete_course/<int:pk>/', views.delete_course, name='delete_course'),
    path('update_course /<int:pk>/' ,views.update_course,name='update_course')


]
