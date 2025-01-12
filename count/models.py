from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()

    def __str__(self):
        return self.name
