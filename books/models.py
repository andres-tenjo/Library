from django.db import models

class BooksModel(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)

    def __str__(self):
        return self.title
