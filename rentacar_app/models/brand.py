from rentacar_app import models
from rentacar_app.core.models.base_model import BaseModel


class Brand(BaseModel):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name