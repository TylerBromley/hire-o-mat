from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, RedirectView
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.models import User
from .filters import UserProfileFilter
from .forms import CompanyProfileForm, JobForm, UserProfileForm
# DRF STUFF
from rest_framework import authentication, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
# MODELS
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
         context['likes'] = Position.objects.filter(likes=self.request.user.id)
         return context


######### DETAIL VIEWS ##########
class MyUserProfile(LoginRequiredMixin, TemplateView):
    model = UserProfile
    template_name = 'my_user_profile.html'


class MyCompanyProfile(LoginRequiredMixin, TemplateView):
    model = CompanyProfile
    template_name = 'my_company_profile.html'

class ProfileDetail(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'profile_detail.html'

class ComapanyProfileDetail(LoginRequiredMixin, DetailView):
    model = CompanyProfile
    template_name = 'company_profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['position'] = Position.objects.all()
        return context

class JobDetail(LoginRequiredMixin, DetailView):
    model = Position
    template_name = 'job_detail.html'

class JobLikeToggle(LoginRequiredMixin, RedirectView):
    def get_redirect_method(self, *args, **kwargs):
        pos = self.kwargs.get("position")
        obj = get_object_or_404(Position, position=pos)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated():
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        return url_

########## LIST VIEW ###########
class UserProfileList(LoginRequiredMixin, ListView):
    model = UserProfile
    template_name = 'profiles.html'

def profile_search(request):
    user_list = UserProfile.objects.all()
    user_filter = UserProfileFilter(request.GET, queryset=user_list)
    return render(request, 'profile_list.html', {'filter': user_filter})

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

######### API VIEW ###########

class JobLikeAPIToggle(APIView):
    # authentication_classes = (authentication.SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None, format=None):
        pos = self.kwargs.get("position")
        obj = get_object_or_404(Position, pk=pk)
        url_ = obj.get_absolute_url()
        user = self.request.user
        updated = False
        liked = False

        if user.is_authenticated:
            if user in obj.likes.all():
                liked = False
                updated = True
                obj.likes.remove(user)
            else:
                liked = True
                obj.likes.add(user)
                updated = True
        data = {
            "updated": updated,
            "liked": liked
        }
        return Response(data)

    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.get_queryset()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)
