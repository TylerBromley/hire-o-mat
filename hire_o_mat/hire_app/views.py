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

########### MAIN PAGES ############
class HomePage(TemplateView):
    model = UserProfile
    template_name = 'home.html'


class UserHome(LoginRequiredMixin, TemplateView):
    template_name = 'user_home.html'

    def get_context_data(self, **kwargs):
         context = super(UserHome, self).get_context_data(**kwargs)
         context['company'] = CompanyProfile.objects.get(user=self.request.user)
         context['position'] = Position.objects.filter(company=self.request.user.companyprofile.id)
         return context


######### DETAIL VIEWS ##########
class MyUserProfile(LoginRequiredMixin, TemplateView):
    model = UserProfile
    template_name = 'my_user_profile.html'


class MyCompanyProfile(LoginRequiredMixin, TemplateView):
    model = CompanyProfile
    template_name = 'my_company_profile.html'


class JobDetail(LoginRequiredMixin, DetailView):
    model = Position
    template_name = 'job_detail.html'


########## LIST VIEW ###########
class UserProfileList(LoginRequiredMixin, ListView):
    model = UserProfile
    template_name = 'profiles.html'


class CompanyProfileList(LoginRequiredMixin, ListView):
    model = CompanyProfile
    template_name = 'company_profiles.html'


class JobList(LoginRequiredMixin, ListView):
    model = Position
    template_name = 'jobs.html'


############ CREATE #############
class CreateUserProfile(LoginRequiredMixin, CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'create_user_profile.html'
    success_url = reverse_lazy('hire_o_mat:user_home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class CreateCompanyProfile(LoginRequiredMixin, CreateView):
    model = CompanyProfile
    form_class = CompanyProfileForm
    template_name = 'create_company_profile.html'
    success_url = reverse_lazy('hire_o_mat:user_home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CreateJob(LoginRequiredMixin, CreateView):
    model = Position
    form_class = JobForm
    template_name = 'create_job.html'
    success_url = reverse_lazy('hire_o_mat:user_home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.company = self.request.user.companyprofile
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(CreateJob, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


############ UPDATE #############
class UpdateUserProfile(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'edit_user_profile.html'
    success_url = reverse_lazy('hire_o_mat:my_user_profile')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateCompanyProfile(LoginRequiredMixin, UpdateView):
    model = CompanyProfile
    form_class = CompanyProfileForm
    template_name = 'edit_company_profile.html'
    success_url = reverse_lazy('hire_o_mat:my_company_profile')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

