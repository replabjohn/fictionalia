import string

def do_subs(text):

    known_places = [
        "Babylon",
        "Patmos",
        "Ephesus",
        "Smyrna",
        "Pergamum",
        "Thyatira",
        "Sardis",
        "Philadelphia",
        "Laodicea",
        "Jerusalem",
        #"",
        ]

    known_people = [
        #"Jesus Christ", #Nope,decided not to substitute this one...
        "Balaam",
        "Balak",
        "Jezebel",
        "Judah",
        "Reuben",
        "Gad",
        "Asher",
        "Naphtali",
        "Manasseh",
        "Simeon",
        "Levi",
        "Issachar",
        "Zebulun",
        "Joseph",
        "Benjamin",
        #"",
        ]

    known_locals = [
        "Nicolaitans"
        ]

    known_rivers = [
        "Euphrates"
        ]

    chapterheads = ["Revelation 1\n",
                    "Revelation 2\n",
                    "Revelation 3\n",
                    "Revelation 4\n",
                    "Revelation 5\n",
                    "Revelation 6\n",
                    "Revelation 7\n",
                    "Revelation 8\n",
                    "Revelation 9\n",
                    "Revelation 10\n",
                    "Revelation 11\n",
                    "Revelation 12\n",
                    "Revelation 13\n",
                    "Revelation 14\n",
                    "Revelation 15\n",
                    "Revelation 16\n",
                    "Revelation 17\n",
                    "Revelation 18\n",
                    "Revelation 19\n",
                    "Revelation 20\n",
                    "Revelation 21\n",
                    "Revelation 22\n"]

    #drop any quotes that are all UPPER CASE
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

    for rivers in known_rivers:
        if string.find(text, rivers) >-1:
            text = string.replace(text, rivers, "[RIVER]")

    for locals in known_locals:
        if string.find(text, rivers) >-1:
            text = string.replace(text, rivers, "[LOCALS]")

    #stripout the cpater headings ('Revelation 18' etc). Bit of a dead giveaway...
    for chap in chapterheads:
        text = string.replace(text, chap, "") 

    return text

if __name__ == "__main__":
    import os
    text = open(os.path.join("raw", "revelation.txt")).read()
    text = do_subs(text)
    print text
    
                
    