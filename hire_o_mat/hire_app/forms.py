from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import CompanyProfile, Position, Skill, UserProfile

class UserProfileForm(ModelForm):
    skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), widget=forms.CheckboxSelectMultiple)
    photo = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ["about_me", "tagline", "skills", "city", "photo", "main_link", "secondary_link", "work_experience_1"]

        def save(self, commit=True):
            user = super(UserProfileForm, self).save(commit=False)
            user.skills = self.cleaned_data["skills"]
            user.photo = self.cleaned_data["photo"]
            if commit:
                user.save()
            return user

class CompanyProfileForm(ModelForm):
    logo = forms.ImageField(required=False)

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

    class Meta:
        model = Position
        fields = ["position", "description"]

        def save(self, commit=True):
            job = super(JobForm, self).save(commit=False)
            if commit:
                job.save()
            return job

# class Position(models.Model):
#     company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
#     pos = models.CharField(max_length=500)
#     description = models.TextField(null=True, blank=True)
#     photo = models.ImageField(upload_to='images', null=True, blank=True)

#     def __str__(self):
#         return self.pos


# class CompanyProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     company_name = models.CharField(max_length=200)
#     contact_email = models.EmailField(null=True, blank=True)
#     about = models.TextField(null=True, blank=True)
#     city = models.ManyToManyField(City, blank=True)
#     logo = models.ImageField(upload_to='images', null=True, blank=True)
#     is_completed = models.BooleanField(default=False)

# user = models.OneToOneField(User, on_delete=models.CASCADE)
#     about_me = models.TextField(max_length=1000, null=True, blank=True)
#     tagline = models.CharField(max_length=300, null=True, blank=True)
#     skills = models.ManyToManyField(Skill)
#     city = models.ManyToManyField(City, blank=True)
#     photo = models.ImageField(upload_to='images', null=True, blank=True)
#     main_link = models.URLField(null=True, blank=True)
#     secondary_link = models.URLField(null=True, blank=True)
#     work_experience_1 = models.TextField(null=True, blank=True)
#     work_experience_2 = models.TextField(null=True, blank=True)
#     work_experience_3 = models.TextField(null=True, blank=True)
#     is_completed = models.BooleanField(default=False)