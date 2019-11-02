#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

"""A set of routines to create text using Markov chains and a corpus
of text."""

import string, os, random, sys, glob, io

import pickle

import markovify_local as markovify

__VERSION__ = "0.06.3d"


STARTDIR = os.getcwd()
if os.path.isdir(os.path.join("..", "markov_source")):
    os.chdir(os.path.join("..", "markov_source"))


def make_canned_data_new(silent=0):
    """just create our pickled data"""

    DEBUG = 0
    #DEBUG = 1
    
    count = 0 

    sections = ["whats_going_for_it_",
                "the_case_against_",
                "hang_out_at_",
                "from_the_streets_",
                "well_connected_",
                "where_to_buy_",
                "comments_"
                ]

    ARTICLES_PATH = os.path.join(os.getcwd(), "markov_source", "by_section_final")

    for sect in sections:

        count = count + 1

        article_dict = {}

        ARTICLES = glob.glob(os.path.join(ARTICLES_PATH, "%s*.txt" % sect))

        for article_file in ARTICLES:
            article = io.open(article_file, encoding="UTF-8")#.readlines()
            contents = article.read()
            contents = contents.strip()
            newcontents = contents.split("\n")
            newcontents = string.join(newcontents, " ")
            if DEBUG == 1:
                print
                print "contents:"
                print contents.encode("UTF-8")
                print
                print "newcontents:"
                print newcontents.encode("UTF-8")
                print
                print "len(newcontents):", len(newcontents)
                print "type(newcontents):", type(newcontents)
                #break
                #import sys;sys.exit(-1)

            try:
                #if contents not in ["", None]:
                if newcontents not in ["", None]:
                    #according to 'https://inzaniak.github.io/pybistuffblog/posts/2017/April/simple-markov-chains-tutorial.html':
                    #We build the model by using markovify.Text(). The input MUST be a string.
                    str_newcontents = newcontents.encode('ascii', 'ignore')
                    if DEBUG == 1:
                        print
                        print "len(str_newcontents):", len(str_newcontents)
                        print "type(str_newcontents):", type(str_newcontents)
                    # Create a Markov model for each article in our dataset
                    #model = markovify.Text(contents)
                    #model = markovify.Text(contents, state_size = 2)
                    #text_model = markovify.NewlineText(contents, state_size = 2)
                    #model = markovify.NewlineText(contents, state_size = 2)
                    #model = markovify.NewlineText(contents, state_size = 3)

                    #model = markovify.Text(contents, state_size=3, retain_original=True, well_formed)
                    #model = markovify.Text(input_text=str_newcontents, state_size=3, retain_original=True, well_formed=True)
                    model = markovify.Text(input_text=str_newcontents, state_size=3, retain_original=True, well_formed=False)

                    article_dict[article_file] = model
            except:
                print "FAILED ON ARTICLE '%s'" % article_file
                raise

        #Use a markovify's combine method to combine them
        #into one large Markov chain.
        models = list(article_dict.values())

        #text_model = markovify.NewlineText(inp.headline_text, state_size = 2)

        # Combine the Markov models
        model_combination = markovify.combine(models=models)

        # Save the combined Markov models for later use
        pickle_out = open(os.path.join(os.getcwd(), "markov_source", "%scanned_articles.pickle" % sect),"wb")
        pickle.dump(model_combination, pickle_out)

        pickle_out.close()
        if silent == 0:
            print "\twrote pickled article data to '%scanned_articles.pickle'" % sect

    if silent == 0:
        print
        print "DONE"
        print "wrote %s canned data files" % count
        print
    
    combocount = 0

    #do random quotes file too

    sect = "random_quotes_"

    combocount = combocount + 1

    article_dict = {}

    #add in all comments - to make it sound like something suitable for our Guide...
    #article_dict[article_file] = model

    article_file0 = os.path.join(ARTICLES_PATH, "_comments_ALL.txt")
    article0 = io.open(article_file0, 'r', encoding="UTF-8")#.readlines()
    contents0 = article0.read()
    contents0 = contents0.strip()
    newcontents0 = contents0.split("\n")
    newcontents0 = string.join(newcontents0, " ")
    if DEBUG == 1:
        print
        print "contents0:"
        print contents0.encode("UTF-8")
        print
        print "newcontents0:"
        print newcontents0.encode("UTF-8")
        print
        print "len(newcontents0):", len(newcontents0)
        print "type(newcontents0):", type(newcontents0)

    try:
        if newcontents0 not in ["", None]:
            #according to 'https://inzaniak.github.io/pybistuffblog/posts/2017/April/simple-markov-chains-tutorial.html':
            #We build the model by using markovify.Text(). The input MUST be a string.
            str_newcontents0 = newcontents0.encode('ascii', 'ignore')
            if DEBUG == 1:
                print
                print "len(str_newcontents0):", len(str_newcontents0)
                print "type(str_newcontents0):", type(str_newcontents0)
            model0 = markovify.Text(input_text=str_newcontents0, state_size=3, retain_original=True, well_formed=False)
            if silent == 0:
                print "created 'model0' for '%s'" % article_file0

            article_dict[article_file0] = model0
    except:
        print "FAILED ON ARTICLE '%s'" % article_file0
        raise


    #actual random quotes file...

    article_file1 = os.path.join(ARTICLES_PATH, "random_quotes.txt")
    article1 = io.open(article_file1, 'r', encoding="UTF-8")#.readlines()
    contents1 = article1.read()
    contents1 = contents1.strip()
    newcontents1 = contents1.split("\n")
    newcontents1 = string.join(newcontents1, " ")
    if DEBUG == 1:
        print
        print "contents1:"
        print contents1.encode("UTF-8")
        print
        print "newcontents1:"
        print newcontents1.encode("UTF-8")
        print
        print "len(newcontents1):", len(newcontents1)
        print "type(newcontents1):", type(newcontents1)

    try:
        if newcontents1 not in ["", None]:
            #according to 'https://inzaniak.github.io/pybistuffblog/posts/2017/April/simple-markov-chains-tutorial.html':
            #We build the model by using markovify.Text(). The input MUST be a string.
            str_newcontents1 = newcontents1.encode('ascii', 'ignore')
            if DEBUG == 1:
                print
                print "len(str_newcontents1):", len(str_newcontents1)
                print "type(str_newcontents1):", type(str_newcontents1)
            model1 = markovify.Text(input_text=str_newcontents1, state_size=3, retain_original=True, well_formed=False)
            if silent == 0:
                print "created 'model1' for '%s'" % article_file1

            article_dict[article_file1] = model1
    except:
        print "FAILED ON ARTICLE '%s'" % article_file1
        raise

    #...and our version of the Pratchett Quote File 
    combocount = combocount + 1

    article_file2 = os.path.join(ARTICLES_PATH, "discworld_quotes.txt")
    article2 = io.open(article_file2, 'r', encoding="UTF-8")#.readlines()
    contents2 = article2.read()
    contents2 = contents2.strip()
    newcontents2 = contents2.split("\n")
    newcontents2 = string.join(newcontents2, " ")
    if DEBUG == 1:
        print
        print "contents2:"
        print contents2.encode("UTF-8")
        print
        print "newcontents2:"
        print newcontents2.encode("UTF-8")
        print
        print "len(newcontents2):", len(newcontents2)
        print "type(newcontents2):", type(newcontents2)

    try:
        if newcontents2 not in ["", None]:
            #according to 'https://inzaniak.github.io/pybistuffblog/posts/2017/April/simple-markov-chains-tutorial.html':
            #We build the model by using markovify.Text(). The input MUST be a string.
            str_newcontents2 = newcontents2.encode('ascii', 'ignore')
            if DEBUG == 1:
                print
                print "len(str_newcontents2):", len(str_newcontents2)
                print "type(str_newcontents2):", type(str_newcontents2)
            model2 = markovify.Text(input_text=str_newcontents2, state_size=3, retain_original=True, well_formed=False)
            if silent == 0:
                print "created 'model2' for '%s'" % article_file2

            #article_dict[article_file] = model
            article_dict[article_file2] = model2
    except:
        print "FAILED ON ARTICLE '%s'" % article_file2
        raise

    #...and our Douglas Adams quotes File 
    combocount = combocount + 1

    article_file3 = os.path.join(ARTICLES_PATH, "da_quotes.txt")
    article3 = io.open(article_file3, 'r', encoding="UTF-8")#.readlines()
    contents3 = article3.read()
    contents3 = contents3.strip()
    newcontents3 = contents3.split("\n")
    newcontents3 = string.join(newcontents3, " ")
    if DEBUG == 1:
        print
        print "contents3:"
        print contents3.encode("UTF-8")
        print
        print "newcontents3:"
        print newcontents3.encode("UTF-8")
        print
        print "len(newcontents3):", len(newcontents3)
        print "type(newcontents3):", type(newcontents3)

    try:
        if newcontents3 not in ["", None]:
            #according to 'https://inzaniak.github.io/pybistuffblog/posts/3017/April/simple-markov-chains-tutorial.html':
            #We build the model by using markovify.Text(). The input MUST be a string.
            str_newcontents3 = newcontents3.encode('ascii', 'ignore')
            if DEBUG == 1:
                print
                print "len(str_newcontents3):", len(str_newcontents3)
                print "type(str_newcontents3):", type(str_newcontents3)
            model3 = markovify.Text(input_text=str_newcontents3, state_size=3, retain_original=True, well_formed=False)
            if silent == 0:
                print "created 'model3' for '%s'" % article_file3

            #article_dict[article_file] = model
            article_dict[article_file3] = model3
    except:
        print "FAILED ON ARTICLE '%s'" % article_file3
        raise

    #...and our local version of The Annals of the Parrigues by Emily Short
    combocount = combocount + 1

    article_file4 = os.path.join(ARTICLES_PATH, "annals_quotes.txt")
    article4 = io.open(article_file4, 'r', encoding="UTF-8")#.readlines()
    contents4 = article4.read()
    contents4 = contents4.strip()
    newcontents4 = contents4.split("\n")
    newcontents4 = string.join(newcontents4, " ")
    if DEBUG == 1:
        print
        print "contents4:"
        print contents4.encode("UTF-8")
        print
        print "newcontents4:"
        print newcontents4.encode("UTF-8")
        print
        print "len(newcontents4):", len(newcontents4)
        print "type(newcontents4):", type(newcontents4)

    try:
        if newcontents4 not in ["", None]:
            #according to 'https://inzaniak.github.io/pybistuffblog/posts/4017/April/simple-markov-chains-tutorial.html':
            #We build the model by using markovify.Text(). The input MUST be a string.
            str_newcontents4 = newcontents4.encode('ascii', 'ignore')
            if DEBUG == 1:
                print
                print "len(str_newcontents4):", len(str_newcontents4)
                print "type(str_newcontents4):", type(str_newcontents4)
            model4 = markovify.Text(input_text=str_newcontents4, state_size=3, retain_original=True, well_formed=False)
            if silent == 0:
                print "created 'model4' for '%s'" % article_file4

            #article_dict[article_file] = model
            article_dict[article_file4] = model4
    except:
        print "FAILED ON ARTICLE '%s'" % article_file4
        raise

    #Use a markovify's combine method to combine them
    #into one large Markov chain.
    models = [article_dict[article_file0], article_dict[article_file1], article_dict[article_file2], article_dict[article_file3], article_dict[article_file4]]
    print "\tarticle_file0:\t%s\n\tarticle_file1:\t%s\n\tarticle_file2:\t%s\n\tarticle_file3:\t%s\n\tarticle_file4:\t%s\n\n" %  (article_file0, article_file1, article_file2, article_file3, article_file4)
    print models
    weights=[1.5, 1.25, 1, 1, 1]
    print weights

    # Combine the Markov models
    model_combination = markovify.combine(models=models, weights=weights)

    # Save the combined Markov models for later use
    pickle_out = open(os.path.join(os.getcwd(), "markov_source", "%scanned_articles.pickle" % sect),"wb")
    pickle.dump(model_combination, pickle_out)

    pickle_out.close()

    if silent == 0:
        print "\twrote pickled article data to '%scanned_articles.pickle'" % sect

    if silent == 0:
        print
        print "DONE"
        print "wrote %s canned data files" % count
        print
        print "\t(combined %s models files for last ome)" % combocount

    combocount = combocount + 1

    #right... now make the canned data file for the Book of Revelation
    # We'll combine this with a whole lot of other stuff we've already 'canned' using pickle. 
    # We'll only be using this last, biggest combined markov model for a few sections at the end...
    # The Annals of the Parrigues AND Discworld AND HHGTTG AND The Book of revelations will sort of
    # imply that the writer is starting to lose it a bit. (Should give an interesting effect....)

    combocount = combocount + 1

    article_file5 = os.path.join(ARTICLES_PATH, "rev_quotes.txt")
    article5 = io.open(article_file5, 'r', encoding="UTF-8")#.readlines()
    contents5 = article5.read()
    contents5 = contents5.strip()
    newcontents5 = contents5.split("\n")
    newcontents5 = string.join(newcontents5, " ")

    if DEBUG == 1:
        print
        print "contents5:"
        print contents5.encode("UTF-8")
        print
        print "newcontents5:"
        print newcontents5.encode("UTF-8")
        print
        print "len(newcontents5):", len(newcontents5)
        print "type(newcontents5):", type(newcontents5)

    try:
        if newcontents5 not in ["", None]:
            #according to 'https://inzaniak.github.io/pybistuffblog/posts/5017/April/simple-markov-chains-tutorial.html':
            #We build the model by using markovify.Text(). The input MUST be a string.
            str_newcontents5 = newcontents5.encode('ascii', 'ignore')
            if DEBUG == 1:
                print
                print "len(str_newcontents5):", len(str_newcontents5)
                print "type(str_newcontents5):", type(str_newcontents5)
            model5 = markovify.Text(input_text=str_newcontents5, state_size=3, retain_original=True, well_formed=False)
            if silent == 0:
                print "created 'model5' for '%s'" % article_file5

            article_dict[article_file5] = model5
    except:
        print "FAILED ON ARTICLE '%s'" % article_file5
        raise

    #let's make out last huge strange pickle file...
    #Use a markovify's combine method to combine them
    #into one large Markov chain.

    tmp_pickle_in = open(os.path.join(os.getcwd(), "markov_source", "where_to_buy_canned_articles.pickle"),"rb")
    tmp_model_combo = pickle.load(tmp_pickle_in)

    models_new = [tmp_model_combo, article_dict[article_file0], article_dict[article_file1], article_dict[article_file2], article_dict[article_file3], article_dict[article_file4], article_dict[article_file5]]
    print "\tarticle_file0:\t%s\n\tarticle_file1:\t%s\n\tarticle_file2:\t%s\n\tarticle_file3:\t%s\n\tarticle_file4:\t%s\n\tarticle_file5:\t%s\n\n" %  (article_file0, article_file1, article_file2, article_file3, article_file4, article_file5)
    print models_new
    ## Experiment a bit to see what sort of weights get the best results...
    #weights_new = [1.25, 1.15, 1, 1, 1, 1, 1.55]
    #weights_new = [1.55, 1.25, 1, 1, 1, 1, 3]
    weights_new = [1.75, 1.25, 1, 1, 1, 1, 2]
    print weights_new

    # Combine the Markov models
    model_combination_new = markovify.combine(models=models_new, weights=weights_new)

    # Save the combined Markov models for later use
    pickle_out = open(os.path.join(os.getcwd(), "markov_source", "final_canned_articles.pickle"),"wb")
    pickle.dump(model_combination_new, pickle_out)
    pickle_out.close()
    print "wrote file '%s'" % (os.path.join(os.getcwd(), "markov_source", "final_canned_articles.pickle"))



