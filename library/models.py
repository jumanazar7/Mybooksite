from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    desc = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    full_name = models.CharField(max_length=255)
    bio = models.TextField()
    image = models.ImageField(upload_to="authors")
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.ImageField(upload_to="books")
    genres = models.ManyToManyField(Genre)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    stars = models.FloatField(verbose_name="Reyting")
    isbn_number = models.PositiveBigIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
