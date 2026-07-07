from django.db import models

class Glaze(models.Model):
    name = models.CharField(max_length=100)
    cone = models.CharField(max_length=20)
    color = models.CharField(max_length=50, default="Unknown")
    surface = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.color:
            self.color = "Unknown"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GlazeIngredient(models.Model):
    glaze = models.ForeignKey(Glaze, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    unit = models.CharField(max_length=20, default="percent")

    def __str__(self):
        return f"{self.glaze.name} - {self.ingredient.name}"
