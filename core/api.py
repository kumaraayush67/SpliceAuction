from django.shortcuts import redirect
from django.contrib.auth import login
from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer

class CreateCustomer(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            customer = serializer.save()
            login(request, customer.user)
            return redirect('index')
        else:
            return redirect('index')
