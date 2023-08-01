from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

# To override the string method of django in admin panel, for name attribute.
    def __str__(self):
        return self.name