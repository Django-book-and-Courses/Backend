from rest_framework import generics
from cursos.models import Curso
from cursos.serializers import CursoModelSerializer

class CursoCreateListView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoModelSerializer

class CursoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoModelSerializer
