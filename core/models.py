from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    VENDOR = 'VENDOR'
    BIDDER = 'BIDDER'

    CUSTOMER_TYPE_CHOICES = [
        (VENDOR, 'Vendor'),
        (BIDDER, 'Bidder')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_type = models.CharField(max_length=10, choices=CUSTOMER_TYPE_CHOICES)
    company_name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    telephone = models.CharField(max_length=15)
    address_line_one = models.CharField(max_length=25)
    address_line_two = models.CharField(max_length=25)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    postal_zip = models.CharField(max_length=6)
    country = models.CharField(max_length=10)

