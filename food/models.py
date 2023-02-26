from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    featured_image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Food, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


