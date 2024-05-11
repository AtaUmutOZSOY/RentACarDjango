from django.db import models
from rentacar_app.core.models.base_model import BaseModel

class Brand(BaseModel):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class BrandModel(BaseModel):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.brand.name} - {self.name}"

class Car(BaseModel):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    brand_model = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    car_image = models.ImageField(upload_to='car_images/')

    def __str__(self):
        return f"{self.brand_model.name} - {self.description}"
