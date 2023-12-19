from django.db import models
class Watch(models.Model):
    name=models.CharField(max_length=250)
    price=models.IntegerField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name
# Create your models here.
