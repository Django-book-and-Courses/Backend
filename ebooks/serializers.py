from rest_framework import serializers
from ebooks.models import Ebook

class EbookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ebook
        fields = '__all__'