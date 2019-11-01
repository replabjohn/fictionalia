#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

__VERSION__ = "0.9.2a"
__MAKESHIELD_VERSION__ = "0.8c"
DEBUG = 0
#DEBUG = 1

GRAPHICSMODE = "PIL"
#GRAPHICSMODE = "PyGame"

# Use GRAPHICSMODE = "PIL" for standalone Python module or when PDF output is required (using the reportlab toolkit), 
# Use GRAPHICSMODE = "PyGame" for use with Renpy (which is incompatible with PIL)

#standard imports
import random, string
import os, glob, sys
import pprint as pp

#used for saving class files
import pickle

#import of other modules from the game
#import subjects
import names
#from PIL import Image, ImageFilter

from types import *

rootdir = os.getcwd()

if GRAPHICSMODE == "PIL":
    import PIL
    import PIL.Image as PilImage #to avoid nameclashes with Renpy functions
    if DEBUG == 1:
        print "PIL.Image.__file__:", PilImage.__file__
    import PIL.ImageFilter as ImageFilter
    if DEBUG == 1:
        print "PIL.ImageFilter.__file__:", ImageFilter.__file__
        print

elif GRAPHICSMODE == "PyGame":
    import pygame_sdl2 as pygame
    if DEBUG == 1:
        print "pygame.__file__:", pygame.__file__
    import pygame_sdl2
    if DEBUG == 1:
        print "pygame_sdl2.__file__:", pygame_sdl2.__file__
        print
    #pygame_sdl2.import_as_pygame()
    from pygame_sdl2 import image, display
    pygame_sdl2.init()
    pygame_sdl2.display.init()

    if __name__ == "__main__":
        #screen = pygame.display.set_mode((1280, 720))
        screen = pygame.display.set_mode((1,1))


##### SCHOOL STUFF ##### 

def make_possesive(name):
    #Now uses curly quotes instead of straight quotation marks
    #reverted to straight quotes - curly quotes broke things :(
    #they appear in signs as \u2019
    if name[-1] == "s":
        return "%s'" % name
        #return "%s’" % name
    else:
        return "%s's" % name
        #return "%s’s" % name

