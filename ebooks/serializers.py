from rest_framework import serializers
from ebooks.models import Ebook

class EbookModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ebook
        fields = '__all__'