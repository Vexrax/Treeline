from django.db import models

# Create your models here.

#Tables required
##Items Table
##Champion Table?
##Best Stuff Table(Contains current common build and rune pages): This will likely be the only one accessed from front end
##Games Analyized Table

'''
Model for all the champion static data, this should only be modified when we dont have the data for a champion
'''
class champions(models.Model):

    champ_name = models.CharField(max_length=25)
    champ_id = models.SmallIntegerField()

    QName = models.CharField(max_length=30)
    WName = models.CharField(max_length=30)
    EName = models.CharField(max_length=30)
    RName = models.CharField(max_length=30)

    QUrl = models.TextField()
    WUrl = models.TextField()
    EUrl = models.TextField()
    RUrl = models.TextField()


class bestPractices(models.Model):
    event_id = models.IntegerField(unique=True, primary_key=True)
    #champ_profile = models.ForeignKey(champions, on_delete=models.CASCADE)#An external key linking to the champions database
    champ_id = models.SmallIntegerField(null=False)#the id of the champ
    winrate = models.FloatField(default=0)
    playrate = models.FloatField(default=0)
    games_played = models.IntegerField(default=0)
    role_type = models.CharField(max_length=10)# Primary or Secondary
    role = models.CharField(max_length=10)# Role
    starting_items = models.CharField(max_length=30)#Starting items ID
    final_items = models.CharField(max_length=30) #Final items. 3 Items that are not boots
    skilling_order = models.CharField(max_length=30)#Contains values 1-4 for q-r abilities. For first 13 levels
    rune_trees = models.CharField(max_length=30)#Contains the ID of the primary and secondary rune trees
    tree_1 = models.CharField(max_length=30)#conaints the ID of the selected runes in the primary tree
    tree_2 = models.CharField(max_length=30)#contains the ID of the selected runes in the secondary tree
    #anything else?
    #could add 3 columns which link to the items table
    #could remove champ_profile
    #could have linkers to rune table

class gamesAnalyzed(models.Model):
    entry_id = models.IntegerField(unique=True, primary_key=True)#will be the game ID plus the participant id. This way it will be unique
    game_id = models.IntegerField()#the riot given game id
    participant_id = models.SmallIntegerField()#the riot given Participant ID
    champ_id = models.SmallIntegerField()
    role = models.CharField(max_length=15, default="")
    win = models.BooleanField()
    champion_level = models.SmallIntegerField()
    game_length = models.IntegerField()
    game_rank = models.CharField(max_length=20, default="")
    #Summoners
    summoner_spell_1 = models.SmallIntegerField()
    summoner_spell_2 = models.SmallIntegerField()
    #Items
    item_1 = models.SmallIntegerField() #item ids 1-6
    item_2 = models.SmallIntegerField()
    item_3 = models.SmallIntegerField()
    item_4 = models.SmallIntegerField()
    item_5 = models.SmallIntegerField()
    item_6 = models.SmallIntegerField()
    trinket = models.SmallIntegerField()#trinket id

    starting_items = models.CharField(max_length=50, default="") # contains a comma seperated list of starting item ids

    #Money
    gold_earned = models.SmallIntegerField()
    #gold_spent = models.SmallIntegerField()
    cs = models.SmallIntegerField()
    neutral_minions_killed = models.SmallIntegerField()
    neutral_minions_killed_team_jungle = models.SmallIntegerField()
    neutral_minions_killed_enemy_jungle = models.SmallIntegerField()

    #KDA
    kills = models.SmallIntegerField()
    deaths = models.SmallIntegerField()
    assists = models.SmallIntegerField()

    #Combat
    #Damage Dealt
    total_damage_dealt = models.IntegerField()
    physical_damage_dealt = models.IntegerField()
    magic_damage_dealt = models.IntegerField()
    true_damage_dealt = models.IntegerField()
    total_damage_dealt_to_champions = models.IntegerField()
    physical_damage_dealt_to_champions = models.IntegerField()
    magic_damage_dealt_to_champions = models.IntegerField()
    true_damage_dealt_to_champions = models.IntegerField()
    damage_to_objectives = models.IntegerField()
    #Damage Taken
    total_damage_taken = models.IntegerField()
    physical_damage_taken = models.IntegerField()
    magic_damage_taken = models.IntegerField()
    true_damage_taken = models.IntegerField()
    #Other
    cc_duration  = models.SmallIntegerField()
    total_healing  = models.SmallIntegerField()
    #Runes
    primary_tree = models.SmallIntegerField()
    secondary_tree = models.SmallIntegerField()
    rune_1 = models.SmallIntegerField()
    rune_2 = models.SmallIntegerField()
    rune_3 = models.SmallIntegerField()
    rune_4 = models.SmallIntegerField()
    rune_5 = models.SmallIntegerField()
    rune_6 = models.SmallIntegerField()
    #Skilling Order
    skilling_order = models.CharField(max_length=35, default="")


    



