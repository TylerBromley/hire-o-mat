from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "hire_o_mat"
urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('user_home/', views.UserHome.as_view(), name='user_home'),
    path('create_profile/', views.CreateUserProfile.as_view(), name="create_user_profile"),
    path('create_biz_profile/', views.CreateCompanyProfile.as_view(), name="create_company_profile"),
    path('my_user_profile/', views.MyUserProfile.as_view(), name="my_user_profile"),
    path('my_company_profile/', views.MyCompanyProfile.as_view(), name="my_company_profile"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, 
document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, 
document_root=settings.MEDIA_ROOT)