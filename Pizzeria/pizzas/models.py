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


class Post(models.Model):
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="images", blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.text
