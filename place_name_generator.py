#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

#place_name_generator.py

__VERSION__ = "0.3h"

import random
import sys, string

class Town:

    def __init__(self):
        self.name = None
        self.description = []
        self.MC_attitude_to = 0

    def populate(self):
        self.name = make_name(VERBOSE=0, LOG=0)
        self.MC_attitude_to = random.choice((-1, 1))
        num_description_words = 4
        if self.MC_attitude_to == -1:
            #use negative words
            #use list to make a copy of the original
            poss_descriptions = list(description_words_bad)
        elif self.MC_attitude_to == 1:
            #use positive words
            #use list to make a copy of the original
            poss_descriptions = list(description_words_good)
        for f in range(0, num_description_words):
            word = random.choice(poss_descriptions)
            poss_descriptions.remove(word)
            self.description.append(word)
        self.description.sort()

    def get_description(self):
        if self.description != None:
            posswords = list(self.description)
            word1 = random.choice(posswords)
            posswords.remove(word1)
            word2 = random.choice(posswords)
            return random.choice(("%s and %s" % (word1, word2),
                                 "%s, %s" % (word1, word2)))

    def __repr__(self):
        return """name:\t%s
description:\t%s
MC_attitude_to:\t%s""" % (self.name, self.description, self.MC_attitude_to)


root_words=[
    "Ac",       # Accrington,Acomb, Acton, Matlock
    "Stock",    # Stockwell, Stockton
    "Brix",     # Brixton, Brixham
    "Vaux",
    "Clopp",
    "Clap",
    "Comp",
    "Camber",
    "Cam",
    "Hoddes",
    "Lon",
    "Lun",
    "Mer",
    "Mere",
    "Nott",     # Nottingham
    "Craw",     # Crawley
    "Pen",
    "Man",      # Manchester, Manston, Mansfield
    "Mor",
    "Dean",
    "Dene",
    "Farn",     # Farnham
    "Rother",   # Rotherham
    "Ber",      # Bermondsey, Berwick
    "Cat",      # Catford
    "Catt",
    "Pus",
    #"Pudding",
    "Pud",
    #"Custard",
    "Cust",
    "Pie",
    "Ayles",    # Aylesbury
    "Lan",      # Lancaster
    "Chi",      # Chichester
    "Chis",     # Chiswick
    "Chin",
    "Prest",
    "Beck",
    "Avon",     # Avon is a common river name in England. Avon is the old Celtic word for river
    "Grin",     # East Grinstead
    "Wal",
    "Coven",    # Coventry
    "Rush",
    "Whit",     # WHITCHURCH is a common place name. It means white church (because the church was made of white stone)
    "Nor",      # Norwich
    "Green",    # Greenwich
    "Gat",      # Gatwick
    "Chis",     # Chiswick
    "Tam",      # Tamworth
    "Wim",      # Wimbledon
    "Bar",      # Barking
    "Bex",      # Bexley, Bexhill-on-Sea (Old English, box, the tree)
    "Black",
    "Brom",     # Bromley It was broom leah or clearing where broom grew
    "Crickle",  # Cricklewood
    "Croy",     # Croydon
    "En",       # Enfield (from the Saxon Eana's feld)
    "Finch",    # Finchley
    "Hack",     # Hackney
    "Hamp",     # Hampstead (name meant homestead)
    "Kings",    # Kingston (Kingston Upon Thames was once the king's tun or estate)
    "Ave",
    "Lam",
    "Lamb",
    "Mus",      # Muswell Hill (Muswell is derived from words meaning mossy spring)
    "Plum",     # Plumstead The Saxon word stede meant place or farm
    "Rich",     # Richmond
    "Sur",      # Surbiton
    "Ted",      # Teddington
    "Wan",      # Wanstead, Wandsworth
    "Crox",     # Croxley
    "Alders",   # Aldersgate
    "Aber",     # Aberystwyth, Aberdeen, Abergavenny
    "Ast",	    # Aston, Astley (means "east")
    "Whit",     # Whitby
    "Sel",      # Selby
    "Cros",     # Crosby
    "Form",     # Formby,
    "Cor",      # Corby
    "Dun",      # Dundee, Dungannon, Donegal, Dundalk, Dundrum (means "fort")
    "Dum",      # Dumbarton, Dumfries,
    "Brad",     # Bradford
    "Wat",      # Watford
    "Castle",   # Castleford
    "Bux",      # Buxton, Burford,
    "Dork",     # Dorking
    "Bark",     # Barking
    "Pen",      # Penzance, Pendle, Penrith, Penarth, Pencoed, Penmaen, Pengam, Penffordd, Pembrokeshire, Pen-y-gwryd
    "Shep",     # (Old English for "sheep") Shepshed, Shepton Mallet
    "Ship",     # (Old English for "sheep") Shipton, Shipley
    "Stan",	    # (Old English for stone, stony) Stanmore, Stamford, Stanlow
    "Ax",       # Axminster
    "Ex",       # Exeter, River Exe, Exemoor
    "Becon",    # Becontree, Bekonscot
    "Ken",      # Kennington, Kensal Green, Kensington, Kentish Town, Kenton
    "Crud",     # Crudwell
    "Buckle",   # Upper Bucklebury
    "Mud",      # Mudford Sock
    "Cock",     # Cockshot
    "Crap",     # Crapstone, Devon
    "Ac",       # Acton
    "Ald",      # Aldgate
    "Bal",      # Balham
    "Drum",
    "Totten",   # Tottenham, Tottenham Hale
    "Totter",   # Totteridge & Whetstone
    "Uck",      # Uckfield
    "Mort",     # Mortlake
    "Pig",
    "Pock",
    "Scars",
    "Broad",
    "Bliss",
    "Fuggle",
    "Birch",
    "Ash",
    "Crench",
    "Stane",
    "Dax",
    "Rut",      #Rutland
    "Hamble",   #Hambleton
    "Wych",     #Wychavon, Wychwood
    "Waver",    #Waverley
    "Wat",      #Watford
    "Tweed",
    "Barrow",
    "Bar",
    "Horn",     #Hornchurch, Hornsey
    "Bog",      #Bognor
    "New",      #Newton
    "Wood",     #Woodside, Wood Side, Woodford
    "Burn",     #Burnside
    "Burne",    #Burnside
    "Cro",     
    "Crow",     #Crowthorne, Crowhurst
    "Green",    #Greenford, Greenhill, Green Hill
    "Ribble",   #Ribble valley
    "Rib",      #Ribble valley
    "Med",      #Medway
    "Bon",
#    "Od",
]

