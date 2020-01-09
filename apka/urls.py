from django.urls import path
from .views import kontakt
from .views import PostListView, PostDetailView, PostCreateView


urlpatterns = [
    path('', PostListView.as_view(), name='Home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('kontakt/', kontakt, name='Kontakt')
]