def make_name(VERBOSE=1):
    Saints_names = [
    #from Wikipedia's "List of Catholic saints"
    #
    #(Only taken up to 1850)

        "Aaron of Aleth",       #Aaron of Aleth (? – 552), Hermit
        "Aaron",                #Aaron of Aleth (? – 552), Hermit
        "Abamun of Tarnut",     #Abamun of Tarnut (? – 372), Martyr
        "Abamun",               #Abamun of Tarnut (? – 372), Martyr
        "Adalard of Corbie",    #Adalard of Corbie (751 – 827), canonized in 1024 by Pope John XIX.
        "Adalard",              #Adalard of Corbie (751 – 827), canonized in 1024 by Pope John XIX.
        "Adalbert of Prague",   #Adalbert of Prague (c. 956 – 997), canonized in 997 by Pope Gregory V.
        "Adalbert",             #Adalbert of Prague (c. 956 – 997), canonized in 997 by Pope Gregory V.
        "Adelaide of Italy",    #Adelaide of Italy (931–999), Married layperson of the Archdiocese of Burgundy, Queen of Italy and Burgundy, Empress, canonized 1097 by Pope Urban II.
        "Adelaide",             #Adelaide of Italy (931–999), Married layperson of the Archdiocese of Burgundy, Queen of Italy and Burgundy, Empress, canonized 1097 by Pope Urban II.
        "Afra of Augsburg",     #Saint Afra of Augsburg (? – 304), Martyr
        "Afra",                 #Saint Afra of Augsburg (? – 304), Martyr
        "Agnes of Montepulciano",#Agnes of Montepulciano, O.P. (1268–1317), canonized in 1726 by Pope Benedict XIII.
        "Agnes of Rome",        #Saint Agnes of Rome (c. 291 – 304), Virgin, Martyr
        "Agnes",                #Agnes of Montepulciano, O.P. (1268–1317), canonized in 1726 by Pope Benedict XIII.
        "Agnes",                #Saint Agnes of Rome (c. 291 – 304), Virgin, Martyr
        "Albert of Sicily",     #Albert of Sicily (c. 1240–1307), canonized in 1476 by Pope Sixtus IV.
        "Albert",               #Albert of Sicily (c. 1240–1307), canonized in 1476 by Pope Sixtus IV.
        "Albertus Magnus",      #Albertus Magnus (c. 1200 – 1280), canonized in 1931 by Pope Pius XI
        "Albertus",             #Albertus Magnus (c. 1200 – 1280), canonized in 1931 by Pope Pius XI
        "Ame",                  #Saint Ame (b.? – 627), canonized in 1049 by Pope Leo IX.
        "Andrew Corsini",       #Andrew Corsini (1302–1373), canonized in 1629 by Pope Urban VIII.
        "Andrew",               #Andrew Corsini (1302–1373), canonized in 1629 by Pope Urban VIII.
        "Anselm of Canterbury", #Anselm of Canterbury (c. 1033–1109), canonized in 1163 by Pope Alexander III.
        "Anselm",               #Anselm of Canterbury (c. 1033–1109), canonized in 1163 by Pope Alexander III.
        "Anthony of Padua",     #Anthony of Padua (1195–1231), canonized in 1232 by Pope Gregory IX.
        "Anthony",              #Anthony of Padua (1195–1231), canonized in 1232 by Pope Gregory IX.
        "Antoninus of Florence",#Antoninus of Florence (1389–1459), canonized in 1523 by Pope Adrian VI.
        "Antoninus",            #Antoninus of Florence (1389–1459), canonized in 1523 by Pope Adrian VI.
        "Aphrodisius",          #(? – 65), Priest of the Diocese of Béziers, Martyr
        "Belina",               #Belina (b.? – 1135), canonized in 1203 by Pope Innocent III.
        "Benedict of Nursia",   #Benedict of Nursia (c. 480 – 543), canonized in 1220 by Pope Honorius III.
        "Benedict",             #Benedict of Nursia (c. 480 – 543), canonized in 1220 by Pope Honorius III.
        "Benno of Meissen",     #Benno of Meissen (c. 1010–1106), canonized in 1523 by Pope Adrian VI.
        "Benno",                #Benno of Meissen (c. 1010–1106), canonized in 1523 by Pope Adrian VI.
        "Berard of Carbio",     #Berard of Carbio (b.? – 1220), canonized in 1481 by Pope Sixtus IV.
        "Berard",               #Berard of Carbio (b.? – 1220), canonized in 1481 by Pope Sixtus IV.
        "Bernard of Corleone",  #Bernard of Corleone (1605–1667), canonized in 2001 by Pope John Paul II.
        "Bernard",              #Bernard of Corleone (1605–1667), canonized in 2001 by Pope John Paul II.
        "Bernardino of Siena",  #Bernardino of Siena (1380–1444), canonized in 1450 by Pope Nicholas V.
        "Bernardino Realino",   #Bernardino Realino (15–1616), Professed Priest of the Jesuits; Venerated on July 31, 1838, Beatified on January 12, 1896, by Pope Leo XIII, Canonized on June 22, 1947, by Pope Pius XII.
        "Bernardino",           #Bernardino of Siena (1380–1444), canonized in 1450 by Pope Nicholas V.
        "Bernardino",           #Bernardino Realino (15–1616), Professed Priest of the Jesuits; Venerated on July 31, 1838, Beatified on January 12, 1896, by Pope Leo XIII, Canonized on June 22, 1947, by Pope Pius XII.
        "Bertrand of Comminges",#Bertrand of Comminges (1050–1126), canonized in 1220 by Pope Honorius III.
        "Bertrand",             #Bertrand of Comminges (1050–1126), canonized in 1220 by Pope Honorius III.
        "Bonaventure",          #Bonaventure (1221–1274), canonized in 1482 by Pope Sixtus IV.
        "Bononio",              #Bononio (b.? – 1026), canonized in 1026 by Pope John XIX.
        "Bridget of Sweden",    #Bridget of Sweden (1303–1373), canonized in 1391 by Pope Boniface IX.
        "Bridget",              #Bridget of Sweden (1303–1373), canonized in 1391 by Pope Boniface IX.
        "Bruno of Segni",       #Bruno of Segni, (c. 1047–1123), canonized in 1181 by Pope Lucius III.
        "Bruno",                #Bruno of Segni, (c. 1047–1123), canonized in 1181 by Pope Lucius III.
        "Casimir",              #Casimir (1458–1484), canonized in 1521 by Pope Leo X.
        "Catherine of Bologna", #Catherine of Bologna (1413–1463), canonized in 1712 by Pope Clement XI.
        "Catherine of Genoa",   #Catherine of Genoa (1447–1510), canonized in 1737 by Pope Clement XII.
        "Catherine of Ricci",   #Catherine of Ricci, O.S.D. (1522–1590), canonized in 1746 by Pope Benedict XIV.
        "Catherine of Siena",   #Catherine of Siena (1347–1380), canonized in 1461 by Pope Pius II.
        "Catherine of Sweden",  #Catherine of Sweden (c. 1332–1381), canonized in 1484 by Pope Innocent VIII.
        "Catherine",            #Catherine of Bologna (1413–1463), canonized in 1712 by Pope Clement XI.
        "Catherine",            #Catherine of Genoa (1447–1510), canonized in 1737 by Pope Clement XII.
        "Catherine",            #Catherine of Ricci, O.S.D. (1522–1590), canonized in 1746 by Pope Benedict XIV.
        "Catherine",            #Catherine of Siena (1347–1380), canonized in 1461 by Pope Pius II.
        "Catherine",            #Catherine of Sweden (c. 1332–1381), canonized in 1484 by Pope Innocent VIII.
        "Charles Borromeo",     #Charles Borromeo (1538–1584), canonized in 1610 by Pope Paul V.
        "Charles",              #Charles Borromeo (1538–1584), canonized in 1610 by Pope Paul V.
        "Clare of Assisi",      #Clare of Assisi (1194–1253), canonized in 1255 by Pope Alexander IV.
        "Clare",                #Clare of Assisi (1194–1253), canonized in 1255 by Pope Alexander IV.
        "Conrad of Constance",  #Conrad of Constance (c. 900 – 975), canonized in 1123 by Pope Callixtus II.
        "Conrad of Piacenza",   #Conrad of Piacenza (c. 1290–1351), canonized in 1625 by Pope Urban VIII.
        "Conrad",               #Conrad of Constance (c. 900 – 975), canonized in 1123 by Pope Callixtus II.
        "Conrad",               #Conrad of Piacenza (c. 1290–1351), canonized in 1625 by Pope Urban VIII.
        "Cunigunde of Luxembourg",#Cunigunde of Luxembourg, OSB (c. 975 – 1040), Empress, canonized in 1200 by Pope Innocent II.
        "Cunigunde",            #Cunigunde of Luxembourg, OSB (c. 975 – 1040), Empress, canonized in 1200 by Pope Innocent II.
        "Edward the Confessor", #Edward the Confessor (1003–1066), canonized in 1161 by Pope Alexander III.
        "Edward",               #Edward the Confessor (1003–1066), canonized in 1161 by Pope Alexander III.
        "Elizabeth of Hungary", #Elizabeth of Hungary (1207–1235), patron saint of the homeless, blessed by St. Francis of Assisi, associated with the Third Order of St. Francis, first saint associated with roses through the miracle of the roses; canonized in 1235 by Pope Gregory IX.
        "Elizabeth of Portugal",#Elizabeth of Portugal (1271–1336), canonized in 1625 by Pope Urban VIII.
        "Elizabeth",            #Elizabeth of Hungary (1207–1235), patron saint of the homeless, blessed by St. Francis of Assisi, associated with the Third Order of St. Francis, first saint associated with roses through the miracle of the roses; canonized in 1235 by Pope Gregory IX.
        "Elizabeth",            #Elizabeth of Portugal (1271–1336), canonized in 1625 by Pope Urban VIII.
        "Emma of Lesum",        #Emma of Lesum (c. 975–980 – 1038)
        "Emma",                 #Emma of Lesum (c. 975–980 – 1038)
        "Felix of Cantalice",   #Felix of Cantalice (1515–1587), canonized in 1712 by Pope Clement I.
        "Felix of Valois",      #Felix of Valois (1127–1212), canonized in 1262 by Pope Urban IV.
        "Felix",                #Felix of Cantalice (1515–1587), canonized in 1712 by Pope Clement I.
        "Felix",                #Felix of Valois (1127–1212), canonized in 1262 by Pope Urban IV.
        "Frances of Rome",      #Frances of Rome (1384–1440), canonized in 1608 by Pope Paul V.
        "Frances",              #Frances of Rome (1384–1440), canonized in 1608 by Pope Paul V.
        "Francis Borgia",       #Francis Borgia (1510–1572), canonized in 1670 by Pope Clement X.
        "Francis de Sales",     #Francis de Sales (1567–1622), canonized in 1665 by Pope Alexander VII.
        "Francis of Assisi",    #Francis of Assisi (1181/1182 – 1226), Italian Roman Catholic friar and preacher; canonized in 1228, by Pope Gregory IX.
        "Francis of Paola",     #Francis of Paola (1416–1507), canonized in 1519 by Pope Leo X.
        "Francis Xavier",       #Francis Xavier, S.J. (1506–1552), canonized in 1622 by Pope Gregory XV.
        "Francis",              #Francis Borgia (1510–1572), canonized in 1670 by Pope Clement X.
        "Francis",              #Francis de Sales (1567–1622), canonized in 1665 by Pope Alexander VII.
        "Francis",              #Francis of Assisi (1181/1182 – 1226), Italian Roman Catholic friar and preacher; canonized in 1228, by Pope Gregory IX.
        "Francis",              #Francis of Paola (1416–1507), canonized in 1519 by Pope Leo X.
        "Francis",              #Francis Xavier, S.J. (1506–1552), canonized in 1622 by Pope Gregory XV.
        "Gerard of Potenza",    #Gerard of Potenza (b.? – 1118), canonized in 1119 by Pope Callixtus II.
        "Gerard of Toul",       #Gerard of Toul (935 – 994), canonized in 1050 by Pope Leo IX.
        "Gerard",               #Gerard of Potenza (b.? – 1118), canonized in 1119 by Pope Callixtus II.
        "Gerard",               #Gerard of Toul (935 – 994), canonized in 1050 by Pope Leo IX.
        "Hedwig of Silesia",    #Hedwig of Silesia (1174–1243), canonized in 1267 by Pope Clement IV.
        "Hedwig",               #Hedwig of Silesia (1174–1243), canonized in 1267 by Pope Clement IV.
        "Hildebrand of Sovana", #Hildebrand of Sovana, Pope Gregory VII, (c. 1015–1085), Pope; canonized in 1728 by Pope Benedict XIII.
        "Hildebrand",           #Hildebrand of Sovana, Pope Gregory VII, (c. 1015–1085), Pope; canonized in 1728 by Pope Benedict XIII.
        "Hildegard of Bingen",  #Hildegard of Bingen (1098–1179), Professed religious of the Benedictine Nuns; beatified in 1326, canonized in 2012 by Pope Benedict XVI), Doctor of the Church in 2012.
        "Hildegard",            #Hildegard of Bingen (1098–1179), Professed religious of the Benedictine Nuns; beatified in 1326, canonized in 2012 by Pope Benedict XVI), Doctor of the Church in 2012.
        "Homobonus of Cremona", #Homobonus of Cremona (b.? – 1197), canonized in 1199 by Pope Innocent III.
        "Homobonus",            #Homobonus of Cremona (b.? – 1197), canonized in 1199 by Pope Innocent III.
        "Hugh of Chateauneuf",  #Hugh of Châteauneuf (1053–1132). canonized in 1134 by Pope Innocent II.
        "Hugh of Cluny",        #Hugh of Cluny a.k.a. Saint Hugh the Great, (1024–1109), canonized in 1120 by Pope Callixtus II.
        "Hugh of Lincoln",      #Hugh of Lincoln (1135/40 – 1200), canonized in 1220 by Pope Honorius III.
        "Hugh the Great",       #Hugh of Cluny a.k.a. Saint Hugh the Great, (1024–1109), canonized in 1120 by Pope Callixtus II.
        "Hugh",                 #Hugh of Châteauneuf (1053–1132). canonized in 1134 by Pope Innocent II.
        "Hugh",                 #Hugh of Cluny a.k.a. Saint Hugh the Great, (1024–1109), canonized in 1120 by Pope Callixtus II.
        "Hugh",                 #Hugh of Lincoln (1135/40 – 1200), canonized in 1220 by Pope Honorius III.
        "Hyacinth of Poland",   #Hyacinth of Poland (ca. 1185–1257), canonized in 1594 by Pope Clement VIII.
        "Hyacinth",             #Hyacinth of Poland (ca. 1185–1257), canonized in 1594 by Pope Clement VIII.
        "Isidore the Laborer",  #Isidore the Laborer (c. 1070 – 1130), canonized in 1622 by Pope Gregory XV.
        "Isidore",              #Isidore the Laborer (c. 1070 – 1130), canonized in 1622 by Pope Gregory XV.
        "James of the Marches", #James of the Marches, O.F.M. (ca. 1391 – 1476), canonized in 1726 by Pope Benedict XIII.
        "James",                #James of the Marches, O.F.M. (ca. 1391 – 1476), canonized in 1726 by Pope Benedict XIII.
        "Joan of Arc",          #Joan of Arc (1412–1431), French heroine and martyr; canonized in 1920 by Pope Benedict XV.
        "Joan",                 #Joan of Arc (1412–1431), French heroine and martyr; canonized in 1920 by Pope Benedict XV.
        "John of Beverley",     #John of Beverley (b.? – 721), canonized in 1037 by Pope Benedict IX.
        "John of Capistrano",   #John of Capistrano (1386–1456), canonized in 1690 by Pope Alexander VIII.
        "John of God",          #John of God (1495–1550), canonized in 1690 by Pope Alexander VIII.
        "John of Matha",        #John of Matha (1160–1213), canonized in 1266 by Pope Alexander VII.
        "John of Nepomuk",      #John of Nepomuk (c. 1345 – 1393), canonized in 1729 by Pope Benedict XIII.
        "John of Sahagun",      #John of Sahagún (1419–1479), canonized in 1690 by Pope Alexander VIII.
        "John of the Cross",    #John of the Cross, O.C.D. (1542–1591), canonized in 1726 by Pope Benedict XIII.
        "John Twenge",          #John Twenge (1319–1379), canonized in 1401 by Pope Boniface IX.
        "John",                 #John of Beverley (b.? – 721), canonized in 1037 by Pope Benedict IX.
        "John",                 #John of Capistrano (1386–1456), canonized in 1690 by Pope Alexander VIII.
        "John",                 #John of God (1495–1550), canonized in 1690 by Pope Alexander VIII.
        "John",                 #John of Matha (1160–1213), canonized in 1266 by Pope Alexander VII.
        "John",                 #John of Nepomuk (c. 1345 – 1393), canonized in 1729 by Pope Benedict XIII.
        "John",                 #John of Sahagún (1419–1479), canonized in 1690 by Pope Alexander VIII.
        "John",                 #John of the Cross, O.C.D. (1542–1591), canonized in 1726 by Pope Benedict XIII.
        "John",                 #John Twenge (1319–1379), canonized in 1401 by Pope Boniface IX.
        "Joseph of Cupertino",  #Joseph of Cupertino, O.F.M. Conv. (Giuseppe Desa) (1603–1663), canonized in 1767 by Pope Clement XIII.
        "Joseph",               #Joseph of Cupertino, O.F.M. Conv. (Giuseppe Desa) (1603–1663), canonized in 1767 by Pope Clement XIII.
        "Juan de Ribera",       #Juan de Ribera (ca. 1532 – 1611), Archbishop of Valencia; Venerated on December 8, 1759, Beatified on September 18, 1796, by Pope Pius VI, Canonized on June 12, 1960, by Pope John XXIII.
        "Juan Diego",           #Juan Diego (1474–1548), is the first Roman Catholic indigenous American saint;[2] canonized in 2002 by Pope John Paul II.
        "Juan",                 #Juan de Ribera (ca. 1532 – 1611), Archbishop of Valencia; Venerated on December 8, 1759, Beatified on September 18, 1796, by Pope Pius VI, Canonized on June 12, 1960, by Pope John XXIII.
        "Juan",                 #Juan Diego (1474–1548), is the first Roman Catholic indigenous American saint;[2] canonized in 2002 by Pope John Paul II.
        "Juliana Falconieri",   #Juliana Falconieri O.S.M., (1270–1341), canonized in 1737 by Pope Clement XII.
        "Juliana",              #Juliana Falconieri O.S.M., (1270–1341), canonized in 1737 by Pope Clement XII.
        "Kinga of Poland",      #Kinga of Poland (1224–1292), canonized in 1690 by Pope Alexander VIII.
        "Kinga",                #Kinga of Poland (1224–1292), canonized in 1690 by Pope Alexander VIII.
        "Lawrence",             # (c. 225–258), Martyr of Rome
        "Lodovico Pavoni",      #Lodovico Pavoni (1784–1849), Priest and founder of the Sons of Mary Immaculate (Pavonians); Venerated on June 5, 1947, Beatified on April 14, 2002, by Pope John Paul II, Canonized on October 16, 2016, by Pope Francis.
        "Lodovico",             #Lodovico Pavoni (1784–1849), Priest and founder of the Sons of Mary Immaculate (Pavonians); Venerated on June 5, 1947, Beatified on April 14, 2002, by Pope John Paul II, Canonized on October 16, 2016, by Pope Francis.
        "Louis Bertrand",       #Louis Bertrand, O.P., (1526–1581), canonized in 1671 by Pope Clement X.
        "Louis of Toulouse",    #Louis of Toulouse (1274–1297), canonized in 1317 by Pope John XXII.
        "Louis",                #Louis Bertrand, O.P., (1526–1581), canonized in 1671 by Pope Clement X.
        "Louis",                #Louis of Toulouse (1274–1297), canonized in 1317 by Pope John XXII.
        "Margaret of Cortona",  #Margaret of Cortona, T.O.S.F. (1247–1297), canonized in 1728 by Pope Benedict XIII.
        "Margaret of Scotland", #Margaret of Scotland (c. 1045–1093), Married layperson and Queen of Scotland; canonized in 1250 by Pope Innocent IV.
        "Margaret",             #Margaret of Cortona, T.O.S.F. (1247–1297), canonized in 1728 by Pope Benedict XIII.
        "Margaret",             #Margaret of Scotland (c. 1045–1093), Married layperson and Queen of Scotland; canonized in 1250 by Pope Innocent IV.
        "Mun",                  #Saint Mun (? – 635), Bishop and Hermit
        "Mungo of Glasgow",     #Saint Mungo of Glasgow (died 614)
        "Mungo",                #Saint Mungo of Glasgow (died 614)
        "Nicholas of Tolentino",#Nicholas of Tolentino (c. 1246–1305), canonized in 1447 (or 1446) by Pope Eugene IV.
        "Nicholas",             #Nicholas of Tolentino (c. 1246–1305), canonized in 1447 (or 1446) by Pope Eugene IV.
        "Nicola Pellegrino",    #Nicola Pellegrino (1075–1094), canonized in 1098 by Pope Urban II.
        "Nicola",               #Nicola Pellegrino (1075–1094), canonized in 1098 by Pope Urban II.
        "Norbert of Xanten",    #Norbert of Xanten (c. 1080–1134), canonized in 1582 by Pope Gregory XIII.
        "Norbert",              #Norbert of Xanten (c. 1080–1134), canonized in 1582 by Pope Gregory XIII.
        "Osmund",               #Osmund (b.? – 1099), canonized in 1457 by Pope Callixtus III.
        "Otto of Bamberg",      #Otto of Bamberg (1060 or 1061–1139). canonized in 1189 by Pope Clement III.
        "Otto",                 #Otto of Bamberg (1060 or 1061–1139). canonized in 1189 by Pope Clement III.
        "Paschal Baylon",       #Paschal Baylon (1540–1592), canonized in 1690 by Pope Alexander VIII.
        "Paschal",              #Paschal Baylon (1540–1592), canonized in 1690 by Pope Alexander VIII.
        "Pedro Armengol",       #Pedro Armengol (c. 1238 – 1304), canonized in 1687 by Pope Innocent XI.
        "Pedro",                #Pedro Armengol (c. 1238 – 1304), canonized in 1687 by Pope Innocent XI.
        "Peter of Alcantara",   #Peter of Alcantara (1499–1562), canonized in 1669 by Pope Clement IX.
        "Peter of Anagni",      #Peter of Anagni (b.? – 1105), canonized in 1109 by Pope Paschal II.
        "Peter of Verona",      #Peter of Verona, O.P. (a.k.a. Peter "Martyr" of Verona) (1206–1252), canonized in 1253 by Pope Innocent IV.
        "Peter",                #Peter of Alcantara (1499–1562), canonized in 1669 by Pope Clement IX.
        "Peter",                #Peter of Anagni (b.? – 1105), canonized in 1109 by Pope Paschal II.
        "Peter",                #Peter of Verona, O.P. (a.k.a. Peter "Martyr" of Verona) (1206–1252), canonized in 1253 by Pope Innocent IV.
        "Procopius of Sazava",  #Procopius of Sázava (c. 970 – 1053), canonized in 1204 by Pope Innocent III.
        "Procopius",            #Procopius of Sázava (c. 970 – 1053), canonized in 1204 by Pope Innocent III.
        "Raymond Nonnatus",     #Raymond Nonnatus (1204–1240), canonized in 1657 by Pope Alexander VII.
        "Raymond",              #Raymond Nonnatus (1204–1240), canonized in 1657 by Pope Alexander VII.
        "Romaric",              #Romaric (b.? – 653), canonized in 1049 by Pope Leo IX.
        "Romuald",              #Romuald (c. 950 – 1027), canonized in 1582 by Pope Gregory XIII.
        "Rose of Lima",         #Rose of Lima, T.O.S.D., (1586–1617), canonized in 1671 by Pope Clement X.
        "Rose",                 #Rose of Lima, T.O.S.D., (1586–1617), canonized in 1671 by Pope Clement X.
        "Sigfrid of Sweden",    #Sigfrid of Sweden (b.? – 1045), canonized in (date unknown) by Pope Adrian IV.
        "Sigfrid",              #Sigfrid of Sweden (b.? – 1045), canonized in (date unknown) by Pope Adrian IV.
        "Stanislaus Kostka",    #Stanislaus Kostka, S.J. (1550–1568), canonized in 1726 by Pope Benedict XIII.
        "Stanislaus",           #Stanislaus Kostka, S.J. (1550–1568), canonized in 1726 by Pope Benedict XIII.
        "Stephen of Muret",     #Stephen of Muret (1045–1124), canonized in 1189 by Pope Clement III.
        "Stephen",              #Stephen of Muret (1045–1124), canonized in 1189 by Pope Clement III.
        "Sturm",                #Saint Sturm (c. 705 – 779), canonized in 1139 by Pope Innocent II.
        "Teresa of Avila",      #Teresa of Ávila (1515–1582), canonized in 1622 by Pope Gregory XV.
        "Teresa",               #Teresa of Ávila (1515–1582), canonized in 1622 by Pope Gregory XV.
        "Theresa of Portugal",  #Theresa of Portugal (1080 – 1130), canonized in 1705 by Pope Clement XI.
        "Theresa",              #Theresa of Portugal (1080 – 1130), canonized in 1705 by Pope Clement XI.
        "Thomas Aquinas",       #Thomas Aquinas (1225–1274), canonized in 1323 by Pope John XXII.
        "Thomas Becket",        #Thomas Becket (b. 1119 or 1120–1170), Archbishop of Canterbury; canonized in 1173 by Pope Alexander III.
        "Thomas de Cantilupe",  #Thomas de Cantilupe (c. 1218–1282), canonized in 1320 by Pope John XXII.
        "Thomas More",          #Thomas More (1478–1535), canonized in 1935 by Pope Pius XI.
        "Thomas of Villanova",  #Thomas of Villanova (1488–1555), canonized in 1658 by Pope Alexander VII.
        "Thomas",               #Thomas Aquinas (1225–1274), canonized in 1323 by Pope John XXII.
        "Thomas",               #Thomas Becket (b. 1119 or 1120–1170), Archbishop of Canterbury; canonized in 1173 by Pope Alexander III.
        "Thomas",               #Thomas de Cantilupe (c. 1218–1282), canonized in 1320 by Pope John XXII.
        "Thomas",               #Thomas More (1478–1535), canonized in 1935 by Pope Pius XI.
        "Thomas",               #Thomas of Villanova (1488–1555), canonized in 1658 by Pope Alexander VII.
        "Ulrich of Augsburg",   #Ulrich of Augsburg (890 – 973), canonized in 993 by Pope John XV.
        "Ulrich",               #Ulrich of Augsburg (890 – 973), canonized in 993 by Pope John XV.
        "Vergilius of Salzburg",#Vergilius of Salzburg (c. 700 – 784), canonized in 1232 by Pope Gregory IX.
        "Vergilius",            #Vergilius of Salzburg (c. 700 – 784), canonized in 1232 by Pope Gregory IX.
        "Vincent de Paul",      #Vincent de Paul (1581–1660), canonized in 1737 by Pope Clement XII.
        "Vincent Ferrer",       #Vincent Ferrer, O.P. (1350–1419), canonized in 1455 by Pope Callixtus III.
        "Vincent",              #Vincent de Paul (1581–1660), canonized in 1737 by Pope Clement XII.
        "Vincent",              #Vincent Ferrer, O.P. (1350–1419), canonized in 1455 by Pope Callixtus III.
        "William of Gellone",   #William of Gellone (755 – 812 or 814), canonized in 1066 by Pope Alexander II.
        "William of Perth",     #William of Perth (b.? – c. 1201), canonized in 1256 by Pope Alexander IV.
        "William of Roskilde",  #William of Roskilde (da) (b.? – 1073 or 1074), canonized in 1224 by Pope Honorius III.
        "William",              #William of Gellone (755 – 812 or 814), canonized in 1066 by Pope Alexander II.
        "William",              #William of Perth (b.? – c. 1201), canonized in 1256 by Pope Alexander IV.
        "William",              #William of Roskilde (da) (b.? – 1073 or 1074), canonized in 1224 by Pope Honorius III.
        "Wolfgang of Regensburg",#Wolfgang of Regensburg (c.934 – 994), canonized in 1051 by Pope Leo IX.
        "Wolfgang",             #Wolfgang of Regensburg (c.934 – 994), canonized in 1051 by Pope Leo IX.
        "Wulstan",              #Wulstan (c. 1008–1095), canonized in 1203 by Pope Celestine III.
        "Zita of Lucca",        #Zita of Lucca (c. 1212 – 1272), canonized in 1696 by Pope Innocent XII.
        "Zita",                 #Zita of Lucca (c. 1212 – 1272), canonized in 1696 by Pope Innocent XII.

    #from Encyclopaedia Britannica's "List of saints"
    #
    #The following is a list of saints recognized by the Roman Catholic
    #Church and/or Eastern Orthodox churches...
        "Adalbert",             #Adalbert (Bohemian)
        "Adamnan",              #Adamnan (Irish)
        "Adelaide",             #Adelaide (French)
        "Agatha",               #Agatha (Italian)
        "Agnes",                #Agnes (Roman)
        "Agobard",              #Agobard (Spanish)
        "Aidan",                #Aidan (English)
        "Aidan",                #Aidan (Irish)
        "Alban",                #Alban (English)
        "Albertus Magnus",      #Albertus Magnus (German)
        "Albertus",             #Albertus Magnus (German)
        "Alexander Nevsky",     #Alexander Nevsky (Russian)
        "Alexander",            #Alexander Nevsky (Russian)
        "Alexis",               #Alexis (Russian)
        "Aloysius Gonzaga",     #Aloysius Gonzaga (Italian)
        "Aloysius",             #Aloysius Gonzaga (Italian)
        "Ambrose",              #Ambrose (Gaulish)
        "Andrew of Crete",      #Andrew of Crete (Syrian)
        "Andrew",               #Andrew (biblical)
        "Andrew",               #Andrew of Crete (Syrian)
        "Angela Merici",        #Angela Merici (Italian)
        "Angela",               #Angela Merici (Italian)
        "Anne",                 #Anne (biblical)
        "Anselm of Canterbury", #Anselm of Canterbury (English)
        "Anselm",               #Anselm of Canterbury (English)
        "Anthony of Egypt",     #Anthony of Egypt (Egyptian)
        "Anthony of Kiev",      #Anthony of Kiev (Ukrainian)
        "Anthony of Padua",     #Anthony of Padua (Portuguese)
        "Anthony",              #Anthony of Egypt (Egyptian)
        "Anthony",              #Anthony of Kiev (Ukrainian)
        "Anthony",              #Anthony of Padua (Portuguese)
        "Arsenius the Great",   #Arsenius the Great (Roman)
        "Arsenius",             #Arsenius the Great (Roman)
        "Athanasius",           #Athanasius (Egyptian)
        "Augustine of Canterbury",#Augustine of Canterbury (English)
        "Augustine",            #Augustine of Canterbury (English)
        "Augustine",            #Augustine (Numidian)
        "Bacchus",              #Saints Sergius and Bacchus (Roman)
        "Barbara",              #Barbara (other)
        "Barnabas",             #Barnabas (biblical)
        "Bartholomew",          #Bartholomew (biblical)
        "Basil the Great",      #Basil the Great (Turkish)
        "Basil",                #Basil the Great (Turkish)
        "Bede the Venerable",   #Bede the Venerable (English)
        "Bede",                 #Bede the Venerable (English)
        "Benedict of Nursia",   #Benedict of Nursia (Italian)
        "Benedict",             #Benedict of Nursia (Italian)
        "Benno",                #Benno (German)
        "Bernadette of Lourdes",#Bernadette of Lourdes (French)
        "Bernadette",           #Bernadette of Lourdes (French)
        "Bernard de Clairvaux", #Bernard de Clairvaux (French)
        "Bernard of Menthon",   #Bernard of Menthon (Italian)
        "Bernard",              #Bernard de Clairvaux (French)
        "Bernard",              #Bernard of Menthon (Italian)
        "Blaise",               #Blaise (Turkish)
        "Bonaventure",          #Bonaventure (Italian)
        "Boniface",             #Boniface (English)
        "Brendan",              #Brendan (Irish)
        "Bridget of Sweden",    #Bridget of Sweden (Swedish)
        "Bridget",              #Bridget of Sweden (Swedish)
        "Brigit of Ireland",    #Brigit of Ireland (Irish)
        "Brigit",               #Brigit of Ireland (Irish)
        "Bruno of Querfurt",    #Bruno of Querfurt (Saxon)
        "Bruno the Carthusian", #Bruno the Carthusian (German)
        "Bruno the Great",      #Bruno the Great (German)
        "Bruno",                #Bruno of Querfurt (Saxon)
        "Bruno",                #Bruno the Carthusian (German)
        "Bruno",                #Bruno the Great (German)
        "Catherine of Alexandria",#Catherine of Alexandria (Egyptian)
        "Catherine of Bologna", #Catherine of Bologna (Italian)
        "Catherine of Genoa",   #Catherine of Genoa (Italian)
        "Catherine of Siena",   #Catherine of Siena (Italian)
        "Catherine of Sweden",  #Catherine of Sweden (Swedish)
        "Catherine",            #Catherine (Italian)
        "Catherine",            #Catherine of Alexandria (Egyptian)
        "Catherine",            #Catherine of Bologna (Italian)
        "Catherine",            #Catherine of Genoa (Italian)
        "Catherine",            #Catherine of Siena (Italian)
        "Catherine",            #Catherine of Sweden (Swedish)
        "Cecilia",              #Cecilia (Roman)
        "Chad",                 #Chad (English)
        "Christopher",          #Christopher (Roman)
        "Ciaran of Clonmacnoise",#Ciaran of Clonmacnoise (Irish)
        "Ciaran",               #Ciaran of Clonmacnoise (Irish)
        "Clare of Assisi",      #Clare of Assisi (Italian)
        "Clare",                #Clare of Assisi (Italian)
        "Clement of Alexandria",#Clement of Alexandria (Egyptian)
        "Clement of Alexandria",#Clement of Alexandria (Greek)
        "Clement",              #Clement of Alexandria (Egyptian)
        "Clement",              #Clement of Alexandria (Greek)
        "Clotilda",             #Clotilda (Frankish)
        "Colette",              #Colette (French)
        "Colman of Lindisfarne",#Colman of Lindisfarne (Irish)
        "Colman",               #Colman of Lindisfarne (Irish)
        "Columba",              #Columba (Irish)
        "Columban",             #Columban (Irish)
        "Cornelius",            #Cornelius (Roman)
        "Cosmas",               #Cosmas (Turkish)
        "Crispin",              #Crispin (Roman)
        "Cuthbert Mayne",       #Cuthbert Mayne (English)
        "Cuthbert",             #Cuthbert (English)
        "Cuthbert",             #Cuthbert Mayne (English)
        "Cyprian",              #Cyprian (Bulgarian)
        "Cyprian",              #Cyprian (Tunisian)
        "Cyril of Alexandria",  #Cyril of Alexandria (Egyptian)
        "Cyril of Jerusalem",   #Cyril of Jerusalem (Roman)
        "Cyril",                #Cyril of Alexandria (Egyptian)
        "Cyril",                #Cyril of Jerusalem (Roman)
        "Cyril",                #Saints Cyril and Methodius (Greek)
        "Damian",               #Damian (Turkish)
        "Damien of Molokai",    #Damien of Molokai (American)
        "Damien of Molokai",    #Damien of Molokai (Belgian)
        "Damien",               #Damien of Molokai (American)
        "Damien",               #Damien of Molokai (Belgian)
        "David",                #David (Welsh)
        "Denis",                #Denis (French)
        "Deusdedit",            #Deusdedit (Italian)
        "Dionysius of Alexandria", #Dionysius of Alexandria (Egyptian)
        "Dionysius",            #Dionysius of Alexandria (Egyptian)
        "Dioynsius",            #Dioynsius (Greek - birthplace unconfirmed)
        "Dominic",              #Dominic (Spanish)
        "Dunstan of Canterbury",#Dunstan of Canterbury (English)
        "Dunstan",              #Dunstan of Canterbury (English)
        "Edmund of Abington",   #Edmund of Abington (English)
        "Edmund",               #Edmund of Abington (English)
        "Edward the Confessor", #Edward the Confessor (English)
        "Edward",               #Edward the Confessor (English)
        "Elizabeth of Hungary", #Elizabeth of Hungary (Hungarian)
        "Elizabeth of Portugal",#Elizabeth of Portugal (Portuguese)
        "Elizabeth",            #Elizabeth of Hungary (Hungarian)
        "Elizabeth",            #Elizabeth of Portugal (Portuguese)
        "Ephraem Syrus",        #Ephraem Syrus (Syrian)
        "Ephraem Syrus",        #Ephraem Syrus (Syrian)
        "Erasmus",              #Erasmus (Roman)
        "Eusebius of Samosata", #Eusebius of Samosata (Syrian)
        "Eusebius of Vercelli", #Eusebius of Vercelli (Italian)
        "Eusebius",             #Eusebius (Greek)
        "Eusebius",             #Eusebius of Samosata (Syrian)
        "Eusebius",             #Eusebius of Vercelli (Italian)
        "Eustace",              #Eustace (Roman)
        "Eustathius of Antioch",#Eustathius of Antioch (Turkish)
        "Eustathius of Thessalonica",#Eustathius of Thessalonica (Turkish)
        "Eustathius",           #Eustathius of Antioch (Turkish)
        "Eustathius",           #Eustathius of Thessalonica (Turkish)
        "Euthymius of Turnovo", #Euthymius of Tŭrnovo (Bulgarian)
        "Euthymius the Great",  #Euthymius the Great (Armenian)
        "Euthymius",            #Euthymius of Tŭrnovo (Bulgarian)
        "Euthymius",            #Euthymius the Great (Armenian)
        "Fabian",               #Fabian (Roman)
        "Faustus of Riez",      #Faustus of Riez (French)
        "Faustus",              #Faustus of Riez (French)
        "Felix of Valois",      #Felix of Valois (French)
        "Felix",                #Felix of Valois (French)
        "Flavian",              #Flavian (Turkish)
        "Frances of Rome",      #Frances of Rome (Italian)
        "Frances",              #Frances of Rome (Italian)
        "Francis Borgia",       #Francis Borgia (Spanish)
        "Francis de Sales",     #Francis of Sales (French)
        "Francis of Assisi",    #Francis of Assisi (Italian)
        "Francis of Paola",     #Francis of Paola (Italian)
        "Francis of Sales",     #Francis of Sales (French)
        "Francis Xavier",       #Francis Xavier (Spanish)
        "Francis",              #Francis Borgia (Spanish)
        "Francis",              #Francis of Assisi (Italian)
        "Francis",              #Francis of Paola (Italian)
        "Francis",              #Francis of Sales (French)
        "Francis",              #Francis Xavier (Spanish)
        "Fulbert of Chartres",  #Fulbert of Chartres (French)
        "Fulbert",              #Fulbert of Chartres (French)
        "Fulgentius of Ruspe",  #Fulgentius of Ruspe (Tunisian)
        "Fulgentius",           #Fulgentius of Ruspe (Tunisian)
        "Gabriel",              #Gabriel (archangel, venerated as a saint by some traditions)
        "Gaius",                #Gaius (Roman)
        "Genevieve",            #Geneviève (French)
        "George",               #George  (Roman)
        "Gerard",               #Gerard (Hungarian)
        "Gerard",               #Gerard (Italian)
        "Germanus of Paris",    #Germanus of Paris (French)
        "Germanus",             #Germanus of Paris (French)
        "Gilbert of Sempringham",#Gilbert of Sempringham (English)
        "Gilbert",              #Gilbert of Sempringham (English)
        "Gregory of Nyssa",     #Gregory of Nyssa (Turkish)
        "Gregory of Tours",     #Gregory of Tours (Frankish)
        "Gregory Palamas",      #Gregory Palamas (Greek)
        "Gregory Thaumaturgus", #Gregory Thaumaturgus (Turkish)
        "Gregory the Illuminator", #Gregory the Illuminator (Armenian)
        "Gregory",              #Gregory of Nyssa (Turkish)
        "Gregory",              #Gregory of Tours (Frankish)
        "Gregory",              #Gregory Palamas (Greek)
        "Gregory",              #Gregory Thaumaturgus (Turkish)
        "Gregory",              #Gregory the Illuminator (Armenian)
        "Helena",               #Helena (Roman)
        "Hilarion",             #Hilarion (Palestinian)
        "Hilary of Arles",      #Hilary of Arles (Gaulish)
        "Hilary of Poitiers",   #Hilary of Poitiers (French)
        "Hilary",               #Hilary (Italian)
        "Hilary",               #Hilary of Arles (Gaulish)
        "Hilary",               #Hilary of Poitiers (French)
        "Hilda of Whitby",      #Hilda of Whitby (English)
        "Hilda",                #Hilda of Whitby (English)
        "Hildegard",            #Hildegard (German)
        "Hippolytus of Rome",   #Hippolytus of Rome (Roman)
        "Hippolytus",           #Hippolytus of Rome (Roman)
        "Hugh of Cluny",        #Hugh of Cluny (French)
        "Hugh of Lincoln",      #Hugh of Lincoln (English)
        "Hugh of Lincoln",      #Hugh of Lincoln (French)
        "Hugh",                 #Hugh of Cluny (French)
        "Hugh",                 #Hugh of Lincoln (English)
        "Hugh",                 #Hugh of Lincoln (French)
        "Ignatius of Loyola",   #Ignatius of Loyola (Spanish)
        "Ignatius",             #Ignatius of Loyola (Spanish)
        "Isaac Jogues",         #Isaac Jogues (French)
        "Isaac the Great",      #Isaac the Great (Armenian)
        "Isaac",                #Isaac Jogues (French)
        "Isaac",                #Isaac the Great (Armenian)
        "Isidore of Sevilla",   #Isidore of Sevilla (Spanish)
        "Isidore",              #Isidore of Sevilla (Spanish)
        "James",                #James, son of Alphaeus (biblical)
        "James",                #James, son of Zebedee (biblical)
        "James",                #James, the Lord’s brother (biblical)
        "Jerome",               #Jerome (Roman)
        "Joachim",              #Joachim (biblical)
        "Joan of Arc",          #Joan of Arc (French)
        "Joan",                 #Joan of Arc (French)
        "John Bosco",           #John Bosco (Italian)
        "John Cassian",         #John Cassian (Roman)
        "John Eudes",           #John Eudes (French)
        "John Leonardi",        #John Leonardi (Italian)
        "John Neumann",         #John Neumann (Bohemian)
        "John of Avila",        #John of Avila (Spanish)
        "John of Beverley",     #John of Beverley (English)
        "John of Capistrano",   #John of Capistrano (Austrian)
        "John of Damascus",     #John of Damascus (Syrian)
        "John of Matha",        #John of Matha (French)
        "John of the Cross",    #John of the Cross (Spanish)
        "John the Apostle",     #John the Apostle (biblical)
        "John the Baptist",     #John the Baptist (biblical)
        "John the Faster",      #John the Faster (Turkish)
        "John",                 #John Bosco (Italian)
        "John",                 #John Cassian (Roman)
        "John",                 #John Eudes (French)
        "John",                 #John Leonardi (Italian)
        "John",                 #John Neumann (Bohemian)
        "John",                 #John of Avila (Spanish)
        "John",                 #John of Beverley (English)
        "John",                 #John of Capistrano (Austrian)
        "John",                 #John of Damascus (Syrian)
        "John",                 #John of Matha (French)
        "John",                 #John of the Cross (Spanish)
        "John",                 #John the Apostle (biblical)
        "John",                 #John the Baptist (biblical)
        "John",                 #John the Faster (Turkish)
        "Joseph of Arimathea",  #Joseph of Arimathea (biblical)
        "Joseph of Volokolamsk",#Joseph of Volokolamsk (Russian)
        "Joseph",               #Joseph (biblical)
        "Joseph",               #Joseph of Volokolamsk (Russian)
        "Juan Diego",           #Juan Diego (Mexican)
        "Juan",                 #Juan Diego (Mexican)
        "Judas",                #Judas (biblical)
        "Junipero Serra",       #Junípero Serra (Spanish)
        "Junipero",             #Junípero Serra (Spanish)
        "Justus",               #Justus (English)
        "Justus",               #Justus (Italian)
        "Juvenal",              #Juvenal (Roman - birthplace unconfirmed)
        "Kenneth",              #Kenneth (Irish)
        "Kentigern",            #Kentigern (Scottish)
        "Kevin",                #Kevin (Irish)
        "Laurentius of Canterbury",#Laurentius of Canterbury (English)
        "Laurentius",           #Laurentius of Canterbury (English)
        "Lawrence of Brindisi", #Lawrence of Brindisi (Italian)
        "Lawrence",             #Lawrence (Roman)
        "Lawrence",             #Lawrence of Brindisi (Italian)
        "Linus",                #Linus (Roman)
        "Louise de Marillac",   #Louise de Marillac (French)
        "Louise",               #Louise de Marillac (French)
        "Lucian of Antioch",    #Lucian of Antioch (Syrian)
        "Lucian",               #Lucian of Antioch (Syrian)
        "Lucy",                 #Lucy (Italian)
        "Ludmila",              #Ludmila (Bohemian)
        "Luke",                 #Luke (biblical)
        "Margaret Clitherow",   #Margaret Clitherow (English)
        "Margaret of Antioch",  #Margaret of Antioch (Syrian)
        "Margaret of Scotland", #Margaret of Scotland (Scottish)
        "Margaret",             #Margaret Clitherow (English)
        "Margaret",             #Margaret of Antioch (Syrian)
        "Margaret",             #Margaret of Scotland (Scottish)
        "Mark",                 #Mark (biblical)
        "Mark",                 #Mark (Roman)
        "Martin de Porres",     #Martín de Porres (Peruvian)
        "Martin of Tours",      #Martin of Tours (French)
        "Martin",               #Martín de Porres (Peruvian)
        "Martin",               #Martin of Tours (French)
        "Mary Magdalene",       #Mary Magdalene (biblical)
        "Mary of the Incarnation",#Mary of the Incarnation (French)
        "Mary",                 #Mary (biblical)
        "Mary",                 #Mary Magdalene (biblical)
        "Mary",                 #Mary of the Incarnation (French)
        "Matthew",              #Matthew (biblical)
        "Matthias",             #Matthias (biblical)
        "Maurice",              #Maurice (Swiss)
        "Maximus the Confessor",#Maximus the Confessor (Turkish)
        "Maximus the Greek",    #Maximus the Greek (Greek)
        "Maximus",              #Maximus the Confessor (Turkish)
        "Maximus",              #Maximus the Greek (Greek)
        "Methodius",            #Saints Cyril and Methodius (Greek)
        "Michael",              #Michael (archangel, venerated as a saint by some traditions)
        "Nicholas of Flue",     #Nicholas of Flüe (Swiss)
        "Nicholas",             #Nicholas (Turkish)
        "Nicholas",             #Nicholas of Flüe (Swiss)
        "Nicodemus the Hagiorite",#Nicodemus the Hagiorite (Greek)
        "Nicodemus",            #Nicodemus the Hagiorite (Greek)
        "Ninian",               #Ninian (Scottish)
        "Norbert of Xanten",    #Norbert of Xanten (German)
        "Norbert",              #Norbert of Xanten (German)
        "Odo of Cluny",         #Odo of Cluny (French)
        "Odo",                  #Odo of Cluny (French)
        "Olga",                 #Olga (Russian)
        "Oliver Plunket",       #Oliver Plunket (Irish)
        "Oliver",               #Oliver Plunket (Irish)
        "Osmund of Salisbury",  #Osmund of Salisbury (English)
        "Osmund",               #Osmund of Salisbury (English)
        "Oswald of Northumbria",#Oswald of Northumbria (English)
        "Oswald of York",       #Oswald of York (English)
        "Oswald",               #Oswald of Northumbria (English)
        "Oswald",               #Oswald of York (English)
        "Padre Pio",            #Padre Pio (Italian)
        "Patrick",              #Patrick (English)
        "Patrick",              #Patrick (Irish)
        "Paul of the Cross",    #Paul of the Cross (Italian)
        "Paul of Thebes",       #Paul of Thebes (Egyptian)
        "Paul",                 #Paul (biblical)
        "Paul",                 #Paul of the Cross (Italian)
        "Paul",                 #Paul of Thebes (Egyptian)
        "Paulinus",             #Paulinus (English)
        "Pelagia of Antioch",   #Pelagia of Antioch (Syrian)
        "Pelagia",              #Pelagia of Antioch (Syrian)
        "Perpetua",             #Perpetua (Roman)
        "Peter Claver",         #Peter Claver (Spanish)
        "Peter Martyr",         #Peter Martyr (Italian)
        "Peter Nolasco",        #Peter Nolasco (French)
        "Peter of Alcantara",   #Peter of Alcántara (Spanish)
        "Peter the Venerable",  #Peter the Venerable (French)
        "Peter",                #Peter (biblical)
        "Peter",                #Peter Claver (Spanish)
        "Peter",                #Peter Martyr (Italian)
        "Peter",                #Peter Nolasco (French)
        "Peter",                #Peter of Alcántara (Spanish)
        "Peter",                #Peter the Venerable (French)
        "Philip Neri",          #Philip Neri (Italian)
        "Philip the Apostle",   #Philip the Apostle (biblical)
        "Philip the Evangelist",#Philip the Evangelist (biblical)
        "Philip",               #Philip Neri (Italian)
        "Philip",               #Philip the Apostle (biblical)
        "Philip",               #Philip the Evangelist (biblical)
        "Photius",              #Photius (Turkish)
        "Polycarp",             #Polycarp (Greek)
        "Pontian",              #Pontian (Roman)
        "Quadratus",            #Quadratus (Roman)
        "Raphael",              #Raphael (archangel, venerated as a saint by some traditions)
        "Raymond of Penafort",  #Raymond of Peñafort (Spanish)
        "Raymond",              #Raymond of Peñafort (Spanish)
        "Remigius of Reims",    #Remigius of Reims (French)
        "Remigius",             #Remigius of Reims (French)
        "Richard of Chichester",#Richard of Chichester (English)
        "Richard",              #Richard of Chichester (English)
        "Rose of Lima",         #Rose of Lima (Peruvian)
        "Rose",                 #Rose of Lima (Peruvian)
        "Sebastian",            #Sebastian (Roman)
        "Sergius",              #Saints Sergius and Bacchus (Roman)
        "Severus of Antioch",   #Severus of Antioch (Turkish)fP
        "Severus",              #Severus of Antioch (Turkish)
        "Silas",                #Silas (biblical)
        "Simeon Stylites",      #Simeon Stylites (Syrian)
        "Simeon",               #Simeon Stylites (Syrian)
        "Simon the Apostle",    #Simon the Apostle (biblical)
        "Simon",                #Simon the Apostle (biblical)
        "Stanislaus of Krakow", #Stanislaus of Kraków (Polish)
        "Stanislaus",           #Stanislaus of Kraków (Polish)
        "Stephen of Perm",      #Stephen of Perm (Russian)
        "Stephen",              #Stephen (biblical)
        "Stephen",              #Stephen of Perm (Russian)
        "Swithin",              #Swithin (English)
        "Symeon the New Theologian",#Symeon the New Theologian (Turkish)
        "Symeon",               #Symeon the New Theologian (Turkish)
        "Teresa of Avila",      #Teresa of Ávila (Spanish)
        "Teresa",               #Teresa of Ávila (Spanish)
        "Theodore of Canterbury",#Theodore of Canterbury (English)
        "Theodore Studites",    #Theodore Studites (Turkish)
        "Theodore",             #Theodore of Canterbury (English)
        "Theodore",             #Theodore Studites (Turkish)
        "Theodosius of Palestine",#Theodosius of Palestine (Palestinian)
        "Theodosius",           #Theodosius of Palestine (Palestinian)
        "Theophanes the Confessor", #Theophanes the Confessor (Byzantine)
        "Theophanes",           #Theophanes the Confessor (Byzantine)
        "Theophilus of Alexandria",#Theophilus of Alexandria (Egyptian)
        "Theophilus of Antioch",#Theophilus of Antioch (Syrian)
        "Theophilus",           #Theophilus of Alexandria (Egyptian)
        "Theophilus",           #Theophilus of Antioch (Syrian)
        "Therese of Lisieux",   #Thérèse of Lisieux (French)
        "Therese",              #Thérèse of Lisieux (French)
        "Thomas Aquinas",       #Thomas Aquinas (Italian)
        "Thomas Becket",        #Thomas Becket (English)
        "Thomas More",          #Thomas More (English)
        "Thomas",               #Thomas (biblical)
        "Thomas",               #Thomas Aquinas (Italian)
        "Thomas",               #Thomas Becket (English)
        "Thomas",               #Thomas More (English)
        "Timothy",              #Timothy (biblical)
        "Titus",                #Titus (biblical)
        "Ulrich",               #Ulrich (German)
        "Ursula",               #Ursula (other)
        "Valentine",            #Valentine (Roman)
        "Veronica",             #Veronica (biblical)
        "Vincent Ferrer",       #Vincent Ferrer (French)
        "Vincent of Lerins",    #Vincent of Lérins (French)
        "Vincent",              #Vincent Ferrer (French)
        "Vincent",              #Vincent of Lérins (French)
        "Vitalian",             #Vitalian (Italian)
        "Vladimir",             #Vladimir I (Ukrainian)
        "Wilfrid",              #Wilfrid (English)
        "Wulfstan",             #Wulfstan (English)
        "Zephyrinus",           #Zephyrinus (Italian - birthplace unconfirmed)
        "Zosimus",              #Zosimus (Greek)

        #A very short list of FICTIONAL saints - as used in fictional schools
        #These are the ONLY ONES that are fictional in this list.
        #All the rest are REAL!
        "Trinian",             #St Trinians -  from the cartoons by Ronald Searle, and later films
        "Custard",             #St Custards - from the Nigel Molesworth books by Geoffrey Willans (illustrated by Ronald Searle)
        "Lemon",               #The Beano ran a series entitled The Belles of St. Lemons, inspired by the original St. Trinian's cartoons
        #Repeated to make them that tiny bit more likely to come up :)
        "Trinian",
        "Custard",
        "Lemon"#,
    ]

    #if VERBOSE == 1:
    #    print "%s saints known about" % len(Saints_names)

    school_types= ["Sixth Form College",
                    "6th Form College",
                    "Academy",
                    "Academy",
                    "Free School",
                    "Comprehensive School",
                    "Grammar School",
                    "College",
                    "College",
                    "School"#,
                    ]

    saint = random.choice(Saints_names)

    beginning = random.choice(("St", "St.", "Saint"))
    school_type = random.choice(school_types)

    """
    if len(string.split(saint, " ")) == 1:
        saint = "%s %s " % (beginning, make_possesive(saint))
    else:
        saint = "the %s %s " % (beginning, saint)
"""
    name = "%s %s" % (beginning, saint)
    #name_short = "%s " % (saint) 

    if len(string.split(saint, " ")) == 1:
        saint = "%s %s" % (beginning, make_possesive(saint))
        name_full = "%s %s" % (saint, school_type)
        name_short = "%s " % (saint) 
    else:
        name_short = "%s %s" % (beginning, make_possesive(string.split(saint)[0]))
        saint = "the %s %s" % (beginning, saint)
        name_full = "%s %s" % (saint, school_type)

    return (name, name_short, name_full, school_type)

