from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import UserSerializer



class RegisterAPI(APIView):

     def post(self, request):
         try:
             serializer  = UserSerializer(data=request.data)
             serializer.is_valid(raise_exception=True)
             serializer.save()
             return Response(serializer.data)

         except Exception as e:
                   print(e)





class LoginAPI(APIView):

     def post(self, request):
         try:
             username  = request.data.get('username')
             password = request.data.get('password')
             user = authenticate(username=username, password=password)
             if user:
                   return Response({"token": user.auth_token.key, "username": username})
             else:
                   return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

         except Exception as e:
                   print(e)




