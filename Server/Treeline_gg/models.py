from django.db import models

# Create your models here.

#Tables required
##Items Table
##Champion Table?
##Best Stuff Table(Contains current common build and rune pages): This will likely be the only one accessed from front end
##Games Analyized Table

class champions(models.Model):
    champ_name = models.CharField(max_length=25)
    champ_id = models.SmallIntegerField()

class bestPractices(models.Model):
    champ_profile = models.ForeignKey(champions, on_delete=models.CASCADE)#An external key linking to the champions database
    champ_id = models.SmallIntegerField(null=False)#the id of the champ
    role_1 = models.CharField(max_length=10)#primary role
    role_2 = models.CharField(max_length=10)#secondary role
    startingItems = models.CharField(max_length=30)#Starting items ID
    finalItems = models.CharField(max_length=30) #Final items. 3 Items that are not boots
    skillingOrder = models.CharField(max_length=30)#Contains values 1-4 for q-r abilities. For first 13 levels
    rune_trees = models.CharField(max_length=30)#Contains the ID of the primary and secondary rune trees
    tree_1 = models.CharField(max_length=30)#conaints the ID of the selected runes in the primary tree
    tree_2 = models.CharField(max_length=30)#contains the ID of the selected runes in the secondary tree
    #anything else?
    #could add 3 columns which link to the items table
    #could remove champ_profile
    #could have linkers to rune table

class gamesAnalyzed(models.Model):
    entry_id = models.IntegerField(unique=True)#will be the game ID plus the participant id. This way it will be unique
    game_id = models.IntegerField()#the riot given game id
    participant_id = models.SmallIntegerField()#the riot given Participant ID
    game_length = models.BigIntegerField()#game length
    item_1 = models.SmallIntegerField() #item ids 1-6
    item_2 = models.SmallIntegerField()
    item_3 = models.SmallIntegerField()
    item_4 = models.SmallIntegerField()
    item_5 = models.SmallIntegerField()
    item_6 = models.SmallIntegerField()
    trinket = models.SmallIntegerField()#trinket id
    



