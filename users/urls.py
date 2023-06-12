from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='sign-up'),
    path('signin/', views.SignIn.as_view(), name='sign-in'),
    path('logout/', views.Logout.as_view(), name='logout')
]
