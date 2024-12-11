from django.db import models


class Brand(models.Model):
    brand_name = models.CharField(max_length=50, unique=True)
    brand_country = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.brand_name


class Car(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='post/photos')
    year = models.IntegerField()
    price = models.IntegerField()
    horsepower = models.IntegerField()
    added = models.DateTimeField(default='2024-12-11 05:00:00')
    is_available = models.BooleanField(default=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
