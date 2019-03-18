from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.models import User
from .forms import CompanyProfileForm, JobForm, UserProfileForm

from .models import CompanyProfile, Position, UserProfile

class HomePage(TemplateView):
    model = UserProfile
    template_name = 'home.html'

class UserProfileList(LoginRequiredMixin, ListView):
    model = UserProfile
    template_name = 'profiles.html'

class CompanyProfileList(LoginRequiredMixin, ListView):
    model = CompanyProfile
    template_name = 'company_profiles.html'

class CreateUserProfile(LoginRequiredMixin, CreateView):
    model = UserProfile
    form_class = UserProfileForm
    # fields = ["about_me", "tagline", "skills", "city", "photo", "main_link", "secondary_link", "work_experience_1"]
    template_name = 'create_user_profile.html'
    success_url = reverse_lazy('hire_o_mat:user_home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class CreateCompanyProfile(LoginRequiredMixin, CreateView):
    model = CompanyProfile
    form_class = CompanyProfileForm
    # fields = ["company_name", "contact_email", "about", "city", "logo"]
    template_name = 'create_company_profile.html'
    success_url = reverse_lazy('hire_o_mat:user_home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CreateJob(LoginRequiredMixin, CreateView):
    model = CompanyProfile
    form_class = JobForm
    # fields = ["company_name", "contact_email", "about", "city", "logo"]
    template_name = 'create_job.html'
    success_url = reverse_lazy('hire_o_mat:user_home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JobList(LoginRequiredMixin, ListView):
    model = Position
    template_name = 'jobs.html'

class UserHome(LoginRequiredMixin, TemplateView):
    template_name = 'user_home.html'


class MyUserProfile(LoginRequiredMixin, TemplateView):
    model = UserProfile
    template_name = 'my_user_profile.html'

class MyCompanyProfile(LoginRequiredMixin, TemplateView):
    model = CompanyProfile
    template_name = 'my_company_profile.html'

class UpdateUserProfile(LoginRequiredMixin, UpdateView):
    model = UserProfile
    # form_class = UserProfileForm
    fields = ["about_me", "tagline", "skills", "city", "main_link", "secondary_link", "work_experience_1"]
    template_name = 'edit_user_profile.html'
    success_url = reverse_lazy('hire_o_mat:my_user_profile')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# class ChirpCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     template_name = 'new_post.html'
#     fields = ['body']
#     login_url = 'login'

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)