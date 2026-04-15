from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)
    home_address = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    service = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
