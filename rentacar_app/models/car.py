from django.db import models
from rentacar_app.core.models.base_model import BaseModel



class Car(BaseModel):
    brand_name = models.CharField(max_length=10)
    brand_model = models.CharField(max_length=10)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    car_image = models.ImageField(upload_to='car_images/')

    def __str__(self):
        return f"{self.brand_name} {self.brand_model} {self.description}"
