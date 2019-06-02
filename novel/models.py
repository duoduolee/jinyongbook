from django.db import models

# Create your models here.
class Novel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        managed = True
        db_table = 'novel'

