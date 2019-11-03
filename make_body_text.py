#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

#make_body_text.py

import os, random, string, io

import markov_new, markovify_local

def check_for_files():
    """check to see if our working text files and pickle files (ie
    canned Markov data files) exist or not. If they don't, create them."""

    #could probably improve this. Does the subprocess method work on
    #platforms other than Windows?

    thisdir = os.getcwd()

    #text files made by 'markov_source/make_by_section.py', used for Simple text versions
    if not os.path.isfile(os.path.join(thisdir, "markov_source", "by_section_final", "_whats_going_for_it_ALL.txt")):
        os.chdir(os.path.join(thisdir, "markov_source"))
        import subprocess
        print subprocess.check_output(['python','make_by_section.py'])
        #print subprocess.check_output(['ls','-l'])
        os.chdir(thisdir)

    #pickle files made by 'markov_new.py', used for Markov chain versions
    if not os.path.isfile(os.path.join(thisdir, "markov_source", "whats_going_for_it_canned_articles.pickle")):
        markov_new.make_canned_data_new(silent=0)


def make_body_simple(useprint=0,CENSORED=1):
    """sample basic setup as markov_new.make_story_from_canned_data_new_final(),
    but simply picks sentences at random from our list of all known sentences from that section"""

    sections = ["whats_going_for_it_",
                "hang_out_at_",
                "the_case_against_",
                "well_connected_",
                "from_the_streets_"#,
                #"where_to_buy_"
                ]

    ARTICLES_PATH = os.path.join(os.getcwd(), "markov_source", "by_section_final")

    STORY = ""
    used_sentences = []

    for sect in sections:
        if sect== "well_connected_":
            this_sect_name = "Travel information:"
        elif sect== "from_the_streets_":
            this_sect_name = "Reviewer comments:"
        elif sect== "the_case_against_":
            this_sect_name = "Negatives:"
        else:
            this_sect_name = ""

        had_trains  = 0
        had_driving = 0

        sentences = ""
        #paralength = random.choice(range(2,5))
        paralength = random.choice(range(3,6))
        sentence_count = 0

        if sect == "whats_going_for_it_":
            #num_sentences = random.choice(range(5,20))
            #num_sentences = random.choice(range(19,20))
            #num_sentences = random.choice(range(10,30))
            num_sentences = random.choice(range(8,20))
        else:
            #num_sentences = random.choice(range(2,5))
            #num_sentences = random.choice(range(4,5))
            num_sentences = random.choice(range(2,10))

        #ARTICLES = glob.glob(os.path.join(ARTICLES_PATH, "%s*.txt" % sect))
        infn = "%s" % os.path.join(ARTICLES_PATH,  "_%sALL.txt" % sect)
        #infile = open(infn, "r").read()
        infile = io.open(infn, "r", encoding="utf-8").read()

        split_sentences = markovify_local.split_into_sentences(infile)

        for f in range(0,num_sentences):
            sentence_count = sentence_count + 1
            THIS_SENTENCE = random.choice(split_sentences)
            while THIS_SENTENCE in used_sentences:
                THIS_SENTENCE = random.choice(split_sentences)
            used_sentences.append(THIS_SENTENCE)

            #don't want multiple "trains:" or "driving:" sections in our travel information...
            if this_sect_name == "Travel information:":
                if had_trains == 1 and had_driving == 1:
                    THIS_SENTENCE = ""
                if string.find(THIS_SENTENCE, "Trains:") > -1:
                    if had_trains == 1:
                        while string.find(THIS_SENTENCE, "Trains:") > -1:
                            THIS_SENTENCE = random.choice(split_sentences)
                    had_trains = 1
                if string.find(THIS_SENTENCE, "Driving:"):
                    if had_driving == 1:
                        while string.find(THIS_SENTENCE, "Driving:") > -1:
                            THIS_SENTENCE = random.choice(split_sentences)
                    had_driving = 1

            #check and fix broken brackets and quotes
            if string.find(THIS_SENTENCE, "(") > -1:
                if string.find(THIS_SENTENCE, ")") == -1:
                    THIS_SENTENCE = string.replace(THIS_SENTENCE, ".", ").")
            if string.find(THIS_SENTENCE, ")") > -1:
                if string.find(THIS_SENTENCE, "(") == -1:
                    THIS_SENTENCE = "(%s" % THIS_SENTENCE
            if string.find(THIS_SENTENCE, '"') > -1:
                if string.count(THIS_SENTENCE, '"') == 1:
                    if string.find(THIS_SENTENCE, '", ') > -1:
                        THIS_SENTENCE = '"%s' % THIS_SENTENCE
                    elif THIS_SENTENCE[0] == '"':
                        THIS_SENTENCE = string.replace(THIS_SENTENCE, ".", '".')
                    elif THIS_SENTENCE[-2] == '"':
                        THIS_SENTENCE = '"%s' % THIS_SENTENCE
                    else:
                        THIS_SENTENCE = random.choice(('"%s' % THIS_SENTENCE,
                                                       string.replace(THIS_SENTENCE, ".", '".')))
            if sentences == "":
                sentences = THIS_SENTENCE
            elif sentence_count % paralength != 0:
                if THIS_SENTENCE != None:
                    sentences = "%s %s" % (string.strip(sentences), string.strip(THIS_SENTENCE))
            else:
                sentences = "%s\n\n%s" % (sentences, THIS_SENTENCE)
       
        if STORY == "":
            STORY = "%s\n%s\n" %(this_sect_name,sentences)
            #STORY = sentences
        else:
            #STORY = "%s\n%s\n" %(this_sect_name,STORY)
            #STORY = "%s\n\n%s" % (STORY, sentences)
            STORY = "%s\n\n%s\n%s" %(STORY, this_sect_name, sentences)

    #special fiddles... :(
    #sometimes get this wierd character sequence [".".".] ... remove this if we can fix it elsewhere...
    STORY = STORY.replace('''".".".''', '".')

    if  CENSORED == 1:
        STORY = STORY.replace("fuck", 'f***')
        STORY = STORY.replace("bastard", 'b*****d')
        STORY = STORY.replace("gobshite", 'gobs***e')
        STORY = STORY.replace("piss", 'p**s')
        STORY = STORY.replace("shit", 's**t')
        STORY = STORY.replace("wanker", 'w****r')

    if useprint == 1:
        print STORY

    return STORY


