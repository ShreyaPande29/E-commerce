from django.urls import path
from eshop import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.user_login,name='login'),
    path('signup/',views.SignUp,name='signup'),
]