from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from decimal import Decimal


class Food(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    featured_image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(blank=True, null=True)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=Decimal('0.00')
        )
    num_ratings = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Food, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
