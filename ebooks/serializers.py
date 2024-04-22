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
    authors = AuthorModelSerializer(many=True)  # Relacionamento Many-to-Many
    genres = GenreModelSerializer(many=True)  # Relacionamento Many-to-Many
    
    class Meta:
        model = Ebook
        fields = ["title", "summary", "authors", "genres", "publication_date", "num_pages", "cover_photo", "created_by", "created_at", "updated_at"]  

    # def get_authors(self,obj):
    #     authors = authors.obj.all()

        

    def validate_num_pages(self,value):
        if value < 5:
            raise serializers.ValidationError('Precisa ter mais de 5 páginas')
    
