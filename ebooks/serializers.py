from rest_framework import serializers
from ebooks.models import Ebook,Author,Genre
from datetime import datetime

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
  
class EbookListDetailSerializer(serializers.ModelSerializer):
    authors = AuthorModelSerializer(many=True)  # Relacionamento Many-to-Many
    genres = GenreModelSerializer(many=True)  # Relacionamento Many-to-Many

    # Configura apenas em que formato estas informacoes devem ser exibidas
    publication_date = serializers.DateField(format="%d/%m/%Y")  # Formato Brasileiro
    created_at = serializers.DateTimeField(format="%d/%m/%Y as %H:%M:%S")  # Formato Brasileiro
    updated_at = serializers.DateTimeField(format="%d/%m/%Y as %H:%M:%S")  # Formato Brasileiro

    class Meta:
        model = Ebook
        fields = ["id","title", "summary", "authors", "genres", "publication_date", "num_pages", "cover_photo", "created_by", "created_at", "updated_at"]

class EbookModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ebook
        fields = ["title", "summary", "authors", "genres", "publication_date", "num_pages", "cover_photo", "created_by", "created_at", "updated_at"]  

    def validate_num_pages(self,value):
        if value is None:
            raise serializers.ValidationError("The number of pages must be provided.")
        if value < 5:
            raise serializers.ValidationError("An ebook must have at least 5 pages.")
        return value
    
    # Função de validação personalizada para verificar o formato da data
    def validate_brazilian_date(value):
        try:
            # Tenta converter o valor para um objeto datetime no formato "dd/mm/aaaa"
            datetime.strptime(value, '%d/%m/%Y')
        except ValueError:
            raise serializers.ValidationError("A data deve estar no formato dd/mm/aaaa.")
    
    created_at = serializers.ReadOnlyField()  # Auto-generated, should not be explicitly set
    updated_at = serializers.ReadOnlyField()  # Auto-generated, should not be explicitly set
    publication_date = serializers.DateField(required=False)  # Optional field
   