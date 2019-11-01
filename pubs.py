#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

__VERSION__ = "0.0.5f"

import string, os, random
import names
import pycorpora

from make_school import MakeCreatureDescriptionsDict

def get_colour():
    heraldic_cols = {
    "Murrey":       {"Name":               "Murrey",
                     #"Colour":             "dark reddish purple",
                     "Colour":             "purple",
                     "Screen Colour":      "#8b004b",
                     "RGB Colour":         (139, 0, 75)
                     },
    "Sanguine":     {"Name":                "Sanguine",
                     #"Colour":              "blood red",
                     "Colour":              "red",
                     "Screen Colour":       "#b22222",
                     "RGB Colour":          (178, 34, 34)
                     },
##    "Tenné":        {"Name":                "Tenné",
##                     "Colour":              "orange",
##                     "Screen Colour":       "#c67000",
##                     "RGB Colour":          (198, 112, 0)
##                     },
    "Argent":       {"Name":                "Argent",
                     "Colour":              "white",
                     "Screen Colour":       "#fdfdfd",
                     "RGB Colour":          (253, 253, 253)
                     },
    "Or":           {"Name":                "Or",
                     "Colour":              "yellow",
                     "Screen Colour":       "#fefe00",
                     "RGB Colour":          (254, 254, 0)
                     },
    "Gules":        {"Name":                "Gules",
                     "Colour":              "red",
                     "Screen Colour":       "#ee0000",
                     "RGB Colour":          (238, 0, 0)
                     },
    "Sable":        {"Name":                "Sable",
                     "Colour":              "black",
                     "Screen Colour":       "#111111",
                     "RGB Colour":          (17, 17, 17)
                     },
    "Azure":        {"Name":                "Azure",
                     "Colour":              "blue",
                     "Screen Colour":       "#0000cc",
                     "RGB Colour":          (0, 0, 204)
                     },
    "Vert":         {"Name":                "Vert",
                     "Colour":              "green",
                     "Screen Colour":       "#008000",
                     "RGB Colour":          (0, 128, 0)
                     },
    "Purpure":      {"Name":                "Purpure",
                     "Colour":              "purple",
                     "Screen Colour":       "#600060",
                     "RGB Colour":          (96, 0, 96)
                     }
    }
    this_col = random.choice(heraldic_cols.keys())
    return heraldic_cols[this_col]["Colour"]

