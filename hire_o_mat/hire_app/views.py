from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User

from .models import CompanyProfile, UserProfile

class HomePage(TemplateView):
    model = UserProfile
    template_name = 'home.html'

class CreateUserProfile(LoginRequiredMixin, TemplateView):
    model = UserProfile
    template_name = 'create_user_profile.html'

class CreateCompanyProfile(LoginRequiredMixin, TemplateView):
    model = CompanyProfile
    template_name = 'create_company_profile.html'

class UserHome(LoginRequiredMixin, TemplateView):
    template_name = 'user_home.html'

