import graphene
from graphene_django.types import DjangoObjectType
from books.models import *

class AuthorsType(DjangoObjectType):
    class Meta:
        model = AuthorsModel
        fields = '__all__'

class CategoriesType(DjangoObjectType):
    class Meta:
        model = CategoriesModel
        fields = '__all__'

class EditorType(DjangoObjectType):
    class Meta:
        model = EditorModel
        fields = '__all__'

class BooksType(DjangoObjectType):
    class Meta:
        model = BooksModel
        fields = '__all__'

class Query(object):
    all_authors = graphene.List(AuthorsType)
    all_categories = graphene.List(CategoriesType)
    all_editors = graphene.List(EditorType)
    all_books = graphene.List(BooksType)
    
    def resolve_all_authors(self, info, **kwargs):
        return AuthorsModel.objects.all()
    
    def resolve_all_categories(self, info, **kwargs):
        return CategoriesModel.objects.all()
    
    def resolve_all_editors(self, info, **kwargs):
        return EditorModel.objects.all()

    def resolve_all_books(self, info, **kwargs):
        return BooksModel.objects.all()