def make_body_markov(useprint=0, CENSORED=1, style="normal"):
    """wrapper for markov_new.make_story_from_canned_data_new_final"""

    if style == "normal":
        STORY = markov_new.make_story_from_canned_data_new_final(useprint, CENSORED)
    elif style == "final":
        STORY = markov_new.make_story_from_canned_data_new_final_rev(useprint, CENSORED)
    else:
        STORY = markov_new.make_story_from_canned_data_new_final(useprint, CENSORED)
    return STORY


def make_body_markov_rev(useprint=0, CENSORED=1):
    """wrapper for markov_new.make_story_from_canned_data_new_final_rev"""

    STORY = markov_new.make_story_from_canned_data_new_final_rev(useprint, CENSORED)
    return STORY


def do_substitutions(STORY, big_town_dict, town, known_towns=None, VERBOSE=0):
    """Checks for our place holders (ie, '[PLACE]', '[PERSON]','[RIVER]'
    etc, inserted when we run the file markov_source\make_by_section.py).

    Replaces them with names or items that make sense in the context of this
    document.
    """
    
    if VERBOSE == 1:
        print "Doing substitutions..."

    #improve this later...

    DEBUG = 1
    #DEBUG = 0
    
    #USED IN TESTING
##    MAINPLACE = "MAINPLACE"
##    LOCALS = "LOCALS"
##    RIVER = "RIVER"
##    PLACE = "PLACE"
##    PUB = "PUB"
##    PERSON = "\nPERSON:\n"
##    COUNTY = "COUNTY"

    USEDPUBS = []
    #list it to make a copy, so we don't change the orginal
    POSSPUBS = list(big_town_dict[town].pubs)

    USEDPLACES = []
    #list it to make a copy
    POSSPLACES = list(known_towns)

    USEDPEOPLE = []
    #list it to make a copy
    POSSPEOPLE = list(big_town_dict["reviewers"])

    #The real substitutions...
    MAINPLACE = town
    COUNTY = big_town_dict["county"]
    #Boring, but they'll do...
    RIVER = str(COUNTY).replace("shire", "")
    LOCALS = "%sians" % RIVER

    #STORY = make_body_text.make_body_text(mode=None, useprint=0, big_town_dict, this_town_name)

    NEWSTORY = ""

    prevline = ""
    for line in STORY.split("\n"):
        if string.find(line, "[") > -1:
            if string.find(line, "[MAINPLACE]") > -1:
                if VERBOSE > 0:
                    print "... replacing [MAINPLACE]... ",
                line = string.replace(line, "[MAINPLACE]", MAINPLACE)
                if VERBOSE == 1:
                    print ".",

            if string.find(line, "[LOCALS]") > -1:
                if VERBOSE > 0:
                    print "... replacing [LOCALS]... ",
                line = string.replace(line, "[LOCALS]", LOCALS)
                if VERBOSE == 1:
                    print ".",

            if string.find(line, "[RIVER]") > -1:
                if VERBOSE > 0:
                    print "... replacing [RIVER]... ",
                line = string.replace(line, "[RIVER]", RIVER)
                if VERBOSE == 1:
                    print ".",

            if string.find(line, "[COUNTY]") > -1:
                if VERBOSE > 0:
                    print "... replacing [COUNTY]... ",
                line = string.replace(line, "[COUNTY]", COUNTY)
                if VERBOSE == 1:
                    print ".",

            if string.find(line, "[PLACE]") > -1:
                if VERBOSE == 1:
                    print "... replacing [PLACE]... ",
                if known_towns != None:
                    if len(known_towns) >1:
                        if len(USEDPLACES) == len(POSSPLACES):
                            USEDPLACES = []
                            POSSPLACES = list(known_towns)
                        if POSSPLACES == []:
                            USEDPLACES = []
                            POSSPLACES = list(known_towns)
                        PLACE = random.choice(POSSPLACES)
                        replacecount = 0
                        while PLACE == MAINPLACE:
                            replacecount = replacecount +1
                            if VERBOSE == 1:
                                print "...PLACE == MAINPLACE ... REPLACING... ",
                            PLACE = random.choice(POSSPLACES)
                            if replacecount == 100:
                                if VERBOSE == 1:
                                    print "... UNABLE TO REPLACE. GIVING UP!... ",
                                #WTF? Give up!
                                break
                        USEDPLACES.append(PLACE)
                        POSSPLACES.remove(PLACE)
                line = string.replace(line, "[PLACE]", PLACE, maxreplace=1)
                if VERBOSE == 1:
                    print ".",
                if VERBOSE > 1:
                    print "... replaced '%s' with '%s'... " % ("[PLACE]", PLACE)

                while string.find(line, "[PLACE]") > -1:
                    if POSSPLACES == []:
                        USEDPLACES = []
                        POSSPLACES = list(known_towns)
                    PLACE = random.choice(POSSPLACES)
                    while PLACE in USEDPLACES:
                        PLACE = random.choice(POSSPLACES)
                    USEDPLACES.append(PLACE)
                    POSSPLACES.remove(PLACE)

                    line = string.replace(line, "[PLACE]", PLACE, maxreplace=1)

                    if VERBOSE == 1:
                        print ".",
                    if VERBOSE > 1:
                        print "... replaced '%s' with '%s' (MULTIPLE PLACES ON THIS LINE!)... " % ("[PLACE]", PLACE)

                if VERBOSE == 1:
                    print ".",

            if string.find(line, "[PUB]") > -1:
                if VERBOSE == 1:
                    print "... replacing [PUB]... ",
                if len(POSSPUBS) == 0:
                    if VERBOSE > 1:
                        print "... !!! RESETTING USEDPUBS TO [] !!! ... "
                        print "... !!! RESETTING POSSPUBS TO big_town_dict[town].pubs !!! ... "
                    USEDPUBS = []
                    POSSPUBS = list(big_town_dict[town].pubs)
                elif len(USEDPUBS) == len(POSSPUBS):
                    USEDPUBS = []
                    POSSPUBS = list(big_town_dict[town].pubs)
                    if VERBOSE > 1:
                        print "... !! RESETTING USEDPUBS TO [] !! ... "
                        print "... !! RESETTING POSSPUBS TO big_town_dict[town].pubs !! ... "
                PUB = random.choice(POSSPUBS)
                while PUB in USEDPUBS:
                    PUB = random.choice(POSSPUBS)
                USEDPUBS.append(PUB)
                POSSPUBS.remove(PUB)
                line = string.replace(line, "[PUB]", PUB, maxreplace=1)
                #more than one instance of [PUB] on this line?

                if VERBOSE == 1:
                    print ".",
                if VERBOSE > 1:
                    print "... replaced '%s' with '%s'... " % ("[PUB]", PUB)

                while string.find(line, "[PUB]") > -1:
                    if POSSPUBS == []:
                        USEDPUBS = []
                        POSSPUBS = list(big_town_dict[town].pubs)
                    PUB = random.choice(POSSPUBS)
                    while PUB in USEDPUBS:
                        PUB = random.choice(POSSPUBS)
                    USEDPUBS.append(PUB)
                    POSSPUBS.remove(PUB)
                    line = string.replace(line, "[PUB]", PUB, maxreplace=1)

                    if VERBOSE == 1:
                        print ".",
                    if VERBOSE > 1:
                        print "... replaced '%s' with '%s' (MULTIPLE PUBS ON THIS LINE!)... " % ("[PUB]", PUB)

            if string.find(line, "[PERSON]") > -1:
                if VERBOSE == 1:
                    print "... replacing [PERSON]... ",
                if len(USEDPEOPLE) == len(POSSPEOPLE):
                    USEDPEOPLE = []
                    POSSPEOPLE = list(big_town_dict["reviewers"])
                elif len(POSSPEOPLE) == 0:
                    USEDPEOPLE = []
                    POSSPEOPLE = list(big_town_dict["reviewers"])

                PERSON = random.choice(POSSPEOPLE)
                USEDPEOPLE.append(PERSON)
                POSSPEOPLE.remove(PERSON)
                PERSON = "\n\n%s:\n" % PERSON
                line = string.replace(line, "[PERSON]", PERSON)
                if VERBOSE == 1:
                    print ".",

            if string.find(line, "[THIS_COUNTRY]") > -1:
                THIS_COUNTRY = big_town_dict["this country"]
                line = string.replace(line, "[THIS_COUNTRY]", THIS_COUNTRY)
                if VERBOSE == 1:
                    print ".",
                if VERBOSE > 1:
                    print "... replaced '%s' with '%s' ... " % ("[THIS_COUNTRY]", THIS_COUNTRY)

            if string.find(line, "[THIS_NATIONALITY]") > -1:
                THIS_NATIONALITY = big_town_dict["this nationality"]
                line = string.replace(line, "[THIS_NATIONALITY]", THIS_NATIONALITY)
                if VERBOSE == 1:
                    print ".",
                if VERBOSE > 1:
                    print "... replaced '%s' with '%s' ... " % ("[THIS_NATIONALITY]", THIS_NATIONALITY)

            if string.find(line, "[OTHER_COUNTRY]") > -1:
                OTHER_COUNTRY = random.choice(["Turkey", "Romania", "Vietnam", "Nigeria",
                                               "Greece", "Colombia", "Thailand", "Italy", "Spain"])
                line = string.replace(line, "[OTHER_COUNTRY]", OTHER_COUNTRY, maxreplace=1)
                while string.find(line, "[OTHER_COUNTRY]") > -1:
                    OTHER_COUNTRY2 = random.choice(["Turkish", "Romanian", "Vietnamese", "Nigerian",
                                                    "Greek", "Colombian", "Thai", "Italian", "Spanish"])
                    while OTHER_COUNTRY2 == OTHER_COUNTRY:
                        OTHER_COUNTRY2 = random.choice(["Turkish", "Romanian", "Vietnamese", "Nigerian",
                                                        "Greek", "Colombian", "Thai", "Italian", "Spanish"])
                    line = string.replace(line, "[OTHER_COUNTRY]", OTHER_COUNTRY2, maxreplace=1)
                    if VERBOSE == 1:
                        print ".",
                    if VERBOSE > 1:
                        print "... replaced '%s' with '%s' (MULTIPLE COUNTRIES ON THIS LINE!)... " % ("[OTHER_COUNTRY]", OTHER_COUNTRY2)

                if VERBOSE == 1:
                    print ".",
                if VERBOSE > 1:
                    print "... replaced '%s' with '%s' ... " % ("[OTHER_COUNTRY]", OTHER_COUNTRY)

            if string.find(line, "[OTHER_NATIONALITY]") > -1:
                OTHER_NATIONALITY = random.choice(["Turkish", "Romanian", "Vietnamese", "Nigerian",
                                    "Greek", "Colombian", "Thai", "Italian", "Spanish"])
                line = string.replace(line, "[OTHER_NATIONALITY]", OTHER_NATIONALITY, maxreplace=1)
                while string.find(line, "[OTHER_NATIONALITY]") > -1:
                    OTHER_NATIONALITY2 = random.choice(["Turkish", "Romanian", "Vietnamese", "Nigerian",
                                        "Greek", "Colombian", "Thai", "Italian", "Spanish"])
                    while OTHER_NATIONALITY2 == OTHER_NATIONALITY:
                        OTHER_NATIONALITY2 = random.choice(["Turkish", "Romanian", "Vietnamese", "Nigerian",
                                            "Greek", "Colombian", "Thai", "Italian", "Spanish"])
                    line = string.replace(line, "[OTHER_NATIONALITY]", OTHER_NATIONALITY2, maxreplace=1)
                    if VERBOSE == 1:
                        print ".",
                    if VERBOSE > 1:
                        print "... replaced '%s' with '%s' (MULTIPLE NATIONALITIES ON THIS LINE!)... " % ("[OTHER_NATIONALITY]", OTHER_NATIONALITY2)

                if VERBOSE == 1:
                    print ".",
                if VERBOSE > 1:
                    print "... replaced '%s' with '%s' ... " % ("[OTHER_NATIONALITY]", OTHER_NATIONALITY)

            if string.find(line, "[RAILWAY]") > -1:
                if VERBOSE == 1:
                    print "... replacing [RAILWAY]... ",

                #improve these later?
                replacement = random.choice(("railway", "rail line"))
                line = string.replace(line, "[RAILWAY]", replacement)
                if VERBOSE == 1:
                    print ".",

        if line == "\n" and prevline == "\n":
            line = ""

        if NEWSTORY == "":
            NEWSTORY = line
        else:
            try:
                NEWSTORY = u"%s\n%s" % (NEWSTORY, line.decode("UTF=8", "ignore"))
            except:
                try:
                    NEWSTORY = u"%s\n%s" % (NEWSTORY, line.encode("UTF=8", "ignore"))
                except:
                    try:
                        NEWSTORY = "%s\n%s" % (NEWSTORY, line.decode("ascii", "ignore"))
                    except:
                        NEWSTORY = "%s\n%s" % (NEWSTORY, line.encode("ascii", "ignore"))

        prevline = line

    #special fiddles... dealing with known, one-off problems...
    NEWSTORY = string.replace(NEWSTORY, " Ufo ", " UFO ")
    NEWSTORY = string.replace(NEWSTORY, " Inn Inn", " Inn")
    NEWSTORY = string.replace(NEWSTORY, " tube station", " station")
    NEWSTORY = string.replace(NEWSTORY, " on the tube's ", " on the ")

    ##THESE FIDDLES ATTEMPT TO FIX FORMATTING PROBLEMS IN THE OUTPUT
    ##AND MAY WELL BE WRONG AND/OR LATER REMOVED.

    while string.find(NEWSTORY, ":\n\n") > -1:
        NEWSTORY = string.replace(NEWSTORY, ":\n\n", ":\n")

    #EXPERIMENTAL... WILL THIS WORK???
    NEWSTORY = string.replace(NEWSTORY, " \n", " ")

    #EXPERIMENTAL... WILL THIS WORK???
    while string.find(NEWSTORY, "\n\n\n") > -1:
        NEWSTORY = string.replace(NEWSTORY, "\n\n\n", "\n")

    #NEWSTORY = NEWSTORY.encode('utf-8')
    NEWSTORY = make_prettier(NEWSTORY)
    try:
        NEWSTORY = NEWSTORY.decode('utf-8', 'ignore')
    except:
        NEWSTORY = NEWSTORY.encode('utf-8', 'ignore')

    if VERBOSE == 1:
        print "."

    if DEBUG == 1:
        outfile = open(os.path.join("TEMP", "STORY.txt"),"wb")
        for line in NEWSTORY.split("\n"):
            #line= line.encode('utf-8')
            try:
                line = "%s\n" % line
                outfile.write(line.encode('utf-8'))
            except:
                for c in line:
                    outfile.write(c)
        if VERBOSE == 1:
            print "\twrite STORY to '%s'" % (os.path.join("TEMP", "STORY.txt"))
        outfile.close()

    if VERBOSE == 1:
        print "Substitutions complete..."

    return NEWSTORY


