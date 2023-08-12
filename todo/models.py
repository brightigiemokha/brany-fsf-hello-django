from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Item(models.Model):
    srno=models.AutoField(primary_key=True,auto_created=True)
    title=models.CharField(max_length=25)
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

# To override the string method of django in admin panel, for item name.


    def __str__(self):
        return self.name
        
