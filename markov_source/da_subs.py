import string

def do_subs(text):

    known_places = [
        "Magrethea",
        "Kakrafoon",
        "Earth",
        "Sevorbeupstry",
        "Sevorsbeupstry",
        "Preliumtarn",
        "Golgafrincham",
        "Alpha Centauri",
        "Codfish Island",
        ]

    known_people = [
        "[Lallafa]",
        "[Zarquon]",
        "[Zaphod]",
        "[Mark Carwardine]",
        "Mark Carwardine",
        "Douglas Adams",
        "Richard Lewis",
        "Arthur Dent",
        "Ford Prefect",
        "Zaphod Beeblebrox",
        "Prostetnic Vogon Jeltz",
        "Dirk Gently",
        "Jeltz",
        "Slartibartfast",
        "Mr. Prosser",
        "Arthur",
        "Ford",
        "Zaphod",
        "Marvin",
        "Trillian",
        "Hotblack",
        "Zarniwoop",
        "Dirk",
        "Zarquon",
        "Dan Streetmentioner",
        "The Hitchhiker's Guide to the Galaxy",
        "[the silver robot]",
        "Lallafa",
        "[The Guide]",
        '["the management consultant"]',
        'Captain',
        'Number One',
        'Number Three',
        'Frogstar Robot',
        'Man in Shack',
        'Nutrimatic Drink Dispenser',
        'Waiter',
        'Dish of the Day',
        ]

    misc_subs = [
        ["on [Vogsphere]", "in [PLACE]"],
        ["on Sqornshellous Zeta", "in [PLACE]"],
        ["[elevator's]", "[PERSON]'s"],
        [" [electronic I Ching calculator] ", " "],
        ["[the Captain's]", "[PERSON]'s"],
        ["a [Komodo] dragon", "a Komodo dragon"],
        ["the female [kakapo]", "the female kakapo"],
        ["[On how human activity on the Yangtze river affects the Baiji:] ",""],
        ["[On the Rodrigues fruitbat:] ",""],
        [" [the kakapo] "," "],
        [" [blows into his bubble pipe] "," "],
        ]

    #strip character names from the radio script quotes...
    text = text.split("\n")
    for l in range(0, len(text)-1):
        if string.find(text[l], ": ") > -1:
            char, script_line = string.split(text[l], ": ", maxsplit=1)
            if char in known_people:
                text[l] = script_line
            elif string.capwords(char) in known_people: 
                text[l] = script_line
    text = string.join(text, "\n")

    for place in known_places:
        if string.find(text, place) >-1:
            text = string.replace(text, place, "[PLACE]")
            
    for person in known_people:
        if string.find(text, person) >-1:
            text = string.replace(text, person, "[PERSON]")

    for sub in misc_subs:
        if string.find(text, sub[0]) >-1:
            text = string.replace(text, sub[0], sub[1])

    return text

if __name__ == "__main__":
    import os
    text = open(os.path.join("raw", "da_quotes.txt")).read()
    text = do_subs(text)
    print text
    
                
    