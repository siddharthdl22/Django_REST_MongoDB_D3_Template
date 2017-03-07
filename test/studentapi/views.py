from studentapi.models import Student
from studentapi.serializers import StudentSerializer
from rest_framework_mongoengine import generics


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
