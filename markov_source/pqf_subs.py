import string

def do_subs(text):

    known_places = [
        "Ankh-Morpock",
        "Lancre",
        "Ramtops",
        "Theocracy of Muntab",
        "Genua",
        "Howondaland",
        "Ghat",
        "Tsort",
        "Quirm",
        "Ephebe",
        "Koom Valley",
        "Bridgwater",
        "New Orleans",
        "Manchester",
        "Reading",
        "Bognor",
        "Manchester",
        "Sheffield",
        "New York",
        "Australia",
        "Wyoming",
        "California",
        "the Discworld",
        "Discworld",
        "river Ankh",
        "Morpork",
        "Ankh",
        "[PLACE]-[PLACE]",
        "Epheb",
        "Tadfield",
        ]

    known_people = [
        "Terry Pratchett",
        "Neil Gaiman",
        "Rincewind",
        "Nanny Ogg",
        "Granny Weatherwax",
        "Carrot",
        "Corporal Nobbs",
        "Sergeant Colon",
        "Nobby",
        "Lord Vetinari",
        "Captain Vimes",
        "Sam Vimes",
        "Lady Ramkin",
        "Brutha",
        "the Patrician",
        "Casanunda",
        "Simony",
        "Angalo de Haberdasheri",
        "Masklin",
        "Gaspode",
        "Greebo",
        "Vimes",
        "Albrecht Duerer",
        "Mort",
        "Albert",
        "Death",
        "Sam",
        "Emberella",
        "Magrat",
        "Hodgesaargh",
        "Willikins",
        "Granny",
        "Victor",
        "Dibbler",
        "Detritus",
        "Johnny",
        "Mrs Ogg",
        "Verence",
        "Terry",
        "Douglas Adams",
        "Sham Harga",
        "Perdita",
        "Agnes",
        "Jekub",
        "Vetinari",
        "Aziraphale",
        "Crowley",
        "Anathema",
        "Madame Tracy",
        "R. P. Tyler",
        "Susan",
        "Ventre",
        "Lord Downey",
        "Mister Teatime",
        "Bigmac",
        "Yo-less",
        "Joshua N'Clement",
        "Johnny",
        "William Stickers",
        "Mrs Liberty",
        "Mrs. Nugent",
        "The Librarian",
        "Mustrum Ridcully",
        "Ridcully",
        "Gengiz Cohen",
        "Salzella",
        "Christine",
        "Agnes",
        "Mr Bucket",
        "Cuddy",
        "Lord Rust",
        "Edward d'Eath",
        "Edward",
        "The Patrician",
        "Sister Mary",
        "Mr Young",
        "Jaime",
        "Keli",
        "Princess Keli",
        "Cutwell",
        "Mort",
        "The Archchancellor",
        "the Bursar",
        "Mr. Dibbler",
        "Azhural",
        "Dibbler",
        "Wobbler",
        "Dios",
        "the Senior Wrangler",
        "Windle",
        "Dhblah",
        "Brother Preptil",
        "Vorbis",
        "Sacharissa",
        "Tiffany",
        "Clodpool",
        "Cohen the Barbarian",
        "Herrena the Henna-Haired Harridan",
        "C.M.O.T Dibbler",
        "Nijel",
        "Iplsore",
        "Owlglass",
        "Daggy",
        "Om",
        "Boggis",
        "Tomjon",
        "Nanny",
        "Conina",
        "Cohen",
        "Glod",
        "Twoflower",
        "Ponder Stibbons",
        "Ponder",
        ]

    #drop quotes from DEATH from UPPER CASE
    #naive and simplistic - could be improved...
    text = string.split(text, " ")
    for w in range(0,len(text)):
        if text[w] == string.upper(text[w]):
            text[w] = string.capwords(text[w])
    text = string.join(text, " ")

    for place in known_places:
        if string.find(text, place) >-1:
            text = string.replace(text, place, "[PLACE]")
            
    for person in known_people:
        if string.find(text, person) >-1:
            text = string.replace(text, person, "[PERSON]")

    return text

if __name__ == "__main__":
    import os
    text = open(os.path.join("raw", "pqf2.txt")).read()
    text = do_subs(text)
    print text
    
                
    