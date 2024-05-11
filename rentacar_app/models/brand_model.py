from rentacar_app import models
from rentacar_app.core.models.base_model import BaseModel
from rentacar_app.models.brand import Brand


class BrandModel(BaseModel):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.brand.name} - {self.name}"