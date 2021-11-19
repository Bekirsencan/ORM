from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/student/',include('student.urls', namespace='student')),
    path('api/book/', include('book_api.urls', namespace='book')),
]