def make_old_pub_name():
    "pick a random pub name from a list of real pubs"
    known_pubs = [
    #The 5 Most Popular Pub Names in the UK (Culture Trip)
    #https://theculturetrip.com/europe/united-kingdom/articles/the-5-most-popular-pub-names-in-the-uk/
                  "The Red Lion", "The Royal Oak", "The Crown",
                  "The Crown Inn", "The White Hart", "The Plough",
    #other pubs named in above article...
                  "The Wheatsheaf", "The Barley Mow", "The Green Man",
                  "The Old Cock Inn", "The Cock Public House", "The Tankard Inn",
    #these are the 50 most popular pub names in the UK, according to the Morning Advertiser
    #https://www.morningadvertiser.co.uk/Article/2017/10/23/Most-popular-pub-names-in-the-UK-2017
    #(with a few variations added)
                  "Chequers", "The Chequers Inn", "The Anchor", "The Angel", "The Beehive",
                  "The Bell", "the Bird in Hand", "the Black Bull",
                  "the Black Horse", "the Black Lion", "the Bull's Head",
                  "the Bulls Head", "the Butchers Arms", "the Butchers' Arms",
                  "the Carpenters Arms", "The Coach & Horses", "The Coach and Horses",
                  "the Cricketers", "the Cross Keys", "the Crosses Keys",
                  "The Crown", "the Duke of York", "the Fox & Hounds",
                  "the Fox and Hounds", "The Fox", "the George & Dragon",
                  "the George & Dragon", "The George", "the Golden Lion",
                  "The Greyhound", "the Hare & Hounds", "the Hare and Hounds",
                  "the Horse & Groom", "the Horse and Groom", "the King's Arms",
                  "the King's Head", "the Kings Arms", "the Kings Head",
                  "the Masons Arms", "the Masons' Arms", "the Nag's Head",
                  "the Nags Head", "The Plough", "the Prince of Wales",
                  "the Queen's Head", "the Queens Head", "the Railway Tavern",
                  "the Red Lion", "the Rising Sun", "the Rose & Crown",
                  "the Rose and Crown", "the Royal Oak", "The Ship",
                  "The Star", "the Station Hotel", "The Sun", "The Swan",
                  "The Three Horseshoes", "the Travellers Rest", "The Victoria",
                  "the White Hart", "the White Horse", "the White Lion",
                  "the White Swan", "the Windmill",
    #These are real pubs mentioned in the Guardian's "Let's Move To..." property features.                
                  "Briarbank", "Brig o'Turk", "Burnt Truffle",
                  "Church Street Tavern", "Clockwork Beer Co", "Harry's Bar",
                  "Summat's Brewing", "the Allison Arms", "The Angel",
                  "the Angel", "the Anne of Cleves", "the Armoury",
                  "The Assheton Arms", "the Assheton Arms", "The Badger",
                  "the Badger", "The Bat and Ball", "the Bear",
                  "the Beckford Arms", "the Beehive", "The Bell Inn",
                  "the Bell Inn", "The Birds", "The Black Dog", "The Black Dog",
                  "The Black Lion", "the Black Lion", "The Black Rabbit",
                  "the Black Rabbit", "The Black Rat", "The Black Swan",
                  "the Black Swan", "the Blacksmiths Arms", "The Boat House",
                  "the Boat House", "The Boat Inn", "the Boathouse",
                  "the Borough", "The Borough", "The Bull & Last",
                  "the Bull & Swan", "The Bull and Last", "The Bull and Swan",
                  "the Bull and Swan", "The Butcher's Dog",
                  "the Butcher's Dog", "The Byre Inn", "the Byre Inn",
                  "The Cap and Collar", "the Cap and Collar",
                  "the Chain Locker", "the Cluny", "the Coach & Horses",
                  "The Coach and Horses", "The Cock Tavern", "the Cock Tavern",
                  "the Comm Bar", "the Comm Bar", "The Coopers Arms",
                  "the Coopers Arms", "The Cove House Inn", "the Crab & Lobster",
                  "the Crab and Lobster", "The Crab and Lobster", "The Cricketers",
                  "the Cricketers", "The Crown Inn", "The Crown", "the Crown",
                  "The Curfew", "the Curfew", "the Dartmoor Inn", "The Digby Tap",
                  "the Digby Tap", "the Dog & Bell", "the Dog & Muffler", "The Dog and Bell",
                  "the Dog and Bell", "the Dog and Muffler", "The Dove",
                  "the Dove", "The Drayman's Son", "The Drayman's Son",
                  "the Duke of York", "the Eagle + Child", "the Eagle and Child",
                  "the Earl of March", "the Earl of March", "The Embankment",
                  "The Embankment", "The Errigle Inn", "the Errigle Inn", "The Espy",
                  "the Espy", "The Fat Cat", "the Fat Cat", "The Feathers",
                  "the Feathers", "The Ferry Inn", "the Ferry Inn",
                  "The Feversham Arms", "the Feversham Arms", "The Finnieston",
                  "the Finnieston", "the Forester", "The Fox", "the Fox",
                  "The Free Trade,", "the Free Trade", "The Freemasons",
                  "The Freemasons", "The Gannet", "the Gannet",
                  "the Garden House Inn", "The Gardeners Arms", "the Gardeners Arms",
                  "the Gardeners' Arms", "the George & Dragon",
                  "the George and Dragon", "The George", "the George",
                  "The Gipsy Queen", "the Gipsy Queen", "the Glasshouse Inn",
                  "The Golden Fleece", "the Great Northern Railway Tavern",
                  "the Greene Oak", "The Griffin", "the Griffin", "The Gunton Arms",
                  "the Gunton Arms", "The Hand and Flowers", "The Harbour Inn",
                  "the Harbour Inn", "the Hare", "the Hare", "The Harp",
                  "The Hole in t'Wall", "the Hole in t'Wall", "the Inn",
                  "The Inn", "the Iron Bridge", "the Iron Bridge",
                  "The Jamaica Inn", "the Jamaica Inn", "The Just Reproach",
                  "the Just Reproach", "The King's Head", "the King's Head",
                  "The Kings Arms", "the Kings Arms", "The Lamb Inn",
                  "the Lamb Inn", "The Lamb", "the Lamb", "The Lewes Arms",
                  "the Lewes Arms", "The Lion & Unicorn", "The Lion and Unicorn",
                  "the Lion and Unicorn", "the Lion Inn", "The Lord Nelson",
                  "the Lord Nelson", "the Malt Shovel", "The Marwood",
                  "the Marwood", "The Masons Arms", "the Masons Arms",
                  "the Monico", "the Muddiford Inn", "The New Inn",
                  "the New Inn", "the Nobody Inn", "the Noel Arms",
                  "The Nook", "the Nova Scotia", "The Nutshell",
                  "the Nutshell", "The Old Boat House", "The Old Cannon",
                  "the Old Cannon", "The Old Deanery", "the Old Deanery",
                  "the Old Fire Engine House", "the Old Fire Engine House",
                  "the Old Inn", "The Old Sun Inn", "The Old Sun Inn",
                  "The One Eyed Rat", "The One Eyed Rat", "the Orange Tree",
                  "the Orange Tree", "the Ostrich", "the Ox and Finch",
                  "the Ox and Finch", "the Pandora Inn", "The Pelham Arms",
                  "the Pelham Arms", "The Pheasant", "the Pheasant",
                  "The Pilot Inn", "the Pilot Inn", "the Pink & Lily",
                  "the Pink and Lily", "The Pipe and Glass", "the Pipe and Glass",
                  "the Plough", "The Plume of Feathers", "the Plume of Feathers",
                  "the Queens Head", "The Ram", "the Ram", "the Ramsbottom Tap",
                  "the Raven Inn", "the Raven", "The Red Fox", "the Red Fox",
                  "the Red Lion", "The Richmond Arms", "the Richmond Arms",
                  "The Rising Sun", "the Rock", "the Rose & Crown",
                  "The Rose & Crown", "the Rose and Crown", "The Rose and Crown",
                  "The Rose", "the Rose", "the Royal Oak",
                  "The Royal Oak", "The Running Horses",
                  "the Running Horses", "The Salisbury", "The Salty Dog",
                  "the Salty Dog", "The Salutation Inn", "the Salutation Inn",
                  "the Seven Stars", "the Shepherd & Dog", "the Shepherd and Dog",
                  "the Shepherd and Dog", "The Shibden Mill Inn", "the Shibden Mill Inn",
                  "The Ship Inn", "the Ship Inn", "The Ship", "the Ship", "The Snowdrop",
                  "the Snowdrop", "The Southampton Arms", "the Southampton Arms",
                  "The Sportsman", "the Sportsman", "The Spotted Cow", "the Spyglass",
                  "The Standard Inn", "The Star Inn", "the Star Inn", "the Star",
                  "The Strugglers", "the Strugglers", "the Sun Inn", "The Sun",
                  "the Sun", "The Swan With Two Nicks", "the Swan With Two Nicks",
                  "The Swan", "the Swan", "The Tap House", "the Tap House",
                  "The Thatch", "the Thatch", "The Three Horseshoes",
                  "The Three Tuns", "the Three Tuns", "the Triangle Inn",
                  "The Tyne Bar", "the Tyne Bar", "the Vault", "the Vaults",
                  "the Victoria Inn", "the Water Witch", "the Water Witch",
                  "The West House", "The West House", "the Wheatsheaf",
                  "the Whippet Inn", "the White Cross", "the White Hart Hotel", "the White Hart",
                  "The White Horse", "The White Lion", "The Whitebrook",
                  "The Willow Tree", "The Woolpack", "the Yew Tree Inn",
                  "the Ypres Castle", "West Kirby Tap",
    #couple of random variations on "Harry's Bar"
                  "%s's Bar" % names.getMaleFirstName(),
                  "%s's Bar" % names.getMaleFirstName(),
    #The 23 Weirdest Pub Names In Britain (Buzzfeed)
    #https://www.buzzfeed.com/lukelewis/the-23-weirdest-pub-names-in-britain
                  "The Jolly Taxpayer",     #The Jolly Taxpayer, Portsmouth.
                  "The Nobody Inn",         #The Nobody Inn, Doddiscombsleigh, Devon.
                  "the Bunch Of Carrots",   #Bunch Of Carrots, Hampton Bishop, Hereford
                                            #(the only pub in Britain with the word 'carrots' in the name)
                  "The Quiet Woman",        #The Quiet Woman, Earl Sterndale, Buxton.
                  "The Cat And Custard Pot",#The Cat And Custard Pot, Paddlesworth, Kent.
                  "The Three Legged Mare",  #The Three Legged Mare, High Petergate, York.
                  "The Old Thirteenth Cheshire Astley Volunteer Rifleman Corps Inn",
                                            #The Old Thirteenth Cheshire Astley Volunteer Rifleman Corps Inn, Stalybridge, Tameside.
                  "The Q Inn",              #The Q Inn, Stalybridge, Tameside.
                  "The Hung Drawn And Quartered",#The Hung Drawn And Quartered, London.
                  "Poosie Nansie's",        #Poosie Nansie's, Mauchline, Ayrshire.
                  "The Swan With Two Necks",#The Swan With Two Necks, Newcastle.
                  "The Case Is Altered",    #The Case Is Altered, Pinner, Middlesex.
                  "The Skiving Scholar",    #The Skiving Scholar, Plymouth.
                  "The Pyrotechnists Arms", #The Pyrotechnists Arms, London.
                  "I Am The Only Running Footman",#I Am The Only Running Footman, London.
                  "The Drunken Duck",       #The Drunken Duck, Ambleside, Cumbria.
                  "The Bull And Spectacles",#The Bull And Spectacles, Blithbury, Staffordshire.
                  "The Gate Hangs Well",    #The Gate Hangs Well, Syston, Leicester.
                  "The Goat And Compasses", #The Goat And Compasses, Hull.
                  "The Legend Of Oily Johnnies", #The Legend Of Oily Johnnies, Winscales, Cumbria.
                  "Brown Edge",             #Brown Edge, St Helens, Merseyside.
                  "My Father's Moustache",  #My Father's Moustache, Louth, Lincolnshire.
                  "The Bucket Of Blood",    #The Bucket Of Blood, Hayle, Cornwall.
    #London's Strangest Pub Names (Londonist)
    #https://londonist.com/london/drink/london-s-strangest-pub-names
                  "the Frog and Radiator",  #the Frog and Radiator in Greenwich, closed some time ago
                  "Pratts & Payne",         #Pratts & Payne, Streatham
                  "The Ship & Shovell",     #The Ship & Shovell, Charing Cross
                  "The Camel & Artichoke",  #The Camel & Artichoke, Waterloo
                  "The Job Centre",         #The Job Centre, Deptford
                  "Pepper St Ontiod",       #Pepper St Ontiod, Millwall
                  "The Sylvan Post",        #The Sylvan Post, Forest Hill
                  "John the Unicorn",       #John the Unicorn, Peckham
                  "The Pyrotechnists Arms", #The Pyrotechnists Arms, Nunhead
                  "The Defector's Weld",    #The Defector's Weld, Shepherd's Bush
                  "The Case is Altered",    #The Case is Altered, Eastcote
                  "The Aeronaut",           #The Aeronaut, Acton
                  "The Mad Bishop & Bear",  #The Mad Bishop & Bear, Paddington
                  "The Blacksmith & The Toffeemaker",  #The Blacksmith & The Toffeemaker, Clerkenwell
    #Britain's most curious pub names – and the stories behind them (Daily Telegraph)
    #https://www.telegraph.co.uk/travel/galleries/the-uks-weirdest-pub-names-histories-behind-them/
                  "The Bucket of Blood",    #The Bucket of Blood, Hayle, Cornwall
                  "The Drunken Duck",       #The Drunken Duck, Ambleside, Cumbria
                  "The Nobody Inn",         #The Nobody Inn, Exeter
                  "The Swan with Two Necks",#The Swan with Two Necks, Blackbrook, Staffordshire
                  "The Bull & Spectacles",  #The Bull & Spectacles, Blithbury, Staffordshire
                  "The Bull and Spectacles",#The Bull & Spectacles, Blithbury, Staffordshire
                  "The Cat & Custard Pot",  #The Cat & Custard Pot, Shipton Moyne, Tetbury, Gloucestershire
                  "The Cat and Custard Pot",#The Cat & Custard Pot, Shipton Moyne, Tetbury, Gloucestershire
                  "The Jolly Taxpayer",     #The Jolly Taxpayer, Portsmouth
                  "The Moody Cow",          #The Moody Cow, Upton Hishop, Herefordshire
                  "The Snooty Fox",         #The Snooty Fox, Tetbury, Gloucestershire
                  "The Fat Cat",            #The Fat Cat, Norwich, Norfolk
                  "The Queens Head & Artichoke",  #The Queens Head & Artichoke, London
                  "The Unruly Pig",         #The Unruly Pig, Woodbridge, Suffolk
                  "The Wig & Pen",          #The Wig & Pen, Oxford
                  "The Wig and Pen",        #The Wig & Pen, Oxford
                  "The Ape & Apple",        #The Ape & Apple, Manchester
                  "The Ape and Apple",      #The Ape & Apple, Manchester
                  "The Goat & Tricycle",    #The Goat & Tricycle, Bournemouth
                  "The Goat and Tricycle",  #The Goat & Tricycle, Bournemouth
                  "Sir Loin of Beef",       #Sir Loin of Beef, Southsea, Hampshire
    #other pubs named in above article...
                  "the Wykham Arms",        #the Wykham Arms, Upton Hishop, Herefordshire
                  "the White Hart",         #the White Hart, Tetbury, Gloucestershire
                  "The Queens Head",        #former name of The Queens Head & Artichoke, London
                  "British Larder",         #former name of the Unruly Pig, Woodbridge, Suffolk
    #9 Of The Strangest And Most Hilarious London Pub Names (Secret London)
    #https://secretldn.com/9-strangest-hilarious-london-pub-names/
                  "Dirty Dicks",            #Dirty Dicks, 202 Bishopsgate, EC2M 4NR
                  "The Famous Cock",        #The Famous Cock, 259 Upper St, N1 1RU
                  "Ye Olde Cheshire Cheese",#Ye Olde Cheshire Cheese, 145 Fleet St, EC4A 2BU
                  "The Hole in the Wall",   #The Hole in the Wall, 5 Mepham St, SE1 8SQ
                  "The Bull and Gate",      #The Bull and Gate, 389 Kentish Town Rd, NW5 2TJ
                  "Fanny on the Hill",      #Fanny on the Hill (No longer open)
                  "Filthy Fanny's",         #Filthy Fanny’s, 226 Shoreditch High Street, E1 6PJ
                  "The Job Centre",         #The Job Centre, 120 Deptford High St, SE8 4NP
                  "John the Unicorn",       #John the Unicorn, 157-159 Rye Lane, SE15 4TL
    #Lists of Funny Pub Names (Funny Jokes, funny-jokes.com)
    #https://www.funny-jokes.com/funny/funny_pub_names.htm
                  "The Bolt Hole",          #the bar at the American Embassy in Baghdad
                  "The Idle Cook",          #The Idle Cook - Idle, Bradford, Yorkshire
                  "the Bucket of Blood",    #Bucket of Blood - Phillack, Cornwall
                  "The Fawcett Inn",        #The Fawcett Inn - Portsmouth, Hampshire
                  "The Ram Inn",            #The Ram Inn - Newark, Nottinghamshire
                  "Moderation Inn",         #Moderation Inn - Reading, Berkshire
                  "The Pub with No Name",   #The Pub with No Name - Priors Dean, Hampshire [known by locals as The White Horse Inn]
                  "The Vat and Fiddle",     #The Vat and Fiddle - Nottingham
                  "The Happy Medium",       #The Happy Medium - Chichester, West Sussex
                  "The Hung Drawn And Quartered",#The Hung Drawn And Quartered, London
                  "Hole in the Wall",       #Hole in the Wall - Southsea, Hampshire; 
                                            #(and Caernarvon, north Wales; Little Wilbraham, Cambridgeshire; Waterloo, London;
                                            #Lowside, Bowness Windermere, Cumbria [Hole Int Wall]; and several other venues.
                  "Bank Tavern",            #Bank Tavern, Keswick, Cumbria
                  "The Bleeding Wolf",      #The Bleeding Wolf, Hale, Altrincham, Cheshire
                  "Blooming Fuchsia",       #Blooming Fuchsia, Ipswich, Suffolk
                  "The Cow and Snuffers",   #The Cow and Snuffers, Llandaff, Cardiff, Wales
                  "the Drunken Duck",       #Drunken Duck, Hawkshead, Cumbria
                  "the Mad Dog",            #Mad Dog, Odell, Bedfordshire
                  "The Quiet Woman",        #The Quiet Woman - York [The sign being a woman carrying her own severed head]
                  "the Nobody Inn",         #Nobody Inn - Doddiscombsleigh, Devon
                  "The Tap Shop",           #The Tap Shop, Mid Calder, West Lothian, Scotland.
                  "Devil's Punchbowl",      #Devil's Punchbowl
                  "The Elusive Camel",      #The Elusive Camel
                  "The Hung Drawn And Quartered",       #The Hung Drawn And Quartered
                  "The Fawcett Inn",       #The Fawcett Inn
                  "Dirty Nelly's",         #Dirty Nelly's
                  "The Hairy Lemon",       #The Hairy Lemon
                  "The Three-Legged Mare", #The Three-Legged Mare [Known locally as The Wonky Donkey]
                  "The Wonky Donkey",      #local name for The Three-Legged Mare
                  "The Hog In The Pound",  #The Hog In The Pound
                  "The Pig and Whistle",   #Pig and Whistle
                  "The Roaring Donkey",    #The Roaring Donkey
                  "the Spread Eagle",      #Spread Eagle
                  "Dirty Dick's",          #Dirty Dick's
                  "Filthy Mc Nasty's",     #Filthy Mc Nasty's
                  "Bread of Heaven",       #Bread of Heaven
                  "Goat & Tricycle",       #Goat & Tricycle, Bournemouth.  
              ]

    return random.choice(known_pubs)

