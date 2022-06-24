from asyncio.windows_events import NULL
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.views import APIView
from todo.serializers import TodoSerializer,LoginSerializer
from todo.models import Profile
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
# Create your views here.
class ListTodoAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Profile.objects.all()
    serializer_class = TodoSerializer

class CreateTodoAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Profile.objects.all()
    serializer_class = TodoSerializer

class LoginApiView(APIView):
        def get_objects(self, email,password):
            try:
                allprofile=Profile.objects.all().values()
                
                for element in allprofile:
                    print("request.data['email'] ::::: ",email)
                    print("element['email'] ::::: ",element['email'])


                    if(element['email']==email and element['password']==password):
                        return element


            except Profile.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        def get(self,request,email,password):
            # print("ttttttttttttttttttt ",request.data['email'])

            article = self.get_objects(email,password)
            serializer = TodoSerializer(article)
            if(serializer.data['email']=='' or serializer.data['email']==NULL):
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(serializer.data,status=status.HTTP_200_OK)

class GetTodoAPIView(ListAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    def get_objects(self, id):
        try:
            return Profile.objects.get(id=id)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request, id):
        article = self.get_objects(id)
        serializer = TodoSerializer(article)
        return Response(serializer.data)

class UpdateTodoAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Profile.objects.all()
    serializer_class = TodoSerializer

class DeleteTodoAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Profile.objects.all()
    serializer_class = TodoSerializer