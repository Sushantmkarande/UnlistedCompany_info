from django.db import models

# Create your models here.


class Data(models.Model):
    Name = models.CharField(max_length=30)
    Domain = models.CharField(max_length=50)
    Facebook = models.CharField(max_length=50)
    Instagram = models.CharField(max_length=50)

    def __str__(self):
        return self.Name
