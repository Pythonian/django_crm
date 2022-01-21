from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return the string representation of the model"""
        return self.user.username


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        """Return the string representation of the model"""
        return self.user.username


class Lead(models.Model):
    """Model to represent a Lead instance"""
    SOURCE_CHOICES = (
        ('YouTube', 'YouTube'),
        ('Google', 'Google'),
        ('Newsletter', 'Newsletter'),
    )
    # Lead details for capturing?
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    information = models.TextField()
    phoned = models.BooleanField(default=False)
    source_of_lead = models.CharField(choices=SOURCE_CHOICES, max_length=20)
    additional_files = models.FileField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        """Return the string representation of the model"""
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("leads:detail", kwargs={"pk": self.pk})
