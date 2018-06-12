import json

def getAbilityUrl(champName, abilityNum, patch):
    try:
        champIdList = json.loads(open("../www/static_data/data_files/champion_data.json").read())
        imgId = champIdList['data'][champName]['spells'][abilityNum]['image']['full']
        return "http://ddragon.leagueoflegends.com/cdn/" + patch + "/img/spell/" + imgId
    except KeyError:
        print("KeyError")
        return ""

def getChampIconUrl(champName, patch):
    return "http://ddragon.leagueoflegends.com/cdn/" + patch + "/img/champion/" + champName + ".png"



