from django.db import models

class Clients(models.Model):
    slug = models.SlugField()
    client_name = models.CharField(max_length=250)
    client_phonenumber = models.CharField(max_length=15)
    client_email = models.EmailField()
    client_location = models.CharField(max_length=50)

    def __str__(self):
        return self.client_name
