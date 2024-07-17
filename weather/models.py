from django.db import models

class City(models.Model):
    city_name  = models.CharField(max_length=20)
    
    def __str__(self):
        return self.city_name
