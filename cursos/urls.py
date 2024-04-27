from django.urls import path
from . import views

urlpatterns = [
    path('cursos/', views.CursoCreateListView.as_view(), name='movie-create-list'),
    path('cursos/<int:pk>/', views.CursoRetrieveUpdateDestroyView.as_view(), name='movie-detail-view'),

    # Rotas para Professor
    path('professores/', views.ProfessorCreateListView.as_view(), name='professor-list-create'),
    path('professores/<int:pk>/', views.ProfessorRetrieveUpdateDestroyView.as_view(), name='professor-retrieve-update-destroy'),

    # Rotas para Categoria
    path('categorias/', views.CategoriaCreateListView.as_view(), name='categoria-list-create'),
    path('categorias/<int:pk>/', views.CategoriaRetrieveUpdateDestroyView.as_view(), name='categoria-retrieve-update-destroy'),  
    ]

