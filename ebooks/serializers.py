from rest_framework import serializers
from ebooks.models import Ebook,Author,Genre

class EbookModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ebook
        fields = '__all__'

    # def validate_num_pages(self,value):
    #     if value < 5:
    #         raise serializers.ValidationError('Precisa ter mais de 5 páginas')
    
class AuthorModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = '__all__'
        
    def validate_first_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("O nome deve ter pelo menos 2 caracteres")
        return value
    