def make_story_from_canned_data_new_final(useprint=0, CENSORED=1):

    sections = ["whats_going_for_it_",
                "hang_out_at_",
                "random_quotes_",
                "the_case_against_",
                "well_connected_",
                "from_the_streets_",
                #"where_to_buy_",
                "comments_"
                ]

    ARTICLES_PATH = os.path.join(os.getcwd(), "markov_source", "by_section_final")
    used_sentences = []

    STORY = u""

    for sect in sections:
        if sect == u"well_connected_":
            this_sect_name = u"Travel information:"
        elif sect== u"from_the_streets_":
            this_sect_name = u"Reviewer comments:"
        elif sect== u"the_case_against_":
            this_sect_name = u"Negatives:"
        else:
            this_sect_name = u""

        had_trains  = 0
        had_driving = 0

        sentences = ""
        #paralength = random.choice(range(2,5))
        paralength = random.choice(range(3,6))
        sentence_count = 0

        if sect == u"whats_going_for_it_":
            ##experiment a bit to see what length of text worksbest...
            #num_sentences = random.choice(range(5,20))
            #num_sentences = random.choice(range(19,20))
            #num_sentences = random.choice(range(10,30))
            num_sentences = random.choice(range(5,20))
        elif sect == u"random_quotes_":
            num_sentences = random.choice(range(10,25))
        else:
            ##experiment a bit to see what length of text worksbest...
            #num_sentences = random.choice(range(2,5))
            #num_sentences = random.choice(range(4,5))
            num_sentences = random.choice(range(2,10))

        pickle_in = open(os.path.join(os.getcwd(), "markov_source", "%scanned_articles.pickle" % sect),"rb")
        #pickle_in = io.open(os.path.join(os.getcwd(), "markov_source", "%scanned_articles.pickle" % sect),"rb")
        model_combination = pickle.load(pickle_in)

        for f in range(0,num_sentences):
            sentence_count = sentence_count + 1
            #THIS_SENTENCE = model_combination.make_short_sentence(max_chars=120, min_chars=20)
            ##THIS_SENTENCE = model_combination.make_short_sentence(max_chars=180, min_chars=30, tries=100)
            #THIS_SENTENCE = model_combination['model'].make_short_sentence(max_chars=180, min_chars=30)

            #THIS_SENTENCE = model_combination.make_sentence(tries=100, test_output=False)
            THIS_SENTENCE = model_combination.make_short_sentence(max_chars=180, min_chars=30, test_output=False, tries=100)

            #print THIS_SENTENCE
            while THIS_SENTENCE in used_sentences:
                #should be pretty rare, but avoid repeats anyway...
                #THIS_SENTENCE = model_combination.make_short_sentence(max_chars=120, min_chars=20)
                ##THIS_SENTENCE = model_combination.make_short_sentence(max_chars=180, min_chars=30)
                #THIS_SENTENCE = model_combination.make_sentence(tries=100, test_output=False)
                THIS_SENTENCE = model_combination.make_short_sentence(max_chars=180, min_chars=30, test_output=False, tries=100)
            used_sentences.append(THIS_SENTENCE)

            #don't want multiple "trains:" or "driving:" sections in our travel information...
            if this_sect_name == u"Travel information:":
                if had_trains and had_driving:
                    THIS_SENTENCE = u""
                if string.find(THIS_SENTENCE, "Trains:") > -1:
                    if had_trains:
                        while string.find(THIS_SENTENCE, u"Trains:") > -1:
                            #THIS_SENTENCE = model_combination.make_short_sentence(max_chars=120, min_chars=20)
                            ##THIS_SENTENCE = model_combination.make_short_sentence(max_chars=180, min_chars=30)
                            #THIS_SENTENCE = model_combination.make_sentence(tries=100, test_output=False)
                            THIS_SENTENCE = model_combination.make_short_sentence(max_chars=180, min_chars=30, test_output=False, tries=500)
                    had_trains = 1
                if string.find(THIS_SENTENCE, u"Driving:") > -1:
                    if had_driving:
                        while string.find(THIS_SENTENCE, u"Driving:") > -1:
                            #THIS_SENTENCE = model_combination.make_short_sentence(max_chars=120, min_chars=20)
                            ##THIS_SENTENCE = model_combination.make_short_sentence(max_chars=180, min_chars=30)
                            #THIS_SENTENCE = model_combination.make_sentence(tries=100, test_output=False)
                            THIS_SENTENCE = model_combination.make_short_sentence(max_chars=180, min_chars=30, test_output=False, tries=500)
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
                #sentences = THIS_SENTENCE
                sentences = u"\n%s" % (string.strip(THIS_SENTENCE))
            elif sentence_count % paralength != 0:
                if THIS_SENTENCE != None:
                    sentences = u"%s %s" % (string.strip(sentences), string.strip(THIS_SENTENCE))
            else:
                #sentences = u"%s\n\n%s" % (sentences, THIS_SENTENCE)
                sentences = u"%s\n\n%s" % (sentences, THIS_SENTENCE)
       
        if STORY == u"":
            STORY = u"%s\n%s\n" %(this_sect_name,sentences)
            #STORY = sentences
        else:
            #STORY = "%s\n%s\n" %(this_sect_name,STORY)
            #STORY = "%s\n\n%s" % (STORY, sentences)
            STORY = u"%s\n\n%s\n%s" %(STORY, this_sect_name, sentences)

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
    

