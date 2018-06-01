"""this module will try and determine the role of the player"""
import json
# Soooo.... what do ya think about neural netting this thing lol


def determineRole(game_timeline, game_data, participant_id):
    # We will first determine if comp is running support meta. TO do this we will check if a player is lacking flash
    # If it is support meta, the smite champ will be carry and remainder will be bot
    # If not support meta then smite will be jungler and x,y will be used for final two
    # To improve recognition check for support items from the possible support
    is_carry_comp = False
   
    #Check which team the person we are analyzing is on
    team = 1
    if participant_id > 3:
        team = 2 
    
    for i in range((3*team) - 3, (3*team)):
        current_participant_data = game_data["participants"][i]
        # Flash spell id is 4
        if current_participant_data["spell1Id"] != 4 and current_participant_data["spell2Id"] != 4:
            is_carry_comp = True
    
    current_participant_data = game_data["participants"][participant_id - 1]
    if (is_carry_comp):
        #Smite id is 11
        if current_participant_data["spell1Id"] == 11 or current_participant_data["spell2Id"] == 11:
            return "Hyper"
        
        if current_participant_data["spell1Id"] != 4 and current_participant_data["spell2Id"] != 4:
            return "Support"
        
        return "Bottom"
    
    #if it is hyper comp then it will have returned by now. 
    # So we can just default check for jungle now
    if current_participant_data["spell1Id"] == 11 or current_participant_data["spell2Id"] == 11:
        return "Jungle"


    other_participant_id = 0
    for i in range((3*team) - 3, (3*team)):
        #get id of other laner
        temp_particiapnt_checker = game_data["participants"][i]
        if temp_particiapnt_checker["spell1Id"] != 11 and temp_particiapnt_checker["spell2Id"] != 11 and i + 1 != participant_id:
            other_participant_id = i + 1
            break
    if(other_participant_id == 0):
        #unable to find othe participant for some reason
        return "Undetermined"
    
    votes_for_bottom = 0
    votes_for_top = 0
    for i in range(1, 4):
        #loop through time frames 1 to 3 and see who is lower on the frame
        current_frame = game_timeline["frames"][i]["participantFrames"]
        if(current_frame[str(participant_id)]["position"]["y"] > current_frame[str(other_participant_id)]["position"]["y"]):
            votes_for_top += 1
        else:
            votes_for_bottom += 1
    if(votes_for_top > votes_for_bottom):
        return "Top"
    return "Bottom"


def getStartingItems(game_timeline, participant_id):
    #get items purchased between 0 and 60 seconds
    frame = game_timeline["frames"][1]
    events = frame["events"]
    items = []
    for event in events:
        try:
            event["participantId"]
        except KeyError:
            continue
        if event["participantId"] == participant_id:
            try:
                if event["type"] == "ITEM_PURCHASED":
                    items.append(event["itemId"])
                if event["type"] == "ITEM_SOLD" or event["type"] == "ITEM_DESTROYED":
                    items.remove(event["itemId"])
            except ValueError:
                print("Error removing item from list")
    if(len(items) == 0):
        return ""
    itemString = ""
    for i in range(0, len(items) - 1):
        itemString += str(items[i]) + ", "
    
    itemString += str(items[len(items) - 1])
    return itemString

def getPointsOfInterest(game_timeline):
    #Currently checks for champion and building kills
    eventLine = []
    for x in eventLine:
        print(x['a'])
    for frame in game_timeline["frames"]:
        for event in frame["events"]:
            if(event["type"] == "CHAMPION_KILL"):
                eventLine.append(event)
            elif(event["type"] == "BUILDING_KILL"):
                eventLine.append(event)
    return eventLine    

# Testing
# game = ""
# timeline = ""
# with open("../../../www/static_data/data_files/example_game_json.json") as gameJson:
#     game = json.load(gameJson)

# with open("../../../www/static_data/data_files/example_timeline.json") as timelineJson:
#     timeline = json.load(timelineJson)

# print(determineRole(timeline, game, 4))


# with open("../../../www/static_data/data_files/example_timeline.json") as gameJson:
#     game = json.load(gameJson)

# getPointsOfInterest(game)
