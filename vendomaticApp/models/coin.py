from django.db import models

class Coin(models.Model):

    """
    This class is the blueprint for instanciating the Coin Object.
    
    """

    coin_count = models.IntegerField()

    class Meta:
        verbose_name = ("coin")
        verbose_name_plural = ("coins")

    def __str__(self):
        return self.coin_count