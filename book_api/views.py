from book.models import Book
from rest_framework import generics
from .serializers import BookSerializer


class get_all_books(generics.ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()
