from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    class Meta:
        verbose_name_plural = 'Countries'
    

    def __str__(self):
        return self.name
    

class Adventure(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

