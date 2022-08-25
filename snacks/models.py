from django.db import models

# Create your models here.
class Snack(models.Model):
    name = models.CharField(max_length=256)
    # more to be added here soon
    #
    #
    #
    
    # conventional?
    def __str__(self):
        return self.name