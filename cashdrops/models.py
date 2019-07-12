from django.db import models
from django.shortcuts import render
from agents.models import Agent
from clients.models import Clients
from django.utils.text import slugify


STATUS = (
    ('Pending', 'pending'),
    ('Complete', 'complete'),
    ('Cancelled', 'cancelled')
)

CURRENCY = (
    ('CHOOSE RATE','choose rate'),
    ('USD', 'usd'),
    ('SSP', 'ssp'),
    ('GBP', 'gbp'),
    ('UGX', 'ugx'),
    ('TSH', 'tsh'),

)

class Cashdrop(models.Model):
    slug = models.SlugField(
        default='',
        editable=False,
    )
    delivery_location = models.CharField(max_length=250)
    receiver = models.CharField(max_length=250)
    date_of_delivery = models.DateField(auto_now=False)
    date_sent = models.DateField(auto_now_add=True)
    delivery_amount = models.IntegerField()
    rate = models.CharField(choices=CURRENCY, default='choose rate', max_length=30)
    delivery_agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)
    sent_by = models.ForeignKey(Clients, on_delete=models.SET_NULL, null=True)
    status = models.CharField(choices=STATUS, default='Pending', max_length=30)

    def __str__(self):
        return self.receiver

    def get_agent_url(self):
        return reverse('cashdrop_edit', kwargs={'pk': self.pk, 'slug': self.slug})


    def save(self, *args, **kwargs):
        cashdrop_slug = self.receiver
        self.slug = slugify(cashdrop_slug, allow_unicode=True)
        super().save(*args, **kwargs)