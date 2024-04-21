from django.contrib import admin
from .models import Author, Genre, Ebook

# Registro do modelo Author com o decorator @admin.register
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # Personalizações podem ser adicionadas aqui
    list_display = ('first_name', 'last_name')  # Campos exibidos no admin
    search_fields = ('first_name', 'last_name')  # Campos pesquisáveis

# Registro do modelo Genre com o decorator @admin.register
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    # Personalizações podem ser adicionadas aqui
    list_display = ('name',)  # Apenas um campo é necessário para exibição
    search_fields = ('name',)  # Campo pesquisável

# Registro do modelo Ebook com o decorator @admin.register
@admin.register(Ebook)
class EbookAdmin(admin.ModelAdmin):
    # Personalizações adicionais para Ebook
    list_display = ('title', 'publication_date', 'num_pages', 'created_by')  # Campos exibidos
    search_fields = ('title', 'summary')  # Campos pesquisáveis
    list_filter = ('authors', 'genres', 'publication_date')  # Filtros para facilitar a navegação
