from django.db import models

class Beverage (models.Model):

    """
    This class is the blueprint for instanciating the Beverage Object.
    
    """

    name = models.CharField(max_length=50)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = ("beverage")
        verbose_name_plural = ("beverages")

    def __str__(self):
        return self.name

    
