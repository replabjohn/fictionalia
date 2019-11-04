#STUB

import random, string, os, sys

import reportlab
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont, stringWidth

import names, place_name_generator
import art, pubs, food_and_drink
import newspapers, crimes, ghosts
import blurbwriter, make_covers, make_body_text


def registerFonts(VERBOSE=0, SILENT=0):
    #VERBOSE = 1
    VERBOSE = 0

    if SILENT == 1:
        VERBOSE = 0

    if VERBOSE ==1 :
        if SILENT != 1:
            print "registering Fonts..."

    KNOWN_FONT_PAIRS = [
        #Gentium Basic
        ["Gentium Basic",                      "GenBasR.ttf"],
        ["Gentium Basic Bold",                 "GenBasB.ttf"],
        ["Gentium Basic Bold Italic",          "GenBasBI.ttf"],
        ["Gentium Basic Italic",               "GenBasI.ttf"],
        #Gill Sans Nova
        ["Gill Sans Nova Bold",                "GillSansBoNova.ttf"],
        ["Gill Sans Nova Cond Ultra Bold",     "GillSansCondUltraBoNova.ttf"],
        ["Gill Sans Nova Ultra Bold",          "GillSansUltraBoNova.ttf"],
        ]

    startdir = os.getcwd()

    FONTDIR = "."

    if os.path.isdir(os.path.join(os.getcwd(), "fonts")):
        FONTDIR = os.path.join(os.getcwd(), "fonts")
        if VERBOSE == 1:
            print "Found fontdir: '%s'" % FONTDIR
    os.chdir(FONTDIR)

    for f in KNOWN_FONT_PAIRS:
        fontname, ttffile = f
        if os.path.isfile(ttffile):
            if VERBOSE == 1:
                printstring = " found '%s' ... " % fontname
                print printstring
            try:
                registerFont(TTFont(fontname, ttffile))
                #KNOWN_FONTS.append(fontname)
                if VERBOSE > 1:
                   print "Registered OK."
                elif VERBOSE > 0:
                   print ".",
                else:
                   pass
            except reportlab.pdfbase.ttfonts.TTFError:
                print "ERROR REGISTERING FONT!"
    if VERBOSE == 1:
        if SILENT != 1:
            print "OK\n"
    os.chdir(startdir)


def make_title(author=None):
    if author == None:
        poss_start_bits = ("A Gazetteer of", "A Guide to",
                           "A Gazetteer of", "A Guide to",
                           "An Almanac of", "The Almanac of",
                           "A Young Person's Guide to",
                           "The Hitchhikers' Guide to",
                           "A Hitchhikers' Guide to",
                           "A Hitchhiker's Guide to",
                           "Notes on", "A Journey Around", "Some Notes on",
                           "Journeying Around", "Travelling Around",
                           "A Random Journey Around",
                           "Random Journeys Around",
                           "Some Journeys in",
                           "The Ultimate Guide to",
                           "A Young Ladies Guide to",
                           "Adventures in",
                           "Travel Tales from",
                           "Notes from",    #"Notes from the Road", "Notes from a Small Island"
                           "An Uncommon Guide to",  # "An Uncommon Guide to the Art of Long-term World Travel by Rolf Potts
                           "")
    else:
        if len(author) == 2:
            author_firstname, author_surname = string.split(author, " ")
        else:
            #assume multiple surnames rather than multiple firstnames
            author_firstname, author_surname = string.split(author, " ", maxsplit=1)

        poss_start_bits = ("A Gazetteer of", "A Guide to",
                           "A Gazetteer of", "A Guide to",
                           "An Almanac of", "The Almanac of",
                           "A Young Person's Guide to",
                           "The Hitchhikers' Guide to",
                           "A Hitchhikers' Guide to",
                           "A Hitchhiker's Guide to",
                           "Notes on", "A Journey Around", "Some Notes on",
                           "Journeying Around", "Travelling Around",
                           "A Random Journey Around",
                           "Random Journeys Around",
                           "Some Journeys in",
                           "The Ultimate Guide to",
                           "A Young Ladies Guide to",
                           "Adventures in",
                           "Travel Tales from",
                           "Notes from",    #"Notes from the Road", "Notes from a Small Island"
                           "An Uncommon Guide to",  # "An Uncommon Guide to the Art of Long-term World Travel by Rolf Potts
                           "%s's Wanderings in" % author_firstname,
                           "%s's Wanderings in" % author_surname,
                           "%s's Adventures in" % author_firstname,
                           "%s's Adventures in" % author_surname,
                           "%s's Guide to" % author_surname,
                           "%s's Guide to" % author_surname,
                           "")

    start_bit = random.choice(poss_start_bits)

    county = random.choice(place_name_generator.root_words)
    while county[-1] == "s":
        county = random.choice(place_name_generator.root_words)
    use_infix = random.choice((0,0,1))
    if use_infix == 1:
        inx = random.choice(place_name_generator.infixes)
        county = "%s%s" % (county, inx)
    if county[-1] != "s":
        county = string.capitalize("%sshire" % county)
    else:
        county = string.capitalize("%shire" % county)
    midline = random.choice(("", "the County of "))
    if start_bit == "":
        if midline == "":
            title_long = """%s""" % (county)
            title_split = """%s""" % (county)
        else:
            title_long = """%s%s""" % (midline, county)
            title_split = """%s
%s""" % (midline, county)
    else:
        if midline == "":
            title_long = """%s %s""" % (start_bit, county)
            title_split = """%s    
%s""" % (start_bit, county)
        else:
            title_long = """%s %s%s""" % (start_bit, midline, county)
            title_split = """%s    
%s
%s""" % (start_bit, midline, county)

    return (county, title_long, title_split)

