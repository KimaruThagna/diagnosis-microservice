from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
# Create your models here.

class Diagnosis(models.Model):
    diagnosis = models.TextField(max_length=2000)
    consulting_doctor = JSONField()
    visiting_patient = JSONField()

    def __str__(self):
        return self.diagnosis