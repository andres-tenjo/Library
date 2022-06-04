from django.db import models

class AuthorsModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CategoriesModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class EditorModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BooksModel(models.Model):
    title = models.CharField('Título', max_length=100)
    subtitle = models.CharField('Subtitulo', max_length=100)
    authors = models.ManyToManyField(AuthorsModel)
    categories = models.ManyToManyField(CategoriesModel)
    published = models.DateField('Fecha publicación', blank=True, null=True)
    editor = models.ForeignKey(EditorModel, on_delete=models.CASCADE)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.title