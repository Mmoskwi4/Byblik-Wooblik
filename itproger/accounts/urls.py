from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from .views import register

urlpatterns = [
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('logout-then-login', logout_then_login, name='logout_then_login'),
    path('registration/', register, name='register'),
    path('password-reset/', PasswordResetView.as_view(template_name='resetpass/password_reset.html'), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='resetpass/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='resetpass/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name='resetpass/password_reset_complete.html'),
         name='password_reset_complete'),
]