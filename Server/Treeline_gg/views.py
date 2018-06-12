"""The basic views file. Will serve the html pages"""
import os
import json
from django.shortcuts import HttpResponse, render
from django.http import HttpResponseRedirect
from django.template import loader
from Data_Files import getStatic as getStatic


from django.template.defaulttags import register

import Data_Files.analyzeTimeline as analyzeTimeline

patch = "8.10.1"


def index(request):
    '''
        Renders the index page.
    '''
    # get current dir
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # open champion json file
    with open(os.path.join(BASE_DIR, '../www/static_data/data_files/champs.json')) as f:
        data = json.load(f)
        data = data["data"]

    # loop through json adding id and url
    for key in data:
        data[key]["boxID"] = "champion_" + key
        data[key]["redirect"] = "/champion/" + key
        data[key]["url"] = "http://ddragon.leagueoflegends.com/cdn/" + patch + "/img/champion/" + key + ".png"
        #data[key]["url"] = "/static/icons/champions/" + key + ".png"

    #print(data)
    #create context var
    context = {
        'champions': data,
    }

    #get template
    template = loader.get_template("homePage.html")
    return HttpResponse(template.render(context, request))


def handle_search(request):
    '''
        Used for handling search requests done through the search bar in the navigation bar.
    '''
    champ = request.path[10:]
    if request.method == "POST":
        #Need some error checking

        return HttpResponseRedirect('/champion/' + request.POST.get("title", ""))
    else:
        template = loader.get_template("championpage.html")
        context = {
            'championImg': getStatic.getChampIconUrl(champ, patch),
            'Championname': champ,
            'SummonerSpell1': "http://ddragon.leagueoflegends.com/cdn/" + patch + "/img/spell/" + getSummonerSpell(champ, 1, "somerole") + ".png",
            'SummonerSpell2': "http://ddragon.leagueoflegends.com/cdn/" + patch + "/img/spell/" + getSummonerSpell(champ, 1, "somerole") + ".png",
            'QSpellImg': getStatic.getAbilityUrl(champ, 0, patch),
            'WSpellImg': getStatic.getAbilityUrl(champ, 1, patch),
            'ESpellImg': getStatic.getAbilityUrl(champ, 2, patch),
            'RSpellImg': getStatic.getAbilityUrl(champ, 3, patch),

        }

        print(request.path[10:])
        return HttpResponse(template.render(context, request))

def getSummonerSpell(champ, magnitude, role):
    return "SummonerFlash"
    #not done


def test_page(request):
    '''
        Renders whatever the current test page is
    '''
    with open('../www/static_data/data_files/example_timeline.json') as f:
        game_timeline = json.load(f)

    context = {
        'eventTimeline': analyzeTimeline.getPointsOfInterest(game_timeline),
    }
    ##end sections

    template = loader.get_template("testpage.html")
    return HttpResponse(template.render(context, request))

def load_rune_page(request):
    """A demonstration function to show what variables need to be fed to call a rune page"""
    ptree = 8200 #this will be fed in later
    stree = 8100
    with open('../www/static_data/data_files/rune_data.json') as f:
        rune_page_json = json.load(f)
    #the full runepage json needds to be loaded along with the string name of the primary and secondary rune pages
    #An iteratable list of the active runes also is required to be passed
    #this has no error checking, that should be done before passing the values
    context = {
        'runePageJSON': rune_page_json,
        'primaryTree': ptree,
        'secondaryTree': stree,
        'activeRunes': {8214, 8226, 8234, 8232, 8126, 8120},
    }
    ##end sections

    template = loader.get_template("testpage.html")
    return HttpResponse(template.render(context, request))
#create custom tags for later use
#these are just to get data from the dict created above
@register.simple_tag
def get_item(myDict, key):
    return myDict.get(key)
@register.simple_tag
def get_boxID(myDict, key):
    return myDict.get(key).get("boxID")
@register.simple_tag
def get_url(myDict, key):
    return myDict.get(key)["url"]
@register.simple_tag
def get_redirect(myDict, key):
    return myDict.get(key).get("redirect")
@register.simple_tag
def get_name(myDict, key):
    return myDict.get(key).get("name")
@register.simple_tag
def is_active_rune(active_runes, current_rune):
    for numb in active_runes:
        if numb == current_rune["id"]:
            return current_rune["id"]
    return str(current_rune["id"]) + "_greyscale"
@register.simple_tag
def get_map_left(event):
    return ((event["position"]["x"] / 15398) * 100) #this is this max x value for the map
@register.simple_tag
def get_map_top(event):
    return ((1- (event["position"]["y"] / 15398)) * 100) #this is this max y value for the map
