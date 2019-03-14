from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import UserProfile, Skill

class UserProfileForm(ModelForm):
    skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = UserProfile
        fields = ["about_me", "tagline", "skills", "city", "photo", "main_link", "secondary_link", "work_experience_1"]

        def save(self, commit=True):
            user = super(UserProfileForm, self).save(commit=False)
            user.skills = self.cleaned_data["skills"]
            if commit:
                user.save()
            return user

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