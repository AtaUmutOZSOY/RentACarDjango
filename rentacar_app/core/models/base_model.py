from django.db import models

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)  # Use AutoField for automatic ID generation
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True