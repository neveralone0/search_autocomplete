from django.shortcuts import render
from django.http import JsonResponse
from django.conf import Settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from ipware import get_client_ip
from faker import Faker
from .models import FakeAddress


fake = Faker()


def generate_data(request):
    for i in range(100):
        FakeAddress.objects.create(address=fake.address())
    return JsonResponse({'status': 200})


def home(request):
    return render(request, 'index.html')


def search_address(request):
    address = request.GET.get('address')
    payload = []
    if address:
        fake_address_objs = FakeAddress.objects.filter(address__icontains=address)
        for fake_address_objs in fake_address_objs:
            payload.append(fake_address_objs.address)
    return JsonResponse({'status': 200, 'data': payload})
