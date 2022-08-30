from django.urls import path
from .views import register, profile, DeleteUser, user_detail
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(
                                                    template_name='users/login.html'
                                                ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
                                                    template_name='users/logout.html'
                                                  ), name='logout'),
    path('profile/', profile, name='profile'),
    path('delete/<int:pk>/', DeleteUser.as_view(), name='delete_user'),
    path('detail/<int:pk>/', user_detail, name="user-detail"),
]