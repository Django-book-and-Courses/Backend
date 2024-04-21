from django.urls import path
from . import views

urlpatterns = [
    path('ebooks/', views.EbookCreateListView.as_view(), name='movie-create-list'),
    path('ebooks/<int:pk>/', views.EbookRetrieveUpdateDestroyView.as_view(), name='movie-detail-view'),
    ]