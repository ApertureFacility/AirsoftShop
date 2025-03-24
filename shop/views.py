from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Service, Review
from django.shortcuts import render, get_object_or_404
from .models import Review

def home(request):
    """Главная страница с 3 активными услугами и 3 последними отзывами"""
    services = Service.objects.all()[:3]
    treereviews = Review.objects.all().order_by('-date')[:3] 
    return render(request, 'shop/homePage.html', {
        'services': services,
        'treereviews': treereviews
    })

def products(request):
    """Страница всех продуктов/услуг"""
    services = Service.objects.all() 
    return render(request, 'shop/productsPage.html', {'services': services})

def reviews_view(request):
    """Страница отзывов с пагинацией"""
    reviews_list = Review.objects.all().order_by('-date')
    paginator = Paginator(reviews_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'reviews.html', {'page_obj': page_obj})

def user_reviews(request):
    """Отзывы пользователей с пагинацией (альтернативный вариант)"""
    reviews_list = Review.objects.all().order_by('-date')
    paginator = Paginator(reviews_list, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'shop/reviewsPage.html', {'page_obj': page_obj})

def users_view(request):
    """Страница пользователей (без изменений)"""
    return render(request, 'shop/reviewsPage.html')

def review_detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    return render(request, 'shop/review_detail.html', {'review': review})