from rest_framework import generics
from ebooks.models import Ebook, Author, Genre
from ebooks.serializers import EbookModelSerializer, AuthorModelSerializer,GenreModelSerializer,EbookListDetailSerializer

class EbookCreateListView(generics.ListCreateAPIView):
    # permission_classes = 
    queryset = Ebook.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EbookListDetailSerializer
        return EbookModelSerializer


class EbookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookModelSerializer


class AuthorCreateListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

    
class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer
