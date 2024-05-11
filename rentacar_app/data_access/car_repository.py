from typing import Type
from rentacar_app.data_access.base_repository import BaseRepository
from rentacar_app.models import Car


class CarRepository(BaseRepository[Car]):
    def __init__(self, model: Car):
        super().__init__(model)