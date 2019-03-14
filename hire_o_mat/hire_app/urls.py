from django.urls import path

from . import views

app_name = "hire_o_mat"
urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('user_home/', views.UserHome.as_view(), name='user_home'),
    path('create_profile/', views.CreateUserProfile.as_view(), name="create_user_profile"),
    path('create_biz_profile/', views.CreateCompanyProfile.as_view(), name="create_company_profile"),
]