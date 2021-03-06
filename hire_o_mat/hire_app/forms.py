from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import City, CompanyProfile, Message, Position, Skill, UserProfile

class UserProfileForm(ModelForm):
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    photo = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ["about_me", "tagline", "skills", "city",
                  "photo", "main_link", "secondary_link", 
                  "work_experience_1", "work_experience_2", "work_experience_3"
                ]

        def save(self, commit=True):
            user = super(UserProfileForm, self).save(commit=False)
            user.skills = self.cleaned_data["skills"]
            user.photo = self.cleaned_data["photo"]
            if commit:
                user.save()
            return user


class CompanyProfileForm(ModelForm):
    logo = forms.ImageField(required=False)
    city = forms.ModelMultipleChoiceField(
        queryset=City.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = CompanyProfile
        fields = ["company_name", "contact_email", "about", "city", "logo"]

        def save(self, commit=True):
            company = super(CompanyProfileForm, self).save(commit=False)
            company.photo = self.cleaned_data["logo"]
            if commit:
                company.save()
            return company


class JobForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')

        super(JobForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Position
        fields = ["position", "description"]

        def save(self, commit=True):
            job = super(JobForm, self).save(commit=False)
            job.company = self.user.companyprofile.id
            if commit:
                job.save()
            return job

class MessageForm(ModelForm):

    class Meta:
        model = Message
        fields = ["message_title", "message_content"]

        def save(self, commit=True):
            message = super(MessageForm, self).save(commit=False)
            message.sender = self.user.username
            if commit:
                message.save()
            return message
