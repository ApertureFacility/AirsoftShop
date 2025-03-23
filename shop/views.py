from django.shortcuts import render
from .models import Service


goods = [
    {"good_name": "Игрушечная машинка", "status": "в наличии", "category": "children"},
    {"good_name": "Ноутбук", "status": "нет в наличии", "category": "tech"},
    {"good_name": "Книга", "status": "в наличии", "category": "literature"},
    {"good_name": "Наушники", "status": "в наличии", "category": "tech"},
    {"good_name": "Мяч", "status": "нет в наличии", "category": "sport"},
]


user_list = [ 
    {"name": "Алиса", "age": 22, "phone": "123-456-7890", "photo": "user1.png"},
    {"name": "Боб", "age": 30, "phone": "987-654-3210", "photo": "user3.png"},
    {"name": "Чарли", "age": 25, "phone": "555-555-5555", "photo": "user4.png"},
    {"name": "Диана", "age": 28, "phone": "111-222-3333", "photo": "user5.jpg"},
]

def users_view(request):
    return render(request, 'shop/users.html', {'users': user_list})

def home(request):
    services = Service.objects.filter(is_active=True)[:3]  
    return render(request, 'shop/home.html', {'services': services})



def products(request):
    services = Service.objects.all() 
    return render(request, 'shop/products.html', {'services': services})