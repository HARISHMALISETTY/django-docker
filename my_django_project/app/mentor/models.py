from django.db import models
from django.contrib.auth.models import User

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    expertise = models.CharField(max_length=200)
    years_of_experience = models.IntegerField()
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.expertise}"

    class Meta:
        ordering = ['-created_at'] 