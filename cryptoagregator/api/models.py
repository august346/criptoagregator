from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Storage(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, related_name='storages', on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.user.username, self.name)


class Coin(models.Model):
    symbol = models.CharField(max_length=6)
    value = models.DecimalField(max_digits=15, decimal_places=6)
    storage = models.ForeignKey(Storage, related_name='coins', on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {}'.format(self.storage.user.username, self.storage.name, self.symbol)
