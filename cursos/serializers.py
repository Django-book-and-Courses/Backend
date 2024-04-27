from rest_framework import serializers
from cursos.models import Curso

class CursoModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Curso
        fields = '__all__'