def make_story_from_canned_data_new_final_rev(useprint=0, CENSORED=1):

    """uses our final pickle file (containing random quotes, the Book of Revelation etc)"""

    sections = ["whats_going_for_it_",
                "hang_out_at_",
                #"random_quotes_",
                "the_case_against_",
                "final_",
                "well_connected_",
                "from_the_streets_",
                #"where_to_buy_",
                "comments_"
                ]

    ARTICLES_PATH = os.path.join(os.getcwd(), "markov_source", "by_section_final")
    used_sentences = []

    STORY = u""

    for sect in sections:
        if sect == u"well_connected_":
            this_sect_name = u"Travel information:"
        elif sect== u"from_the_streets_":
            this_sect_name = u"Reviewer comments:"
        elif sect== u"the_case_against_":
            this_sect_name = u"Negatives:"
        else:
            this_sect_name = u""

        had_trains  = 0
        had_driving = 0

        sentences = ""
        #paralength = random.choice(range(2,5))
        paralength = random.choice(range(3,6))
        sentence_count = 0

        if sect == u"whats_going_for_it_":
            #num_sentences = random.choice(range(5,20))
            #num_sentences = random.choice(range(19,20))
            #num_sentences = random.choice(range(10,30))
            num_sentences = random.choice(range(5,10))
        elif sect == u"random_quotes_":
            num_sentences = random.choice(range(5,10))
        elif sect == u"final_":
            num_sentences = random.choice(range(15,25))
        else:
            #num_sentences = random.choice(range(2,5))
            #num_sentences = random.choice(range(4,5))
            num_sentences = random.choice(range(2,10))

        #ARTICLES = glob.glob(os.path.join(ARTICLES_PATH, "%s*.txt" % sect))
        #print "SECT:", sect
        #print os.path.join(os.getcwd(), "markov_source", "%scanned_articles.pickle" % sect)
        #pickle_in = open(os.path.join(os.getcwd(), "markov_source", "%scanned_articles.pickle" % sect),"rb")
        pickle_in = open(os.path.join(os.getcwd(), "markov_source", "%scanned_articles.pickle" % sect),"rb")
        #pickle_in = io.open(os.path.join(os.getcwd(), "markov_source", "%scanned_articles.pickle" % sect),"rb")
        model_combination = pickle.load(pickle_in)

        for f in range(0,num_sentences):
            sentence_count = sentence_count + 1
            #THIS_SENTENCE = model_combination.make_short_sentence(max_chars=120, min_chars=20)
            ##THIS_SENTENCE = model_combination.make_short_sentence(max_chars=180, min_chars=30, tries=100)
            #THIS_SENTENCE = model_combination['model'].make_short_sentence(max_chars=180, min_chars=30)

            #THIS_SENTENCE = model_combination.make_sentence(tries=100, test_output=False)
            THIS_SENTENCE = model_combination.make_short_sentence(max_chars=180, min_chars=30, test_output=False, tries=100)

            #print THIS_SENTENCE
            while THIS_SENTENCE in used_sentences:
                #should be pretty rare, but avoid repeats anyway...
                #THIS_SENTENCE = model_combination.make_short_sentence(max_chars=120, min_chars=20)
                ##THIS_SENTENCE = model_combination.make_short_sentence(max_chars=180, min_chars=30)
                #THIS_SENTENCE = model_combination.make_sentence(tries=100, test_output=False)
                THIS_SENTENCE = model_combination.make_short_sentence(max_chars=180, min_chars=30, test_output=False, tries=100)
            used_sentences.append(THIS_SENTENCE)

            #don't want multiple "trains:" or "driving:" sections in our travel information...
            if this_sect_name == u"Travel information:":
                if had_trains == 1 and had_driving == 1:
                    THIS_SENTENCE = u""
                if string.find(THIS_SENTENCE, "Trains:") > -1:
                    if had_trains == 1:
                        while string.find(THIS_SENTENCE, u"Trains:") > -1:
                            #THIS_SENTENCE = model_combination.make_short_sentence(max_chars=120, min_chars=20)
                            ##THIS_SENTENCE = model_combination.make_short_sentence(max_chars=180, min_chars=30)
                            #THIS_SENTENCE = model_combination.make_sentence(tries=100, test_output=False)
                            THIS_SENTENCE = model_combination.make_short_sentence(max_chars=180, min_chars=30, test_output=False, tries=100)
                    had_trains = 1
                if string.find(THIS_SENTENCE, u"Driving:"):
                    if had_driving == 1:
                        while string.find(THIS_SENTENCE, u"Driving:") > -1:
                            #THIS_SENTENCE = model_combination.make_short_sentence(max_chars=120, min_chars=20)
                            ##THIS_SENTENCE = model_combination.make_short_sentence(max_chars=180, min_chars=30)
                            #THIS_SENTENCE = model_combination.make_sentence(tries=100, test_output=False)
                            THIS_SENTENCE = model_combination.make_short_sentence(max_chars=180, min_chars=30, test_output=False, tries=100)
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
                    sentences = u"%s %s" % (string.strip(sentences), string.strip(THIS_SENTENCE))
            else:
                sentences = u"%s\n\n%s" % (sentences, THIS_SENTENCE)
       
        if STORY == u"":
            STORY = u"%s\n%s\n" %(this_sect_name,sentences)
            #STORY = sentences
        else:
            #STORY = "%s\n%s\n" %(this_sect_name,STORY)
            #STORY = "%s\n\n%s" % (STORY, sentences)
            STORY = u"%s\n\n%s\n%s" %(STORY, this_sect_name, sentences)

    #special fiddles... :(
    #sometimes get this wierd character sequence [".".".] ... remove this if we can fix it elsewhere...
    STORY = STORY.replace('''".".".''', '".')

    if  CENSORED == 1:
        STORY = STORY.replace("fuck", 'f***')
        STORY = STORY.replace("bastard", 'b*****d')
    if useprint == 1:
        print STORY

    return STORY
    
