from django.db import models

class Post(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    idcat = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre