from django.urls import path
from . import views

urlpatterns = [
    path('ebooks/', views.EbookCreateListView.as_view(), name='ebook-create-list'),
    path('ebooks/<int:pk>/', views.EbookRetrieveUpdateDestroyView.as_view(), name='ebook-detail-view'),
    path('authors/', views.AuthorCreateListView.as_view(), name='author-create-list'),  # Listar e criar autores
    path('authors/<int:pk>/', views.AuthorRetrieveUpdateDestroyView.as_view(), name='author-detail-view'),  # Operações de CRUD para autores
]
