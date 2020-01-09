from django.urls import path
from .views import home, kontakt


urlpatterns = [
    path('', home, name='Home'),
    path('kontakt/', kontakt, name='Kontakt')
]