from typing import Any, List, Type, TypeVar, Generic, Optional
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

# Model tipini genel bir tür değişkeni olarak tanımlayın.
T = TypeVar('T', bound=models.Model)

class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T]):
        """Model parametresi, repository'nin işleyeceği model sınıfını belirtir."""
        self.model = model

    def get_all(self) -> List[T]:
        """Modelin tüm örneklerini getir."""
        return self.model.objects.all()

    def get_by_id(self, id: int) -> Optional[T]:
        """Verilen ID'ye göre model örneğini getir. Eğer bulunamazsa None döner."""
        try:
            return self.model.objects.get(pk=id)
        except ObjectDoesNotExist:
            return None

    def create(self, **kwargs) -> T:
        """Yeni bir model örneği oluştur ve veritabanına kaydet."""
        instance = self.model(**kwargs)
        instance.save()
        return instance

    def update(self, id: int, **kwargs) -> Optional[T]:
        """Verilen ID'ye göre model örneğini güncelle. Eğer model bulunamazsa None döner."""
        instance = self.get_by_id(id)
        if instance is None:
            return None
       
