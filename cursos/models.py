from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria,related_name="categorias_curso",  null=True, blank=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    carga_horaria = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo
