from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

class City(models.Model):
    city_name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.city_name


class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    contact_email = models.EmailField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    city = models.ManyToManyField(City, blank=True)
    logo = models.ImageField(upload_to='images', null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name


class Position(models.Model):
    position = models.CharField(max_length=500)
    company = models.ForeignKey(CompanyProfile, null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='images', null=True, blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name='position_likes')

    def __str__(self):
        return self.position

    def get_absolute_url(self):
        return reverse("hire_o_mat:job_detail", kwargs={"pk": self.pk})

    def get_like_url(self):
        return reverse("hire_o_mat:job_like_toggle", kwargs={"pk": self.pk})

    def get_api_like_url(self):
        return reverse("hire_o_mat:job_like_api_toggle", kwargs={"pk": self.pk})


class Skill(models.Model):
    skill = models.CharField(max_length=200)

    def __str__(self):
        return self.skill


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_me = models.TextField(max_length=1000, null=True, blank=True)
    tagline = models.CharField(max_length=300, null=True, blank=True)
    skills = models.ManyToManyField(Skill)
    city = models.ManyToManyField(City, blank=True)
    photo = models.ImageField(upload_to='images', null=True, blank=True)
    main_link = models.URLField(null=True, blank=True)
    secondary_link = models.URLField(null=True, blank=True)
    work_experience_1 = models.TextField(null=True, blank=True)
    work_experience_2 = models.TextField(null=True, blank=True)
    work_experience_3 = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Interest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    created = models.DateTimeField(null=True, auto_now_add=True)






