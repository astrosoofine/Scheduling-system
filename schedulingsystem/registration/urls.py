from django.contrib.auth import views as auth_views
from django.urls import path
from .views import * 

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', sign_up, name='signup' ),
    path('', homepage, name="home")
]
