from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from store.forms import LoginForm

urlpatterns = [
    path('', views.home, name="home"),
    # user authentication
    path('accounts/register/',views.RegistrationView.as_view(),name="register"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='account/login.html', authentication_form=LoginForm), name="login"),
    path('accounts/profile/',views.profile,name="profile"), 
    path('accounts/add-address/', views.AddressView.as_view(), name="add-address"),
    
]
