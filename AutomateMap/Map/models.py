from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField(max_length=255, unique=True, null=False)
    longitude = models.FloatField(max_length=255, unique=True, null=False)
    image1 = models.FileField(max_length=255, unique=True, null=False)
    image2 = models.FileField(max_length=255, unique=True, null=False)
    town = models.CharField(max_length=255, null=False)
    country = models.CharField(max_length=255, default="Nigeria")
    description = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = "Places"
        ordering = ("name",)

    def __str__(self):
        return "Kogi State Polytechic " + self.name + " - " + self.town + " - " + self.country

    # def get_absolute_url(self):
    #     return reverse('index')
