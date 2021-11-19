from django.urls import path
from .views import ShowList


app_name = 'student'

urlpatterns = [
    path('',ShowList.as_view(), name='student' )
]