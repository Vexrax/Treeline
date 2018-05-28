"""this module will try and determine the role of the player"""
import riotAPIReference

# Soooo.... what do ya think about neural netting this thing lol

def determineRoleWithGameID(game_id, game_data, participant_id):
    game_timeline = riotAPIReference.getTimelineWithMatchID(game_id)
    #lol now do stuff