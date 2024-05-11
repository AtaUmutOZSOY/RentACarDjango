from typing import Type
from rentacar_app.business.base_service import BaseService
from rentacar_app.models import Car


class CarService(BaseService[Car]):
   def __init__(self, model: Car):
      super().__init__(model)
    