from django.db import models


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique=True)
    mobile_no = models.IntegerField()
    password = models.CharField(max_length=50)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    def __str___(self):
        return self.name