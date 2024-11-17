from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('furnitures/', views.furnitures, name='furnitures'),
    path('furnitures/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),

    path('login/' , views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.custom_logout, name="logout"),
]