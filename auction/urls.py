from django.contrib import admin
from django.urls import path

from core.views import index, contact
from core.api import CreateCustomer


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('api/create/', CreateCustomer.as_view(), name='create_customer'),
]
