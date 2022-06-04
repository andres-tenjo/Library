import graphene
from graphene_django.types import DjangoObjectType
from books.models import BooksModel

class BooksType(DjangoObjectType):
    class Meta:
        model = BooksModel

class Query(object):
    all_books = graphene.List(BooksType)
    
    def resolve_all_books(self, info, **kwargs):
        return BooksModel.objects.all()