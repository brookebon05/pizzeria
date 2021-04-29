from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Toppings(models.Model):
    name = models.CharField(max_length=200)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Toppings"

    def __str__(self):
        return self.name
