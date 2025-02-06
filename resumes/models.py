from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    summary = models.TextField()
    skills = models.TextField()
    experience = models.TextField()
    education = models.TextField()
    template_choice = models.CharField(
        max_length=20,
        choices=[
            ("classic", "Classic"),
            ("modern", "Modern"),
            ("elegant", "Elegant"),
        ],
        default="classic",
    )

    def __str__(self):
        return self.full_name
