from django.db import models

class Fruit(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    is_delicious = models.BooleanField(default=True)

    def __str__(self):
        return self.name
