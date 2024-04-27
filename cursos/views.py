from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Professor, Categoria, Curso
from .serializers import ProfessorModelSerializer, CategoriaModelSerializer, CursoDetailSerializer, CursoModelSerializer

class CursoCreateListView(generics.ListCreateAPIView):
    # permission_classes = 
    queryset = Curso.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CursoDetailSerializer
        return CursoModelSerializer
class CursoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = 
    queryset = Curso.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CursoDetailSerializer
        return CursoModelSerializer


class ProfessorCreateListView(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorModelSerializer
class ProfessorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorModelSerializer

class CategoriaCreateListView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaModelSerializer
class CategoriaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaModelSerializer

    
