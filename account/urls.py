from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #user email verification

    path('register/', views.register, name='register'),
    path('email-verification/<str:uidb64>/<str:token>/', views.email_verification, name='email-verification'),
    path('email-verification-sent/', views.email_verification_sent, name='email-verification-sent'),
    path('email-verification-success/', views.email_verification_success, name='email-verification-success'),
    path('email-verification-failed/', views.email_verification_failed, name='email-verification-failed'),

    #user login

    path('my-login', views.my_login, name='my-login'),
    path('user-logout', views.user_logout, name='user-logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile-management', views.profile_management, name='profile-management'),
    path('delete-account', views.delete_account, name='delete-account'),

    #password management

    #1) submit email form
    path('reset-password', auth_views.PasswordResetView.as_view(), name='reset-password'),

    #2) success message stating that a password reset reset email was sent
    path('reset-password-sent', auth_views.PasswordResetDoneView.as_view(), name='reset-password-sent'),

    #3)Password reset link
    path('reset/<uidb64>/<token>/', atuh_views.PasswordResetConfirmView.as_view(), name='password-reset-confirm')

    # 4) Success message stating that our password was reset
    path('reset-password-complete', auth.views.PasswordResetCompleteView.as_view(), name='password-reset-complete')
