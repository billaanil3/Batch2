from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from CryceTruly.serializers import RegisterSerializser, LoginSerializer
from rest_framework import response, status
from django.contrib.auth import authenticate
from rest_framework import permissions

# Create your views here.

class AuthUserAPIView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        user = request.user
        serializer = RegisterSerializser(user)
        return response.Response({'user': serializer.data})


class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializser

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(username=email, password=password)
        if user:
            serializer = self.serializer_class(user)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response({"message": "Invalid Credentials, try again"}, status=staus.HTTP_400_BAD_REQUEST)