def make_prettier(TEXT):

    """Does some simple string manipulations to make the input TEXT look more
    typographically 'pretty' (and therefore more suitable for use in our
    output PDF).

    Does replacements for en dash, double quotation marks and ellipses.

    (Still a bit experimental, use with caution)."""

    NEWTEXT = ""

    try:
        TEXT = string.replace(TEXT, " - ", u" \u2013 ") #'EN DASH' (U+2013)
        TEXT = string.replace(TEXT, "... ", u"\u2026 ") #(U+2026) Horizontal Ellipsis  “…”
        #assume they're all right single quotes...
        TEXT = string.replace(TEXT, "'", u"\u2019") #'RIGHT SINGLE QUOTATION MARK' (U+2019)
        NEWTEXT = ""
        inquotes = 0
        for chr in TEXT:
            if chr == '"':
                if inquotes == 0:
                    chr = u"\u201c" #U+201C	“	Left double quotation mark
                    inquotes = 1
                elif inquotes == 1:
                    chr = u"\u201d" #U+201D	”	Right double quotation mark
                    inquotes = 0
            NEWTEXT = "%s%s" % (NEWTEXT,chr)
#    return TEXT
    except:
        print "*** ERROR WITH TEXT '%s' ***" % TEXT
    if NEWTEXT == "":
        return TEXT
    else:
        return NEWTEXT


