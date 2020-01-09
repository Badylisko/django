from django.urls import path
from .views import kontakt
from .views import PostListView, PostDetailView


urlpatterns = [
    path('', PostListView.as_view(), name='Home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('kontakt/', kontakt, name='Kontakt')
]