suffixes = ["well",             # Stockwell, Crudwell
            "ton",
            "hall",
            "ville",
            "ham",

            "bury",             # Aylesbury, Canterbury, Dewsbury, Bury, Pendlebury, Newbury, Shrewsbury, Tewkesbury,
                                # Glastonbury (Old English, fortified enclosure)
            "brough",           # Middlesbrough,
            "borough",          # Peterborough, Knaresborough, Scarborough, 
            "burgh"             # Edinburgh, Bamburgh, Jedburgh, Aldeburgh, Musselburgh
            "by",               # Grimsby, Tenby, Derby, Whitby, Selby, Crosby, Formby, Kirkby, Rugby, Helsby, Corby, Wetherby, Lockerbie
            "borough",
            "by",
            "caster",
            "cester",
            "chester",
            "combe",
            "cott",
            "cote",
            "den",
            "don",
            "ey",
            "ea",
            "sea",
            "combe",    # Barcombe, Farncombe, Ilfracombe, (means "valley")
            "cot",      # Ascot, Didcot (Old English for cottage or small building)
            "cott",
            "field",    # Sheffield, Enfield
            "fleet",
            "ford",
            "ham", # make it more common (Ham meant village or estate)
            "ton", # make it more common (Ton is usually a corruption of 'tun', which meant farm or hamlet.)
            "hampton",
            "holm",
            "holme",
            "hurst",    # (Hurst meant a wooded hill)
            "ing",      # Reading, Spalding, Wapping, Kettering, Worthing, Dorking, Barking, Epping, Woking, Pickering
            "ly",
            "ley",
            "leigh",
            "lea",
            "mere",
            "more",     # Dunmore, Lismore, Strathmore
            "stead",
            "sted",
            "stoke",
            "thorpe",   # The Danish word Thorpe meant hamlet or little settlement.
            "stow",     # Stow or stowe is usually derived from stowe, which meant meeting place
            "stowe",
            "try",
            "wald",     # Wald was the Saxon word for forest - often corrupted to weald or wold 
            "weald",
            "wold",
            "church",
            "wick",     # At the end of a name wick sometimes meant trading place (Norwich was the north wick).
                        # It could also mean a port (Greenwich), or a specialised farm (Gatwick was a goat farm,
                        # Chiswick was a cheese farm)
            "worth",    # Worth meant an enclosure or an enclosed settlement
            "hythe",    # Saxon word hythe meant a landing place for boats
            "wood",
            "ware",
            "wark",     # Southwark
            "ney",      # Hackney
            "bury",
            "mond",
            "lock",     # Matlock
            "minster",  # Axminster, Westminster, Kidderminster
            "bourne",   # Eastbourne, Ashbourne (Old English, large brook, large stream)
            "burn",     # Blackburn, Bannockburn
            "dale",     # Airedale, Rochdale
            "mouth",    # Plymouth, Bournemouth, Portsmouth, Monmouth, Sidmouth, Weymouth, Lynmouth (Mouth of a river)
            "ness",     # Sheerness, Skegness, Furness, Durness, Dungeness (promontory, headland - literally 'nose')
            "pool",     # Liverpool, Blackpool, Hartlepool, Welshpool (Old English for harbour) 

            "port",     # Davenport, Southport, Stockport, Bridport, Portsmouth, Newport, Maryport, Ellesmere Port	suffix	
            "shaw",     # (Old English for a wood, a thicket) Openshaw, Wythenshawe, Shaw
            "font",     # Chalfont
            "cote",     # Eastcote
            "ling",     # Ditching
            "fold",     # Lickfold
            "town",
            "bank",
            "bridge",
            "hoe",      # Cockernhoe
            "shot",     # Cockshot
            "shott",    # Cockshot
            "ton",
            "gate",
            "ham",
            "grove",
            "lake",
            "by",
            "holme",
            "dale",
            "howe",
            "hithe",
            "howe",
            "moor",
            "bridge",
            "mount",
            "row", # Barrow, Harrow, Heathrow
            "end", # Gravesend
            "inge",# Lyminge, Sellindge, Beltinge, Pedlinge, Ottinge, Hawkinge, Ospringe
            #(place names ending in ing,inge or ings were usually found on higher ground, or in places which control strategic points)
            "holt", # Northolt, Bergholt (Meant wood in the Saxon language)
            "hurst" # Selhurst, Staplehurst, Chislehurst (Hurst meant a wooded hill)

            ]

