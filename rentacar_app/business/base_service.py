from typing import TypeVar, Generic, Type, Any
from django.db import models

T = TypeVar('T', bound=models.Model)

class BaseService(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    def get_all(self) -> Any:
        """Modelin tüm örneklerini getir."""
        return self.model.objects.all()

    def get_by_id(self, pk: int) -> Any:
        """Bir model örneğini ID'ye göre getir."""
        return self.model.objects.filter(pk=pk).first()

    def create(self, **kwargs) -> Any:
        """Model örneği oluştur."""
        instance = self.model(**kwargs)
        instance.save()
        return instance

    def update(self, pk: int, **kwargs) -> Any:
        """Model örneğini güncelle."""
        instance = self.model.objects.filter(pk=pk).first()
        if instance:
            for key, value in kwargs.items():
                setattr(instance, key, value)
            instance.save()
            return instance
        return None

    def delete(self, pk: int) -> bool:
        """Model örneğini sil."""
        instance = self.model.objects.filter(pk=pk).first()
        if instance:
            instance.delete()
            return True
        return False
