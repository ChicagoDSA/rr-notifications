from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.account_signup, name='account_signup'),
]