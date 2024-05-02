from django.test import TestCase
from .models import Author, Genre, Ebook
from authentication.models import CustomUser
from datetime import date

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configura dados de teste para a classe de testes do modelo Author.
        # Cria um autor no banco de dados que será usado nos métodos de teste.
        Author.objects.create(first_name='John', last_name='Doe')

    def test_string_representation(self):
        # Testa a representação em string do modelo Author.
        # Verifica se o método __str__ retorna o nome completo do autor corretamente.
        author = Author.objects.get(id=1)
        self.assertEqual(str(author), 'John Doe')

class GenreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configura dados de teste para a classe de testes do modelo Genre.
        # Cria um gênero no banco de dados que será usado nos métodos de teste.
        Genre.objects.create(name='Fiction')

    def test_string_representation(self):
        # Testa a representação em string do modelo Genre.
        # Verifica se o método __str__ retorna o nome do gênero corretamente.
        genre = Genre.objects.get(id=1)
        self.assertEqual(str(genre), 'Fiction')

class EbookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configura dados de teste para a classe de testes do modelo Ebook.
        # Cria um usuário, um autor, um gênero e um ebook no banco de dados.
        user = CustomUser.objects.create(username='testuser')
        author1 = Author.objects.create(first_name='John', last_name='Doe')
        genre1 = Genre.objects.create(name='Fiction')
        ebook = Ebook.objects.create(title='Example Book', created_by=user, publication_date=date.today())
        ebook.authors.add(author1)
        ebook.genres.add(genre1)

    def test_string_representation(self):
        # Testa a representação em string do modelo Ebook.
        # Verifica se o método __str__ retorna o título do ebook corretamente.
        ebook = Ebook.objects.get(id=1)
        self.assertEqual(str(ebook), 'Example Book')

    def test_ebook_creation(self):
        # Testa a criação de um ebook no banco de dados.
        # Verifica se o ebook criado é uma instância do modelo Ebook e se os atributos estão corretos.
        ebook = Ebook.objects.get(id=1)
        self.assertTrue(isinstance(ebook, Ebook))
        self.assertEqual(ebook.title, 'Example Book')

    def test_ebook_relations(self):
        # Testa as relações do modelo Ebook com os modelos Author e Genre.
        # Verifica se as relações de autoria e gênero estão corretas.
        ebook = Ebook.objects.get(id=1)
        self.assertEqual(ebook.authors.count(), 1)
        self.assertEqual(ebook.genres.count(), 1)
        self.assertEqual(str(ebook.authors.first()), 'John Doe')
        self.assertEqual(str(ebook.genres.first()), 'Fiction')

    def test_auto_timestamps(self):
        # Testa os campos automáticos de timestamp (created_at e updated_at) do modelo Ebook.
        # Verifica se esses campos são preenchidos automaticamente ao criar o ebook.
        ebook = Ebook.objects.get(id=1)
        self.assertIsNotNone(ebook.created_at)
        self.assertIsNotNone(ebook.updated_at)
