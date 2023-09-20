
from .models import students,course
from .serializers import studentSerializer
from rest_framework import viewsets
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset =students.objects.all()
    serializer_class = studentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset =course.objects.all()
    serializer_class = studentSerializer