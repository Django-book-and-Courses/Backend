from rest_framework import generics
from ebooks.models import Ebook
from ebooks.serializers import EbookModelSerializer

class EbookCreateListView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookModelSerializer

class EbookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookModelSerializer
