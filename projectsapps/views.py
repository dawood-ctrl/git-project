
from .models import students,course
from .serializers import studentSerializer,courseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class Studentget(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            stu=students.objects.get(id=pk)
            serializer = studentSerializer(stu)
            return Response(serializer.data)
        stu=students.objects.all()
        serializer= studentSerializer(stu,many=True)
        return Response(serializer.data)
    

class Studentpost(APIView):    
    def post(self,request,format=None):
        serializers=studentSerializer(data=request.data)
        if  serializers.is_valid():
            serializers.save()
            return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
        return Response (serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Studentput(APIView):
    def put(self,request,pk,format=None):
        # id=pk
        stu=students.objects.get(id=pk)
        serializer = studentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete data updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class studentpatch(APIView):
    def patch(self,request,pk,format=None):
        stu=students.objects.get(id=pk)
        serializer=studentSerializer(stu,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial data updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class studentdelete(APIView):
    def delete(self, request, pk, format=None):
            stu=students.objects.get(pk=pk)
            stu.delete()
            return Response({'msg':'data deleted'})
        

class courseget(APIView):
    def get(self,request,pk=None,format=None):
        if pk is not None:
            stu=course.objects.get(id=pk)
            serializer=courseSerializer(stu)
            return Response(serializer.data)
        stu = course.objects.all()
        serializer=studentSerializer(stu,many=True)
        return Response(serializer.data )

class coursepost(APIView):
    def post(self,request,format=None):
        serializers=courseSerializer(data=request.data)
        if  serializers.is_valid():
            serializers.save()
            return Response({ 'msg': 'data saved' }, status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
class courseput(APIView):
    def put(self,request, pk,format=None):
        stu=course.objects.get(id=pk)
        serializer = courseSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class coursepatch(APIView):
    def patch(self,request,pk,format=None):
        stu=course.objects.get(id=pk)
        serializers=courseSerializer(stu,data=request.data,partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'partial data updated'})
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
class coursedelete(APIView):
    def delete(self, request, pk, format=None):
        try:
            # Attempt to retrieve the course with the specified pk
            course_instance = course.objects.get(pk=pk)
            # Delete the course
            course_instance.delete()
            return Response({'msg': 'data deleted'})
        except course.DoesNotExist:
            # Handle the case where the course with the specified pk does not exist
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)


        
        