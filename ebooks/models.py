from django.db import models
from authentication.models import CustomUser

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Ebook(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True, null=True)
    authors = models.ManyToManyField(Author, related_name="author_ebooks",blank=True, null=True)  
    genres = models.ManyToManyField(Genre, related_name="genre_ebooks",blank=True, null=True) 
    publication_date = models.DateField(blank=True, null=True)
    num_pages = models.PositiveIntegerField(blank=True, null=True)
    cover_photo = models.ImageField(upload_to='book_covers/', blank=True, null=True)  
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL,blank=True, null=True, related_name="created_ebooks")  # Quem criou

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    # Define metadados para o modelo, especificando que o nome plural de 'Ebook' deve ser "Ebook"
    class Meta: 
        verbose_name_plural = "Ebook"
