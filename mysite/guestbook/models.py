from django.db import models

# Create your models here.
class Entry(models.Model):
    entry_text = models.TextField(default="")
    name = models.CharField(max_length=200, default="")
    def __str__(self):
        return self.entry_text
