from django.db import models

# Create your models here.

class champion:
    def __init__(self, name):
        self.isChamp = self.checkIfChampExists()
        self.name = name
        #more data like winrates etc

    def checkIfChampExists(self):
        self.isChamp = False
