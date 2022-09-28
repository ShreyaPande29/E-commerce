from django.urls import path
from eshop import views

urlpatterns = [
    path('',views.index , name='index'),
    path('signup/',views.SignUp, name = 'signup'),
]