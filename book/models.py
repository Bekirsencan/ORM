from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    objects = models.Manager()

    class Meta:
        db_table = 'Category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    about = models.TextField(max_length=1000, null=True)
    price = models.FloatField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="related place",
    )

    objects = models.Manager()

    class Meta:
        db_table = 'books'
        verbose_name = 'book'
        verbose_name_plural = "Books"
