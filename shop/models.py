from django.db import models


class Course(models.Model):
    cover = models.ImageField(upload_to='images', blank=True, null=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    price = models.FloatField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

