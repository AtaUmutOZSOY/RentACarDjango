from rentacar_app import models
from rentacar_app.core.models.base_model import BaseModel
from rentacar_app.models.brand import Brand
from rentacar_app.models.brand_model import BrandModel


class Car(BaseModel):
    brand = models.ForeignKey('brand.Brand', on_delete=models.CASCADE)
    brand_model = models.ForeignKey('brand.BrandModel', on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    car_image = models.ImageField(upload_to='car_images/')

    def __str__(self):
        return f"{self.brand_model.name} - {self.description}"
