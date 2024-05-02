from rest_framework import serializers
from .models import Professor, Categoria, Curso

class ProfessorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class CategoriaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class CursoDetailSerializer(serializers.ModelSerializer):
    # Utilizar CategoriaSerializer para nested serialization
    categorias = CategoriaModelSerializer(many=True, read_only=True)
    professor_nome = serializers.ReadOnlyField(source='professor.nome')

    class Meta:
        model = Curso
        fields = ['id', 'titulo', 'professor', 'professor_nome', 'valor', 'descricao', 'carga_horaria', 'categorias']

# Para criar ou atualizar um Curso com categorias, você pode usar um serializer para operações POST/PUT
class CursoModelSerializer(serializers.ModelSerializer):
    categorias = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), many=True)

    class Meta:
        model = Curso
        fields = ['titulo', 'professor', 'valor', 'descricao', 'carga_horaria', 'categorias']
