from django.urls import path
from . import views

urlpatterns = [
    path('cursos/', views.CursoCreateListView.as_view(), name='movie-create-list'),
    path('cursos/<int:pk>/', views.CursoRetrieveUpdateDestroyView.as_view(), name='movie-detail-view'),
    ]