from django.urls import path
from .views import BooksListView,BookDetailView

urlpatterns = [
    path('library/', BooksListView.as_view(), name="library"),
    path('<int:id>/', BookDetailView.as_view(), name="book-detail"),
]