#####


def make_chain_from_canned_data():
    # Load the canned combined Markov models

    sections = ["whats_going_for_it_",
                "hang_out_at_",
                "the_case_against_",
                "well_connected_",
                "from_the_streets_",
                "where_to_buy_",
                "comments_"
                ]

    ARTICLES_PATH = os.path.join(os.getcwd(), "markov_source")
    fn = os.path.join(ARTICLES_PATH, "%scanned_articles.pickle" % random.choice(sections))
    #pickle_in = open("canned_articles.pickle","rb")
    pickle_in = open(fn,"rb")
    model_combination = pickle.load(pickle_in)

    numparas = random.choice(range(2,5))

    STORY = u""
    #STORY = "%s\n\n" % HEADLINE

    for f in range(0,numparas):
        sentences = u""
        paralength = random.choice(range(2,5))
        for f in range(0,paralength):
            #THIS_SENTENCE = model_combination.make_short_sentence(max_chars=120, min_chars=20)
            THIS_SENTENCE = model_combination.make_sentence(tries=100)
            if sentences == u"":
                sentences = THIS_SENTENCE
            else:
                sentences = u"%s %s" % (sentences, THIS_SENTENCE)
        if STORY == "":
            STORY = sentences
        else:
            STORY = "%s\n\n%s" % (STORY, sentences)

    #print(model_combination.make_sentence())
    #print STORY
    return STORY       


