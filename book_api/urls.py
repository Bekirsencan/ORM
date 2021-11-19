from django.urls import path
from .views import get_all_books

app_name = 'book_api'

urlpatterns = [
    path('', get_all_books.as_view(), name='get_all_books')
]
