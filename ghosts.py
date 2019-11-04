#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

import random, string, time
import names, place_name_generator


def make_ghost(place=None, current_year=None):

    #set up some basic stuff first of all...
    if place == None:
        #make something up...
        place = place_name_generator.make_name()
        place = "%s %s" % (place, random.choice(("Castle", "House", "Manor", "Cathedral", "Palace",
                                                 "Castle", "House", "Manor", "Cathedral", "Palace",
                                                 "Abbey", "Abbey", 
                                                 "Rectory", "Tavern", "Tower", "Chapel")))

    if current_year == None:
        current_year = int(time.localtime()[0])
    else:
        current_year = int(current_year)
        
    report_year = current_year - random.choice(range(3,15))

    past_year= random.choice(range(1500,1920))

    if place[0] != string.upper(place[0]):
        place = "%s%s" % (string.upper(place[0]), place[1:])
                             
    #"The 18th-century St Marks' church" -> "St Marks' church"
    if string.find(string.lower(place), "church") > -1:
        place = string.strip(place[string.find(place, " S")+1:])
    #'the Jarman Museum of Art (with its internationally known Conceptual Art collection)' -> 'the Jarman Museum of Art'
    elif string.find(string.lower(place), "museum") > -1:
        if string.find(string.lower(place), "(") > -1:
            place = string.strip(place[:string.find(place, "(")-1])


    #OK, now get to the ghosty stuff...

    randmonth = random.choice(("January","February","March","April",
                               "May","June","July","August",
                               "September","October","November","December"))
    if randmonth == "February":
        randday = random.choice(range(1,28))
    elif randmonth in ["April","June","September","November"]:
        randday = random.choice(range(1,30))
    else:
        randday = random.choice(range(1,31))

    random_day_of_year = "%s %s" % (randday,
                                    randmonth)

    ghost_gender = random.choice(("female", "female", "female", "male"))    

    namestyle = random.choice(("Spanish", "Italian", "French"))

    if ghost_gender == "female":
        ghost_pronoun = random.choice(("She", "She", "It", "This"))
        persons_name = names.getFemaleName(Style=namestyle, UseLongName=0)
        persons_name2 = names.getFemaleFirstName()
        person_pronoun = "her"
        person_pronoun2 = "herself"
        person_pronoun3 = "she"
    else:
        ghost_pronoun = random.choice(("He", "He", "It", "This"))
        persons_name = names.getMaleName(Style=namestyle, UseLongName=0)
        persons_name2 = names.getMaleFirstName()
        person_pronoun = "his"
        person_pronoun2 = "himself"
        person_pronoun3 = "he"
    persons_first_name = string.split(persons_name)[0]

    phrase1 = random.choice(("is haunted by",
                             "is said to be haunted by",
                             "is rumoured to be haunted by",
                             "is reputedly haunted by",
                             "is reportedly haunted by",
                             "is believed to be haunted by",
                             "is allegedly haunted by"))

    female_ghost_name= random.choice(("The Brown Lady",
                                      "The Grey Lady",
                                      "The White Lady",
                                      "The Blue Lady",
                                      "The Red Lady",
                                      "The Green Lady",
                                      "the Brown Lady",
                                      "the Grey Lady",
                                      "the White Lady",
                                      "the Blue Lady",
                                      "the Red Lady",
                                      "the Green Lady",
                                      "the Lady in Red",
                                      "the Lady in Brown",
                                      "the Lady in Grey",
                                      "the Lady in White",
                                      "the Lady in Blue",
                                      "the Lady in Green",
                                      "The Headless Nun",
                                      "The Screaming Nun",
                                      "The Ghost Nun",
                                      "The Ghostly Nun",
                                      "Bloody %s" % persons_first_name,
                                      "Bloody %s" % persons_name2,
                                      "Bloody %s" % persons_name2,
                                      "Headless %s" % persons_first_name,
                                      "Headless %s" % persons_name2,
                                      ))

    male_ghost_name = random.choice(("The Ghostly Drummer",
                                     "The Ghostly Piper",
                                     "The Man in Brown",
                                     "The Man in Grey",
                                     "The Man in White",
                                     "The Man in Blue",
                                     "The Man in Red",
                                     "The Man in Green",
                                     "Bloody %s" % persons_first_name,
                                     "Bloody %s" % persons_name2,
                                     "Bloody %s" % persons_name2,
                                     "Headless %s" % persons_first_name,
                                     "Headless %s" % persons_name2,
                                     "The Headless Monk",
                                     "The Screaming Monk",
                                     "The Ghost Monk",
                                     "The Ghostly Monk",
                                     ))

    if ghost_gender == "female":
        ghost_name = female_ghost_name
    else:
        ghost_name = male_ghost_name

    clothing_colour = None
    if string.find(ghost_name, "Brown") > -1:
        clothing_colour = "brown"
    elif string.find(ghost_name, "Grey") > -1:
        clothing_colour = "grey"
    elif string.find(ghost_name, "White") > -1:
        clothing_colour = "white"
    elif string.find(ghost_name, "Blue") > -1:
        clothing_colour = "blue"
    elif string.find(ghost_name, "Red") > -1:
        clothing_colour = "red"
    elif string.find(ghost_name, "Green") > -1:
        clothing_colour = "green"
    else:
        clothing_colour = " "

    people = random.choice(("Visitors and staff", "Visitors", "Staff",
                            "Visitors and staff members", "Staff members",
                            "Witnesses", "Residents"))

    people2 = random.choice(("Visitors and staff", "Visitors", "Staff",
                            "Visitors and staff members", "Staff members",
                            "Witnesses", "Residents", "People"))
                            
    signs = random.choice(("have heard apparitional piano music",
                           "have heard ghostly piano music",
                           "have heard voices and whispers in the empty %s" % (random.choice(("hall", "rooms", "building"))),
                           "have heard voices in the empty %s" % (random.choice(("hall", "rooms", "building"))),
                           "have heard whispers in the empty %s" % (random.choice(("hall", "rooms", "building"))),
                           "have reported hearing the sound of children laughing and singing, only to find that there were no children present",
                           "have been plagued by strange noises and unexplained occurrences",
                           "have been plagued by unexplained occurrences and strange noises",
                           "have been plagued by strange noises",
                           "have been plagued by unexplained occurrences",
                           "have felt strong presences and seen strange lights",
                           "have seen strange lights and felt strong presences",
                           "have reported strange lights and strong presences",
                           "have seen floating lights and strange apparitions",
                           "have also reported seeing the ghost of a small, sad girl",
                           "have also reported the sound of a mysterious harp playing",
                           ))

    addenda = "There is also %s%s and %s associated with this place." % (random.choice(("an indelible bloody stain, ", "a bloody stain which could not be removed, ",
                                                                                        "a poltergeist, ", "extreme poltergiest activity, ",
                                                                                        "a terrifying presence, ", "a ghostly soldier, ")),
                                                                           random.choice(("two apparitions", "three apparitions", "four apparitions", "five apparitions",
                                                                                          "two ghosts", "three ghosts", "four ghosts", "five ghosts",
                                                                                          "the ghosts of two teen girls", "the ghosts of three teen girls", "the ghosts of four teen girls", "the ghosts of five teen girls", 
                                                                                          "the ghosts of two young women", "the ghosts of three young women", "the ghosts of four young women", "the ghosts of five young women", 
                                                                                          "the ghosts of two young girls", "the ghosts of three young girls", "the ghosts of four young girls", "the ghosts of five young girls",
                                                                                          "the ghosts of two children", "the ghosts of three children", "the ghosts of four children", "the ghosts of five children",
                                                                                          "other apparitional figures", 
                                                                                          )),
                                                                           random.choice(("a curse", "two curses", "three curses", "four curses", "five curses",
                                                                                          "many reported paranormal occurrences", "many paranormal occurrences",
                                                                                          "floating lights", "the ghostly cry of a wailing baby"))
                                                                         )

    addenda2 = random.choice(("Guard dogs bark into empty room where %s walks." % person_pronoun3,
                              "Dogs are particularly troubled by some kind of sinister presence.",
                              "Dogs seem particularly troubled by some kind of sinister presence.",
                              "Dogs seem particularly troubled by some kind of sinister presence at this site.",
                              "%s report strange experiences and inexplicable events." % people2,
                              "%s report sinister sensations and inexplicable events." % people2,
                              "%s have reported hearing voices and loud footsteps late at night in areas they know to be empty." % people2,
                              "%s have also reported the figure of a spectral %s gazing from a window." % (people2, random.choice(("woman", "man"))),
                              "In %s, %s named %s as as one of the top %s most haunted places in the %s." % (report_year,
                                                                                                        random.choice(("The Guardian",
                                                                                                                       "The Times",
                                                                                                                       "The Daily Mail",
                                                                                                                       "The Daily Telegraph",
                                                                                                                       "the BBC")),
                                                                                                        place,
                                                                                                        random.choice(("five","ten","twenty","five","ten","twenty","fifty","hundred")),
                                                                                                        random.choice(("United Kingdom", "UK", "country"))
                                                                                                        ),
                                                                                                        
                              #"According to at least one source, "
                              '%s describe "a most dreadful expression of distress" on %s face.' % (people2, person_pronoun),
                              '%s describe "an appalling expression of grief" on %s face.' % (people2, person_pronoun),
                              ))


    last_bit = random.choice(("%s %s. " % (people,signs),
                              addenda,
                              addenda2,
                              "%s %s. %s. %s" % (people,signs, addenda, addenda2),
                              "%s. %s." % (addenda, addenda2),
                              "%s %s. %s" % (people,signs, addenda),
                              "%s %s %s. " % (addenda, people,signs),
                              "%s %s. %s" % (people,signs, addenda2),
                              "%s %s %s. " % (addenda2, people,signs),
                              "",
                              ))

    #combine this with stuff above...but later...
    if ghost_gender == "female":

