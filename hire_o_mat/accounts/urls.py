from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'), # http://127.0.0.1:8000/user/user_signup/
]