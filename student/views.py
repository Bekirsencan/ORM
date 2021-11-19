from .models import Student
from .serializers import StudentSerializer
from rest_framework import generics


class ShowList(generics.ListCreateAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()
