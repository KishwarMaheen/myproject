from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    # revise the password reset urls
    path('reset/', PasswordResetView.as_view(template_name="password_reset.html",
                                             email_template_name="password_reset_email.html",
                                             subject_template_name="password_reset_subject.txt"),
         name="password_reset"),
    path('reset/done/', PasswordResetDoneView.as_view(template_name="password_reset_done.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),
         name="password_reset_confirm"),
    path('reset/complete/', PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
         name="password_reset_complete"),
    path('settings/password/', PasswordChangeView.as_view(template_name="password_change.html"),
         name='password_change'),
    path('settings/password/done/', PasswordChangeDoneView.as_view(template_name="password_change_done.html"),
         name='password_change_done'),
]
