# fictionalia
A generator for a guide to a fictional county. (NaNoGenMo 2019 entry)


FICTIONALIA
===========

  As distinct from actual, real worlds, possible worlds or "as if" or
  "what if" worlds are all the ways in which a "world" can be, i.e.
  convenient, useful fictions developed as techniques or devices for
  exploring these issues of necessity and possibility that are
  essential for examining non-existent topics such as _FICTIONALIA_,
  universals, qualities, properties (qualia, like "blueness," for
  instance), numbers...

  -- Dragoş Avădanei
     "Hypothetical Fictionalism", 
     Journal of Romanian Literary Studies. Issue no. 17/2019


WHAT IS THIS?

Fictionalia is my entry for NaNoGenMo 2019. It's a generator that
creates a guidebook to a fictional county.

It was inspired by Emily Short's "Annals of the Parrigues", and aims
to produce something between the Annals of the Parrigues and the
Guardian's "Let's Move To..." property columns (both of which it uses
for input).

It started off when I wanted something quick and easy to use various 
routines from a game I am working on in, but soon grew into something 
much larger.


HOW IT WORKS:
#TO BE DONE

NB. Fictionalia only works in Python 2.x (download Python 2.7 from https://www.python.org/download/releases/2.7/)
I haven't upgraded to Python 3.x, since my other games project uses Renpy, and I believe Renpy hasn't upgraded to Python 3 yet.


CREDITS AND ACKNOWLEDGEMENTS:

  Image sources:

    people images in images\this_person_does_not_exist:
    courtesy of https://thispersondoesnotexist.com/
    The This Person Does Not Exist website
    (thispersondoesnotexist.com) was created by 33-year-old software
    engineer Phillip  Wang.

    building illustrations in images\old_book_illustrations:
    courtesy of http://www.oldbookillustrations.com/
    Old Book Illustrations offers a really nice collection of public
    domain illustrations scanned from old books and vector illustrations
    that can be modified and distributed for both personal and commercial
    projects.

    heraldic images in images\badges:
    Most of the devices and creatures used as charges on the shields came from the
    the Free Heraldry Clipart site.
    http://www.heraldicclipart.com/

  Modules used in this program:

	reportlab
		The reportlab toolkit is used to produce PDF output.
		https://www.reportlab.com/opensource/

	PIL
		The Python Image Library.
		https://pypi.org/project/Pillow/

	pycorpora
		Pycorpora.
		Allison Parrish's simple Python interface for Darius Kazemi's Corpora Project. 
		https://github.com/aparrish/pycorpora

	Corpora
		Darius Kazemi's Corpora Project.
		a collection of static corpora (plural of 'corpus') that are potentially useful in the creation of weird internet stuff.
		https://github.com/dariusk/corpora

	markovify
		the file markovify_local.py is our local version of of Jeremy Singer-Vine's markovify library.
		https://github.com/jsvine/markovify/

	noise
		the maps may possibly use the Perlin noise module.
		https://pypi.org/project/noise/


  Text sources:

	The Guardian:
		The majority (200 or so) of the souorce text files are downloaded
		from the "Let's Move To..." articles in the property section of the
		Guardian (written mainly by Tom Dyckhoff (@tomdyckhoff on Twitter),
		though a few were written by Sophie Heawood (@heawood on Twitter)).
		https://www.theguardian.com/money/series/letsmoveto

	The Pratchett Quote File v6.0.
		Original is available from https://www.lspace.org/books/pqf/index.html.

	quotes from Douglas Adams.
		Originals from:
		https://en.wikiquote.org/wiki/Douglas_Adams
		https://en.wikiquote.org/wiki/Last_Chance_to_See
		https://en.wikiquote.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy

	'The Annals of the Parrigues' by Emily Short.
		Original avaliable as a PDF at:
		https://drive.google.com/file/d/0B97d5C256qbrOHFwSUhsZE4tU0k/view
		(read Emily Short's blog entry about it at:
		https://emshort.blog/tag/the-annals-of-the-parrigues/)

	The Book of Revelation, from the Bible
		The Holy Bible, Modern English Version (MEV)
		https://www.bible.com/bible/1171/REV.1.MEV (onwards)


FUTURE PLANS:

The code is a horror. A kludgy mess. It could probably use some
refactoring. (Unicode handling is especially nasty - multiple nested
try and except blocks. Yuk. I *hate* Unicode :( )

I'm going to spend the next month trying to improve text generation.
I'm going to look into using:

	neural networks
	natural language toolkits



