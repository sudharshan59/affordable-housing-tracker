from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator

class Owner(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name

class House(models.Model):
    title = models.CharField(max_length=255)
    address = models.TextField()
    image = models.ImageField(upload_to='houses/', blank=True, null=True)
    rent = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='houses')
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('housing:house_detail', kwargs={'pk': self.pk})

class Applicant(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    income = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    applied_house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='applicants')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.applied_house.title}"