from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "hire_o_mat"
urlpatterns = [

    path('', views.HomePage.as_view(), name='home'),
    path('user_home/', views.UserHome.as_view(), name='user_home'),
    path('profiles/', views.UserProfileList.as_view(), name='profiles'),
    path('search_profiles/', views.profile_search, name='search_profiles'),
    path('company_profiles/', views.CompanyProfileList.as_view(), name='company_profiles'),
    
    path('create_profile/', views.CreateUserProfile.as_view(), name="create_user_profile"),
    path('my_user_profile/', views.MyUserProfile.as_view(), name="my_user_profile"),
    path('edit_user_profile/<int:pk>', views.UpdateUserProfile.as_view(), name="edit_user_profile"),
    path('profile_detail/<int:pk>', views.ProfileDetail.as_view(), name="profile_detail"),

    path('create_biz_profile/', views.CreateCompanyProfile.as_view(), name="create_company_profile"),
    path('my_company_profile/', views.MyCompanyProfile.as_view(), name="my_company_profile"),
    path('edit_company_profile/<int:pk>', views.UpdateCompanyProfile.as_view(), name="edit_company_profile"),
    path('company_profile_detail/<int:pk>', views.ComapanyProfileDetail.as_view(), name="company_profile_detail"),

    path('create_job/', views.CreateJob.as_view(), name="create_job"),
    path('job_detail/<int:pk>', views.JobDetail.as_view(), name="job_detail"),
    path('jobs/', views.JobList.as_view(), name="jobs"),
    path('job_like_toggle/<int:pk>', views.JobLikeToggle.as_view(), name="job_like_toggle"),
    path('api/<int:pk>/like', views.JobLikeAPIToggle.as_view(), name="job_like_api_toggle"),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, 
document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, 
document_root=settings.MEDIA_ROOT)