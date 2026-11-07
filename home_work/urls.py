from django.urls import path
from .views import home_page, winter, spring, summer, autumn


urlpatterns = [
    path('home', home_page),
    path('profile', winter),
    path('spring', spring),
    path('summer', summer),
    path('autumn', autumn),
]