class School:
    """holder for all the information and images to do with any single instantiation of a school."""

    def __init__(self):
        #for debugging
        self.VERBOSE = 0
        #self.VERBOSE = 1
        self.CREATED_BY_VERSION = __VERSION__

        #Name-related properties
        self.name = None
        self.saints_name = None #won't be used much, but included for completeness
        self.name_short = None
        self.name_full = None
        self.school_type = None

        #uniform-related properties 
        self.badge_blazer_colour    = [None, None]
        self.badge_tie_colour_1     = [None, None]
        self.badge_tie_colour_2     = [None, None]

        #badge-related properties 
        self.badge          = None
        self.badge_blazon   = None
        self.badge_fname    = None

        self.sign           = None
        self.sign_type      = None
        self.sign_fname     = None
        #The font object itself...
        #used for convenience
        self.sign_font      = None
        #Text strings, so we can recreate it after unpicking
        #(Pickle can't handle Font objects)
        self.sign_font_name = None
        self.sign_font_size = None

        #this one used for sign
        self.headteacher_name  = None

        #other properties
        self.languages_taught   = None
        self.subjects_taught    = None

        #map properties
        self.map_orientation    = None
        self.map                = None
        self.map_class_flooringtype   = None
        self.map_office_flooringtype  = None
        self.map_level1_documentnumber  = None
        self.map_level2_documentnumber  = None
        self.map_level3_documentnumber  = None
        self.map_level4_documentnumber  = None

        #Classroom image related properties
        self.class_table_type = None
        self.class_table_image = None
        self.class_flooringtype = None
        self.class_flooring_image = None
        self.class_walltype = None
        self.class_walltype_image = None
        self.class_noticeboardtype = None
        self.class_noticeboard_image = None

        #School gates image related properties
        self.school_building_type= None
        self.school_image       = None
        self.boundry_type       = None
        self.boundry_image      = None

        self.background_houses          = None
        self.background_houses_doors    = None

        self.window_type        = None
        self.window_image       = None
        self.door_type          = None
        self.door_image         = None
        self.school_final_image = None

        self.entrance_type        	        = None
        self.entrance_image        	        = None
        self.close_entrance_image_entrance  = None
        self.close_entrance_image_walls     = None
        self.close_entrance_image_window    = None

        self.num_teachers       = None
        self.num_pupils         = None
        self.num_NPC_pupils     = None

        #characters
        self.teachers   = {}
        self.pupils     = {}
        self.NPC_pupils = {}

        self.teachers_list   = []
        self.pupils_list     = []
        self.NPC_pupils_list = []

        self.AllCharacters  = None

    def populate(self):
        "populate all the required attributes for a new school"
        #get pygame window info. If it's empty, there's no display started,
        #so start one. Pygame falls over if it doesn't have a display set.
        #pygame_display_info = pygame.display.get_wm_info()
##        if pygame_display_info == {}:
##            #screen = pygame.display.set_mode((1280, 720))
##            screen = pygame.display.set_mode((1,1))
##            pygame.display.init()
##
##            #pygame_sdl2.init()
##            #pygame_sdl2.display.init()


# UNCOMMENT THIS FOR TESTING...
# Kills the display if use in Renpy.
# Can't figure out why...
# fix later...?
##        if GRAPHICSMODE == "PyGame":
##            DEBUG = 1
##            if DEBUG == 1:
##                print "GRAPHICSMODE: 'PyGame'"
##            
##            #Pygame falls over if it doesn't have a display set.
##            try:
##                testim = pygame.Surface((1,1), pygame.SRCALPHA, 32) #change its background color 
##                if DEBUG == 1:
##                    print "\ttest Surface opened OK..."
##
##                pics = glob.glob("*.png") # assume we have graphics files in that directory
##                img = pygame.image.load(pics)
##                img = pygame.Surface.convert_alpha(img)
##                if DEBUG == 1:
##                    print "\tcan convert_alpha on an image OK..."
##            except:
##                if DEBUG == 1:
##                    print "\tCan't open a test Surface/convert_alpha on an image in PyGame..."
##                    print "\t(Re-)initialising PyGame..."
##                #raise
##                try:
##                    screen = pygame.display.set_mode((1,1))
##                    pygame.display.init()
##                    print "OK."
##                    print
##                except:
##                    if DEBUG == 1:
##                        print "\tStill no good..."
##                        print "failing."
##                        print
##                    raise

        #name-related attributes
        if self.VERBOSE > 0:
            print 'setting name-related attributes...'
        self.name, self.name_short, self.name_full, self.school_type = make_name()
        #fiddle this to make it actually useful
        self.saints_name = self.name
        self.name = self.name_full
        if self.VERBOSE > 0:
            print "name-related attribute setting complete"
            print "\tself.name:", self.name
            print "\tself.name_short:", self.name_short
            print "\tself.name_full:", self.name_full
            print "\tself.saints_name:", self.saints_name
            print "\tself.school_type:", self.school_type
            print #self

        if self.VERBOSE > 0:
            print "setting badge..."
            #print self

        fname = "badge_%s.png" % self.name_full
        fname = fname.replace("t.", "t")
        fname = fname.replace("'", "")
        fname = fname.replace(" ", "_")
        fname = fname.replace("'", "")
        DeviceDescriptionsDict, CreatureDescriptionsDict, OrdinaryDescriptionsDict = get_descriptions()
        self.badge_blazon, self.badge = make_badge(VERBOSE=self.VERBOSE, FILENAME=fname,
                                               DeviceDescriptionsDict=DeviceDescriptionsDict,
                                               CreatureDescriptionsDict=CreatureDescriptionsDict,
                                               OrdinaryDescriptionsDict=OrdinaryDescriptionsDict,
                                               textfile = None, USESTAINS=1, SILENT=0, GRAPHICSMODE=GRAPHICSMODE)
        self.badge_fname = fname