def make_new_pub_name():
    "make up a new pub name from colours and animal names"
    animal = get_animal_name()
    animal2 = get_animal_name()
    while animal2 == animal:
        animal2 = get_animal_name()
    randum = random.choice((1,2,3,4))
    if randum == 1:
        pubname = "the %s %s" % (get_colour(), animal)
    elif randum == 2:
        pubname = "the %s and %s" % (animal, animal2)
    else:
        pubname = "the %s" % animal

    suffixes = ("Inn", "Tavern")
    use_suffix= random.choice((1,0,0))
    if use_suffix == 1:
        pubname = "%s %s" % (pubname, random.choice(suffixes))
    return string.capwords(pubname)

def make_newest_pub_name():
    "make up a new pub name from animals (from pycorpora) and various items"

    #most of these have appeared in actual pub names...
    items = ['Apple', 'Ball', 'Bell', 'Bones', 'Bush', 'Child',
             'Collar', 'Compass', 'Compasses', 'Crown', 'Custard Pot', 'Feathers',
             'Fiddle', 'Firkin', 'Flagon', 'Flowers', 'Gavel', 'Glass', 'Globe',
             'Hourglass', 'Last', 'Muffler', 'Pen', 'Spectacles', 'Spyglass',
             'Tricycle', 'Whistle']
    item = string.capwords(random.choice(items))
    animal = string.capwords(random.choice(pycorpora.animals.common["animals"]))
    if len(string.split(animal)) > 1:
        animal = string.split(animal)[-1]
    pubname = "the %s and %s" % (animal, item)
    return string.capwords(pubname)


