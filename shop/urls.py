from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import user_reviews 
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', views.home, name='home'), 
    path('home/', RedirectView.as_view(url='/')),
    path('products/', views.products, name='products'),
    path('reviews/', views.user_reviews, name='user_reviews'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)