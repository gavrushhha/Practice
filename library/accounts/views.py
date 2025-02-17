from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from accounts.serializers import UserSerializer
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse

class UserRegistrationAPIView(APIView):
    def get(self, request):
        """Отображает страницу регистрации."""
        return TemplateResponse(request, '/home/sirius/Рабочий стол/books/library/accounts/templates/user_register.html')

    def post(self, request):
        """Обрабатывает регистрацию пользователя."""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('user_login')  
        else:
            print(serializer.errors)
        return TemplateResponse(request, '/home/sirius/Рабочий стол/books/library/accounts/templates/user_register.html', {'errors': serializer.errors})

class UserLoginAPIView(APIView):
    def get(self, request):
        """Отображает страницу входа."""
        return TemplateResponse(request, '/home/sirius/Рабочий стол/books/library/accounts/templates/user_login.html')

    def post(self, request):
        """Обрабатывает вход в систему."""
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('book_list')  
        return TemplateResponse(request, '/home/sirius/Рабочий стол/books/library/accounts/templates/user_login.html', {'error': 'Неверные учетные данные'})

class UserLogoutAPIView(APIView):
    def post(self, request):
        """Выход из системы (POST-запрос)."""
        logout(request)
        return redirect('user_login')  
    def get(self, request):
        """Выход из системы (GET-запрос)."""
        logout(request)
        return redirect('user_login')  