##def do_usage():
##    progname = string.split(sys.argv[0], os.pathsep)[-1]
##    print """%s (VERSION: %s)
##
##    [-r, -R, regenerate]
##    REGENERATE = pull all the original HTML files from local news sites
##    and re-build both the Corpus and the Markov models.
##    Then build a story.
##
##    [-m, -M, make]
##    MAKE = Rebuild data files from existing raw HTML 
##    (ie DO NOT scrape html from local news sites).
##    Then build a story.
##
##    [-n, -N, new]
##    NEW = Rebuild pickled data files from existing data files  
##    (ie DO NOT scrape html from local news sites and DO NOT rebuild temp files -
##    JUST pickle canned data).
##
##    [-s, -S, story]:
##    STORY = build a story using existing Markov chain data.
##
##    [-c, -C, cannedstory]
##    CANNED STORY = build a story using pickled Markov chain data
##    (from a previous run). This is faster than building it at runtime.
##
##    [-g, -G, generate]
##    GENERATE TO FILE = use pickled Markov chain data to build 100 stories,
##    save them to a file.
##
##
##""" %  (progname, __VERSION__)
##    sys.exit(0)


if __name__ == "__main__":

    progname = string.split(sys.argv[0], os.pathsep)[-1]
    progline = "%s (VERSION: %s)\n" %  (progname, __VERSION__)

    print progline

