from django.db import models

# Create your models here.
class Destination(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=20)
    description = models.TextField(max_length=250)
    img1 = models.ImageField(upload_to='images',blank=True)
    img2 = models.ImageField(upload_to='images',blank=True)    
    number = models.IntegerField(default=2)

    class Meta:
        verbose_name_plural = 'Countries'
    

    def __str__(self):
        return self.country
    

class Detailed_desc(models.Model):
    dest_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=20)
    price = models.IntegerField(default=20000)
    rating = models.IntegerField(default=5)
    dest_name = models.CharField(max_length=25)
    img1= models.ImageField(upload_to='images',blank=True )
    img2 = models.ImageField(upload_to='images',blank=True )
    desc = models.TextField()

    class Meta:
        verbose_name_plural = 'Adventures'

    def __str__(self):
        return self.dest_name
    
