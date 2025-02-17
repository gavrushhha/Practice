from django.contrib import admin
from django.urls import path
from books import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.book_list, name='book_list'),
    path('book/new/', views.book_new, name='book_new'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'), 
    path('', include('accounts.urls')),
]
