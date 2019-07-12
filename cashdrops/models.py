from django.db import models
from django.shortcuts import render
from agents.models import Agent
from clients.models import Clients


STATUS = (
    ('Pending', 'pending'),
    ('Complete', 'complete'),
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
    slug = models.SlugField()
    position = models.IntegerField()
    delivery_location = models.CharField(max_length=250)
    delivered_to = models.CharField(max_length=250)
    date_of_delivery = models.DateField(auto_now=False)
    date_sent = models.DateField(auto_now_add=True)
    delivery_amount = models.IntegerField()
    rate = models.CharField(choices=CURRENCY, default='choose rate', max_length=30)
    delivery_agent = models.CharField(max_length=250)
    sent_by = models.CharField(max_length=250)
    status = models.CharField(choices=STATUS, default='Pending', max_length=30)
    remarks = models.TextField()

    def __str__(self):
        return self.delivered_to