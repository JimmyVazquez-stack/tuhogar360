# usuarios/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from djstripe.models import Subscription, Customer

class CustomUser(AbstractUser):
    subscription = models.ForeignKey(Subscription, null=True, blank=True, on_delete=models.SET_NULL, help_text="The user's Stripe Subscription object, if it exists")
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL, help_text="The user's Stripe Customer object, if it exists") 
    # Agrega otros campos según tus necesidades
