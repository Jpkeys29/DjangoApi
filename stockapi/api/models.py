from django.db import models

# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=50)
    ticker = models.CharField(max_length= 10)
    price = models.DecimalField(max_digits=7, decimal_places=3)


# String function to name the object
def __str__(self):
    return self.name