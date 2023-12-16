from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(f'{self.name}')
        super().save()


class Musician(models.Model):
    name_group = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    start_date = models.DateField()
    description = models.TextField(max_length=1000)
    slug = models.SlugField(max_length=255, blank=True, unique=True)

    def __str__(self):
        return f'{self.name_group}'

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(f'{self.name_group}')
        super().save()

    def get_absolute_url(self):
        return reverse('musician_detail', args=(self.slug, ))