##    if len(sys.argv) == 1:
##        do_usage()
##
##    elif sys.argv[1] in ["r", "R", "-R", "-r", "REGENERATE", "Regenerate", "regenerate", "regen"]:
##        #get_corpus(REGENERATE_CORPUS=1)
##        make_chain()
##
##    elif sys.argv[1] in ["m", "M", "-M", "-m", "MAKE", "Make", "make", "mak"]:
##        #get_corpus(REGENERATE_CORPUS=0)
##        make_chain()
##
##    elif sys.argv[1] in ["n", "N", "-n", "-N", "New", "NEW", "new"]:
##        make_canned_data()
##
##    elif sys.argv[1] in ["s", "S", "-s", "-S", "STORY", "Story", "story", "sto"]:
##        make_chain()
##
##    elif sys.argv[1] in ["c", "C", "-c", "-C", "CANNEDSTORY", "CannedStory", "cannedstory", "can"]:
##        make_story_from_canned_data()
##
##    elif sys.argv[1] in ["g", "G", "-g", "-G", "GENERATE", "Generate", "generate", "gen"]:
##        make_story_from_canned_data_to_file()
##
##    else:
##        do_usage()
##
##    #get_corpus()
##    #get_corpus()
    #make_chain()

    #make_chain_new()
    if not os.path.isfile(os.path.join("markov_source", "whats_going_for_it_canned_articles.pickle")):
        print "REGENERATING CANNED DATA"
        make_canned_data_new()
    story =  make_story_from_canned_data_new_final(useprint=1, CENSORED=1)
    #story =  make_chain_from_canned_data()
    #print story
    outfile = io.open(os.path.join("TEMP", "STORY.txt"),"w", encoding="UTF-8")
    outfile.write(story)
    outfile.close()

