from rest_framework import viewsets
from books.api import serializes
from books import models


class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = serializes.BooksSerializer
    queryset = models.Books.objects.all()
