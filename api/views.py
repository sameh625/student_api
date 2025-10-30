from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student, Enrollment, Course
from .serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, generics, viewsets

@api_view(['GET','POST'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
    def get_object(self,pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    def put(self,request,pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class CourseList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)
    
class CourseDetail(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk)
    def put(self, request, pk):
        return self.update(request, pk)
    def delete(self, request, pk):
        return self.destroy(request, pk)

class ViewSet_Enrollment(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

