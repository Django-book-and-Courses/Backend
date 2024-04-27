from django.contrib import admin
from .models import Professor, Categoria, Curso

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("nome", "email")  # Exibe campos na lista do admin
    search_fields = ("nome", "email")  # Permite pesquisa por esses campos


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)  # Exibe campos na lista do admin
    search_fields = ("nome",)  # Permite pesquisa por esses campos


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "professor", "carga_horaria", "categoria")  # Exibe informações no admin
    list_filter = ("professor", "categoria")  # Permite filtrar por esses campos
    search_fields = ("titulo", "descricao")  # Campos que podem ser pesquisados
    raw_id_fields = ("professor", "categoria")  # Melhora a interface para campos ForeignKey
