from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
]
