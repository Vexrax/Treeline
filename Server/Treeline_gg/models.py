from django.db import models

# Create your models here.

class champion(models.Model):
    name = models.CharField(max_length=30)

    def __init__(self, name):
        self.isChamp = self.checkIfChampExists()
        #more data like winrates etc

    def checkIfChampExists(self):
        self.isChamp = False
