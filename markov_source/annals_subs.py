#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

import string
from types import *

def do_subs(text):

    #if type(text) != UnicodeType:
    #    text = unicode(text, encoding="UTF-8") #.encode("UTF-8")
    #text = text.decode('utf-8', 'ignore')

    known_places = [
        "Turfthorpe",
        "Scarwell",
        "Eagleborn",
        "Booknesford",
        "Boltmere",
        "East Bellwood",
        "Castle Becclesthwaite",
        "Cleavestead",
        "Bankton",
        "Broadhowe",
        "Midcombe",
        "Cheriton Magna",
        "Stagby",
        "Bannermill",
        "Castle Shadowhythe",
        "Lower Fugglehithe",
        "Sheriff's Kesthorpe",
        "Finchkirk",
        "Birchhampton",
        "Birchhampton County",
        "Hesslechester",
        "Tweedmore",
        "Brewood",
        "Ravencester Way",
        "Bredark",
        "Crenchcastle Manor",
        "Sheriff's Tweedchester",
        "Stancaster",
        "Broadhowe",
        "Cherryfoot",
        "Cheesemouth",
        "Marefettle",
        "Horsecester-under-Curse",
        "Lower Peterworthy",
        "Dupminster Widdershins",
        "Stonekirk Moor",
        "Rothing",
        "Harecastle",
        "Waltberry End",
        "Colyborough",
        "Pilgrim's Hogberry",
        "Inglecaster-under-Curse",
        "Daxbridge",
        "Tangleëmp",
        "Rughithe",
        "Blisschurch",
        "Sprinfand Convent",
        "Holyminster Arms",
        "Wootton Stanhithe",
        "Sheriff's Manninfield",
        "Elderforke",
        "Brackirk-on-Sea",
        "Bookfield",
        "Axhurst Tower",
        "Accemarch",
        "Latchbex",
        "West Duckomp",
        "Beaconmouth",
        "Samcester Tollgate",
        "Wornchurch",
        "Croycork",
        "Cloutford",
        "Elderbridge",
        "Drumhythe",
        "New Conniswittle",
        "North Bookmouth",
        "Holymore",
        "Blandforke",
        "Invermouth",
        "Furzeloch",
        "Tweedwick",
        "Midstead",
        "Emchurch",
        "Middleminster",
        "Emport",
        "Shammore",
        "Barrowmount",
        "Blythestink",
        "Waltcot",
        "Stagthwaite",
        "Enchstoke",
        "Minchenbrooke Wells",
        "Stoton-on-Op",
        "Danefield",
        "Latchster",
        "Lost Drinchham",
        "Shadowicke Crossroads",
        "Adderfarthing",
        ]

    known_counties = [
        "Grindark Shire",
        "Floodcester Shire",
        "Ravenworthy County",
        "Blissthicke Shire",
        "Birchhampton County",
        "Bearcaster Shire",
        "Brackburton Duchy",
        "Minehampton County",
        "Eagleberg County",
        "Beetlewick Duchy",
        "Weyside Shire",
        "Briarden County",
        "Ottersex",
        "Amblebrook",
        "Basestoke Shire",
        "Shareloch County",
        "Addermarch",
        "Flamewick Shire",
        "Richfield Shire",
        "Houncaster Duchy",
        ]

    known_rivers = [
        "Edle",
        "Pork",
        "Worn",
        "Retch",
        "river Em",
        "river Op",
        "Em",
        "Op",
        ]

    known_pubs = [
        "The Hummingbird Arms",
        "Ginger and Castle",
        "Sign of the Taupe Ox",
        "The Riding Horse Inn",
        "Calf and Compasses",
        "The Stallion Inn",
        "The Almond Heather",
        "Sign of the Silver Mule",
        "Ostrich and Compasses",
        "Tarragon and Blade",
        "Mango-Ginger and Saw",
        "Sign of the Aerosol Mare",
        "Snail and Sarsaparilla",
        "Fenugreek and Sponge",
        "The Pigeon Inn",
        "Mule and Woodruff",
        "Sign of the Cleric Stallion",
        "Rat and Alligator Pepper",
        "Nightingale and Parsley",
        "The Badger Arms",
        "Thyme and Compasses",
        "Sign of the Exasperated Hound",
        "The Lark Inn",
        "The Modernized Bluebell",
        "The Lacklustre Goat",
        "The Taupe Tentpeg",
        "The Beige Castle",
        "The Uncapped Ox",
        "The Whirlwind Dahlia",
        "Calf and Cubeb",
        "Mare and Hemp",
        "The Vegetative Mouse",
        "Lark and Hemp",
        "Garlic Chives and Tentpeg",
        "Sign of the Eggshell Trout",
        "Chicken and Angelica",
        "The Formulaic Gerbera Daisy",
        "Sign of the Registering Carthorse",
        "Sign of the Ruby Turtle",
        "Sign of the Tanked Lamb",
        "The Ground-Line Hitch",
        "Sign of the Cream Stallion",
        "Cress and Castle",
        "The Caribou Inn",
        "The Sticky Gull",
        "Sign of the Subjugated",
        "The Chicken Arms",
        "The Retiring Stallion",
        "The Bowen Knot",
        "Mare and Compasses",
        "Sign of the Stooped Mouse",
        "The Hitless Daffodil",
        "Camel and Sansho",
        "Black Peppercorn and Grinder",
        "Stallion and Sansho",
        "Dog and Cress",
        "Lavender and Compasses",
        "Gecko and Pepperpot",
        "The Mare Arms",
        "The Scrofulous Kangaroo",
        "The Badger Inn",
        "Ostrich and Fingerroot",
        ]

    known_people = [
        "The Duke of Grindark Shire",
        "Juliana Bondeville II",
        "Duchess of Scarwell",
        "King Aethel",
        "Jeannette Parrigue",
        "Gavin Caillot",
        "Jacob Marches",
        "Godiva Viville",
        "Asher Brinon",
        "Jonas Le Cordier",
        "Silvanus",
        "Althalos Port",
        "Richard le Gaucher the Younger",
        "Rowan Goulaffre Junior",
        "Wihtred",
        "Matilde Taillebois",
        "Rafe l'Estourmi II",
        "The Ducal Personage of Blissthicke Shire",
        "Adam de Savage",
        "Beatrix Wadard",
        "Jacob Darell the Older",
        "Berinon Culai",
        "John the Amino",
        "Elanor Torteval",
        "Oswitha Boislevesque",
        "Elanor d'Ecouis",
        "the Ducal Personage",
        "Seraphina Addinell",
        "Doran Couci the Older",
        "Tybalt Vauville",
        "Cedric d'Orbec",
        "The Ducal Personage of Brackburton Duchy",
        "Maria de Coucy",
        "Terrin the Proportionate",
        "Ryia Esteney",
        "King Escwulf",
        "The Duchess",
        "the King under the Mountain",
        "Leo Boivin the Older",
        "Richard du Bec",
        "Abbot Benedict",
        "Jonas Digby",
        "Alys the Defenseless",
        "The Duke of Beetlewick Duchy",
        "Sequana",
        "Cassius de Recusson",
        "the High Priestess of Saint Isaac",
        "Richard Cumin",
        "King Caedwalla",
        "Farfelee Fitton",
        "Tristan the Bounding",
        "Jed De Berchelai",
        "Edwina Ballard",
        "King Ethelwulf",
        "King Edwin",
        "Eanfleda",
        "Adam Meri the Older",
        "Elanor Le Sueur",
        "Asher the Barreled",
        "The Duke of Ottersex",
        "Jeanette Parrigue",
        "John Grimoult",
        "Oswitha Basset the Older",
        "Maria de Vaux",
        "Matilde the Pronged",
        "Phyllis the Brawling",
        "Ronald the Pedestrian",
        "Donald Percy",
        "Jack the Aligned",
        "John Hachet",
        "Cristiana the Heart-shaped",
        "Mirabelle le Bouguignon",
        "Jonas Osmond",
        "Fendrel Grai",
        "Letholdus Strivelyn",
        "Hengest",
        "Horsa",
        "Wurtgern",
        "Leofrick Maignart",
        "Will Falaise",
        "Elaine Saisset",
        "Oswitha Vis-de-Louf",
        "Matilde Quièvremont",
        "Elaine Roger",
        "Berinon the Progressive",
        "Wallace Rome",
        "Aethelwall",
        "Escs",
        "Jacob the Outlaw",
        "Josselyn Pennant",
        "Peter Faucon",
        "Rowan Paixdecoeur",
        "the High Priestess of Parra",
        "Parra",
        "Centwall",
        "Ethels",
        "Obadiah Raleigh",
        "the High Priest of the daemon of purpose",
        "Leofrick la Riviere",
        "The Duke of Houncaster Duchy",
        "Cerdbert",
        "Edwin",
        "Ethelwulf",
        ]

    misc_subs = [
        ["Warning: ", ""], # too jarring when it appears in our output text. Trim it out...
        ]



    for person in known_people:
        if string.find(text, person) >-1:
            text = string.replace(text, person, "[PERSON]")

    for county in known_counties:
        if string.find(text, county) >-1:
            text = string.replace(text, county, "[COUNTY]")

    for pub in known_pubs:
        if string.find(text, pub) >-1:
            text = string.replace(text, pub, "[PUB]")

    for place in known_places:
        if string.find(text, place) >-1:
            text = string.replace(text, place, "[PLACE]")

    for river in known_rivers:
        if string.find(text, river) >-1:
            text = string.replace(text, river, "[RIVER]")

    for sub in misc_subs:
        if string.find(text, sub[0]) >-1:
            text = string.replace(text, sub[0], sub[1])

    #strip out headings... they aren't required in our Guide
    #skiplines = [u"Lodging", u"Dining", u"Excursions", u"Transportation", u"Residency", u"Commerce"]
    skiplines = ["Lodging", "Dining", "Excursions", "Transportation", "Residency", "Commerce"]
    newtext = ""
    for line in text.split("\n"):
        line = line.strip()
        if line in skiplines:
            newtext = "%s\n" % newtext
        elif line in known_places:
            newtext = "%s\n" % newtext
        elif line in ("", "\n"):
            pass 	# strim out blank lines
        else:
            #doesn't have to be pretty - only going to be used for input...
            if newtext == "":
                newtext = line
            else:
                newtext = "%s %s" % (newtext,line)
    text = newtext

    return text

if __name__ == "__main__":
    import os
    text = open(os.path.join("raw", "annals.txt")).read()
    text = do_subs(text)
    print text