def make_body_text(mode=None, useprint=0, big_town_dict=None, town=None, known_towns=None, style="normal"):

    if mode == None:
        mode = random.choice(("Simple", "Markov", "Markov"))
        #if we ever get a neural network running, uncomment, the below line...
        #mode = random.choice(("Simple", "Markov", "Markov",
        #                      "NeuralNet", "NeuralNet", "NeuralNet"))
    if mode == "Markov":
        STORY = make_body_markov(useprint=useprint, style=style)
    elif mode == "Simple":
        STORY = make_body_simple(useprint=useprint)
    elif mode == "NeuralNet":
        #implement later
        STORY = None
# Don't want a fallback here - we WANT to know if we fail.
##    else:
##        STORY = make_body_markov(useprint=useprint, style=style)

    #STORY = do_substitutions(STORY, big_town_dict, town, known_towns)
    return STORY


def demo():
    """Brief routine that checks for our working files and then
    outputs an example."""

    check_for_files()

##    MODES = ["Simple", "Markov"]
##
##    #uncomment if we ever get a Neural Net implementation working...
##    #MODES = ["Simple", "Markov", "NeuralNet"]
##    for mode in MODES:
##        printstring = "="*20
##        print "%s\nMODE:\t'%s'\n" % (printstring, mode)
##        print 
##        STORY = make_body_text(mode=mode, useprint=1)
##        print 

    printstring = "="*20
    STORY = make_body_markov_rev(useprint=1, CENSORED=1)
    printstring = "="*20



if __name__ == "__main__":
    demo()
