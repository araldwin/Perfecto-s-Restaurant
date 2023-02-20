from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    people = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='menu/', blank=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name :
            self.slug = slugify(self.name)
        super(Menu , self).save(*args, **kwargs
        )


    def __str__(self):
        return self.name
