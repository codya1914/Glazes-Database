from django.db import models

CONE_CHOICES = [
    ("04", "04"),
    ("6", "6"),
    ("7", "7"),
    ("10", "10")
]

TRANSPARENCY_CHOICES = [
    ("Unknown", "Unknown"),
    ("Opaque", "Opaque"),
    ("Semi-translucent", "Semi-translucent"),
    ("Translucent", "Translucent"),
]

TEXTURE_CHOICES = [
    ("Unknown", "Unknown"),
    ("Glossy", "Glossy"),
    ("Matte", "Matte"),
    ("Satin", "Satin"),
]

class Glaze(models.Model):
    name = models.CharField(max_length=100)
    cone = models.CharField(
        max_length=50,
        choices = CONE_CHOICES
    )
    color = models.CharField(max_length=50, default="Unknown")
    texture = models.CharField(
        max_length=50,
        choices=TEXTURE_CHOICES
    )
    transparency = models.CharField(
        max_length=50,
        choices=TRANSPARENCY_CHOICES
    )
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
