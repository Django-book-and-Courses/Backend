from django.test import TestCase
from .models import Professor, Categoria, Curso

class ProfessorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Criando um objeto Professor para uso nos testes
        Professor.objects.create(nome="Dr. Ana Silva", email="anasilva@example.com")

    def test_string_representation(self):
        professor = Professor.objects.get(id=1)
        self.assertEqual(str(professor), "Dr. Ana Silva")

    def test_email_field(self):
        professor = Professor.objects.get(id=1)
        self.assertEqual(professor.email, "anasilva@example.com")

class CategoriaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Criando um objeto Categoria para uso nos testes
        Categoria.objects.create(nome="Matemática")

    def test_string_representation(self):
        categoria = Categoria.objects.get(id=1)
        self.assertEqual(str(categoria), "Matemática")

class CursoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Criando objetos dependentes
        professor = Professor.objects.create(nome="Dr. Carlos Andrade", email="carlos@example.com")
        categoria_matematica = Categoria.objects.create(nome="Matemática")
        
        # Criando o objeto Curso
        curso = Curso.objects.create(titulo="Álgebra Linear", professor=professor, valor=150.00, carga_horaria=60)
        curso.categorias.add(categoria_matematica)

    def test_string_representation(self):
        curso = Curso.objects.get(id=1)
        self.assertEqual(str(curso), "Álgebra Linear")

    def test_categorias_relation(self):
        curso = Curso.objects.get(id=1)
        self.assertEqual(curso.categorias.count(), 1)
        self.assertEqual(curso.categorias.first().nome, "Matemática")

    def test_curso_fields(self):
        curso = Curso.objects.get(id=1)
        self.assertEqual(curso.valor, 150.00)
        self.assertEqual(curso.descricao, None)  # Testa se o campo opcional 'descricao' é None por padrão
        self.assertEqual(curso.carga_horaria, 60)

