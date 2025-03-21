from django.db import models

# Create your models here.

class Task(models.Model):
    status_choice=[
        ("Pending", "Pending"),
        ("Complete", "Complete"),
    ]
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=100, choices=status_choice, default="Pending")
    image = models.ImageField(upload_to="")
    due_date = models.DateField(null=True, blank=True)