##        if GRAPHICSMODE == "PIL":
##            self.badge_blazon, self.badge = make_badge(VERBOSE=self.VERBOSE, FILENAME=fname,
##                                                   DeviceDescriptionsDict=DeviceDescriptionsDict,
##                                                   CreatureDescriptionsDict=CreatureDescriptionsDict,
##                                                   OrdinaryDescriptionsDict=OrdinaryDescriptionsDict,
##                                                   textfile = None, USESTAINS=1, SILENT=0, GRAPHICSMODE=GRAPHICSMODE)
##        elif GRAPHICSMODE == "PyGame":
##            self.badge_blazon, self.badge =  "", None

        if self.VERBOSE > 0:
            print "badge-related attribute setting complete"
            print "\tself.badge_blazon:", self.badge_blazon
            print "\tself.badge:", self.badge
            print "\tfname:", fname
            print #self

        if self.VERBOSE > 0:
            print "setting uniform-related attributes"
            #print #self

        heraldic_cols = {
        "Murrey":       {"Name":               "Murrey",
                         "Colour":             "dark reddish purple",
                         "Screen Colour":      "#8b004b",
                         "RGB Colour":         (139, 0, 75)
                         },
        "Sanguine":     {"Name":                "Sanguine",
                         "Colour":              "blood red",
                         "Screen Colour":       "#b22222",
                         "RGB Colour":          (178, 34, 34)
                         },
        "Tenné":        {"Name":                "Tenné",
                         "Colour":              "orange",
                         "Screen Colour":       "#c67000",
                         "RGB Colour":          (198, 112, 0)
                         },
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

        #Field is the main colour of a shield.
        field = string.split(self.badge_blazon, ",")[0]
        everything_else = string.join(string.split(self.badge_blazon, ",")[1:])

        if string.find(field, "Murrey") > -1:
            self.badge_blazer_colour = ["purple", heraldic_cols["Murrey"]["RGB Colour"]]
            self.badge_tie_colour_1  = ["purple", heraldic_cols["Murrey"]["RGB Colour"]]
        elif string.find(field, "Sanguine") > -1:
            self.badge_blazer_colour = ["maroon", heraldic_cols["Sanguine"]["RGB Colour"]]
            self.badge_tie_colour_1  = ["maroon", heraldic_cols["Sanguine"]["RGB Colour"]]
        elif string.find(field, "Gules") > -1:
            self.badge_blazer_colour = ["red", heraldic_cols["Gules"]["RGB Colour"]]
            self.badge_tie_colour_1  = ["red", heraldic_cols["Gules"]["RGB Colour"]]
        elif string.find(field, "Sable") > -1:
            self.badge_blazer_colour = ["black", heraldic_cols["Sable"]["RGB Colour"]]
            self.badge_tie_colour_1  = ["black", heraldic_cols["Sable"]["RGB Colour"]]
        elif string.find(field, "Azure") > -1:
            self.badge_blazer_colour = ["blue", heraldic_cols["Azure"]["RGB Colour"]]
            self.badge_tie_colour_1  = ["blue", heraldic_cols["Azure"]["RGB Colour"]]
        elif string.find(field, "Vert") > -1:
            self.badge_blazer_colour = ["green", heraldic_cols["Vert"]["RGB Colour"]]
            self.badge_tie_colour_1  = ["green", heraldic_cols["Vert"]["RGB Colour"]]
        elif string.find(field, "Purpure") > -1:
            self.badge_blazer_colour = ["purple", heraldic_cols["Purpure"]["RGB Colour"]]
            self.badge_tie_colour_1  = ["purple", heraldic_cols["Purpure"]["RGB Colour"]]

        if string.find(field, "Argent") > -1:
            self.badge_tie_colour_2 = ["white", heraldic_cols["Argent"]["RGB Colour"]]
        elif string.find(field, "Or") > -1:
            self.badge_tie_colour_2 = ["yellow", heraldic_cols["Or"]["RGB Colour"]]
        elif string.find(field, "Tenné") > -1:
            self.badge_tie_colour_2 = ["orange", heraldic_cols["Tenné"]["RGB Colour"]]

        if self.badge_blazer_colour  == [None, None]:
            if string.find(everything_else, "Sable") > -1:
                self.badge_blazer_colour = ["black", heraldic_cols["Sable"]["RGB Colour"]]
                self.badge_tie_colour_1   = ["black", heraldic_cols["Sable"]["RGB Colour"]]
            elif string.find(everything_else, "Azure") > -1:
                self.badge_blazer_colour = ["blue", heraldic_cols["Azure"]["RGB Colour"]]
                self.badge_tie_colour_1   = ["blue", heraldic_cols["Azure"]["RGB Colour"]]
            elif string.find(everything_else, "Purpure") > -1:
                self.badge_blazer_colour = ["purple", heraldic_cols["Purpure"]["RGB Colour"]]
                self.badge_tie_colour_1   = ["purple", heraldic_cols["Purpure"]["RGB Colour"]]
            elif string.find(everything_else, "Murrey") > -1:
                self.badge_blazer_colour = ["purple", heraldic_cols["Murrey"]["RGB Colour"]]
                self.badge_tie_colour_1   = ["purple", heraldic_cols["Murrey"]["RGB Colour"]]
            elif string.find(everything_else, "Sanguine") > -1:
                self.badge_blazer_colour = ["maroon", heraldic_cols["Sanguine"]["RGB Colour"]]
                self.badge_tie_colour_1   = ["maroon", heraldic_cols["Sanguine"]["RGB Colour"]]
            elif string.find(everything_else, "Gules") > -1:
                self.badge_blazer_colour = ["red", heraldic_cols["Gules"]["RGB Colour"]]
                self.badge_tie_colour_1   = ["red", heraldic_cols["Gules"]["RGB Colour"]]
            elif string.find(everything_else, "Vert") > -1:
                self.badge_blazer_colour = ["green", heraldic_cols["Vert"]["RGB Colour"]]
                self.badge_tie_colour_1   = ["green", heraldic_cols["Vert"]["RGB Colour"]]

        #not found a dark colour? Just make the blazer colour random then.
        if self.badge_blazer_colour  == [None, None]:
            self.badge_blazer_colour = random.choice((
                ["black", heraldic_cols["Sable"]["RGB Colour"]],
                ["blue", heraldic_cols["Azure"]["RGB Colour"]],
                ["purple", heraldic_cols["Murrey"]["RGB Colour"]],
                ["maroon", heraldic_cols["Sanguine"]["RGB Colour"]],
                ["red", heraldic_cols["Gules"]["RGB Colour"]],
                ["black", heraldic_cols["Sable"]["RGB Colour"]],
                ["blue", heraldic_cols["Azure"]["RGB Colour"]],
                ["green", heraldic_cols["Vert"]["RGB Colour"]],
                ["purple", heraldic_cols["Purpure"]["RGB Colour"]]
                ))
            self.badge_tie_colour_1 = self.badge_blazer_colour


    def save(self,fname=None):
        """used for saving class files.
        Mainly used for testing - won't be used in the final game.
        returns the filename we used"""
        if fname == None:
            fname = "school_%s.save" % self.name_full
            fname = fname.replace("'", "")
            fname = fname.replace(". ", "_")
            fname = fname.replace(" ", "_")
            fname = fname.replace("'", "")
        thisdir = os.getcwd()
        tempdir = "TEMP"

        if os.path.isdir(os.path.join(thisdir, "TEMP")):
            tempdir = os.path.join(thisdir, "TEMP")
        #elif os.path.isdir(os.path.join(thisdir, "..", "TEMP")):
        #    tempdir = os.path.join(thisdir, "..", "TEMP")

        if os.path.isdir(tempdir):
            os.chdir(tempdir)


        #if we try pickling as is we get following error message:
        #raise TypeError, "can't pickle %s objects" % base.__name__
        #TypeError: can't pickle Font objects

        #set sign_font to NONE to get around this
        #we have both self.sign_font_name and self.sign_font_size set,
        # so we should be able to reconstuct the FOnt object fron those on re-loading    

        self.sign_font      = None
        #school.sign_font_name = signFont[1]
        #school.sign_font_size = BIGFONT_SIZE

        #we can't pickle a pygame Surface
        #and pygame_sdl2 doesn's have the
        #pygame.image.tostring() method.
        #
        #We'll just have to save an image file, and
        #use the filename as the badge contents in
        #our save file
        #self.badge = pygame.image.tostring(self.badge)
        badge_fname = "school_%s_badge.png" % self.name_full
        badge_fname = string.replace(badge_fname, " ", "_")
        badge_fname = string.replace(badge_fname, "'", "")
        self.badge_fname = badge_fname
        if GRAPHICSMODE == "PyGame":
            if type(self.badge) == StringType:
                pass # must have already saved it?
            else:
                print "self.badge:", self.badge
                print "badge_fname:", badge_fname
                pygame.image.save(self.badge,badge_fname)
        elif GRAPHICSMODE == "PIL":
            #not really needed, since we can pickle PIL objects,
            #but doing it to stay consistent with Pygame
            self.badge.save(badge_fname, "PNG")
        self.badge = badge_fname

        outfile = open(fname, "wb")
        #pickle.dump(self, outfile)
        try:
            pickle.dump(self, outfile)
        except:
            print "!!! CANNOT FUCKING PICKLE !!!"
            for q in self.__dict__.keys():
                print "\tremoving '%s'"% q
                self.__dict__[q] = None
                try:
                    pickle.dump(self, outfile)
                    print "\t !!! IT WORKED !!!"
                    print "'%s' WAS THE PROBLEM!" % q
                    print
                    break
                except:
                    print "\tNOPE.. STILL FAILED..."
                
            pickle.dump(self, outfile)
            
        outfile.close()

        if self.VERBOSE > 0:
            print "wrote file '%s' OK" % fname

        os.chdir(thisdir)
        return fname

    def load(self,fname=None):
        """loads a pickled class file.
        Mainly used for testing - won't be used in the final game"""
        if fname == None:
            fname = "school_%s.save" % self.name_full
            fname = fname.replace("'", "")
            fname = fname.replace(". ", "_")
            fname = fname.replace(" ", "_")
            fname = fname.replace("'", "")
        thisdir = os.getcwd()
        tempdir = "TEMP"

        if os.path.isdir(os.path.join(thisdir, "TEMP")):
            tempdir = os.path.join(thisdir, "TEMP")
        elif os.path.isdir(os.path.join(thisdir, "..", "TEMP")):
            tempdir = os.path.join(thisdir, "..", "TEMP")

        if os.path.isdir(tempdir):
            os.chdir(tempdir)

        if os.path.isfile(fname):
            infile = open(fname, "rb")
            #self = pickle.load(infile)
            if self.VERBOSE > 0:
                print "\tOpened file '%s' OK..." % fname
            temp_school = School()
            temp_school = pickle.load(infile)
            #self = pickle.load(infile)
            #temp_school = pickle.load(fname)
            #temp_school.load(infile)
            infile.close()

            for prop in temp_school.__dict__.keys():
                if self.VERBOSE > 0:
                    print("loading '%s'..." % prop),  
                self.__dict__[prop] = temp_school.__dict__[prop]
                if self.VERBOSE > 0:
                    print "\t...OK"

        else:
            print "ERROR: CAN'T FIND SAVE FILE '%s'!" % fname
            os.chdir(thisdir)
            return -1

        #rebuild the Font object we couldn't pickle
        if self.sign_font_name != None:
            if os.path.isdir(os.path.join("..", "fonts")):
                if self.sign_font_size != None:
                    if GRAPHICSMODE == "PIL":
                        from PIL import ImageFont
                        self.sign_font = ImageFont.truetype(os.path.join("..", "fonts", self.sign_font_name), self.sign_font_size, encoding='unic')
                    elif GRAPHICSMODE == "PyGame":
                        self.sign_font = pygame.font.Font(os.path.join("..", "fonts", self.sign_font_name), self.sign_font_size)
            elif os.path.isdir("fonts"):
                if self.sign_font_size != None:
                    if GRAPHICSMODE == "PIL":
                        from PIL import ImageFont
                        self.sign_font = ImageFont.truetype(os.path.join("fonts", self.sign_font_name), self.sign_font_size, encoding='unic')
                    elif GRAPHICSMODE == "PyGame":
                        self.sign_font = pygame.font.Font(os.path.join("fonts", self.sign_font_name), self.sign_font_size)

        #rebuild the self.badge image that we couldn't pickle
        if self.badge != None:
            badge_fname = self.badge
            if os.path.isfile(badge_fname):
                if GRAPHICSMODE == "PyGame":
                    pygame.image.load(self.badge,badge_fname)
                elif GRAPHICSMODE == "PIL":
                    self.badge = PilImage.open(badge_fname)

        #rebuild the self.sign image that we couldn't pickle
        if self.sign != None:
            sign_fname = self.sign
            if os.path.isfile(sign_fname):
                if GRAPHICSMODE == "PyGame":
                    pygame.image.load(self.sign,sign_fname)
                elif GRAPHICSMODE == "PIL":
                    self.badge = PilImage.open(sign_fname)

        os.chdir(thisdir)
        return None



    def __str__(self):
        """returns a long printable list (OK, string) of this schools's attributes.
        VERY DUMB - converts unicode characters to question marks - designed to be
        printable on anything. DO NOT RELY ON IT TO BE ACCURATE."""
        myname = None
        for i in dir():
            if isinstance(eval(i), School):
                myname = i
#        printstring = "%s\n" % self.__class__.__name__
        #wanted a way of finding out the name of the instance of the class, but couldn't figure out a way to do it...
        if myname == "self":
            myname = self.name_full
        printstring = "%s (%s)" % (myname, self.__class__.__name__)
        vars = self.__dict__.keys()
        vars.sort()
        for x in vars:
            z = x.ljust(20)
            try:
                printable_var = self.__dict__[x].encode("ASCII")
                #printstring = "%s\n\t%s: %s" % (printstring, z, self.__dict__[x])
                printstring = "%s\n\t%s: %s" % (printstring, z, printable_var)
            except:
                printstring = "%s\n\t%s: " % (printstring, z)
                #print "x", x
                #print "self.__dict__[x]", self.__dict__[x]
                for dodgy_character in str(self.__dict__[x]):
                    try:
                        printable_char = dodgy_character.encode("ASCII")
                        printstring = "%s%s" % (printstring, printable_char)
                    except:
                        printstring = "%s%s" % (printstring, "?")
        return "%s\n" % printstring


##### BADGE STUFF ##### 

# Heraldic_tinctures

def getStain():

    Heraldic_tinctures_Stains = {
        "Murrey":    {"Name":           "Murrey",
                     "Colour":          "dark reddish purple",
                     # murrey is a "stain", i. e. a non-standard tincture, that is a dark reddish purple colour.
                     # In the past it was sometimes taken to be equivalent to Sanguine, but they are now considered two distinct tinctures
                     # from Greek morum, "mulberry". 
                     "Screen Colour":   "#8b004b",
                     "RGB Colour":      (139, 0, 75),
            },

        "Sanguine":    {"Name":         "Sanguine",
                     # Sanguine is a stain, or non-standard tincture in heraldry, of a blood-red colour.
                     #In the past it was sometimes taken to be equivalent to murrey, but they are now considered two distinct tinctures
                     # from Latin sanguineus, "blood red"
                     "Colour":          "blood red",
                     "Screen Colour":   "#b22222",
                     "RGB Colour":      (178, 34, 34),
            },

        "Tenné":    {"Name":            "Tenné",
                     #tenné sometimes termed tenny or tawny) is a "stain", or non-standard tincture,
                     #of orange (in English blazonry), light brown (in French heraldry) or orange-tawny (in continental heraldry) colour.[3]
                     "Colour":          "orange",
                     "Screen Colour":   "#c67000",
                     "RGB Colour":      (198, 112, 0),
            }
        }

    color1 = random.choice(Heraldic_tinctures_Stains.keys())
    color1Dict = Heraldic_tinctures_Stains[color1]
    return color1Dict


def getMetal():

    Heraldic_tinctures_Metals = {
        "Argent":    {"Name":           "Argent",
                      #Argent is derived from the Latin argentum, "silver". Sometimes
                      #depicted as metallic silver or faint grey, but more often represented by white.
                     "Colour":          "white",
                     "Screen Colour":   "#fdfdfd",
                     "RGB Colour":      (253, 253, 253),
            },
        "Or":       {"Name":            "Or",
                     #Or derives its name from the Latin aurum, "gold". It may be
                     #depicted using either yellow or metallic gold
                     "Colour":          "yellow",
                     "Screen Colour":   "#fefe00",
                     "RGB Colour":      (254, 254, 0),
            }
        }

    color1 = random.choice(Heraldic_tinctures_Metals.keys())
    color1Dict = Heraldic_tinctures_Metals[color1]
    return color1Dict

def getColour():

    Heraldic_tinctures_Colours = {
        "Gules":    {"Name":            "Gules",
                     #Gules is the tincture with the colour red.
                     #The term gules derives from the Old French word "goules", literally "throats".
                     "Colour":          "red",
                     "Screen Colour":   "#ee0000",
                     "RGB Colour":      (238, 0, 0),
                     },
        "Sable":    {"Name":            "Sable",
                     #sable is the tincture black. 
                     #The name derives from the black fur of the sable, a species of marten.
                     "Colour":          "black",
                     "Screen Colour":   "#111111",
                     "RGB Colour":      (17, 17, 17),
            },
        "Azure":    {"Name":           "Azure",
                     #azure is the tincture with the colour blue
                     #The term azure derives from the name of the deep blue stone now called lapis lazuli (stone of Lazhward).
                     "Colour":          "blue",
                     "Screen Colour":   "#0000cc",
                     "RGB Colour":      (0, 0, 204),
                     },
        "Vert":    {"Name":           "Vert",
                     #vert is the name of the tincture equivalent to the colour "green".
                     #The word vert is simply the French for "green".
                     "Colour":          "green",
                     "Screen Colour":   "#008000",
                     "RGB Colour":      (0, 128, 0),
            },
        "Purpure":    {"Name":          "Purpure",
                     #purpure is a tincture, equivalent to the colour "purple".
                     "Colour":          "purple",
                     "Screen Colour":   "#600060",
                     "RGB Colour":      (96, 0, 96),
            }
        }

    color1 = random.choice(Heraldic_tinctures_Colours.keys())
    color1Dict = Heraldic_tinctures_Colours[color1]
    return color1Dict


def MakeDeviceDescriptionsDict():
    """created a dict of device descriptions from the text contained in the file "_descriptions.csv" """

    DeviceDescriptionsDict = {}

    #TEST = 1
    TEST = 0

    rootdir = os.getcwd()

    # special fiddle for when being run from the Renpy launcher
    if string.find(rootdir, "renpy-6.99.14.3-sdk") > -1:
        os.chdir("E:\Projects\NEW RENPY GAME\game")
        rootdir = os.getcwd()

    if TEST == 1:
        badgesdir = os.path.join(rootdir, "game", "images", "badges")
    else:
        badgesdir = os.path.join(rootdir, "images", "badges")

    devicesdir = os.path.join(badgesdir, "Devices")

    if os.path.isfile(os.path.join(devicesdir, "_descriptions.csv")):
        #print "FOUND _descriptions.csv in", devicesdir
        descriptions = open(os.path.join(devicesdir, "_descriptions.csv")).readlines()
        for d in descriptions:
            if string.find(d, ",") > -1:
                fn, sing, plural = string.split(d, ",")
                DeviceDescriptionsDict[fn] = [string.strip(sing), string.strip(plural)]
    return DeviceDescriptionsDict

def MakeCreatureDescriptionsDict():
    CreatureDescriptionsDict = {}

    #TEST = 1
    TEST = 0

    rootdir = os.getcwd()

    # special fiddle for when being run from the Renpy launcher
    if string.find(rootdir, "renpy-6.99.14.3-sdk") > -1:
        os.chdir("E:\Projects\NEW RENPY GAME\game")
        rootdir = os.getcwd()

    if TEST == 1:
        badgesdir = os.path.join(rootdir, "game", "images", "badges")
    else:
        badgesdir = os.path.join(rootdir, "images", "badges")

    creaturesdir = os.path.join(badgesdir, "Creatures")

    if os.path.isfile(os.path.join(creaturesdir, "_descriptions.csv")):
        descriptions = open(os.path.join(creaturesdir, "_descriptions.csv")).readlines()
        for d in descriptions:
            if string.find(d, ",") > -1:
                fn, sing, plural = string.split(d, ",")
                CreatureDescriptionsDict[fn] = [string.strip(sing), string.strip(plural)]

    return CreatureDescriptionsDict

def MakeOrdinaryDescriptionsDict():
    OrdinaryDescriptionsDict = {}

    #TEST = 1
    TEST = 0

    rootdir = os.getcwd()

    # special fiddle for when being run from the Renpy launcher
    if string.find(rootdir, "renpy-6.99.14.3-sdk") > -1:
        os.chdir("E:\Projects\NEW RENPY GAME\game")
        rootdir = os.getcwd()

    if TEST == 1:
        badgesdir = os.path.join(rootdir, "game", "images", "badges")
    else:
        badgesdir = os.path.join(rootdir, "images", "badges")

    ordinariesdir = os.path.join(badgesdir, "Ordinaries")

    if os.path.isfile(os.path.join(ordinariesdir, "_descriptions.csv")):
        descriptions = open(os.path.join(ordinariesdir, "_descriptions.csv")).readlines()
        for d in descriptions:
            if string.find(d, ",") > -1:
                fn, sing, plural = string.split(d, ",")
                OrdinaryDescriptionsDict[fn] = [string.strip(sing), string.strip(plural)]

    return OrdinaryDescriptionsDict


def guess_description_from_Filename(fn):
    fn =string.split(fn, ".")[0]
    fn = string.replace(fn, "-", " ")
    fn = string.replace(fn, "_", " ")
    newfn = ""
    for l in fn:
        if l == " ":
            newfn = "%s%s"% (newfn, l)
        elif l in ["1","2","3","4","5","6","7","8","9","0"]:
            newfn = "%s%s"% (newfn, l)
        elif l == string.upper(l):
            newfn = "%s %s"% (newfn, string.lower(l))
        else:
            newfn = "%s%s"% (newfn, l)
    return string.strip(newfn)



def make_PyGame_Mask(im, GRAPHICSMODE="PyGame"):
    print "im:", im


    if GRAPHICSMODE == "PyGame":
        newim = pygame.Surface((im.get_width(),im.get_height()), pygame.SRCALPHA, 32) #change its background color 

        MASKCOL = (100,100,10) # an ugly olive colour - shouldn't appear in any of our shields
        MASKCOL = pygame.Color(100,100,10,255)
        THRESHOLD = 20

        pygame.Surface.lock(im)

        for imx in range(0, im.get_width()):
            for imy in range(0, im.get_height()):
                color = im.get_at((imx,imy))
                if color[3] < THRESHOLD:
                    newim.set_at((imx,imy), MASKCOL)
                else:
                    newim.set_at((imx,imy), color)
        newim.set_colorkey(MASKCOL)
        pygame.Surface.unlock(im)
        return newim

    else:
        return im

def change_Shield_Color (im, newcolor, GRAPHICSMODE="PIL"):
    """changes white in supplied image (im) to specified colour (newcolour)"""
    DEBUG = 0
    #DEBUG = 1

    if DEBUG == 1:
        print "newcolor:", newcolor
        print "im:", im
    
    THRESHOLD = 225 # Doesn't rely on colour being exactly 255,255,255

    if GRAPHICSMODE == "PIL":
        im.convert("RGBA")
        newimdata = []
        for color in im.getdata():
            if color[0] > THRESHOLD:
                if color[1] > THRESHOLD:
                    if color[2] > THRESHOLD:
                        if color[3] > THRESHOLD:
                            newimdata.append(newcolor)
                        else:
                            newimdata.append(color)
                    else:
                        newimdata.append(color)
                else:
                    newimdata.append(color)
            else:
                newimdata.append(color)
        #print
        newim = PilImage.new("RGBA",im.size)
        newim.putdata(newimdata)

    elif GRAPHICSMODE == "PyGame":
        im.convert()
        if DEBUG == 1:
            print "newcolor:", newcolor
        newcolor = pygame.Color(newcolor[0], newcolor[1], newcolor[2], 255) # why the HELL does pygame reverse RBG -> GBR???

        if DEBUG == 1:
            print "newcolor(converted):", newcolor
        newim = pygame.Surface((im.get_width(),im.get_height()), pygame.SRCALPHA, 32) #change its background color 

        tochange = pygame.Color(THRESHOLD, THRESHOLD, THRESHOLD,255) # or whatever yellow color you want

        thresh = (20, 20, 20, 20) # or whatever threshold works

        if DEBUG == 1:
            print "newim:",newim 
            print "type(newim):",type(newim)
            print "im:",im
            print "type(im):",type(im)
            print "tochange:",tochange
            print "thresh:",thresh
            print "newcolor:",newcolor

        pygame.Surface.lock(im)

        for imx in range(0, im.get_width()):
            for imy in range(0, im.get_height()):
                color = im.get_at((imx,imy))
                if color[0] > THRESHOLD:
                    if color[1] > THRESHOLD:
                        if color[2] > THRESHOLD:
                            if color[3] > THRESHOLD:
                                newim.set_at((imx,imy), newcolor)
                            else:
                                newim.set_at((imx,imy), color)
                        else:
                            newim.set_at((imx,imy), color)
                    else:
                        newim.set_at((imx,imy), color)
                else:
                    newim.set_at((imx,imy), color)

        if DEBUG == 1:
            if os.path.isfile("E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFILE_OLD.png"):
                os.remove("E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFILE_OLD.png")
            if os.path.isfile("E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFILE.png"):
                os.rename("E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFILE.png", "E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFILE_OLD.png")
            pygame.image.save(newim, "E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFILE.png")
            print "wrote file 'E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFILE.png'"
            print

        pygame.Surface.unlock(im)

    return newim


def change_Other_Color(im, newcolor, GRAPHICSMODE="PIL"):
    #DEBUGS = 0
    DEBUG = 1

    if GRAPHICSMODE == "PIL":
        im.convert("RGBA")
        newimdata = []
        CHANGECOLOR = (204,204,204,255) # RGB + ALPHA CHANNEL
        for color in im.getdata():
            if color == CHANGECOLOR:
                newimdata.append(newcolor)
            else:
                newimdata.append(color)
        newim = PilImage.new("RGBA",im.size)
        newim.putdata(newimdata)

    elif GRAPHICSMODE == "PyGame":
        im.convert()
        if DEBUG == 1:
            print "newcolor:", newcolor
        newcolor = pygame.Color(newcolor[0], newcolor[1], newcolor[2], 255) # why the HELL does pygame reverse RBG -> GBR???
        if DEBUG == 1:
            print "newcolor(converted):", newcolor
        newim = pygame.Surface((im.get_width(),im.get_height()), pygame.SRCALPHA, 32) #change its background color 

        CHANGECOLOR = pygame.Color(204,204,204,255) # RGB + ALPHA CHANNEL

        pygame.Surface.lock(im)

        for imx in range(0, im.get_width()):
            for imy in range(0, im.get_height()):
                color = im.get_at((imx,imy))
                if color == CHANGECOLOR:
                    newim.set_at((imx,imy), newcolor)
                else:
                    newim.set_at((imx,imy), color)

        if DEBUG == 1:
            if os.path.isfile("E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFILE_OLD.png"):
                os.remove("E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFILE_OLD.png")
            if os.path.isfile("E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFILE.png"):
                os.rename("E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFILE.png", "E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFILE_OLD.png")
            pygame.image.save(newim, "E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFILE.png")
            print "wrote file 'E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFILE.png'"
            print

        pygame.Surface.unlock(im)

    return newim


def change_Black_Outline_Color(im, newcolor, GRAPHICSMODE="PIL"):
    DEBUG = 0
    if GRAPHICSMODE == "PIL":
        im.convert("RGBA")
        newimdata = []

        THRESHOLD = 25
        for color in im.getdata():
            if color[0] < THRESHOLD:
                if color[1] < THRESHOLD:
                    if color[2] < THRESHOLD:
                        if color[3] > 200:
                            newimdata.append(newcolor)
                        else:
                            newimdata.append(color)
                    else:
                        newimdata.append(color)
                else:
                    newimdata.append(color)
            else:
                newimdata.append(color)
        newim = PilImage.new("RGBA",im.size)
        newim.putdata(newimdata)


    elif GRAPHICSMODE == "PyGame":
        im.convert()
        if DEBUG == 1:
            print "newcolor:", newcolor
        newcolor = pygame.Color(newcolor[0], newcolor[1], newcolor[2], 255) # why the HELL does pygame reverse RBG -> GBR???

        if DEBUG == 1:
            print "newcolor(converted):", newcolor
        newim = pygame.Surface((im.get_width(),im.get_height()), pygame.SRCALPHA, 32) #change its background color 

        THRESHOLD = 25

        tochange = pygame.Color(THRESHOLD, THRESHOLD, THRESHOLD,255) # or whatever yellow color you want

        thresh = (30, 30, 30, 30) # or whatever threshold works

        if DEBUG == 1:
            print "newim:",newim 
            print "type(newim):",type(newim)
            print "im:",im
            print "type(im):",type(im)
            print "tochange:",tochange
            print "thresh:",thresh
            print "newcolor:",newcolor

        pygame.Surface.lock(im)

        for imx in range(0, im.get_width()):
            for imy in range(0, im.get_height()):
                color = im.get_at((imx,imy))
                if color[0] <  THRESHOLD:
                    if color[1] <  THRESHOLD:
                        if color[2] <  THRESHOLD:
                            if color[3] > 200:
                                newim.set_at((imx,imy), newcolor)
                            else:
                                newim.set_at((imx,imy), color)
                        else:
                            newim.set_at((imx,imy), color)
                    else:
                        newim.set_at((imx,imy), color)
                else:
                    newim.set_at((imx,imy), color)

        if DEBUG == 1:
            print "os.getcwd()", os.getcwd()
            if os.path.isfile("E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFILE_OLD_B.png"):
                os.remove("E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFILE_OLD_B.png")
            if os.path.isfile("E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFILE_B.png"):
                os.rename("E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFILE_B.png", "E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFILE_OLD_B.png")
            pygame.image.save(newim, "E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFILE_B.png")
            print "wrote file 'E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFILE_B.png'"
            print

        pygame.Surface.unlock(im)

    return newim


def make_Creature_Badge(color1Dict, color2Dict, VERBOSE=1, CreatureDescriptionsDict=None, SILENT=0, GRAPHICSMODE="PIL"):

    TEST = 1

    if VERBOSE > 0:
        print "  Making badge (Type: Creature)"
        print "  GRAPHICSMODE:", GRAPHICSMODE
    else:
        if SILENT != 1:
            print ".",
        else:
            pass
    #pick a shield
    creaturesdir = os.getcwd()
    shielddir = os.path.join(creaturesdir, "..", "Shields")
    os.chdir(shielddir)
    allshields = glob.glob("*.*") # assume we only have graphics files in that directory
    #remove descriptions file etc
    for s in allshields:
        if s[0] == "_":
            allshields.remove(s)
    shieldToUse = random.choice(allshields)

    if VERBOSE > 0:
        print "  Chose shield '%s'" % shieldToUse

    if GRAPHICSMODE == "PIL":
        img = PilImage.open(shieldToUse)
    elif GRAPHICSMODE == "PyGame":
        img = pygame.image.load(shieldToUse)
        if img.get_alpha():
            img = pygame.Surface.convert_alpha(img)
            if VERBOSE > 0:
                print "    ALPHA CHANNEL IN IMAGE - used img.convert_alpha()"
        else:
            img = img.convert()
            img.set_colorkey((255,0,255))
            if VERBOSE > 0:
                print "    NO ALPHA CHANNEL IN IMAGE - used img.set_colorkey(255,0,255)"

    #set the shield background colour
    if VERBOSE > 0:
        print "  Setting shield background to '%s' (%s)" % (color1Dict["Name"], color1Dict["Colour"])
    newshield = change_Shield_Color(img, color1Dict["RGB Colour"], GRAPHICSMODE)
       
    #pick a creature to go on the shield
    os.chdir(creaturesdir)
    allcreatures = glob.glob("*.*") # assume we only have graphics files in that directory
    #remove descriptions file etc
    newcreatures = []
    for nx in range(0, len(allcreatures)):
        if allcreatures[nx][0] == "_":
            pass
        else:
            newcreatures.append(allcreatures[nx])
    allcreatures = newcreatures

    creatureToUse = random.choice(allcreatures)

    if VERBOSE > 0:
        print "  Chose creature '%s'" % creatureToUse

    if VERBOSE > 0:
        print "  Setting creature colour to '%s' (%s)" % (color2Dict["Name"], color2Dict["Colour"])


    if GRAPHICSMODE == "PIL":
        img2 = PilImage.open(creatureToUse)
    elif GRAPHICSMODE == "PyGame":
        img2 = pygame.image.load(creatureToUse)
        if img2.get_alpha():
            img2 = pygame.Surface.convert_alpha(img2)
            if VERBOSE > 0:
                print "    ALPHA CHANNEL IN IMAGE - used img2.convert_alpha()"
        else:
            img2 = img2.convert()
            img2.set_colorkey((255,0,255))
            if VERBOSE > 0:
                print "    NO ALPHA CHANNEL IN IMAGE - used img2.set_colorkey(255,0,255)"


    if color2Dict["Name"] in ["Sable", "Purpure"]:
        myGray = (180, 180, 180)
        if string.find(creatureToUse, "roper") > -1:
            #a charge that is 'proper' is in its natural colours - therefore we don't need to recolour it
            newCreature = img2
        else:
            newCreature = change_Black_Outline_Color(img2, myGray, GRAPHICSMODE)
            newCreature = change_Shield_Color(newCreature, color2Dict["RGB Colour"], GRAPHICSMODE)
    else:
        newCreature = change_Shield_Color(img2, color2Dict["RGB Colour"], GRAPHICSMODE)

    #resize the creature...
    mysize = 250 # ie take up half of the shield

    if GRAPHICSMODE == "PIL":
        if newCreature.size[0] > newCreature.size[1]:
            wpercent = (mysize/float(newCreature.size[0]))
            hsize = int((float(newCreature.size[1])*float(wpercent)))
            newCreature = newCreature.resize((mysize,hsize), PilImage.ANTIALIAS)
        else:
            wpercent = (mysize/float(newCreature.size[1]))
            hsize = int((float(newCreature.size[0])*float(wpercent)))
            newCreature = newCreature.resize((hsize, mysize), PilImage.ANTIALIAS)
    elif GRAPHICSMODE == "PyGame":
        newCreature_size = (newCreature.get_width(),newCreature.get_height())
        if newCreature_size[0] > newCreature_size[1]:
            wpercent = (mysize/float(newCreature_size[0]))
            hsize = int((float(newCreature_size[1])*float(wpercent)))
            newCreature = pygame.transform.smoothscale(newCreature, (mysize,hsize))
        else:
            wpercent = (mysize/float(newCreature_size[1]))
            hsize = int((float(newCreature_size[0])*float(wpercent)))
            newCreature = pygame.transform.smoothscale(newCreature, (hsize, mysize))

    #now superimpose the device on the shield (centering it, and using a mask) 
    bg = newshield
    ironman = newCreature

    if GRAPHICSMODE == "PIL":
        text_img = PilImage.new('RGBA', newshield.size, (0, 0, 0, 0))
        text_img.paste(bg, ((text_img.width - bg.width) // 2, (text_img.height - bg.height) // 2))
        text_img.paste(ironman, ((text_img.width - ironman.width) // 2, (text_img.height - ironman.height -50) // 2), mask=ironman)
    elif GRAPHICSMODE == "PyGame":
        text_img = pygame.Surface((newshield.get_width(),newshield.get_height()), pygame.SRCALPHA, 32)
        text_img.blit(bg, ((text_img.get_width() - bg.get_width()) // 2, (text_img.get_height() - bg.get_height()) // 2))
        text_img.blit(ironman, ((text_img.get_width() - ironman.get_width()) // 2, (text_img.get_height() - ironman.get_height() -50) // 2), None) # paint to screen

        if DEBUG == 1:
            pygame.image.save(text_img, "E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFINALFILE.png")
            print "WROTE 'E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFINALFILE.png'"

    #now blazon the shield (ie make the description in a standard heraldic form)

    # Blazons are unpunctuated, except that the tinctures and charges begin with a capital letter.
    blazon = string.capitalize(color1Dict["Name"])  

    if CreatureDescriptionsDict != None:
        if CreatureDescriptionsDict.has_key(creatureToUse):
            #blazon = "%s, %s" % (blazon, string.capitalize(CreatureDescriptionsDict[creatureToUse][0]))
            blazon = "%s, %s" % (blazon, CreatureDescriptionsDict[creatureToUse][0])
        else:
            #blazon = "%s, %s" % (blazon, string.capitalize(guess_description_from_Filename(creatureToUse)))
            blazon = "%s, %s" % (blazon, guess_description_from_Filename(creatureToUse))
    else:
        #blazon = "%s, %s" % (blazon, string.capitalize(guess_description_from_Filename(creatureToUse)))
        blazon = "%s, %s" % (blazon, guess_description_from_Filename(creatureToUse))
    if string.find(creatureToUse, "roper") > -1:
        pass # a charge that is 'proper' is in its natural colours - therefor we don't need to say which tincture it's in
    else:
        blazon = "%s %s" % (blazon, string.capitalize(color2Dict["Name"]))

    return blazon, text_img



def make_Device_Badge(color1Dict, color2Dict, VERBOSE=1, DeviceDescriptionsDict=None, SILENT=0, GRAPHICSMODE="PIL"):

    TEST = 1

    #These devices are ALWAYS of a specified colour (eg, a bezant is always Or (yellow).
    #Therefore, we don't have to give a tincture when blazoning them.
    blazon_exceptions = ["bezant.png", "plate.png", "ogress,png", "torteau.png", "hurt.png"]

    if VERBOSE > 0:
        print "  Making badge (Type: Device)"
    else:
        if SILENT != 1:
            print ".",
        else:
            pass

    #used later
    numDevices = random.choice((1,1,1,1,3,3,2)) # 4 devices not implemented yet

    #pick a shield
    devicesdir = os.getcwd()
    shielddir = os.path.join(devicesdir, "..", "Shields")
    os.chdir(shielddir)
    allshields = glob.glob("*.*") # assume we only have graphics files in that directory
    #remove descriptions file etc
    for s in allshields:
        if s[0] == "_":
            allshields.remove(s)
    shieldToUse = random.choice(allshields)

    if numDevices > 1:
        while shieldToUse == "swiss.png":
            #swiss shield dips at the top, meaning if we put our devices "in chief" they will overflow
            shieldToUse = random.choice(allshields)
    if VERBOSE > 0:
        print "  Chose shield '%s'" % shieldToUse

    if GRAPHICSMODE == "PIL":
        img = PilImage.open(shieldToUse)
    elif GRAPHICSMODE == "PyGame":
        img = pygame.image.load(shieldToUse)
        if img.get_alpha():
            img = pygame.Surface.convert_alpha(img)
            if VERBOSE > 0:
                print "    ALPHA CHANNEL IN IMAGE - used img.convert_alpha()"
        else:
            img = img.convert()
            img.set_colorkey((255,0,255))
            if VERBOSE > 0:
                print "    NO ALPHA CHANNEL IN IMAGE - used img.set_colorkey(255,0,255)"


    #set the shield background colour
    if VERBOSE > 0:
        print "  Setting shield background to '%s' (%s)" % (color1Dict["Name"], color1Dict["Colour"])
    newshield = change_Shield_Color(img, color1Dict["RGB Colour"], GRAPHICSMODE)
       
    #pick a device to go on the shield
    os.chdir(devicesdir)
    alldevices = glob.glob("*.*") # assume we only have graphics files in that directory
    #remove descriptions file etc
    newdevices = []
    #print "len(alldevices):", len(alldevices)
    for nx in range(0, len(alldevices)):
        if alldevices[nx][0] == "_":
            pass
        else:
            newdevices.append(alldevices[nx])
    alldevices = newdevices

    deviceToUse = random.choice(alldevices)

    if VERBOSE > 0:
        print "  Chose device '%s'" % deviceToUse

    if VERBOSE > 0:
        print "  Setting device colour to '%s' (%s)" % (color2Dict["Name"], color2Dict["Colour"])
    if GRAPHICSMODE == "PIL":
        img2 = PilImage.open(deviceToUse)
    elif GRAPHICSMODE == "PyGame":
       img2 = pygame.image.load(deviceToUse)
       if img2.get_alpha():
           img2 = pygame.Surface.convert_alpha(img2)
           if VERBOSE > 0:
               print "    ALPHA CHANNEL IN IMAGE - used img2.convert_alpha()"
       else:
           img2 = img2.convert()
           img2.set_colorkey((255,0,255))
           if VERBOSE > 0:
               print "    NO ALPHA CHANNEL IN IMAGE - used img2.set_colorkey(255,0,255)"

    if color2Dict["Name"] in ["Sable", "Purpure"]:
        myGray = (180, 180, 180)
        if string.find(deviceToUse, "roper") > -1:
            #a charge that is 'proper' is in its natural colours - therefore we don't need to recolour it
            newDevice = img2
        elif deviceToUse in blazon_exceptions:
            newDevice = img2
        else:
            newDevice = change_Black_Outline_Color(img2, myGray, GRAPHICSMODE)
            newDevice = change_Shield_Color(newDevice, color2Dict["RGB Colour"], GRAPHICSMODE)
    else:
        newDevice = change_Shield_Color(img2, color2Dict["RGB Colour"], GRAPHICSMODE)

    location = None

    if numDevices == 1:
        #resize the device...
        mysize = 250 # ie take up half of the shield
        if GRAPHICSMODE == "PIL":
            if newDevice.size[0] > newDevice.size[1]:
                wpercent = (mysize/float(newDevice.size[0]))
                hsize = int((float(newDevice.size[1])*float(wpercent)))
                newDevice = newDevice.resize((mysize,hsize), PilImage.ANTIALIAS)
            else:
                wpercent = (mysize/float(newDevice.size[1]))
                hsize = int((float(newDevice.size[0])*float(wpercent)))
                newDevice = newDevice.resize((hsize, mysize), PilImage.ANTIALIAS)
        elif GRAPHICSMODE == "PyGame":
            newDevice_size = (newDevice.get_width(),newDevice.get_height())
            if newDevice_size[0] > newDevice_size[1]:
                wpercent = (mysize/float(newDevice_size[0]))
                hsize = int((float(newDevice_size[1])*float(wpercent)))
                newDevice = pygame.transform.smoothscale(newDevice, (mysize,hsize))
            else:
                wpercent = (mysize/float(newDevice_size[1]))
                hsize = int((float(newDevice_size[0])*float(wpercent)))
                newDevice = pygame.transform.smoothscale(newDevice, (hsize, mysize))

        #now superimpose the device on the shield (centering it, and using a mask) 
        bg = newshield
        ironman = newDevice
        if GRAPHICSMODE == "PIL":
            text_img = PilImage.new('RGBA', newshield.size, (0, 0, 0, 0))
            text_img.paste(bg, ((text_img.width - bg.width) // 2, (text_img.height - bg.height) // 2))
            text_img.paste(ironman, ((text_img.width - ironman.width) // 2, (text_img.height - ironman.height -50) // 2), mask=ironman)

        elif GRAPHICSMODE == "PyGame":
            text_img = pygame.Surface((newshield.get_width(),newshield.get_height()), pygame.SRCALPHA, 32)
            text_img.blit(bg, ((text_img.get_width() - bg.get_width()) // 2, (text_img.get_height() - bg.get_height()) // 2))
            text_img.blit(ironman, ((text_img.get_width() - ironman.get_width()) // 2, (text_img.get_height() - ironman.get_height() -50) // 2), None) # paint to screen


    elif numDevices == 2:

        location = random.choice(("in chief", "in fess", "in pale"))

        #resize the device...

        if GRAPHICSMODE == "PIL":
            mysize = newshield.width/4
            if newDevice.size[0] > newDevice.size[1]:
                wpercent = (mysize/float(newDevice.size[0]))
                hsize = int((float(newDevice.size[1])*float(wpercent)))
                newDevice = newDevice.resize((mysize,hsize), PilImage.ANTIALIAS)

            else:
                wpercent = (mysize/float(newDevice.size[1]))
                hsize = int((float(newDevice.size[0])*float(wpercent)))
                newDevice = newDevice.resize((hsize, mysize), PilImage.ANTIALIAS)

        elif GRAPHICSMODE == "PyGame":
            mysize = newshield.get_width()/4
            newDevice_size = (newDevice.get_width(),newDevice.get_height())
            if newDevice_size[0] > newDevice_size[1]:
                wpercent = (mysize/float(newDevice_size[0]))
                hsize = int((float(newDevice_size[1])*float(wpercent)))
                newDevice = pygame.transform.smoothscale(newDevice, (mysize,hsize))
            else:
                wpercent = (mysize/float(newDevice_size[1]))
                hsize = int((float(newDevice_size[0])*float(wpercent)))
                newDevice = pygame.transform.smoothscale(newDevice, (hsize, mysize))

        bg = newshield
        ironman = newDevice

        if location == "in chief":
            if GRAPHICSMODE == "PIL":
                text_img = PilImage.new('RGBA', newshield.size, (0, 0, 0, 0))
                xCentre = (text_img.width / 2) - (ironman.width / 2)
                text_img.paste(bg, ((text_img.width - bg.width) // 2, (text_img.height - bg.height) // 2))
                #device #1
                text_img.paste(ironman, (xCentre - int(xCentre/2), (int(xCentre/4))), mask=ironman)
                #device #2
                text_img.paste(ironman, (xCentre + int(xCentre/2), (int(xCentre/4))), mask=ironman)
            elif GRAPHICSMODE == "PyGame":
                text_img = pygame.Surface((newshield.get_width(),newshield.get_height()), pygame.SRCALPHA, 32)
                xCentre = (text_img.get_width() / 2) - (ironman.get_width() / 2)
                text_img.blit(bg, ((text_img.get_width() - bg.get_width()) // 2, (text_img.get_height() - bg.get_height()) // 2))
                #device #1
                text_img.blit(ironman, (xCentre - int(xCentre/2), (int(xCentre/4))), None) # paint to screen
                #device #2
                text_img.blit(ironman, (xCentre + int(xCentre/2), (int(xCentre/4))), None) # paint to screen

        elif location == "in fess":
            if GRAPHICSMODE == "PIL":
                text_img = PilImage.new('RGBA', newshield.size, (0, 0, 0, 0))
                xCentre = (text_img.width / 2) - (ironman.width / 2)
                text_img.paste(bg, ((text_img.width - bg.width) // 2, (text_img.height - bg.height) // 2))
                #device #1
                text_img.paste(ironman, (xCentre - int(xCentre/2.5), (text_img.height - int(ironman.height*1.15)) // 2), mask=ironman)
                #device #2
                text_img.paste(ironman, (xCentre + int(xCentre/2.5), (text_img.height - int(ironman.height*1.15)) // 2), mask=ironman)
            elif GRAPHICSMODE == "PyGame":
                text_img = pygame.Surface((newshield.get_width(),newshield.get_height()), pygame.SRCALPHA, 32)
                xCentre = (text_img.get_width() / 2) - (ironman.get_width() / 2)
                text_img.blit(bg, ((text_img.get_width() - bg.get_width()) // 2, (text_img.get_height() - bg.get_height()) // 2))
                #device #1
                text_img.blit(ironman, (xCentre - int(xCentre/2.5), (text_img.get_height() - int(ironman.get_height()*1.15)) // 2), None) # paint to screen
                #device #2
                text_img.blit(ironman, (xCentre + int(xCentre/2.5), (text_img.get_height() - int(ironman.get_height()*1.15)) // 2), None) # paint to screen

        elif location == "in pale":
            if GRAPHICSMODE == "PIL":
                text_img = PilImage.new('RGBA', newshield.size, (0, 0, 0, 0))
                xCentre = (text_img.width / 2) - (ironman.width / 2)
                text_img.paste(bg, ((text_img.width - bg.width) // 2, (text_img.height - bg.height) // 2))
                #device #1
                text_img.paste(ironman, (xCentre, ((text_img.height - int(ironman.height*1.5)) // 2 - int(xCentre/2.5))), mask=ironman)
                #device #2
                text_img.paste(ironman, (xCentre, ((text_img.height - int(ironman.height*1.15))// 2 + int(xCentre/2.5))), mask=ironman)
            elif GRAPHICSMODE == "PyGame":
                text_img = pygame.Surface((newshield.get_width(),newshield.get_height()), pygame.SRCALPHA, 32)
                xCentre = (text_img.get_width() / 2) - (ironman.get_width() / 2)
                text_img.blit(bg, ((text_img.get_width() - bg.get_width()) // 2, (text_img.get_height() - bg.get_height()) // 2))
                #device #1
                text_img.blit(ironman, (xCentre, ((text_img.get_height() - int(ironman.get_height()*1.5)) // 2 - int(xCentre/2.5))), None) # paint to screen
                #device #2
                text_img.blit(ironman, (xCentre, ((text_img.get_height() - int(ironman.get_height()*1.15))// 2 + int(xCentre/2.5))), None) # paint to screen

    elif numDevices == 4:
        pass
        #do this later...

    else:
        #should be three devices to get this far

        location = random.choice((None, None, "in chief", "in fess", "in pale"))

        #resize the device...
        if GRAPHICSMODE == "PIL":
            mysize = int(newshield.width/4.5)
            if newDevice.size[0] > newDevice.size[1]:
                wpercent = (mysize/float(newDevice.size[0]))
                hsize = int((float(newDevice.size[1])*float(wpercent)))
                newDevice = newDevice.resize((mysize,hsize), PilImage.ANTIALIAS)
            else:
                wpercent = (mysize/float(newDevice.size[1]))
                hsize = int((float(newDevice.size[0])*float(wpercent)))
                newDevice = newDevice.resize((hsize, mysize), PilImage.ANTIALIAS)
        elif GRAPHICSMODE == "PyGame":
            mysize = int(newshield.get_width()/4.5)
            newDevice_size = (newDevice.get_width(),newDevice.get_height())
            if newDevice_size[0] > newDevice_size[1]:
                wpercent = (mysize/float(newDevice_size[0]))
                hsize = int((float(newDevice_size[1])*float(wpercent)))
                newDevice = pygame.transform.smoothscale(newDevice, (mysize,hsize))
            else:
                wpercent = (mysize/float(newDevice_size[1]))
                hsize = int((float(newDevice_size[0])*float(wpercent)))
                newDevice = pygame.transform.smoothscale(newDevice, (hsize, mysize))

        bg = newshield
        ironman = newDevice

        if location == None:
            #When three similar charges are placed on a shield, it is assumed that two are in
            #chief and one is in base, unless otherwise specified.
            if GRAPHICSMODE == "PIL":
                text_img = PilImage.new('RGBA', newshield.size, (0, 0, 0, 0))
                xCentre = (text_img.width / 2) - (ironman.width / 2)
                text_img.paste(bg, ((text_img.width - bg.width) // 2, (text_img.height - bg.height) // 2))
                #device #1
                text_img.paste(ironman, (xCentre - int(xCentre/2.5), (xCentre - int(xCentre/2))), mask=ironman)
                #device #2
                text_img.paste(ironman, (xCentre + int(xCentre/2.5), (xCentre - int(xCentre/2))), mask=ironman)
                #device #3
                text_img.paste(ironman, (xCentre, (xCentre + int(xCentre/2))), mask=ironman)
            elif GRAPHICSMODE == "PyGame":
                text_img = pygame.Surface((newshield.get_width(),newshield.get_height()), pygame.SRCALPHA, 32)
                xCentre = (text_img.get_width() / 2) - (ironman.get_width() / 2)
                text_img.blit(bg, ((text_img.get_width() - bg.get_width()) // 2, (text_img.get_height() - bg.get_height()) // 2))
                #device #1
                #text_img.paste(ironman, (xCentre - int(xCentre/2.5), (xCentre - int(xCentre/2))), mask=ironman)
                text_img.blit(ironman, (xCentre - int(xCentre/2.5), (xCentre - int(xCentre/2))), None) # paint to screen
                #device #2
                text_img.blit(ironman, (xCentre + int(xCentre/2.5), (xCentre - int(xCentre/2))), None) # paint to screen
                #device #3
                text_img.blit(ironman, (xCentre, (xCentre + int(xCentre/2))), None) # paint to screen

        elif location == "in chief":
            if GRAPHICSMODE == "PIL":
                text_img = PilImage.new('RGBA', newshield.size, (0, 0, 0, 0))
                xCentre = (text_img.width / 2) - (ironman.width / 2)
                text_img.paste(bg, ((text_img.width - bg.width) // 2, (text_img.height - bg.height) // 2))
                #device #1
                text_img.paste(ironman, (xCentre - int(xCentre/1.5), (int(xCentre/4))), mask=ironman)
                #device #2
                text_img.paste(ironman, (xCentre, (int(xCentre/4))), mask=ironman)
                #device #3
                text_img.paste(ironman, (xCentre + int(xCentre/1.5), (int(xCentre/4))), mask=ironman)
            elif GRAPHICSMODE == "PyGame":
                text_img = pygame.Surface((newshield.get_width(),newshield.get_height()), pygame.SRCALPHA, 32)
                xCentre = (text_img.get_width() / 2) - (ironman.get_width() / 2)
                text_img.blit(bg, ((text_img.get_width() - bg.get_width()) // 2, (text_img.get_height() - bg.get_height()) // 2))
                #device #1
                text_img.blit(ironman, (xCentre - int(xCentre/1.5), (int(xCentre/4))), None) # paint to screen
                #device #2
                text_img.blit(ironman, (xCentre, (int(xCentre/4))), None) # paint to screen
                #device #3
                text_img.blit(ironman, (xCentre + int(xCentre/1.5), (int(xCentre/4))), None) # paint to screen

        elif location == "in fess":
            if GRAPHICSMODE == "PIL":
                text_img = PilImage.new('RGBA', newshield.size, (0, 0, 0, 0))
                xCentre = (text_img.width / 2) - (ironman.width / 2)
                text_img.paste(bg, ((text_img.width - bg.width) // 2, (text_img.height - bg.height) // 2))
                #device #1
                text_img.paste(ironman, (xCentre - int(xCentre/1.5), (text_img.height - int(ironman.height*1.15)) // 2), mask=ironman)
                #device #2
                text_img.paste(ironman, (xCentre, (text_img.height - int(ironman.height*1.15)) // 2), mask=ironman)
                #device #3
                text_img.paste(ironman, (xCentre + int(xCentre/1.5), (text_img.height - int(ironman.height*1.15)) // 2), mask=ironman)
            elif GRAPHICSMODE == "PyGame":
                text_img = pygame.Surface((newshield.get_width(),newshield.get_height()), pygame.SRCALPHA, 32)
                xCentre = (text_img.get_width() / 2) - (ironman.get_width() / 2)
                text_img.blit(bg, ((text_img.get_width() - bg.get_width()) // 2, (text_img.get_height() - bg.get_height()) // 2))
                #device #1
                #text_img.paste(ironman, (xCentre - int(xCentre/1.5), (text_img.height - int(ironman.height*1.15)) // 2), mask=ironman)
                text_img.blit(ironman, (xCentre - int(xCentre/1.5), (text_img.get_height() - int(ironman.get_height()*1.15)) // 2), None) # paint to screen
                #device #2
                text_img.blit(ironman, (xCentre, (text_img.get_height() - int(ironman.get_height()*1.15)) // 2), None) # paint to screen
                #device #3
                text_img.blit(ironman, (xCentre + int(xCentre/1.5), (text_img.get_height() - int(ironman.get_height()*1.15)) // 2), None) # paint to screen

        elif location == "in pale":
            if GRAPHICSMODE == "PIL":
                text_img = PilImage.new('RGBA', newshield.size, (0, 0, 0, 0))
                xCentre = (text_img.width / 2) - (ironman.width / 2)
                text_img.paste(bg, ((text_img.width - bg.width) // 2, (text_img.height - bg.height) // 2))
                #device #1
                text_img.paste(ironman, (xCentre, ((text_img.height - int(ironman.height*1.5)) // 2 - int(xCentre/1.5))), mask=ironman)
                #device #2
                text_img.paste(ironman, (xCentre, (text_img.height - int(ironman.height*1.15)) // 2), mask=ironman)
                #device #3
                text_img.paste(ironman, (xCentre, ((text_img.height - int(ironman.height*1.15))// 2 + int(xCentre/1.5))), mask=ironman)
            elif GRAPHICSMODE == "PyGame":
                text_img = pygame.Surface((newshield.get_width(),newshield.get_height()), pygame.SRCALPHA, 32)
                xCentre = (text_img.get_width() / 2) - (ironman.get_width() / 2)
                text_img.blit(bg, ((text_img.get_width() - bg.get_width()) // 2, (text_img.get_height() - bg.get_height()) // 2))
                #device #1
                text_img.blit(ironman, (xCentre, ((text_img.get_height() - int(ironman.get_height()*1.5)) // 2 - int(xCentre/1.5))), None) # paint to screen
                #device #2
                text_img.blit(ironman, (xCentre, (text_img.get_height() - int(ironman.get_height()*1.15)) // 2), None) # paint to screen
                #device #3
                text_img.blit(ironman, (xCentre, ((text_img.get_height() - int(ironman.get_height()*1.15))// 2 + int(xCentre/1.5))), None) # paint to screen

                pygame.image.save(text_img, "E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFINALFILE.png")
                print "WROTE 'E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFINALFILE.png'"


    #now blazon the shield (ie make the description in a standard heraldic form)

    # Blazons are unpunctuated, except that the tinctures and charges begin with a capital letter.
    blazon = string.capitalize(color1Dict["Name"])  

    if numDevices == 1:
        if DeviceDescriptionsDict != None:
            if DeviceDescriptionsDict.has_key(deviceToUse):
                #blazon = "%s, %s" % (blazon, string.capitalize(DeviceDescriptionsDict[deviceToUse][0]))
                blazon = "%s, %s" % (blazon, DeviceDescriptionsDict[deviceToUse][0])
            else:
                #blazon = "%s, %s" % (blazon, string.capitalize(guess_description_from_Filename(deviceToUse)))
                blazon = "%s, %s" % (blazon, guess_description_from_Filename(deviceToUse))
        else:
            #blazon = "%s, %s" % (blazon, string.capitalize(guess_description_from_Filename(deviceToUse)))
            blazon = "%s, %s" % (blazon, guess_description_from_Filename(deviceToUse))

        if string.find(deviceToUse, "roper") > -1:
            pass # a charge that is 'proper' is in its natural colours - therefore we don't need to say which tincture it's in
        elif deviceToUse in blazon_exceptions:
            pass
        else:
            blazon = "%s %s" % (blazon, string.capitalize(color2Dict["Name"]))

    elif numDevices == 2:
        if DeviceDescriptionsDict != None:
            #will need to alter this once we have possibility of more than one device as a charge...
            if DeviceDescriptionsDict.has_key(deviceToUse):
                #blazon = "%s, %s" % (blazon, string.capitalize(DeviceDescriptionsDict[deviceToUse][0]))
                blazon = "%s, two %s" % (blazon, DeviceDescriptionsDict[deviceToUse][1])
            else:
                #blazon = "%s, %s" % (blazon, string.capitalize(guess_description_from_Filename(deviceToUse)))
                blazon = "%s, two %s" % (blazon, guess_description_from_Filename(deviceToUse))
        else:
            #blazon = "%s, %s" % (blazon, string.capitalize(guess_description_from_Filename(deviceToUse)))
            blazon = "%s, three %s" % (blazon, guess_description_from_Filename(deviceToUse))
        if location != None:
            blazon = "%s %s" % (blazon, location)

        if string.find(deviceToUse, "roper") > -1:
            pass # a charge that is 'proper' is in its natural colours - therefore we don't need to say which tincture it's in
        elif deviceToUse in blazon_exceptions:
            pass
        else:
            #blazon = "%s %s" % (blazon, string.capitalize(color2Dict["Name"]))
            blazon = "%s %s" % (blazon, string.capitalize(color2Dict["Name"]))

    elif numDevices == 3:
        if DeviceDescriptionsDict != None:
            #will need to alter this once we have possibility of more than one device as a charge...
            if DeviceDescriptionsDict.has_key(deviceToUse):
                #blazon = "%s, %s" % (blazon, string.capitalize(DeviceDescriptionsDict[deviceToUse][0]))
                blazon = "%s, three %s" % (blazon, DeviceDescriptionsDict[deviceToUse][1])
            else:
                #blazon = "%s, %s" % (blazon, string.capitalize(guess_description_from_Filename(deviceToUse)))
                blazon = "%s, three %s" % (blazon, guess_description_from_Filename(deviceToUse))
        else:
            #blazon = "%s, %s" % (blazon, string.capitalize(guess_description_from_Filename(deviceToUse)))
            blazon = "%s, three %s" % (blazon, guess_description_from_Filename(deviceToUse))
        if location != None:
            blazon = "%s %s" % (blazon, location)

        if string.find(deviceToUse, "roper") > -1:
            pass # a charge that is 'proper' is in its natural colours - therefore we don't need to say which tincture it's in
        elif deviceToUse in blazon_exceptions:
            pass
        else:
            #blazon = "%s %s" % (blazon, string.capitalize(color2Dict["Name"]))
            blazon = "%s %s" % (blazon, string.capitalize(color2Dict["Name"]))

    if numDevices == 4:
        pass
        #fill in later

        if string.find(deviceToUse, "roper") > -1:
            pass # a charge that is 'proper' is in its natural colours - therefore we don't need to say which tincture it's in
        else:
            #blazon = "%s %s" % (blazon, string.capitalize(color2Dict["Name"]))
            blazon = "%s %s" % (blazon, string.capitalize(color2Dict["Name"]))

    return blazon, text_img

def make_Ordinary_Badge(color1Dict, color2Dict, VERBOSE=1, OrdinaryDescriptionsDict=None, SILENT=0, GRAPHICSMODE="PIL"):

    TEST = 1

    if VERBOSE > 0:
        print "  Making badge (Type: Ordinary)"
    else:
        if SILENT != 1:
            print ".",
        else:
            pass

    #pick a shield
    ordinariesdir = os.getcwd()
    os.chdir(ordinariesdir)
    allshields = glob.glob("*.*") # assume we only have graphics files in that directory

    #remove descriptions file etc
    newshields = []
    for nx in range(0, len(allshields)):
        if allshields[nx][0] == "_":
            pass
        else:
            newshields.append(allshields[nx])
    allshields = newshields

    shieldToUse = random.choice(allshields)

    if VERBOSE > 0:
        print "  Chose shield '%s'" % shieldToUse

    if GRAPHICSMODE == "PIL":
        img = PilImage.open(shieldToUse)
    elif GRAPHICSMODE == "PyGame":
        img = pygame.image.load(shieldToUse)
        if img.get_alpha():
            img = pygame.Surface.convert_alpha(img)
            if VERBOSE > 0:
                print "    ALPHA CHANNEL IN IMAGE - used img.convert_alpha()"
        else:
            img = img.convert()
            img.set_colorkey((255,0,255))
            if VERBOSE > 0:
                print "    NO ALPHA CHANNEL IN IMAGE - used img.set_colorkey(255,0,255)"

    #set the shield background colour
    if VERBOSE > 0:
        print "  Setting shield background to '%s' (%s)" % (color1Dict["Name"], color1Dict["Colour"])
    newshield = change_Shield_Color(img, color1Dict["RGB Colour"], GRAPHICSMODE)

    if VERBOSE > 0:
        print "  Setting ordinary colour to '%s' (%s)" % (color2Dict["Name"], color2Dict["Colour"])
    newshield = change_Other_Color(newshield, color2Dict["RGB Colour"], GRAPHICSMODE)

    os.chdir(ordinariesdir)

    #now blazon the shield (ie make the description in a standard heraldic form)

    # Blazons are unpunctuated, except that the tinctures and charges begin with a capital letter.
    blazon = string.capitalize(color1Dict["Name"])  

    if OrdinaryDescriptionsDict != None:
        if OrdinaryDescriptionsDict.has_key(shieldToUse):
            #blazon = "%s, %s" % (blazon, string.capitalize(OrdinaryDescriptionsDict[deviceToUse][0]))
            blazon = "%s, %s" % (blazon, OrdinaryDescriptionsDict[shieldToUse][0])
        else:
            #blazon = "%s, %s" % (blazon, string.capitalize(guess_description_from_Filename(deviceToUse)))
            blazon = "%s, %s" % (blazon, guess_description_from_Filename(shieldToUse))
    else:
        #blazon = "%s, %s" % (blazon, string.capitalize(guess_description_from_Filename(deviceToUse)))
        blazon = "%s, %s" % (blazon, guess_description_from_Filename(shieldToUse))
    if string.find(shieldToUse, "roper") > -1:
        pass # a charge that is 'proper' is in its natural colours - therefore we don't need to say which tincture it's in
    else:
        #blazon = "%s %s" % (blazon, string.capitalize(color2Dict["Name"]))
        blazon = "%s %s" % (blazon, string.capitalize(color2Dict["Name"]))

    return blazon, newshield


def make_Quartered_Badge(color1Dict, color2Dict, VERBOSE=1, OrdinaryDescriptionsDict=None, DeviceDescriptionsDict=None, SILENT=0, GRAPHICSMODE="PIL"):

    TEST = 1

    if VERBOSE > 0:
        print "  Making badge (Type: Quartered)"
    else:
        if SILENT != 1:
            print ".",
        else:
            pass

    StainNames  = ["Murrey", "Sanguine", "Tenné"]
    MetalNames  = ["Argent", "Or"]
    ColourNames = ["Gules", "Sable", "Azure", "Vert", "Purpure"]

    if color1Dict["Name"] in ColourNames:
        color3Dict = getMetal()
        color3 = color3Dict["Name"]
        color3name = color1Dict["Colour"]
    elif color1Dict["Name"] in StainNames:
        color3Dict = getMetal()
        color3 = color3Dict["Name"]
        color3name = color3Dict["Colour"]
    elif color1Dict["Name"] in MetalNames:
        color3Dict = getColour()
        color3 = color3Dict["Name"]
        color3name = color3Dict["Colour"]

    #the files in the shields directory that are quartered -
    #the filenames aren't consistent enough to rely on them.
    #Don't forget to update them if we add more!        
    known_quarters = ["pg28gr1quarterly.png",
                      "quarter.png",
                      "quarterly.png",
                      ]
    devicetype = random.choice((0,1,2,3,4))
        #0: no devices
        #1: devices on quarters 1 & 4 (Top left, bottom right)
        #2: devices on quarters 2 & 3 (Top right, bottom left)
        #3: devices on quarters 1, 2, 3 & 4
        #4: unique devices on quarters 1, 2, 3 & 4 #


    #pick a shield
    ordinariesdir = os.getcwd()
    os.chdir(ordinariesdir)

    shieldToUse = random.choice(known_quarters)

    if VERBOSE > 0:
        print "  Chose shield '%s'" % shieldToUse

    if GRAPHICSMODE == "PIL":
        img = PilImage.open(shieldToUse)
    elif GRAPHICSMODE == "PyGame":
        img = pygame.image.load(shieldToUse)

        if img.get_alpha():
            #img = img.convert_alpha()
            img = pygame.Surface.convert_alpha(img)
            if VERBOSE > 0:
                print "    ALPHA CHANNEL IN IMAGE - used img.convert_alpha()"
        else:
            img = img.convert()
            img.set_colorkey((255,0,255))
            if VERBOSE > 0:
                print "    NO ALPHA CHANNEL IN IMAGE - used img.set_colorkey(255,0,255)"

    #set the shield background colour
    if VERBOSE > 0:
        print "  Setting shield background to '%s' (%s)" % (color1Dict["Name"], color1Dict["Colour"])
    newshield = change_Shield_Color(img, color1Dict["RGB Colour"], GRAPHICSMODE)

    if VERBOSE > 0:
        print "  Setting quarters colour to '%s' (%s)" % (color2Dict["Name"], color2Dict["Colour"])
    newshield = change_Other_Color(newshield, color2Dict["RGB Colour"], GRAPHICSMODE)

    blazon = "" # finish later...   

    if devicetype == 0: 
        #0: no devices
        if VERBOSE > 0:
            print "  (no devices)"
        #blazon it here, since other versions require info about the devices used

        # Blazons are unpunctuated, except that the tinctures and charges begin with a capital letter.
        #blazon = string.capitalize(color1Dict["Name"])
        blazon = "Quarterly %s and %s" % (color1Dict["Name"], color2Dict["Name"])

        text_img = newshield

    else:

        #pick a device to go on the shield
        devicesdir = os.path.join(ordinariesdir, "..", "Devices")
        devicesdir = os.path.join(ordinariesdir, "..", "Devices")
        os.chdir(devicesdir)
        alldevices = glob.glob("*.*") # assume we only have graphics files in that directory
        #remove descriptions file etc
        newdevices = []

        for nx in range(0, len(alldevices)):
            if alldevices[nx][0] == "_":
                pass
            else:
                newdevices.append(alldevices[nx])
        alldevices = newdevices

        deviceToUse = random.choice(alldevices)

        if VERBOSE > 0:
            print "  Chose device '%s'" % deviceToUse

        #resize the device...
        if GRAPHICSMODE == "PIL":
            newDevice = PilImage.open(deviceToUse)
            mysize = int(newshield.width / 3.5)
            if newDevice.size[0] > newDevice.size[1]:
                wpercent = (mysize/float(newDevice.size[0]))
                hsize = int((float(newDevice.size[1])*float(wpercent)))
                newDevice = newDevice.resize((mysize,hsize), PilImage.ANTIALIAS)
            else:
                wpercent = (mysize/float(newDevice.size[1]))
                hsize = int((float(newDevice.size[0])*float(wpercent)))
                newDevice = newDevice.resize((hsize, mysize), PilImage.ANTIALIAS)
        elif GRAPHICSMODE == "PyGame":
            #newDevice = PilImage.open(deviceToUse)
            newDevice = pygame.image.load(deviceToUse)
            if newDevice.get_alpha():
                #img = img.convert_alpha()
                newDevice = pygame.Surface.convert_alpha(newDevice)
                if VERBOSE > 0:
                    print "    ALPHA CHANNEL IN IMAGE - used newDevice.convert_alpha()"
            else:
                newDevice = newDevice.convert()
                newDevice.set_colorkey((255,0,255))
                if VERBOSE > 0:
                    print "    NO ALPHA CHANNEL IN IMAGE - used newDevice.set_colorkey(255,0,255)"

            mysize = int(newshield.get_width()/ 3.5)
            newDevice_size = (newDevice.get_width(),newDevice.get_height())
            if newDevice_size[0] > newDevice_size[1]:
                wpercent = (mysize/float(newDevice_size[0]))
                hsize = int((float(newDevice_size[1])*float(wpercent)))
                newDevice = pygame.transform.smoothscale(newDevice, (mysize,hsize))
            else:
                wpercent = (mysize/float(newDevice_size[1]))
                hsize = int((float(newDevice_size[0])*float(wpercent)))
                newDevice = pygame.transform.smoothscale(newDevice, (hsize, mysize))


        if devicetype == 1: 
        #1: devices on quarters 1 & 4 (Top left, bottom right)

            if VERBOSE > 0:
                print "      (devices on quarters 1 & 4 (Top left, bottom right))"
            #start blazoning it here...
            blazon = "Quarterly %s and %s" % (color1Dict["Name"], color2Dict["Name"])

            if color1Dict["Name"] in ColourNames:
                color3Dict = getMetal()
                color3 = color3Dict["Name"]
                color3name = color1Dict["Colour"]
            elif color1Dict["Name"] in StainNames:
                color3Dict = getMetal()
                color3 = color3Dict["Name"]
                color3name = color3Dict["Colour"]
            elif color1Dict["Name"] in MetalNames:
                color3Dict = getColour()
                color3 = color3Dict["Name"]
                color3name = color3Dict["Colour"]

            if VERBOSE > 0:
                print "  Setting device colour to '%s' (%s)" % (color3Dict["Name"], color3Dict["Colour"])
            if color3Dict["Name"] in ["Sable", "Purpure"]:
                myGray = (180, 180, 180)
                if string.find(deviceToUse, "roper") > -1:
                    #a charge that is 'proper' is in its natural colours - therefore we don't need to recolour it
                    pass
                else:
                    newDevice = change_Black_Outline_Color(newDevice, myGray, GRAPHICSMODE)
                    newDevice = change_Shield_Color(newDevice, color3Dict["RGB Colour"], GRAPHICSMODE)
            else:
                newDevice = change_Shield_Color(newDevice, color3Dict["RGB Colour"], GRAPHICSMODE)

            bg = newshield
            ironman = newDevice

            if GRAPHICSMODE == "PIL":
                text_img = PilImage.new('RGBA', newshield.size, (0, 0, 0, 0))
                xCentre = (text_img.width / 2)
                text_img.paste(bg, ((text_img.width - bg.width) // 2, (text_img.height - bg.height) // 2))
                #device #1 (quarter 1)
                text_img.paste(ironman, ((xCentre - int(xCentre/2) - (ironman.width/2)), (xCentre - (int(xCentre/2))) - (ironman.height/2)), mask=ironman)
                #device #2 (quarter 4)
                text_img.paste(ironman, (xCentre + int(xCentre/2) - (ironman.width/2), xCentre + (int(xCentre/2)) - (ironman.height/2)), mask=ironman)

            elif GRAPHICSMODE == "PyGame":
                text_img = pygame.Surface((newshield.get_width(),newshield.get_height()), pygame.SRCALPHA, 32)
                xCentre = (text_img.get_width() / 2)
                text_img.blit(bg, ((text_img.get_width() - bg.get_width()) // 2, (text_img.get_height() - bg.get_height()) // 2))
                #device #1 (quarter 1)
                text_img.blit(ironman, ((xCentre - int(xCentre/2) - (ironman.get_width()/2)), (xCentre - (int(xCentre/2))) - (ironman.get_height()/2)), None) # paint to screen
                #device #2 (quarter 4)
                text_img.blit(ironman, (xCentre + int(xCentre/2) - (ironman.get_width()/2), xCentre + (int(xCentre/2)) - (ironman.get_height()/2)), None) # paint to screen

                if DEBUG == 1:
                    pygame.image.save(text_img, "E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFINALFILE.png")
                    print "WROTE 'E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFINALFILE.png'"

            #now finish blazoning it...
            blazon = "%s, 1st and 4th" % blazon

            if DeviceDescriptionsDict != None:
                if DeviceDescriptionsDict.has_key(deviceToUse):
                    #blazon = "%s, %s" % (blazon, string.capitalize(OrdinaryDescriptionsDict[deviceToUse][0]))
                    blazon = "%s %s" % (blazon, DeviceDescriptionsDict[deviceToUse][0])
                else:
                    #blazon = "%s, %s" % (blazon, string.capitalize(guess_description_from_Filename(deviceToUse)))
                    blazon = "%s %s" % (blazon, guess_description_from_Filename(deviceToUse))
            else:
                #blazon = "%s, %s" % (blazon, string.capitalize(guess_description_from_Filename(deviceToUse)))
                blazon = "%s %s" % (blazon, guess_description_from_Filename(deviceToUse))
            if string.find(deviceToUse, "roper") > -1:
                pass # a charge that is 'proper' is in its natural colours - therefore we don't need to say which tincture it's in
            else:
                blazon = "%s %s" % (blazon, string.capitalize(color3Dict["Name"]))

        elif devicetype == 2: 
        #2: devices on quarters 2 & 3 (Top right, bottom left)
            if VERBOSE > 0:
                print "      (devices on quarters 2 & 3 (Top right, bottom left))"
            #blazon it here
            blazon = "Quarterly %s and %s" % (color1Dict["Name"], color2Dict["Name"])

            if color2Dict["Name"] in ColourNames:
                color3Dict = getMetal()
                color3 = color3Dict["Name"]
                color3name = color1Dict["Colour"]
            elif color2Dict["Name"] in StainNames:
                color3Dict = getMetal()
                color3 = color3Dict["Name"]
                color3name = color3Dict["Colour"]
            elif color2Dict["Name"] in MetalNames:
                color3Dict = getColour()
                color3 = color3Dict["Name"]
                color3name = color3Dict["Colour"]

            if VERBOSE > 0:
                print "  Setting device colour to '%s' (%s)" % (color3Dict["Name"], color3Dict["Colour"])

            if GRAPHICSMODE == "PIL":
                img2 = PilImage.open(deviceToUse)
            elif GRAPHICSMODE == "PyGame":
                img2 = pygame.image.load(deviceToUse)
                if img2.get_alpha():
                    #img2 = img.convert_alpha()
                    img2 = pygame.Surface.convert_alpha(img2)
                    if VERBOSE > 0:
                        print "    ALPHA CHANNEL IN IMAGE - used img2.convert_alpha()"
                else:
                    img2 = img.convert()
                    img2.set_colorkey((255,0,255))
                    if VERBOSE > 0:
                        print "    NO ALPHA CHANNEL IN IMAGE - used img2.set_colorkey(255,0,255)"

            if color3Dict["Name"] in ["Sable", "Purpure"]:
                myGray = (180, 180, 180)
                if string.find(deviceToUse, "roper") > -1:
                    #a charge that is 'proper' is in its natural colours - therefore we don't need to recolour it
                    #newDevice = img2
                    pass
                else:
                    newDevice = change_Black_Outline_Color(newDevice, myGray, GRAPHICSMODE)
                    newDevice = change_Shield_Color(newDevice, color3Dict["RGB Colour"], GRAPHICSMODE)
            else:
                newDevice = change_Shield_Color(newDevice, color3Dict["RGB Colour"], GRAPHICSMODE)

            bg = newshield
            ironman = newDevice

            if GRAPHICSMODE == "PIL":
                text_img = PilImage.new('RGBA', newshield.size, (0, 0, 0, 0))
                xCentre = (text_img.width / 2)
                text_img.paste(bg, ((text_img.width - bg.width) // 2, (text_img.height - bg.height) // 2))
                #device #1 (quarter 2)
                text_img.paste(ironman, (xCentre + int(xCentre/2)- (ironman.width/2), xCentre - (int(xCentre/2)) - (ironman.width/2)), mask=ironman)
                #device #2 (quarter 4)
                text_img.paste(ironman, (xCentre - int(xCentre/2) - (ironman.width/2), xCentre + (int(xCentre/2)) - (ironman.width/2)), mask=ironman)

            elif GRAPHICSMODE == "PyGame":
                text_img = pygame.Surface((newshield.get_width(),newshield.get_height()), pygame.SRCALPHA, 32)
                xCentre = (text_img.get_width() / 2)
                text_img.blit(bg, ((text_img.get_width() - bg.get_width()) // 2, (text_img.get_height() - bg.get_height()) // 2))
                #device #1 (quarter 2)
                text_img.blit(ironman, (xCentre + int(xCentre/2)- (ironman.get_width()/2), xCentre - (int(xCentre/2)) - (ironman.get_width()/2)), None) # paint to screen
                #device #2 (quarter 4)
                text_img.blit(ironman, (xCentre - int(xCentre/2) - (ironman.get_width()/2), xCentre + (int(xCentre/2)) - (ironman.get_width()/2)), None) # paint to screen

                if DEBUG == 1:
                    pygame.image.save(text_img, "E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFINALFILE.png")
                    print "WROTE 'E:\\Projects\\NEW RENPY GAME\\TEMP\\TESTFINALFILE.png'"

            #now finish blazoning it...
            blazon = "%s, 2nd and 3rd" % blazon

            if DeviceDescriptionsDict != None:
                if DeviceDescriptionsDict.has_key(deviceToUse):
                    #blazon = "%s, %s" % (blazon, string.capitalize(OrdinaryDescriptionsDict[deviceToUse][0]))
                    blazon = "%s %s" % (blazon, DeviceDescriptionsDict[deviceToUse][0])
                else:
                    #blazon = "%s, %s" % (blazon, string.capitalize(guess_description_from_Filename(deviceToUse)))
                    blazon = "%s %s" % (blazon, guess_description_from_Filename(deviceToUse))
            else:
                #blazon = "%s, %s" % (blazon, string.capitalize(guess_description_from_Filename(deviceToUse)))
                blazon = "%s %s" % (blazon, guess_description_from_Filename(deviceToUse))
            if string.find(deviceToUse, "roper") > -1:
                pass # a charge that is 'proper' is in its natural colours - therefore we don't need to say which tincture it's in
            else:
                #blazon = "%s %s" % (blazon, string.capitalize(color2Dict["Name"]))
                blazon = "%s %s" % (blazon, string.capitalize(color3Dict["Name"]))

        #this is where it starts to get complicated...

            #EXAMPLE BLAZON:
            """Quarterly, 1st and 4th, Gules a castle Or (Castile), 2nd and 3rd, Argent a lion rampant (Leon) """

        elif devicetype == 3: 
        #3: devices on quarters 1, 2, 3 & 4
            if VERBOSE > 0:
                print "      (devices on quarters 1, 2, 3 & 4)"
            #start blazoning it here...
            blazon = "Quarterly %s and %s" % (color1Dict["Name"], color2Dict["Name"])

            if color1Dict["Name"] in ColourNames:
                color3Dict = getMetal()
                color3 = color3Dict["Name"]
                color3name = color3Dict["Colour"]
            elif color1Dict["Name"] in StainNames:
                color3Dict = getMetal()
                color3 = color3Dict["Name"]
                color3name = color3Dict["Colour"]
            elif color1Dict["Name"] in MetalNames:
                color3Dict = getColour()
                color3 = color3Dict["Name"]
                color3name = color3Dict["Colour"]

            if color2Dict["Name"] in ColourNames:
                color4Dict = getMetal()
                color4 = color4Dict["Name"]
                color4name = color4Dict["Colour"]
            elif color2Dict["Name"] in StainNames:
                color4Dict = getMetal()
                color4 = color4Dict["Name"]
                color4name = color4Dict["Colour"]
            elif color2Dict["Name"] in MetalNames:
                color4Dict = getColour()
                color4 = color4Dict["Name"]
                color4name = color4Dict["Colour"]

            if VERBOSE > 0:
                print "      need 2 devices..."
                print "      %s is DEVICE2" % (deviceToUse)
                print "  Setting device2 colour to '%s' (%s)" % (color3Dict["Name"], color3Dict["Colour"])

            if GRAPHICSMODE == "PIL":
                device2 = PilImage.open(deviceToUse)

            elif GRAPHICSMODE == "PyGame":
                device2 = pygame.image.load(deviceToUse)
                if device2.get_alpha():
                    #device2 = device2.convert_alpha()
                    device2 = pygame.Surface.convert_alpha(device2)
                    if VERBOSE > 0:
                        print "    ALPHA CHANNEL IN IMAGE - used device2.convert_alpha()"
                else:
                    device2 = device2.convert()
                    device2.set_colorkey((255,0,255))
                    if VERBOSE > 0:
                        print "    NO ALPHA CHANNEL IN IMAGE - used device2.set_colorkey(255,0,255)"


            if color3Dict["Name"] in ["Sable", "Purpure"]:
                myGray = (180, 180, 180)
                if string.find(deviceToUse, "roper") > -1:
                    #a charge that is 'proper' is in its natural colours - therefore we don't need to recolour it
                    newDevice2 = device2
                else:
                    newDevice2 = change_Black_Outline_Color(device2, myGray, GRAPHICSMODE)
                    newDevice2 = change_Shield_Color(newDevice2, color2Dict["RGB Colour"], GRAPHICSMODE)
            else:
                newDevice2 = change_Shield_Color(device2, color2Dict["RGB Colour"], GRAPHICSMODE)
    
            deviceToUse2 = random.choice(alldevices)
            while deviceToUse2 == deviceToUse:
                deviceToUse2 = random.choice(alldevices)

            if GRAPHICSMODE == "PIL":
                device3 = PilImage.open(deviceToUse2)

            elif GRAPHICSMODE == "PyGame":
                device3 = pygame.image.load(deviceToUse2)
                if device3.get_alpha():
                    #device3 = device3.convert_alpha()
                    device3 = pygame.Surface.convert_alpha(device3)
                    if VERBOSE > 0:
                        print "    ALPHA CHANNEL IN IMAGE - used device3.convert_alpha()"
                else:
                    device3 = device3.convert()
                    device3.set_colorkey((255,0,255))
                    if VERBOSE > 0:
                        print "    NO ALPHA CHANNEL IN IMAGE - used device3.set_colorkey(255,0,255)"

            if VERBOSE > 0:
                print "  Chose device '%s' for newDevice3" % deviceToUse2
                print "  Setting device3 colour to '%s' (%s)" % (color4Dict["Name"], color4Dict["Colour"])

            if color4Dict["Name"] in ["Sable", "Purpure"]:
                myGray = (180, 180, 180)
                if string.find(deviceToUse2, "roper") > -1:
                    #a charge that is 'proper' is in its natural colours - therefore we don't need to recolour it
                    newDevice3 = device3
                else:
                    newDevice3 = change_Black_Outline_Color(device3, myGray, GRAPHICSMODE)
                    newDevice3 = change_Shield_Color(newDevice3, color4Dict["RGB Colour"], GRAPHICSMODE)
            else:
                newDevice3 = change_Shield_Color(device3, color4Dict["RGB Colour"], GRAPHICSMODE)

            #resize the devices...
            if GRAPHICSMODE == "PIL":
                mysize = int(newshield.width / 3.5)
                if newDevice2.size[0] > newDevice2.size[1]:
                    wpercent = (mysize/float(newDevice2.size[0]))
                    hsize = int((float(newDevice2.size[1])*float(wpercent)))
                    newDevice2 = newDevice2.resize((mysize,hsize), PilImage.ANTIALIAS)
                else:
                    wpercent = (mysize/float(newDevice2.size[1]))
                    hsize = int((float(newDevice2.size[0])*float(wpercent)))
                    newDevice2 = newDevice2.resize((hsize, mysize), PilImage.ANTIALIAS)

                if newDevice3.size[0] > newDevice3.size[1]:
                    wpercent = (mysize/float(newDevice3.size[0]))
                    hsize = int((float(newDevice3.size[1])*float(wpercent)))
                    newDevice3 = newDevice3.resize((mysize,hsize), PilImage.ANTIALIAS)
                else:
                    wpercent = (mysize/float(newDevice3.size[1]))
                    hsize = int((float(newDevice3.size[0])*float(wpercent)))
                    newDevice3 = newDevice3.resize((hsize, mysize), PilImage.ANTIALIAS)

            elif GRAPHICSMODE == "PyGame":
                mysize = int(newshield.get_width() / 3.5)

                newDevice2_size = (newDevice2.get_width(),newDevice2.get_height())
                if newDevice2_size[0] > newDevice2_size[1]:
                    wpercent = (mysize/float(newDevice2_size[0]))
                    hsize = int((float(newDevice2_size[1])*float(wpercent)))
                    newDevice2 = pygame.transform.smoothscale(newDevice2, (mysize,hsize))
                else:
                    wpercent = (mysize/float(newDevice2_size[1]))
                    hsize = int((float(newDevice2_size[0])*float(wpercent)))
                    newDevice2 = pygame.transform.smoothscale(newDevice2, (hsize, mysize))

                newDevice3_size = (newDevice3.get_width(),newDevice3.get_height())
                if newDevice3_size[0] > newDevice3_size[1]:
                    wpercent = (mysize/float(newDevice3_size[0]))
                    hsize = int((float(newDevice3_size[1])*float(wpercent)))
                    newDevice3 = pygame.transform.smoothscale(newDevice3, (mysize,hsize))
                else:
                    wpercent = (mysize/float(newDevice2_size[1]))
                    hsize = int((float(newDevice3_size[0])*float(wpercent)))
                    newDevice3 = pygame.transform.smoothscale(newDevice3, (hsize, mysize))

            bg = newshield
            ironman = newDevice2

            if GRAPHICSMODE == "PIL":
                text_img = PilImage.new('RGBA', newshield.size, (0, 0, 0, 0))
                xCentre = (text_img.width / 2)
                text_img.paste(bg, ((text_img.width - bg.width) // 2, (text_img.height - bg.height) // 2))
                #device #1 (quarter 1)
                text_img.paste(ironman, ((xCentre - int(xCentre/2) - (ironman.width/2)), (xCentre - (int(xCentre/2))) - (ironman.height/2)), mask=ironman)
                #device #2 (quarter 3)
                text_img.paste(ironman, (xCentre + int(xCentre/2) - (ironman.width/2), xCentre + (int(xCentre/2)) - (ironman.height/2)), mask=ironman)
                ironman2 = newDevice3
                #device #3 (quarter 2)
                text_img.paste(ironman2, (xCentre + int(xCentre/2) - (ironman2.width/2), xCentre - (int(xCentre/2)) - (ironman2.height/2)), mask=ironman2)
                #device #4 (quarter 4)
                text_img.paste(ironman2, (xCentre - int(xCentre/2) - (ironman2.width/2), xCentre + (int(xCentre/2)) - (ironman2.height/2)), mask=ironman2)

            elif GRAPHICSMODE == "PyGame":
                text_img = pygame.Surface((newshield.get_width(),newshield.get_height()), pygame.SRCALPHA, 32)
                xCentre = (text_img.get_width() / 2)
                text_img.blit(bg, ((text_img.get_width() - bg.get_width()) // 2, (text_img.get_height() - bg.get_height()) // 2))
                #device #1 (quarter 1)
                text_img.blit(ironman, ((xCentre - int(xCentre/2) - (ironman.get_width()/2)), (xCentre - (int(xCentre/2))) - (ironman.get_height()/2)), None) # paint to screen
                #device #2 (quarter 3)
                text_img.blit(ironman, (xCentre + int(xCentre/2) - (ironman.get_width()/2), xCentre + (int(xCentre/2)) - (ironman.get_height()/2)), None) # paint to screen
                ironman2 = newDevice3
                #device #3 (quarter 2)
                text_img.blit(ironman2, (xCentre + int(xCentre/2) - (ironman2.get_width()/2), xCentre - (int(xCentre/2)) - (ironman2.get_height()/2)), None) # paint to screen
                #device #4 (quarter 4)
                text_img.blit(ironman2, (xCentre - int(xCentre/2) - (ironman2.get_width()/2), xCentre + (int(xCentre/2)) - (ironman2.get_height()/2)), None) # paint to screen

            #now finish blazoning it...
            blazon = "%s, 1st and 4th" % blazon

            if DeviceDescriptionsDict != None:
                if DeviceDescriptionsDict.has_key(deviceToUse):
                    #blazon = "%s, %s" % (blazon, string.capitalize(OrdinaryDescriptionsDict[deviceToUse][0]))
                    blazon = "%s %s" % (blazon, DeviceDescriptionsDict[deviceToUse][0])
                else:
                    #blazon = "%s, %s" % (blazon, string.capitalize(guess_description_from_Filename(deviceToUse)))
                    blazon = "%s %s" % (blazon, guess_description_from_Filename(deviceToUse))
            else:
                #blazon = "%s, %s" % (blazon, string.capitalize(guess_description_from_Filename(deviceToUse)))
                blazon = "%s %s" % (blazon, guess_description_from_Filename(deviceToUse))
            if string.find(deviceToUse, "roper") > -1:
                pass # a charge that is 'proper' is in its natural colours - therefore we don't need to say which tincture it's in
            else:
                #blazon = "%s %s" % (blazon, string.capitalize(color2Dict["Name"]))
                blazon = "%s %s" % (blazon, string.capitalize(color3Dict["Name"]))

            blazon = "%s, 2nd and 3rd" % blazon

            if DeviceDescriptionsDict != None:
                if DeviceDescriptionsDict.has_key(deviceToUse2):
                    #blazon = "%s, %s" % (blazon, string.capitalize(OrdinaryDescriptionsDict[deviceToUse][0]))
                    blazon = "%s %s" % (blazon, DeviceDescriptionsDict[deviceToUse2][0])
                else:
                    #blazon = "%s, %s" % (blazon, string.capitalize(guess_description_from_Filename(deviceToUse)))
                    blazon = "%s %s" % (blazon, guess_description_from_Filename(deviceToUse2))
            else:
                #blazon = "%s, %s" % (blazon, string.capitalize(guess_description_from_Filename(deviceToUse)))
                blazon = "%s %s" % (blazon, guess_description_from_Filename(deviceToUse2))
            if string.find(deviceToUse2, "roper") > -1:
                pass # a charge that is 'proper' is in its natural colours - therefore we don't need to say which tincture it's in
            else:
                #blazon = "%s %s" % (blazon, string.capitalize(color2Dict["Name"]))
                blazon = "%s %s" % (blazon, string.capitalize(color4Dict["Name"]))



        elif devicetype == 4: 
        #4: UNIQUE devices on quarters 1, 2, 3 & 4

        #I've messed up the numbering of the quarters in the code - but it works, and the output doesn't break the heraldic
        #rule of tinctures, so I'm not going to mess with it!

            if VERBOSE > 0:
                print "      (unique devices on quarters 1, 2, 3 & 4)"
            #start blazon here...
            blazon = "Quarterly %s and %s" % (color1Dict["Name"], color2Dict["Name"])

            if color1Dict["Name"] in ColourNames:
                color3Dict = getMetal()
                color3 = color3Dict["Name"]
                color3name = color3Dict["Colour"]
                color5Dict = getMetal()
                color5 = color5Dict["Name"]
                color5name = color5Dict["Colour"]
            elif color1Dict["Name"] in StainNames:
                color3Dict = getMetal()
                color3 = color3Dict["Name"]
                color3name = color3Dict["Colour"]
                color5Dict = getMetal()
                color5 = color5Dict["Name"]
                color5name = color5Dict["Colour"]
            elif color1Dict["Name"] in MetalNames:
                color3Dict = getColour()
                color3 = color3Dict["Name"]
                color3name = color3Dict["Colour"]
                color5Dict = getColour()
                color5 = color5Dict["Name"]
                color5name = color5Dict["Colour"]

            if color2Dict["Name"] in ColourNames:
                color4Dict = getMetal()
                color4 = color4Dict["Name"]
                color4name = color4Dict["Colour"]
                color6Dict = getMetal()
                color6 = color6Dict["Name"]
                color6name = color6Dict["Colour"]
            elif color2Dict["Name"] in StainNames:
                color4Dict = getMetal()
                color4 = color4Dict["Name"]
                color4name = color4Dict["Colour"]
                color6Dict = getMetal()
                color6 = color6Dict["Name"]
                color6name = color6Dict["Colour"]
            elif color2Dict["Name"] in MetalNames:
                color4Dict = getColour()
                color4 = color4Dict["Name"]
                color4name = color4Dict["Colour"]
                color6Dict = getColour()
                color6 = color6Dict["Name"]
                color6name = color6Dict["Colour"]

            usedDevices = [deviceToUse]

            if VERBOSE > 0:
                print "      need 4 devices..."
                print "      %s is DEVICE2" % (deviceToUse)
                print "  Setting device2 colour to '%s' (%s)" % (color3Dict["Name"], color3Dict["Colour"])

            #DEVICE #2
            if GRAPHICSMODE == "PIL":
                device2 = PilImage.open(deviceToUse)

            elif GRAPHICSMODE == "PyGame":
                device2 = pygame.image.load(deviceToUse)
                if device2.get_alpha():
                    #device3 = device3.convert_alpha()
                    device2 = pygame.Surface.convert_alpha(device2)
                    if VERBOSE > 0:
                        print "    ALPHA CHANNEL IN IMAGE - used device2.convert_alpha()"
                else:
                    device2 = device2.convert()
                    device2.set_colorkey((255,0,255))
                    if VERBOSE > 0:
                        print "    NO ALPHA CHANNEL IN IMAGE - used device2.set_colorkey(255,0,255)"


            if color3Dict["Name"] in ["Sable", "Purpure"]:
                myGray = (180, 180, 180)
                if string.find(deviceToUse, "roper") > -1:
                    #a charge that is 'proper' is in its natural colours - therefore we don't need to recolour it
                    newDevice2 = device2
                else:
                    newDevice2 = change_Black_Outline_Color(device2, myGray, GRAPHICSMODE)
                    newDevice2 = change_Shield_Color(newDevice2, color2Dict["RGB Colour"], GRAPHICSMODE)
            else:
                newDevice2 = change_Shield_Color(device2, color2Dict["RGB Colour"], GRAPHICSMODE)

            #DEVICE #3
            deviceToUse2 = random.choice(alldevices)
            while deviceToUse2 in usedDevices:
                deviceToUse2 = random.choice(alldevices)
            usedDevices.append(deviceToUse2)

            if GRAPHICSMODE == "PIL":
                device3 = PilImage.open(deviceToUse2)

            elif GRAPHICSMODE == "PyGame":
                device3 = pygame.image.load(deviceToUse2)
                if device3.get_alpha():
                    device3 = pygame.Surface.convert_alpha(device3)
                    if VERBOSE > 0:
                        print "    ALPHA CHANNEL IN IMAGE - used device3.convert_alpha()"
                else:
                    device3 = device3.convert()
                    device3.set_colorkey((255,0,255))
                    if VERBOSE > 0:
                        print "    NO ALPHA CHANNEL IN IMAGE - used device3.set_colorkey(255,0,255)"

            if VERBOSE > 0:
                print "  Chose device '%s' for newDevice3" % deviceToUse2
                print "      Setting device3 colour to '%s' (%s)" % (color4Dict["Name"], color4Dict["Colour"])

            if color4Dict["Name"] in ["Sable", "Purpure"]:
                myGray = (180, 180, 180)
                if string.find(deviceToUse2, "roper") > -1:
                    #a charge that is 'proper' is in its natural colours - therefore we don't need to recolour it
                    newDevice3 = device3
                else:
                    newDevice3 = change_Black_Outline_Color(device3, myGray, GRAPHICSMODE)
                    newDevice3 = change_Shield_Color(newDevice3, color4Dict["RGB Colour"], GRAPHICSMODE)
            else:
                newDevice3 = change_Shield_Color(device3, color4Dict["RGB Colour"], GRAPHICSMODE)

            #DEVICE #4    
            deviceToUse3 = random.choice(alldevices)
            while deviceToUse3 in usedDevices:
                deviceToUse3 = random.choice(alldevices)
            usedDevices.append(deviceToUse3)

            if GRAPHICSMODE == "PIL":
                device4 = PilImage.open(deviceToUse3)

            elif GRAPHICSMODE == "PyGame":
                device4 = pygame.image.load(deviceToUse3)
                if device4.get_alpha():
                    #device3 = device3.convert_alpha()
                    device4 = pygame.Surface.convert_alpha(device4)
                    if VERBOSE > 0:
                        print "    ALPHA CHANNEL IN IMAGE - used device4.convert_alpha()"
                else:
                    device4 = device4.convert()
                    device4.set_colorkey((255,0,255))
                    if VERBOSE > 0:
                        print "    NO ALPHA CHANNEL IN IMAGE - used device4.set_colorkey(255,0,255)"

            if VERBOSE > 0:
                print "  Chose device '%s' for newDevice4" % deviceToUse3
                print "      Setting device4 colour to '%s' (%s)" % (color5Dict["Name"], color5Dict["Colour"])

            if color5Dict["Name"] in ["Sable", "Purpure"]:
                myGray = (180, 180, 180)
                if string.find(deviceToUse3, "roper") > -1:
                    #a charge that is 'proper' is in its natural colours - therefore we don't need to recolour it
                    newDevice4 = device4
                else:
                    newDevice4 = change_Black_Outline_Color(device4, myGray, GRAPHICSMODE)
                    newDevice4 = change_Shield_Color(newDevice4, color5Dict["RGB Colour"], GRAPHICSMODE)
            else:
                newDevice4 = change_Shield_Color(device4, color5Dict["RGB Colour"], GRAPHICSMODE)

            #DEVICE #5
            deviceToUse4 = random.choice(alldevices)
            while deviceToUse4 in usedDevices:
                deviceToUse4 = random.choice(alldevices)
            usedDevices.append(deviceToUse4)

            if GRAPHICSMODE == "PIL":
                device5 = PilImage.open(deviceToUse4)

            elif GRAPHICSMODE == "PyGame":
                device5 = pygame.image.load(deviceToUse4)
                if device5.get_alpha():
                    #device5 = device5.convert_alpha()
                    device5 = pygame.Surface.convert_alpha(device5)
                    if VERBOSE > 0:
                        print "    ALPHA CHANNEL IN IMAGE - used device5.convert_alpha()"
                else:
                    device5 = device5.convert()
                    device5.set_colorkey((255,0,255))
                    if VERBOSE > 0:
                        print "    NO ALPHA CHANNEL IN IMAGE - used device5.set_colorkey(255,0,255)"

            if VERBOSE > 0:
                print "  Chose device '%s' for newDevice5" % deviceToUse4
                print "      Setting device5 colour to '%s' (%s)" % (color6Dict["Name"], color6Dict["Colour"])

            if color6Dict["Name"] in ["Sable", "Purpure"]:
                myGray = (180, 180, 180)
                if string.find(deviceToUse4, "roper") > -1:
                    #a charge that is 'proper' is in its natural colours - therefore we don't need to recolour it
                    newDevice5 = device5
                else:
                    newDevice5 = change_Black_Outline_Color(device5, myGray, GRAPHICSMODE)
                    newDevice5 = change_Shield_Color(newDevice5, color6Dict["RGB Colour"], GRAPHICSMODE)
            else:
                newDevice5 = change_Shield_Color(device5, color6Dict["RGB Colour"], GRAPHICSMODE)

            #resize the devices...
            if GRAPHICSMODE == "PIL":
                mysize = int(newshield.width / 3.5)
                if newDevice2.size[0] > newDevice2.size[1]:
                    wpercent = (mysize/float(newDevice2.size[0]))
                    hsize = int((float(newDevice2.size[1])*float(wpercent)))
                    newDevice2 = newDevice2.resize((mysize,hsize), PilImage.ANTIALIAS)
                else:
                    wpercent = (mysize/float(newDevice2.size[1]))
                    hsize = int((float(newDevice2.size[0])*float(wpercent)))
                    newDevice2 = newDevice2.resize((hsize, mysize), PilImage.ANTIALIAS)

                if newDevice3.size[0] > newDevice3.size[1]:
                    wpercent = (mysize/float(newDevice3.size[0]))
                    hsize = int((float(newDevice3.size[1])*float(wpercent)))
                    newDevice3 = newDevice3.resize((mysize,hsize), PilImage.ANTIALIAS)
                else:
                    wpercent = (mysize/float(newDevice3.size[1]))
                    hsize = int((float(newDevice3.size[0])*float(wpercent)))
                    newDevice3 = newDevice3.resize((hsize, mysize), PilImage.ANTIALIAS)

                if newDevice4.size[0] > newDevice4.size[1]:
                    wpercent = (mysize/float(newDevice4.size[0]))
                    hsize = int((float(newDevice4.size[1])*float(wpercent)))
                    newDevice4 = newDevice4.resize((mysize,hsize), PilImage.ANTIALIAS)
                else:
                    wpercent = (mysize/float(newDevice4.size[1]))
                    hsize = int((float(newDevice4.size[0])*float(wpercent)))
                    newDevice4 = newDevice4.resize((hsize, mysize), PilImage.ANTIALIAS)

                if newDevice5.size[0] > newDevice5.size[1]:
                    wpercent = (mysize/float(newDevice5.size[0]))
                    hsize = int((float(newDevice5.size[1])*float(wpercent)))
                    newDevice5 = newDevice5.resize((mysize,hsize), PilImage.ANTIALIAS)
                else:
                    wpercent = (mysize/float(newDevice5.size[1]))
                    hsize = int((float(newDevice5.size[0])*float(wpercent)))
                    newDevice5 = newDevice5.resize((hsize, mysize), PilImage.ANTIALIAS)
            elif GRAPHICSMODE == "PyGame":
                mysize = int(newshield.get_width() / 3.5)
                newDevice2_size = (newDevice2.get_width(),newDevice2.get_height())
                if newDevice2_size[0] > newDevice2_size[1]:
                    wpercent = (mysize/float(newDevice2_size[0]))
                    hsize = int((float(newDevice2_size[1])*float(wpercent)))
                    newDevice2 = pygame.transform.smoothscale(newDevice2, (mysize,hsize))
                else:
                    wpercent = (mysize/float(newDevice2_size[1]))
                    hsize = int((float(newDevice2_size[0])*float(wpercent)))
                    newDevice2 = pygame.transform.smoothscale(newDevice2, (hsize, mysize))

                newDevice3_size = (newDevice3.get_width(),newDevice3.get_height())
                if newDevice3_size[0] > newDevice3_size[1]:
                    wpercent = (mysize/float(newDevice3_size[0]))
                    hsize = int((float(newDevice3_size[1])*float(wpercent)))
                    newDevice3 = pygame.transform.smoothscale(newDevice3, (mysize,hsize))
                else:
                    wpercent = (mysize/float(newDevice2_size[1]))
                    hsize = int((float(newDevice3_size[0])*float(wpercent)))
                    newDevice3 = pygame.transform.smoothscale(newDevice3, (hsize, mysize))

                newDevice4_size = (newDevice4.get_width(),newDevice4.get_height())
                if newDevice4_size[0] > newDevice4_size[1]:
                    wpercent = (mysize/float(newDevice4_size[0]))
                    hsize = int((float(newDevice4_size[1])*float(wpercent)))
                    newDevice4 = pygame.transform.smoothscale(newDevice4, (mysize,hsize))
                else:
                    wpercent = (mysize/float(newDevice4_size[1]))
                    hsize = int((float(newDevice4_size[0])*float(wpercent)))
                    newDevice4 = pygame.transform.smoothscale(newDevice4, (hsize, mysize))

                newDevice5_size = (newDevice5.get_width(),newDevice5.get_height())
                if newDevice5_size[0] > newDevice5_size[1]:
                    wpercent = (mysize/float(newDevice5_size[0]))
                    hsize = int((float(newDevice5_size[1])*float(wpercent)))
                    newDevice5 = pygame.transform.smoothscale(newDevice5, (mysize,hsize))
                else:
                    wpercent = (mysize/float(newDevice5_size[1]))
                    hsize = int((float(newDevice5_size[0])*float(wpercent)))
                    newDevice5 = pygame.transform.smoothscale(newDevice5, (hsize, mysize))


            bg = newshield

            #Heraldically, the quarters are numbered from top left to bottom right:
            # 1,2
            # 3,4
            #When I wrote this bit of code, I numbered the quarters clockwise... oops.
            #Will have to be careful when creating the blazon for these!

            if GRAPHICSMODE == "PIL":
                text_img = PilImage.new('RGBA', newshield.size, (0, 0, 0, 0))
                xCentre = (text_img.width / 2)
                text_img.paste(bg, ((text_img.width - bg.width) // 2, (text_img.height - bg.height) // 2))

                #device #1 (quarter 1)
                ironman = newDevice2
                text_img.paste(ironman, ((xCentre - int(xCentre/2) - (ironman.width/2)), (xCentre - (int(xCentre/2))) - (ironman.height/2)), mask=ironman)
                #device #2 (quarter 2)
                ironman2 = newDevice4
                text_img.paste(ironman2, (xCentre + int(xCentre/2) - (ironman2.width/2), xCentre + (int(xCentre/2)) - (ironman2.height/2)), mask=ironman2)
                #device #3 (quarter 3)
                ironman = newDevice3
                text_img.paste(ironman, (xCentre + int(xCentre/2) - (ironman.width/2), xCentre - (int(xCentre/2)) - (ironman.height/2)), mask=ironman)
                #device #4 (quarter 4)
                ironman2 = newDevice5
                text_img.paste(ironman2, (xCentre - int(xCentre/2) - (ironman2.width/2), xCentre + (int(xCentre/2)) - (ironman2.height/2)), mask=ironman2)

            elif GRAPHICSMODE == "PyGame":
                text_img = pygame.Surface((newshield.get_width(),newshield.get_height()), pygame.SRCALPHA, 32)
                xCentre = (text_img.get_width() / 2)
                text_img.blit(bg, ((text_img.get_width() - bg.get_width()) // 2, (text_img.get_height() - bg.get_height()) // 2))

                #device #1 (quarter 1)
                ironman = newDevice2
                text_img.blit(ironman, ((xCentre - int(xCentre/2) - (ironman.get_width()/2)), (xCentre - (int(xCentre/2))) - (ironman.get_height()/2)), None) # paint to screen

                #device #2 (quarter 2)
                ironman2 = newDevice4
                text_img.blit(ironman2, (xCentre + int(xCentre/2) - (ironman2.get_width()/2), xCentre + (int(xCentre/2)) - (ironman2.get_height()/2)), None) # paint to screen

                #device #3 (quarter 3)
                ironman = newDevice3
                text_img.blit(ironman, (xCentre + int(xCentre/2) - (ironman.get_width()/2), xCentre - (int(xCentre/2)) - (ironman.get_height()/2)), None) # paint to screen

                #device #4 (quarter 4)
                ironman2 = newDevice5
                text_img.blit(ironman2, (xCentre - int(xCentre/2) - (ironman2.get_width()/2), xCentre + (int(xCentre/2)) - (ironman2.get_height()/2)), None) # paint to screen

            #EXAMPLE BLAZON:
            #"""Quarterly, 1st and 4th, Gules a castle Or (Castile), 2nd and 3rd, Argent a lion rampant (Leon) """

            #now finish blazoning it...
            #FIRST QUARTER
            blazon = "%s, 1st" % blazon
            if DeviceDescriptionsDict != None:
                if DeviceDescriptionsDict.has_key(deviceToUse):
                    blazon = "%s %s" % (blazon, DeviceDescriptionsDict[deviceToUse][0])
                else:
                    blazon = "%s %s" % (blazon, guess_description_from_Filename(deviceToUse))
            else:
                blazon = "%s %s" % (blazon, guess_description_from_Filename(deviceToUse))
            if string.find(deviceToUse, "roper") > -1:
                pass # a charge that is 'proper' is in its natural colours
            else:
                blazon = "%s %s" % (blazon, string.capitalize(color2Dict["Name"]))

            #SECOND QUARTER
            blazon = "%s, 2nd" % blazon
            if DeviceDescriptionsDict != None:
                if DeviceDescriptionsDict.has_key(deviceToUse2):
                    blazon = "%s %s" % (blazon, DeviceDescriptionsDict[deviceToUse2][0])
                else:
                    blazon = "%s %s" % (blazon, guess_description_from_Filename(deviceToUse2))
            else:
                blazon = "%s %s" % (blazon, guess_description_from_Filename(deviceToUse2))
            if string.find(deviceToUse2, "roper") > -1:
                pass # a charge that is 'proper' is in its natural colours
            else:
                blazon = "%s %s" % (blazon, string.capitalize(color4Dict["Name"]))

            #THIRD QUARTER
            blazon = "%s, 3rd" % blazon
            if DeviceDescriptionsDict != None:
                if DeviceDescriptionsDict.has_key(deviceToUse4):
                    blazon = "%s %s" % (blazon, DeviceDescriptionsDict[deviceToUse4][0])
                else:
                    blazon = "%s %s" % (blazon, guess_description_from_Filename(deviceToUse4))
            else:
                blazon = "%s %s" % (blazon, guess_description_from_Filename(deviceToUse4))
            if string.find(deviceToUse4, "roper") > -1:
                pass # a charge that is 'proper' is in its natural colours
            else:
                blazon = "%s %s" % (blazon, string.capitalize(color6Dict["Name"]))

            #FOURTH QUARTER
            blazon = "%s, 4th" % blazon
            if DeviceDescriptionsDict != None:
                if DeviceDescriptionsDict.has_key(deviceToUse3):
                    blazon = "%s %s" % (blazon, DeviceDescriptionsDict[deviceToUse3][0])
                else:
                    blazon = "%s %s" % (blazon, guess_description_from_Filename(deviceToUse3))
            else:
                blazon = "%s %s" % (blazon, guess_description_from_Filename(deviceToUse3))
            if string.find(deviceToUse3, "roper") > -1:
                pass # a charge that is 'proper' is in its natural colours
            else:
                blazon = "%s %s" % (blazon, string.capitalize(color5Dict["Name"]))

    os.chdir(ordinariesdir)

    return blazon, text_img



def make_badge(VERBOSE=1, FILENAME="GENERATED_BADGE.png", DeviceDescriptionsDict={}, CreatureDescriptionsDict={},
               OrdinaryDescriptionsDict={}, textfile=None, USESTAINS=1, SAVETOFILE=1, SILENT=0, GRAPHICSMODE="PIL"):

    """Makes a single badge. Needs Description Dictionaries passed in if returned blazons are to be useful.
    Returns a 2-tuple of blazon, badge."""

    TEST = 1

    if USESTAINS == 1:
        var1 = random.choice(("Colour", "Colour", "Colour", "Metal", "Metal", "Stain"))
    else:
        var1 = random.choice(("Colour", "Colour", "Colour", "Metal", "Metal"))
    if var1 == "Metal":
        color1Dict = getMetal()
        color1 = color1Dict["Name"]
        color1name = color1Dict["Colour"]
        color2Dict = getColour()
        color2 = color2Dict["Name"]
        color2name = color2Dict["Colour"]
    elif var1 == "Colour":
        color1Dict = getColour()
        color1 = color1Dict["Name"]
        color1name = color1Dict["Colour"]
        color2Dict = getMetal()
        color2 = color2Dict["Name"]
        color2name = color2Dict["Colour"]
    else:
        color1Dict = getStain()
        color1 = color1Dict["Name"]
        color1name = color1Dict["Colour"]
        color2Dict = getMetal()
        color2 = color2Dict["Name"]
        color2name = color2Dict["Colour"]

    if VERBOSE > 0:
        print
        print "color1:\t%s\t(%s)" % (color1, color1name)
        print "color2:\t%s\t(%s)" % (color2, color2name)

#    if os.path.isdir("game"):
#        os.chdir("game")

##    if string.split(os.getcwd(), os.path.sep)[-1] != "game":
##        if VERBOSE > 0:
##            print "changing directory FROM '%s'" % os.getcwd()
##        while string.split(os.getcwd(), os.path.sep)[-1] != "game":
##            os.chdir("..")
##        if VERBOSE > 0:
##            print "changed directory TO '%s'" % os.getcwd()

    rootdir = os.getcwd()

    # special fiddle for when being run from the Renpy launcher
    if string.find(rootdir, "renpy-6.99.14.3-sdk") > -1:
        #os.chdir("E:\Projects-DISTROS\Random_Heraldry_Generator-%s-win\Random_Heraldry_Generator-%s-win" % (__VERSION__, __VERSION__))
        os.chdir("E:\Projects\NEW RENPY GAME\game")
        rootdir = os.getcwd()

    badgesdir = os.path.join(rootdir, "images", "badges")
    #TEMPDIR = os.path.join(rootdir, "..", "TEMP")
    TEMPDIR = os.path.join(rootdir, "TEMP")

    creaturesdir = os.path.join(badgesdir, "Creatures")
    devicesdir = os.path.join(badgesdir, "Devices")
    #print devicesdir
    ordinariesdir = os.path.join(badgesdir, "Ordinaries")
    shieldsdir = os.path.join(badgesdir, "Shields")

    badgeType = random.choice(("Creature", "Device", "Ordinary", "Quartered"))

    if badgeType == "Creature":
        if VERBOSE > 0:
            print "badgeType: Creature"
        os.chdir(creaturesdir)
        blazon, badge = make_Creature_Badge(color1Dict, color2Dict, VERBOSE, CreatureDescriptionsDict, SILENT, GRAPHICSMODE)
        #will make more use of the blazon later...
        if VERBOSE > 0:
            print "  BLAZON:"
            print "      '%s'" % blazon
    elif badgeType == "Device":
        if VERBOSE > 0:
            print "badgeType: Device"
        os.chdir(devicesdir)
        blazon, badge = make_Device_Badge(color1Dict, color2Dict, VERBOSE, DeviceDescriptionsDict, SILENT, GRAPHICSMODE)
        #will make more use of the blazon later...
        if VERBOSE > 0:
            print "  BLAZON:"
            print "      '%s'" % blazon
    elif badgeType == "Ordinary":
        if VERBOSE > 0:
            print "badgeType: Ordinary"
        os.chdir(ordinariesdir)
        blazon, badge = make_Ordinary_Badge(color1Dict, color2Dict, VERBOSE, OrdinaryDescriptionsDict, SILENT, GRAPHICSMODE)
        #will make more use of the blazon later...
        if VERBOSE > 0:
            print "  BLAZON:"
            print "      '%s'" % blazon
    elif badgeType == "Quartered":
        if VERBOSE > 0:
            print "badgeType: Quartered"
        os.chdir(ordinariesdir)
        blazon, badge = make_Quartered_Badge(color1Dict, color2Dict, VERBOSE, OrdinaryDescriptionsDict,
                                     DeviceDescriptionsDict, SILENT, GRAPHICSMODE)
        if VERBOSE > 0:
            print "  BLAZON:"
            print "      '%s'" % blazon
    if textfile != None:
        if SAVETOFILE == 1:
            textfile.write("%s\n" % FILENAME)
        textfile.write("\t%s\n\n" % blazon)

    if SAVETOFILE == 1:
        if GRAPHICSMODE == "PIL":
            badge.save(os.path.join(TEMPDIR, FILENAME))
            #badge.save(os.path.join(rootdir, "images", "temp", FILENAME))
        elif GRAPHICSMODE == "PyGame":
            pygame.image.save(badge, os.path.join(TEMPDIR, FILENAME))
            #pygame.image.save(badge, os.path.join(rootdir, "images", "temp", FILENAME))
        if VERBOSE > 0:
            print "\twrote file '%s'" % os.path.join(TEMPDIR, FILENAME)
            #print "\twrote file '%s'" % os.path.join(rootdir, "images", "temp", FILENAME)
            print

    os.chdir(rootdir)

    return blazon, badge



def make_badges(num, VERBOSE=1, FILENAME_PREFIX="GENERATED_BADGE_", USESTAINS=1, SILENT=0, GRAPHICSMODE="PIL"):
    """a wrapper for the make_badge function"""

    #get the descriptions (for use in making the blazons)
    DeviceDescriptionsDict, CreatureDescriptionsDict, OrdinaryDescriptionsDict = get_descriptions()

    TEST = 1

#    if os.path.isdir("game"):
#        os.chdir("game")

##    if string.split(os.getcwd(), os.path.sep)[-1] != "game":
##        if VERBOSE > 0:
##            print "changing directory FROM '%s'" % os.getcwd()
##        while string.split(os.getcwd(), os.path.sep)[-1] != "game":
##            os.chdir("..")
##        if VERBOSE > 0:
##            print "changed directory TO '%s'" % os.getcwd()

    #textfile = open(os.path.join(os.getcwd(), "..", "TEMP", "blazon_output.txt"), "w")
    textfile = open(os.path.join(os.getcwd(), "TEMP", "blazon_output.txt"), "w")

    for f in range(0,num):
        if num > 999:
            make_badge(VERBOSE=VERBOSE, FILENAME="%s%.4d.png" % (FILENAME_PREFIX, f+1),
                       DeviceDescriptionsDict=DeviceDescriptionsDict, CreatureDescriptionsDict=CreatureDescriptionsDict,
                       OrdinaryDescriptionsDict=OrdinaryDescriptionsDict,
                       textfile = textfile, USESTAINS=USESTAINS, SILENT=SILENT, GRAPHICSMODE=GRAPHICSMODE)
        else:
            make_badge(VERBOSE=VERBOSE, FILENAME="%s%.3d.png" % (FILENAME_PREFIX, f+1),
                       DeviceDescriptionsDict=DeviceDescriptionsDict, CreatureDescriptionsDict=CreatureDescriptionsDict,
                       OrdinaryDescriptionsDict=OrdinaryDescriptionsDict,
                       textfile = textfile, USESTAINS=USESTAINS, SILENT=SILENT, GRAPHICSMODE=GRAPHICSMODE)
    
    textfile.close()



#--- helper functions, for running from the command line ---

def do_usage():
    """short routine that just prints usage info and quits"""
    progname = sys.argv[0]
    if string.find(progname, os.sep) > -1:
        progname = string.split(sys.argv[0], os.sep)[-1]
    elif string.find(progname, os.altsep) > -1:
        progname = string.split(sys.argv[0], os.altsep)[-1]
    print """
%s (version: %s)

USAGE:

    "-h", "-?", "help", "--help", "h":
        prints this help message
                
    "-v", "--verbose":
        turns on verbose mode (prints useful messages about what the program is doing)

    "-c", "--clean":
        deletes all files from the temporary directory

    "-ns", "--nostain": 
        don't use the stains (non-standard tinctures) of
        Murrey (dark reddish purple), Sanguine (blood red) and Tenné (orange)        

    "-s", "--silent": 
        don't produced any output messages at all        

    n:(a number), n=(a number)
        sets the number of badges to create
    
""" % (progname, __VERSION__)
    sys.exit()


def do_clean(VERBOSE=0):
    """short routine that deletes all files from the temporary output directory"""
    thisdir = os.getcwd()
    tempdir = "TEMP"

    if os.path.isdir(os.path.join(thisdir, "TEMP")):
        tempdir = os.path.join(thisdir, "TEMP")
    elif os.path.isdir(os.path.join(thisdir, "..", "TEMP")):
        tempdir = os.path.join(thisdir, "..", "TEMP")

    if os.path.isdir(tempdir):
        os.chdir(tempdir)
        if VERBOSE > 0:
            print "  cleaning temporary directory '%s'" % tempdir
        filestogo = glob.glob("*.*")
        gonecount = 0
        for fg in filestogo:
            try:
                os.remove(fg)
                gonecount = gonecount +1
            except:
                if VERBOSE > 0:
                    print "  !!! COULDN@T DELETE FILE '%s'" % fg
                else:
                    pass
        if VERBOSE > 0:
            print "  Deleted %s files" % gonecount
            print
    os.chdir(thisdir)

def get_num(arg):
    if string.find(arg, ":") >-1:
        n = string.split(arg, ":")[1]
        try:
            n = int(n)
            num = n
            return n
        except:
            return None
    elif string.find(arg, "=") >-1:
        n = string.split(arg, "=")[1]
        try:
            n = int(n)
            num = n
            return n
        except:
            return None
    else:
        return None


def get_descriptions():
    "get the descriptions (for use in making the blazons)"
    DeviceDescriptionsDict = MakeDeviceDescriptionsDict()
    CreatureDescriptionsDict = MakeCreatureDescriptionsDict()
    OrdinaryDescriptionsDict = MakeOrdinaryDescriptionsDict()
    return DeviceDescriptionsDict, CreatureDescriptionsDict, OrdinaryDescriptionsDict


def test_names():
    #sometimes get the following error:
    #UnicodeDecodeError: 'utf8' codec can't decode byte 0xed in
    #position 7: invalid continuation byte

    SAINTS = [
        "Aaron of Aleth",  "Aaron",  "Abamun of Tarnut",  "Abamun",
        "Adalard of Corbie",  "Adalard",  "Adalbert of Prague",
        "Adalbert",  "Adelaide of Italy",  "Adelaide",  "Afra of Augsburg",
        "Afra",  "Agnes of Montepulciano",  "Agnes of Rome",
        "Agnes",  "Agnes",  "Albert of Sicily",  "Albert",
        "Albertus Magnus",  "Albertus",  "Ame",  "Andrew Corsini",
        "Andrew",  "Anselm of Canterbury",  "Anselm",  "Anthony of Padua",
        "Anthony",  "Antoninus of Florence",  "Antoninus",
        "Aphrodisius",  "Belina",  "Benedict of Nursia",  "Benedict",
        "Benno of Meissen",  "Benno",  "Berard of Carbio",  "Berard",
        "Bernard of Corleone",  "Bernard",  "Bernardino of Siena",
        "Bernardino Realino",  "Bernardino",  "Bernardino",  "Bertrand of Comminges",
        "Bertrand",  "Bonaventure",  "Bononio",
        "Bridget of Sweden",  "Bridget",  "Bruno of Segni",  "Bruno",
        "Casimir",  "Catherine of Bologna",  "Catherine of Genoa",
        "Catherine of Ricci",  "Catherine of Siena",  "Catherine of Sweden",
        "Catherine",  "Catherine",  "Catherine",
        "Catherine",  "Catherine",  "Charles Borromeo",  "Charles",
        "Clare of Assisi",  "Clare",  "Conrad of Constance",  "Conrad of Piacenza",
        "Conrad",  "Conrad",  "Cunigunde of Luxembourg",
        "Cunigunde",  "Edward the Confessor",  "Edward",
        "Elizabeth of Hungary",  "Elizabeth of Portugal",
        "Elizabeth",  "Elizabeth",  "Emma of Lesum",  "Emma",  "Felix of Cantalice",
        "Felix of Valois",  "Felix",  "Felix",
        "Frances of Rome",  "Frances",  "Francis Borgia",  "Francis de Sales",
        "Francis of Assisi",  "Francis of Paola",  "Francis Xavier",
        "Francis",  "Francis",  "Francis",  "Francis",
        "Francis",  "Gerard of Potenza",  "Gerard of Toul",  "Gerard",
        "Gerard",  "Hedwig of Silesia",  "Hedwig",  "Hildebrand of Sovana",
        "Hildebrand",  "Hildegard of Bingen",  "Hildegard",
        "Homobonus of Cremona",  "Homobonus",  "Hugh of Chateauneuf",
        "Hugh of Cluny",  "Hugh of Lincoln",  "Hugh the Great",
        "Hugh",  "Hugh",  "Hugh",  "Hyacinth of Poland",  "Hyacinth",
        "Isidore the Laborer",  "Isidore",  "James of the Marches",
        "James",  "Joan of Arc",  "Joan",  "John of Beverley",
        "John of Capistrano",  "John of God",  "John of Matha",
        "John of Nepomuk",  "John of Sahagun",  "John of the Cross",
        "John Twenge",  "John",  "John",  "John",  "John",  "John",  "John",
        "John",  "John",  "Joseph of Cupertino",  "Joseph",  "Juan de Ribera",
        "Juan Diego",  "Juan",  "Juan",  "Juliana Falconieri",
        "Juliana",  "Kinga of Poland",  "Kinga",
        "Lawrence",  "Lodovico Pavoni",  "Lodovico",  "Louis Bertrand",
        "Louis of Toulouse",  "Louis",  "Louis",
        "Margaret of Cortona",  "Margaret of Scotland",  "Margaret",
        "Margaret",  "Mun",  "Mungo of Glasgow",  "Mungo",  "Nicholas of Tolentino",
        "Nicholas",  "Nicola Pellegrino",  "Nicola",
        "Norbert of Xanten",  "Norbert",  "Osmund",  "Otto of Bamberg",
        "Otto",  "Paschal Baylon",  "Paschal",  "Pedro Armengol",
        "Pedro",  "Peter of Alcantara",  "Peter of Anagni",
        "Peter of Verona",  "Peter",  "Peter",  "Peter",
        "Procopius of Sazava",  "Procopius",  "Raymond Nonnatus",
        "Raymond",  "Romaric",  "Romuald",  "Rose of Lima",  "Rose",
        "Sigfrid of Sweden",  "Sigfrid",  "Stanislaus Kostka",
        "Stanislaus",  "Stephen of Muret",  "Stephen",  "Sturm",
        "Teresa of Avila",  "Teresa",  "Theresa of Portugal",
        "Theresa",  "Thomas Aquinas",  "Thomas Becket",  "Thomas de Cantilupe",
        "Thomas More",  "Thomas of Villanova",  "Thomas",
        "Thomas",  "Thomas",  "Thomas",  "Thomas",  "Ulrich of Augsburg",
        "Ulrich",  "Vergilius of Salzburg",  "Vergilius",
        "Vincent de Paul",  "Vincent Ferrer",  "Vincent",  "Vincent",
        "William of Gellone",  "William of Perth",  "William of Roskilde",
        "William",  "William",  "William",  "Wolfgang of Regensburg",
        "Wolfgang",  "Wulstan",  "Zita of Lucca",
        "Zita",  "Adalbert",  "Adamnan",  "Adelaide",  "Agatha",
        "Agnes",  "Agobard",  "Aidan",  "Aidan",  "Alban",  "Albertus Magnus",
        "Albertus",  "Alexander Nevsky",  "Alexander",
        "Alexis",  "Aloysius Gonzaga",  "Aloysius",  "Ambrose",
        "Andrew of Crete",  "Andrew",  "Andrew",  "Angela Merici",
        "Angela",  "Anne",  "Anselm of Canterbury",  "Anselm",
        "Anthony of Egypt",  "Anthony of Kiev",  "Anthony of Padua",
        "Anthony",  "Anthony",  "Anthony",  "Arsenius the Great",
        "Arsenius",  "Athanasius",  "Augustine of Canterbury",
        "Augustine",  "Augustine",  "Bacchus",  "Barbara",
        "Barnabas",  "Bartholomew",  "Basil the Great",  "Basil",
        "Bede the Venerable",  "Bede",  "Benedict of Nursia",
        "Benedict",  "Benno",  "Bernadette of Lourdes",  "Bernadette",
        "Bernard de Clairvaux",  "Bernard of Menthon",  "Bernard",
        "Bernard",  "Blaise",  "Bonaventure",  "Boniface",  "Brendan",
        "Bridget of Sweden",  "Bridget",  "Brigit of Ireland",
        "Brigit",  "Bruno of Querfurt",  "Bruno the Carthusian",
        "Bruno the Great",  "Bruno",  "Bruno",  "Bruno",  "Catherine of Alexandria",
        "Catherine of Bologna",  "Catherine of Genoa",
        "Catherine of Siena",  "Catherine of Sweden",
        "Catherine",  "Catherine",  "Catherine",  "Catherine",
        "Catherine",  "Catherine",  "Cecilia",  "Chad",
        "Christopher",  "Ciaran of Clonmacnoise",  "Ciaran",  "Clare of Assisi",
        "Clare",  "Clement of Alexandria",  "Clement of Alexandria",
        "Clement",  "Clement",  "Clotilda",  "Colette",
        "Colman of Lindisfarne",  "Colman",  "Columba",  "Columban",
        "Cornelius",  "Cosmas",  "Crispin",  "Cuthbert Mayne",
        "Cuthbert",  "Cuthbert",  "Cyprian",  "Cyprian",
        "Cyril of Alexandria",  "Cyril of Jerusalem",  "Cyril",  "Cyril",
        "Cyril",  "Damian",  "Damien of Molokai",  "Damien of Molokai",
        "Damien",  "Damien",  "David",  "Denis",
        "Deusdedit",  "Dionysius of Alexandria",  "Dionysius",
        "Dioynsius",  "Dominic",  "Dunstan of Canterbury",  "Dunstan",
        "Edmund of Abington",  "Edmund",  "Edward the Confessor",
        "Edward",  "Elizabeth of Hungary",  "Elizabeth of Portugal",
        "Elizabeth",  "Elizabeth",  "Ephraem Syrus",  "Ephraem Syrus",
        "Erasmus",  "Eusebius of Samosata",  "Eusebius of Vercelli",
        "Eusebius",  "Eusebius",  "Eusebius",  "Eustace",
        "Eustathius of Antioch",  "Eustathius of Thessalonica",  "Eustathius",
        "Eustathius",  "Euthymius of Turnovo",  "Euthymius the Great",
        "Euthymius",  "Euthymius",  "Fabian",  "Faustus of Riez",
        "Faustus",  "Felix of Valois",  "Felix",  "Flavian",
        "Frances of Rome",  "Frances",  "Francis Borgia",  "Francis de Sales",
        "Francis of Assisi",  "Francis of Paola",  "Francis of Sales",
        "Francis Xavier",  "Francis",  "Francis",  "Francis",
        "Francis",  "Francis",  "Fulbert of Chartres",  "Fulbert",
        "Fulgentius of Ruspe",  "Fulgentius",  "Gabriel",  "Gaius",
        "Genevieve",  "George",  "Gerard",  "Gerard",
        "Germanus of Paris",  "Germanus",  "Gilbert of Sempringham",  "Gilbert",
        "Gregory of Nyssa",  "Gregory of Tours",  "Gregory Palamas",
        "Gregory Thaumaturgus",  "Gregory the Illuminator",
        "Gregory",  "Gregory",  "Gregory",  "Gregory",  "Gregory",
        "Helena",  "Hilarion",  "Hilary of Arles",
        "Hilary of Poitiers",  "Hilary",  "Hilary",  "Hilary",
        "Hilda of Whitby",  "Hilda",  "Hildegard",  "Hippolytus of Rome",
        "Hippolytus",  "Hugh of Cluny",  "Hugh of Lincoln",
        "Hugh of Lincoln",  "Hugh",  "Hugh",  "Hugh",  "Ignatius of Loyola",
        "Ignatius",  "Isaac Jogues",  "Isaac the Great",  "Isaac",
        "Isaac",  "Isidore of Sevilla",  "Isidore",  "James",
        "James",  "James",  "Jerome",  "Joachim",  "Joan of Arc",
        "Joan",  "John Bosco",  "John Cassian",  "John Eudes",
        "John Leonardi",  "John Neumann",  "John of Avila",
        "John of Beverley",  "John of Capistrano",  "John of Damascus",
        "John of Matha",  "John of the Cross",  "John the Apostle",
        "John the Baptist",  "John the Faster",  "John",  "John",  "John",
        "John",  "John",  "John",  "John",  "John",  "John",  "John",
        "John",  "John",  "John",  "John",  "Joseph of Arimathea",
        "Joseph of Volokolamsk",  "Joseph",  "Joseph",  "Juan Diego",
        "Juan",  "Judas",  "Junipero Serra",  "Junipero",  "Justus",
        "Justus",  "Juvenal",  "Kenneth",  "Kentigern",  "Kevin",
        "Laurentius of Canterbury",  "Laurentius",
        "Lawrence of Brindisi",  "Lawrence",  "Lawrence",  "Linus",
        "Louise de Marillac",  "Louise",  "Lucian of Antioch",  "Lucian",
        "Lucy",  "Ludmila",  "Luke",  "Margaret Clitherow",
        "Margaret of Antioch",  "Margaret of Scotland",  "Margaret",
        "Margaret",  "Margaret",  "Mark",  "Mark",
        "Martin de Porres",  "Martin of Tours",  "Martin",  "Martin",
        "Mary Magdalene",  "Mary of the Incarnation",  "Mary",  "Mary",
        "Mary",  "Matthew",  "Matthias",  "Maurice",
        "Maximus the Confessor",  "Maximus the Greek",  "Maximus",  "Maximus",
        "Methodius",  "Michael",  "Nicholas of Flue",  "Nicholas",
        "Nicholas",  "Nicodemus the Hagiorite",  "Nicodemus",
        "Ninian",  "Norbert of Xanten",  "Norbert",  "Odo of Cluny",
        "Odo",  "Olga",  "Oliver Plunket",  "Oliver",
        "Osmund of Salisbury",  "Osmund",  "Oswald of Northumbria",
        "Oswald of York",  "Oswald",  "Oswald",  "Padre Pio",  "Patrick",
        "Patrick",  "Paul of the Cross",  "Paul of Thebes",  "Paul",
        "Paul",  "Paul",  "Paulinus",  "Pelagia of Antioch",
        "Pelagia",  "Perpetua",  "Peter Claver",  "Peter Martyr",
        "Peter Nolasco",  "Peter of Alcantara",
        "Peter the Venerable",  "Peter",  "Peter",  "Peter",  "Peter",  "Peter",
        "Peter",  "Philip Neri",  "Philip the Apostle",
        "Philip the Evangelist",  "Philip",  "Philip",  "Philip",  "Photius",
        "Polycarp",  "Pontian",  "Quadratus",  "Raphael",
        "Raymond of Penafort",  "Raymond",  "Remigius of Reims",  "Remigius",
        "Richard of Chichester",  "Richard",  "Rose of Lima",  "Rose",
        "Sebastian",  "Sergius",  "Severus of Antioch",  "Severus",
        "Silas",  "Simeon Stylites",  "Simeon",  "Simon the Apostle",
        "Simon",  "Stanislaus of Krakow",  "Stanislaus",
        "Stephen of Perm",  "Stephen",  "Stephen",  "Swithin",
        "Symeon the New Theologian",  "Symeon",  "Teresa of Avila",  "Teresa",
        "Theodore of Canterbury",  "Theodore Studites",  "Theodore",
        "Theodore",  "Theodosius of Palestine",  "Theodosius",
        "Theophanes the Confessor",  "Theophanes",
        "Theophilus of Alexandria",  "Theophilus of Antioch",  "Theophilus",
        "Theophilus",  "Therese of Lisieux",  "Therese",
        "Thomas Aquinas",  "Thomas Becket",  "Thomas More",  "Thomas",
        "Thomas",  "Thomas",  "Thomas",  "Timothy",  "Titus",
        "Ulrich",  "Ursula",  "Valentine",  "Veronica",
        "Vincent Ferrer",  "Vincent of Lerins",  "Vincent",  "Vincent",
        "Vitalian",  "Vladimir",  "Wilfrid",  "Wulfstan",
        "Zephyrinus",  "Zosimus",  "Trinian",  "Custard",  "Lemon",
    ]
   
    FAILCOUNT   = 0
    encoding    = "UTF-8"
    for s in SAINTS:
        try:
            Poss_Saint = unicode(make_possesive(s), encoding)
            print ".",
            if s != unicode(s):
                print "NON-ASCII CHARACTER in '%s'???" % s
        except:
            FAILCOUNT = FAILCOUNT + 1
            print "!"
            print "FAILED ON: '%s'" % s
            print

    print 
    print "%s FAILED NAMES" %  FAILCOUNT
    if FAILCOUNT == 0:
        print "ALL SAINTS NAMES CAN BE ENCODED BY '%s'" % encoding
    else:
        print "%s SAINTS NAMES (of %s) FAIL WHEN ENCODED AS '%s'" % (FAILCOUNT, len(SAINTS), encoding)
    print 

    FAILCOUNT   = 0
    encoding    = "latin-1"
    #encoding    = "UTF-32"
    for s in SAINTS:
        try:
            Poss_Saint = unicode(make_possesive(s), encoding)
            print ".",
        except:
            FAILCOUNT = FAILCOUNT + 1
            #raise
            print "!"
            print "FAILED ON: '%s'" % s
            print

    print 
    print "%s FAILED NAMES" %  FAILCOUNT
    if FAILCOUNT == 0:
        print "ALL SAINTS NAMES CAN BE ENCODED BY '%s'" % encoding
    else:
        print "%s SAINTS NAMES (of %s) FAIL WHEN ENCODED AS '%s'" % (FAILCOUNT, len(SAINTS), encoding)
    print 


        
if __name__ == "__main__":
    print "%s (version: %s)" % (string.split(__file__,"\\")[-1], __VERSION__ )
    print

    if DEBUG == 1:
        test_names()

    VERBOSE = 0
    #VERBOSE = 1
    #num = 50
    num = 1
    USESTAINS = 1
    SILENT = 1
    for arg in sys.argv:
        if arg in ["-h", "-?", "help", "--help", "-help", "h", "?"]:
            do_usage()
        elif arg in ["-v", "--verbose", "-verbose", "v"]:
            VERBOSE = 1
        elif arg in ["-c", "--clean", "-clean", "c"]:
            do_clean(VERBOSE)
        elif arg in ["-ns", "--nostain", "--nostains", "-nostain", "-nostains", "-n"]:
            USESTAINS = 0
        elif arg in ["-s", "s", "--silent"]:
            SILENT = 1
            VERBOSE = 0
        elif arg[0] == "n":
            temp = get_num(arg)
            if temp != None:
                num = temp
        elif arg == sys.argv[0]:
            pass # ignore the program name
        else:
            print "unknown argument '%s'... ignoring..." % arg
                
    name, name_short, name_full, school_type = make_name()
    print "name:", name
    print "name_short:", name_short
    print "name_full:", name_full
    print

    s = School()
    s.VERBOSE=VERBOSE
    s.populate()
    print "s.name:", s.name
    print "s.name_short:", s.name_short
    print "s.name_full:", s.name_full
    print

    print "SAVING SCHOOL DATA TO FILE..."
    fname = s.save()
    print "\twrote file '%s'" % fname
    print "SAVED SCHOOL DATA OK"
    print

    if num == 1:
        if SILENT != 1:
            print "making 1 badge..."
        else:
            pass
    else:
        if SILENT != 1:
            print "making %s badges..." % num
        else:
            pass

    make_badges(num, VERBOSE=VERBOSE, FILENAME_PREFIX="GENERATED_BADGE_", USESTAINS=USESTAINS, SILENT=SILENT, GRAPHICSMODE=GRAPHICSMODE)
    if SILENT != 1:
        print "\nDONE"