def make_pub_name():
    "picks a type of pub name to create and calls the relevant function, returning the name as a string."

    pub_type = random.choice(("old", "old", "new", "new", "new", "newest")) # make new slightly more likely
    if pub_type == "old":
        pubname = make_old_pub_name()
    elif pub_type == "new":
        pubname = make_new_pub_name()
    elif pub_type == "newest":
        pubname = make_newest_pub_name()
    return string.capwords(pubname)


def get_animal_name():

    #don't use these at all - too uncommon
    exceptions = ["camelopard", "camelopards", "centaur", "centaurs",
        "enfield", "enfields", "mischer", "mischers", "pantheon",
        "pantheons", "seadog", "seadogs", "seaunicorn" "seaunicorns",
        "sphynx", "sphynxes", "sphynxes", "sphynxes", "tragopan",
        "Tragopan", "tragopans", "Tragopans", "yale", "yales",
        "yipotrol", "yipotrols"]

    creatures = MakeCreatureDescriptionsDict()
    thiscreature = random.choice(creatures.keys())
    form = random.choice(("singular", "singular", "singular", "plural"))
    if form == "singular":
        creaturename = creatures[thiscreature][0]
    else:
        creaturename = creatures[thiscreature][1]

    #talbots -> dog, hound
    #dog - dog, hound
    #coney -> rabbit
    #martlet?    

    #remove these from decriptions
    killwords = [" and ", " s ", "' faces", "' heads", "'s face",
        "'s head", "affronte", "and ", "and affronte", "at gaze",
        "Bengal", "cabossed", "close", "combatant", "couchant", "couped",
        "courant", "coward", "crowned", "demi", "description (plural)",
        "description (singular)", "displayed and inverted",
        "displayed", "dormant", "double headed", "double queued",
        "doubled-headed", "elevated", "erased", "erect", "gaudant",
        "gaurdant", "guardant", "hauriant", "head erect", "head",
        "heraldic", "holding out the forepaw", "holding out their forepaws",
        "holding out their forepaws", "in her piety",
        "in their piety", "inverted", "involved", "naiant", "Napoleonic",
        "nowed", "pairs of lions", "passant", "proper", "queue nowed",
        "queue", "queued", "queues", "rampant", "rampant",
        "regardant", "rising", "s faces", "s heads", "s' heads",
        "saliant", "salient", "segreant", "sejant coward", "sejant with ball",
        "sejant with balls", "sejant", "springing",
        "statant", "tail", "tails nowed", "trippant", "two",
        "ululant", "volant", "winged", "wings addorsed",
        "wings elevated and addorsed", "wings elevated", "wings", "with"]
        #"  ",
        #" s",

    for word in killwords:
        if string.find(creaturename, word) > -1:
            creaturename = creaturename.replace(word, "")
            #print "'%s'" % creaturename
    creaturename = string.strip(creaturename)
    try:
        if string.split(creaturename)[0] in ("a", "an"):
            creaturename = string.join(string.split(creaturename)[1:])
        if string.split(creaturename)[-1] in ("s", "S"):
            creaturename = string.join(string.split(creaturename)[:-1])
    except:
        pass
    while creaturename in exceptions:
        creaturename = get_animal_name()
    while creaturename == "":        
        creaturename = get_animal_name()

    return creaturename



if __name__ == "__main__":
    for f in range(0,20):
        print
        print make_pub_name()