infixes = ["per",
           #"ping",
           "ing",
           "in",
           "ches",
           "es",
           "ing",
           #"mond",
           "mon",
           "ter",
           #"ble",
           #"ding",  #Teddington
           "ling",
           "e",
           "er",
           "or",
           "en",
           "li",
           "er",
           "s",
           "is",
           "i"
         ]

description_words_good = [
    "great",
    "grand",
    "lovely",
    "cosy",
    "magical",
    "beautiful",
    "picturesque",
    "delightful",
    "busy",
    "vibrant",
    "thriving",
    "lively",
    "popular",
    "perfect",
    "fantastic",
    "charming",
    "bustling",
    "attractive",
    "wonderful",
    ]

description_words_bad = [
    "dull",
    "drab",
    "mediocre",
    "unexceptional",
    "humdrum",
    "boring",
    "dark",
    "dank",
    "gloomy",
    "shabby",
    "uninspiring",
    "miserable",
    "horrible",
    "tedious",
    "dismal",
    "dreary",
    "ordinary",
    "tiresome",
    "plain",
    ]

def add_modifier(name):
    initial_modifiers = ["Great", "Little", "Upper", "Lower", "East", "West", "North", "South",
                         "Great", "Little", "Upper", "Lower", "East", "West", "North", "South",                         
                         "Old", "New",
                         "Chipping", # Chipping Norton, Chipping Campden (from Old English for "market"),
                         "Nether",   # Nether Wallop
                         "Bishop's", # Bishop's Stortford, Bishop's Ichington
                         ]

    suffix_modifiers = ["Town", "Green", "Cross",
                        "Town", "Green", "Cross",   #Kings Cross, Charing Cross, Hatton Cross
                        "-by-Sea",  "-on-Sea",  "Abbey",  "Bois", "Grove", "Heath",
                        "Mallet",   # Shepton Mallet, Curry Mallet
                        "Magna",    # Appleby Magna, Chew Magna, Wigston Magna, Ludford Magna, Canford Magna, Teffont Magna
                                    # from Latin for "great" (Primarily a medieval affectation)
                        "Parva",	# Appleby Parva, Wigston Parva, Ruston Parva, Glen Parva, Thornham Parva, Ludford Parva
                                    # from Latin for "little",
                        "Bottom",   # Pratt's Bottom, Pett Bottom, Bedlam Bottom, Boggy Bottom
                        "End",      # Bell End, Lickey End
                        "Hale",     # Tottenham Hale
                        "Wood",     # Abbey Wood, Colliers Wood
                        "Vale",
                        "Wells",    # Tunbridge Wells, Builth Wells, Llandrindod Wells
                        "Moor",
                        "Downs",
                        "Regis",    # Bognor Regis, Lyme Regis 
                        ]
    use_initial = random.choice((1, 1, 1, 0))
    if use_initial == 1:
        init = random.choice(initial_modifiers)
        while init[:2] == name[:2]:
            init = random.choice(initial_modifiers)
        return "%s %s" % (init, name)
    else:
        suf = random.choice(suffix_modifiers)
        while suf[:2] == name[:2]:
            suf = random.choice(suffix_modifiers)
        name = "%s %s" % (name, suf)
        if string.find(name, "-") >-1:
            name = string.replace(name, " ", "")
        return name