#    appears as an elderly woman
#    a young woman
#    a high school age girl
#    a school age girl 
#    a school age girl 
#    a young girl 

        if clothing_colour in [None, "", " "]:
            wearing = random.choice(("She appears in a long gown.",
                             "Her ghost appears in a long gown.",
                             "Her ghost is seen wearing a long rustling gown.",
                             "Her ghost is seen wearing a long rustling ball gown.",
                             "Her ghost is seen wearing a long rustling ball gown and a tall head of black hair.",
                             "Her ghost is seen wearing a long rustling ball gown and a tall head of blonde hair.",
                             "Her ghost is seen wearing a long rustling ball gown and a tall head of red hair.",
                             "She is seen wearing a long rustling gown.",
                             "She is seen wearing a long rustling ball gown.",
                             "She is seen wearing a long rustling ball gown and a tall head of black hair.",
                             "She is seen wearing a long rustling ball gown and a tall head of blonde hair.",
                             "She is seen wearing a long rustling ball gown and a tall head of red hair."))

        else:
            wearing = random.choice(("She appears in a long %s gown." % clothing_colour,
                             "Her ghost appears in a long %s gown." % clothing_colour,
                             "Her ghost is seen wearing a long rustling %s gown." % clothing_colour,
                             "Her ghost is seen wearing a long rustling %s ball gown." % clothing_colour,
                             "Her ghost is seen wearing a long rustling %s ball gown and a tall head of black hair." % clothing_colour,
                             "Her ghost is seen wearing a long rustling %s ball gown and a tall head of blonde hair." % clothing_colour,
                             "Her ghost is seen wearing a long rustling %s ball gown and a tall head of red hair." % clothing_colour,
                             "She is seen wearing a long rustling %s gown." % clothing_colour,
                             "She is seen wearing a long rustling %s ball gown." % clothing_colour,
                             "She is seen wearing a long rustling %s ball gown and a tall head of black hair." % clothing_colour,
                             "She is seen wearing a long rustling %s ball gown and a tall head of blonde hair." % clothing_colour,
                             "She is seen wearing a long rustling %s ball gown and a tall head of red hair." % clothing_colour,
                             "%s report a woman dressed in %s who disappears without trace." % (people2, clothing_colour)
                                     ))


    elif ghost_gender == "male":
        if clothing_colour in [None, "", " "]:
            wearing = random.choice(("He appears as a man in a long coat who appears accompanied by a chill in the air.",
                                     "He appears as a man in a long coat who appears accompanied by an overwhelming smell of lavender.",
                                     "His ghost appears as a man in a long coat who appears accompanied by an overwhelming smell of lavender.",
                                     "He appears as a tall, dark stranger.",
                                     "He appears as a tall slender figure dressed in a long cape.",
                                     "His ghost appears as a man in a long coat who appears accompanied by a chill in the air.",
                                     "His ghost appears as a man in a long coat who appears accompanied by an overwhelming smell of lavender.",
                                     "His ghost appears as a tall, dark stranger.",
                                     "His ghost appears as a tall slender figure dressed in a long cape."
                                     "He is said to appear in great pain, wearing trousers and a shirt.",
                                     "His ghost is said to appear in great pain, wearing trousers and a shirt.",
                                     "He is said to appear in great pain.",
                                     "His ghost is said to appear in great pain.",
                                     "He is said to appear to be in great pain.",
                                     "His ghost is said to appear to be in great pain.",
                                 ))
        else:
            wearing = random.choice(("He appears as man in a %s coat who appears accompanied by a chill in the air." % clothing_colour,
                                     "He appears as man in a %s coat who appears accompanied by an overwhelming smell of lavender." % clothing_colour,
                                     "He appears as a tall, dark stranger dressed in %s." % clothing_colour,
                                     "He appears as a tall slender figure dressed in %s with a long %s cape." % (clothing_colour, clothing_colour),
                                     "His ghost appears as man in a %s coat who appears accompanied by a chill in the air." % clothing_colour,
                                     "His ghost appears as man in a %s coat who appears accompanied by an overwhelming smell of lavender." % clothing_colour,
                                     "His ghost appears as a tall, dark stranger dressed in %s." % clothing_colour,
                                     "His ghost appears as a tall slender figure dressed in %s with a long %s cape." % (clothing_colour, clothing_colour),
                                     "He is said to appear in great pain, wearing %s trousers and a shirt." % clothing_colour,
                                     "His ghost is said to appear in great pain, wearing %s trousers and a shirt." % clothing_colour,
                                     "%s report a man dressed in %s who disappears without trace." % (people2, clothing_colour),
                                 ))

    grisly_fate1 = random.choice(("was killed by",
                                 "was murdered by",
                                 "was killed in unexplained circumstances, allegedly by",
                                 "was brutally murdered by",
                                 "was murdered while %s slept by" % person_pronoun3,
                                 "was murdered in %s sleep by" % person_pronoun,
                                 "was strangled by",
                                 "was strangled while %s slept by" % person_pronoun3,
                                 "was strangled in %s sleep by" % person_pronoun,
                                 "was poisoned by",
                                 "was killed on the orders of",
                                 "was imprisoned and murdered by",
                                 "suffered a grisly fate at the hands of"))
    if ghost_gender == "female":
        grisly_fate1 = "%s %s" % (grisly_fate1,
                                        random.choice(("her mother", "her father", "her husband",
                                                       "her lover", "a jealous lover", "a spurned lover",
                                                       "a servant girl", "a maid", "a servant",
                                                       "her uncle", "her stepmother", "her stepfather"))
                                        )
    elif ghost_gender == "male":
        grisly_fate1 = "%s %s" % (grisly_fate1,
                                        random.choice(("his mother", "his father", "his wife",
                                                       "his lover", "a jealous lover", "a spurned lover",
                                                       "a servant girl", "a maid", "a servant",
                                                       "his uncle", "her stepmother", "her stepfather"))
                                        )
        
    grisly_fate2 = random.choice(("tragically died in a fire",
                                 "died in a fire",
                                 "died in a suspicous fire",
                                 "drowned %s" % person_pronoun2,
                                 "killed %s" % person_pronoun2,
                                 "was killed in a tragic accident",
                                 "was killed in an accident",
                                 "was killed in a horrifying accident",
                                 "was killed in a terrible accident",
                                 "was decapitated in a tragic accident",
                                 "was decapitated in a horrifying accident",
                                 "was decapitated in a terrible accident",
                                 "was murdered",
                                 "was brutally murdered",
                                 "committed suicide",
                                 "flung %s, or fell, from the roof" % person_pronoun2,
                                 "flung %s from the roof" % person_pronoun2,
                                 "fell from the roof and died",
                                 "drowned %s in the nearby river after the murder of %s lover" % (person_pronoun2, person_pronoun),
                                 "flung %s from the roof after the murder of %s lover" % (person_pronoun2, person_pronoun),
                                 "committed suicide after the murder of %s lover" % (person_pronoun),
                                 "was killed on Christmas Day",
                                 "was murdered on Christmas Day",
                                 "was brutally murdered on Christmas Day",
                                 "was the victim of a brutal crime of passion",
                                 "went mad after being rejected by %s fiancee" % person_pronoun,
                                 "went mad and killed %s after being rejected by %s fiancee" % (person_pronoun2, person_pronoun),
                                 "drowned %s in the nearby river after being abused by %s uncle" % (person_pronoun2, person_pronoun),
                                 "flung %s from the roof after being abused by %s uncle" % (person_pronoun2, person_pronoun),
                                 "committed suicide after being abused by %s uncle" % (person_pronoun),
                                 "died suddenly (in suspicious circumstances)",
                                 "died in suspicious circumstances",
                                 "starved to death",
                                 "was walled up alive",
                                  ))

    randnum = random.choice((0,1))
    if randnum == 0:
        grisly_fate = grisly_fate1
    else:
        grisly_fate = grisly_fate2

    if string.find(grisly_fate, "Christmas") > -1:
        random_day_of_year = "Christmas Day"
        
    bit2 = random.choice(("It is thought that",
                          "It is rumoured that",
                          "Researchers claim that",
                          "Paranormal researchers claim that", 
                          "Researchers say that",
                          "Paranormal researchers say that", 
                          "Researchers think that",
                          "Paranormal researchers think that", 
                          "Locals claim that",
                          "Locals say that",
                          "Locals think that",
                          "One theory is that",
                          "It is possible that",
                          "Believers say that",
                          "Believers claim that",
                          "Believers think that",
                          "A story is told that",
                          "According to the legends,",
                          "According to legend,",
                          ))

    bit3 = "%s is the %s of %s, who %s in %s" % (string.lower(ghost_pronoun),
                                                 random.choice(("restless spirit",
                                                                "spirit",
                                                                "shade",
                                                                "ghost",
                                                                "tormented soul")),
                                                 persons_name,
                                                 grisly_fate,
                                                 past_year
                             )

    bit4 = "The %s%s" % (random.choice(("terrifying ", "ghostly ", "frightening ", "", "")),
                          random.choice(("apparation", "figure", "spectre")))

    bit4 = "%s%s " % (bit4,
                      random.choice((", which has been captured on CCTV,",
                                     ", which sometimes appears as a %smist," % ("%s " % clothing_colour),
                                     ""
                                                     )))

    bit5 = random.choice(("is said to wander the %s on stormy nights" % random.choice(("building", "site", "premises")),
                          "is reputed to wander the %s on stormy nights" % random.choice(("building", "site", "premises")),
                          "wanders the %s on stormy nights" % random.choice(("building", "site", "premises")),
                          "is said to visit at midnight on All Hallows Eve",
                          "is said to visit the %s at midnight on All Hallows Eve" % random.choice(("building", "site", "premises")),
                          "visits at midnight on All Hallows Eve",
                          "visits the %s at midnight on All Hallows Eve" % random.choice(("building", "site", "premises")),
                          "wanders the %s at midnight on All Hallows Eve" % random.choice(("building", "site", "premises")),
                          "is said to be seen only at midnight",
                          "is seen only at midnight",
                          "is said to be seen only at midnight on All Hallows Eve",
                          "is seen only at midnight on All Hallows Eve",
                          "is said to be seen only at midnight on the anniversary of %s death" % person_pronoun, 
                          "is seen only at midnight on the anniversary of %s death" % person_pronoun, 
                          "is said to be seen only on the anniversary of %s death" % person_pronoun, 
                          "is seen only on the anniversary of %s death" % person_pronoun,
                          "is said to be seen only at midnight on the anniversary of %s death (%s)" % (person_pronoun, random_day_of_year), 
                          "is seen only at midnight on the anniversary of %s death (%s)" % (person_pronoun, random_day_of_year), 
                          "is said to be seen only on the anniversary of %s death (%s)" % (person_pronoun, random_day_of_year), 
                          "is seen only on the anniversary of %s death (%s)" % (person_pronoun, random_day_of_year), 
                          "is said to be seen only at midnight on %s birthday (%s)" % (person_pronoun, random_day_of_year), 
                          "is seen only at midnight on %s birthday (%s)" % (person_pronoun, random_day_of_year), 
                          "is said to be seen only on %s birthday (%s)" % (person_pronoun, random_day_of_year), 
                          "is seen only on %s birthday (%s)" % (person_pronoun, random_day_of_year),
                          "is said to be seen only at midnight on %s birthday" % (person_pronoun), 
                          "is seen only at midnight on %s birthday" % (person_pronoun), 
                          "is said to be seen only on %s birthday" % (person_pronoun), 
                          "is seen only on %s birthday" % (person_pronoun),
                          "is frequently spotted late at night",
                          "is frequently seen late at night",
                          "is only seen after the sun goes down",
                          "is only ever seen after the sun goes down",
                          "is only observed after the sun goes down",
                          "has only been observed after the sun goes down",
                          "has only even been seen after the sun goes down",
                          "is only seen after dusk",
                          "is only ever seen after dusk",
                          "is only observed after dusk",
                          "has only been observed after dusk",
                          "has only ever been seen after dusk",
                          "is often seen during the daytime",
                          "is, unusually, seen mainly during the daytime",
                          "is seen mainly during the daytime",
                          "seems to be able to be seen at any time of day or night",
                          "seems, unusually, to be able to be seen at any time of day or night",
                          ))

    bit4_and_5 = "%s%s." % (bit4, bit5)

    bit4_and_5 = random.choice((bit4_and_5,
                               "%s %s" % (bit4_and_5, wearing),
                               "%s %s " % (wearing, bit4_and_5)
                               ))

    try:
        ghost_description = "%s %s %s" % (place, phrase1, ghost_name)
        ghost_description = "%s. %s %s" % (ghost_description, bit2, bit3)
        ghost_description = "%s. %s " % (ghost_description, bit4_and_5)
        ghost_description = "%s%s " % (ghost_description, last_bit)
    except:
        try:
            ghost_description = "%s %s %s" % (place.decode("UTF-8", "ignore"),
                                              phrase1.decode("UTF-8", "ignore"),
                                              ghost_name.decode("UTF-8", "ignore"))
            ghost_description = "%s. %s %s" % (ghost_description,
                                               bit2.decode("UTF-8", "ignore"),
                                               bit3.decode("UTF-8", "ignore"))
            ghost_description = "%s. %s " % (ghost_description,
                                             bit4_and_5.decode("UTF-8", "ignore"))
            ghost_description = "%s%s " % (ghost_description,
                                           last_bit.decode("UTF-8", "ignore"))
        except:
            ghost_description = "%s %s %s" % (place.encode("UTF-8", "ignore"),
                                              phrase1.encode("UTF-8", "ignore"),
                                              ghost_name.encode("UTF-8", "ignore"))
            ghost_description = "%s. %s %s" % (ghost_description,
                                               bit2.encode("UTF-8", "ignore"),
                                               bit3.encode("UTF-8", "ignore"))
            ghost_description = "%s. %s " % (ghost_description,
                                             bit4_and_5.encode("UTF-8", "ignore"))
            ghost_description = "%s%s " % (ghost_description,
                                           last_bit.encode("UTF-8", "ignore"))

    #Easier to fix these here than to track down the original errors.
    # Yeah, call me lazy. :)
    while string.find(ghost_description, "  ") > -1:
        ghost_description = string.replace(ghost_description, "  ", " ")
    while string.find(ghost_description, ".. ") > -1:
        ghost_description = string.replace(ghost_description, ".. ", ". ")

    return ghost_description


if __name__ == "__main__":
    for f in range(0,5):
        ghosty_stuff = make_ghost()
        print ghosty_stuff
        print
    print
