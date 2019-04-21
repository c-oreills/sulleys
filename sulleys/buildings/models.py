from django.db import models

from taggit_autosuggest.managers import TaggableManager

class Building(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    catalogue_number = models.CharField(blank=True, max_length=20)

    description = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    main_image = models.ImageField()

    location = models.CharField(blank=True, max_length=200)

    tags = TaggableManager()

    def __str__(self):
        return f'Building {self.pk} ({self.name})'