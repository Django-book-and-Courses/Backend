from rest_framework import serializers
from ebooks.models import Ebook,Author,Genre

class AuthorModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = '__all__'

    def validate_first_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("O nome deve ter pelo menos 2 caracteres")
        return value

class GenreModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'
 

class EbookModelSerializer(serializers.ModelSerializer):
    # authors = AuthorModelSerializer(many=True)  # Relacionamento Many-to-Many
    # genres = GenreModelSerializer(many=True)  # Relacionamento Many-to-Many
    
    #  está informando ao Django REST Framework (DRF) que este campo representa uma data ou um carimbo de data e hora
    publication_date = serializers.DateField(format="%d-%m-%Y")  # Formato Brasileiro
    created_at = serializers.DateTimeField(format="%d/%m/%Y as %H:%M:%S")  # Formato Brasileiro
    updated_at = serializers.DateTimeField(format="%d/%m/%Y as %H:%M:%S")  # Formato Brasileiro

    class Meta:
        model = Ebook
        fields = ["title", "summary", "authors", "genres", "publication_date", "num_pages", "cover_photo", "created_by", "created_at", "updated_at"]  

    def validate_num_pages(self,value):
        if value is None:
            raise serializers.ValidationError("The number of pages must be provided.")
        if value < 5:
            raise serializers.ValidationError("An ebook must have at least 5 pages.")
        return value
    
