from django.db import models


class Glaze(models.Model):
    CONE_CHOICES = [
        ("04", "Cone 04"),
        ("6", "Cone 6"),
        ("7", "Cone 7"),
        ("10", "Cone 10"),
    ]

    TEXTURE_CHOICES = [
        ("Glossy", "Glossy"),
        ("Matte", "Matte"),
        ("Satin", "Satin"),
    ]

    TRANSPARENCY_CHOICES = [
        ("Opaque", "Opaque"),
        ("Semi-translucent", "Semi-translucent"),
        ("Translucent", "Translucent"),
    ]

    name = models.CharField(max_length=100)
    cone = models.CharField(max_length=10, choices=CONE_CHOICES)
    texture = models.CharField(max_length=50, choices=TEXTURE_CHOICES)
    transparency = models.CharField(max_length=50, choices=TRANSPARENCY_CHOICES)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class GlazeIngredient(models.Model):
    glaze = models.ForeignKey(
        Glaze,
        on_delete=models.CASCADE,
        related_name="ingredients"
    )
    name = models.CharField(max_length=100, blank=True)
    amount = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.name} - {self.amount}"


class GlazePhoto(models.Model):
    glaze = models.ForeignKey(
        Glaze,
        on_delete=models.CASCADE,
        related_name="photos"
    )
    image = models.ImageField(upload_to="glaze_photos/")
    caption = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Photo for {self.glaze.name}"


class GlazeVariant(models.Model):
    glaze = models.ForeignKey(
        Glaze,
        on_delete=models.CASCADE,
        related_name="variants"
    )
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.glaze.name} - {self.name}"


class VariantAdditive(models.Model):
    variant = models.ForeignKey(
        GlazeVariant,
        on_delete=models.CASCADE,
        related_name="additives"
    )
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.amount}"


class VariantPhoto(models.Model):
    variant = models.ForeignKey(
        GlazeVariant,
        on_delete=models.CASCADE,
        related_name="photos"
    )
    image = models.ImageField(upload_to="variant_photos/")
    caption = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Photo for {self.variant.name}"