def make_name(VERBOSE=0, LOG=0):

    if LOG == 1:
        LOGFILENAME = "%s_log.txt" % string.strip(string.split(sys.argv[0],".")[1][1:])
        #print LOGFILENAME
        logfile = open(LOGFILENAME, "a")
        logfile.write("%s\n\n" % (10*"="))

    use_infix = random.choice((0,0,1))
    #use_infix = 1
    if use_infix == 1:
        rt = random.choice(root_words)
        inx = random.choice(infixes)
        #inx = string.lower(random.choice(root_words))
        sx = random.choice(suffixes)

        
        if VERBOSE == 1:
            print "rt:", rt
            print "inx:", inx
            print "sx", sx
            print
            print "rt[-1]:", rt[-1]
            print "inx[0]:", inx[0]
            print (rt[-1] == inx[0])
            print
            print "inx: '%s'" % inx
            print "sx[0]", sx[0]
            print "inx[-1]", inx[-1]
            print "(inx[-1] == sx[0]):", (inx[-1] == sx[0])
            print

        if LOG == 1:
            logfile.write("rt:\t'%s'\n" % rt)
            logfile.write("inx:\t'%s'\n" % inx)
            logfile.write("sx:\t'%s'\n" % sx)
            logfile.write("\n")
            logfile.write("rt[-1]:\t'%s'\n" % rt[-1])
            logfile.write("inx[0]:\t'%s'\n" % inx[0])
            logfile.write(("%s\n" % (rt[-1] == inx[0])))
            logfile.write("\n")
            logfile.write("inx:\t'%s'\n" % inx)
            logfile.write("sx[0]:\t'%s'" % sx[0])
            logfile.write("inx[-1]:\t '%s'\n" % inx[-1])
            logfile.write("(inx[-1] == sx[0]):\t%s\n" % (inx[-1] == sx[0]))
            logfile.write("\n\n")

               
        while (rt[-1] == inx[0]) or (inx[-1] == sx[0]):
            if VERBOSE == 1:
                print "REJECTED '%s%s%s'!" % (rt, inx,sx)
            if LOG == 1:
                logfile.write("REJECTED '%s%s%s'!\n" % (rt, inx,sx))
            rt = random.choice(root_words)
            inx = random.choice(infixes)
            sx = random.choice(suffixes)
        
        name = "%s%s%s" % (rt, inx, sx)

    else:
        rt = random.choice(root_words)
        sx = random.choice(suffixes)

        if VERBOSE == 1:
            print "rt[-1]:",rt[-1]
            print "sx[0]:", sx[0]
            print "rt[-1] == sx[0]:", (rt[-1] == sx[0])
            print
        if LOG == 1:
            logfile.write("rt[-1]:\t'%s'\n" % rt[-1])
            logfile.write("sx[0]:\t'%s'\n" % sx[0])
            logfile.write("rt[-1] == sx[0]:\t'%s'\n" % (rt[-1] == sx[0]))
            logfile.write("\n")

        while rt[-1] == sx[0]:
            if VERBOSE == 1:
                print "REJECTED '%s%s'!" % (rt, sx)
            if LOG == 1:
                logfile.write("REJECTED '%s%s'!\n" % (rt, sx))
            rt = random.choice(root_words)
            sx = random.choice(suffixes)
        name = "%s%s" % (rt, sx)

    if VERBOSE == 1:
        print "NAME: '%s'" % name
    if LOG == 1:
        logfile.write("NAME: '%s'\n" % name)

    #fix known oddnesses...
    if string.find(name, "leing") > -1:
        name = string.replace(name, "leing", "ling")
    if string.find(name, "iea") > -1:
        name = string.replace(name, "iea", "ea")
    if string.find(name, "ein") > -1:
        name = string.replace(name, "ein", random.choice(("en","in")))
    if string.find(name, "shit") > -1:
        #would rather avoid having the word 'shit' in a place name!
        name = string.replace(name, "shit", "shot")



    name2 = name
    if len(name) < 6:
        use_modifer= 1
    else:
        use_modifer= random.choice((0,0,1))
    if use_modifer == 1:
        #name2 = "%s %s" % (random.choice(initial_modifiers), name)
        name2 = add_modifier(name)

    if VERBOSE == 1:
        print "NAME2: '%s'" % name2
    if LOG == 1:
        logfile.write("NAME2: '%s'\n\n" % name2)
        logfile.write("%s\n\n" % (10*"="))

    if LOG == 1:
        logfile.close()
    return name2


def make_town():
    town = Town()
    town.populate
    return town


if __name__=="__main__":
    for f in range(0,10):
        n = make_name(VERBOSE=0, LOG=0)
        print n
        print

    t = make_town()
    t.populate()
    print
    print t
    desc = t.get_description()
    if desc[0] in ("a", "e", "i", "o", "u"):
        desc = "an %s" % desc
    else:
        desc = "a %s" % desc
    print "%s: %s %s town." % (t.name, desc, random.choice(("small", "little")))
    print
