from .views import index, about, contact, portfolio, portfolio_details, resume, services
from django.urls import path


urlpatterns = [
    path('', index),
    path('about/', about),
    path('contact/', contact),
    path('portfolio/', portfolio),
    path('resume/', resume),
    path('services/', services),
    path('portfolio-details/', portfolio_details),

]