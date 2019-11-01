#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

import random, string

all_offences = [

#https://en.wikipedia.org/wiki/List_of_English_criminal_offences
 
#List of English criminal offences
#From Wikipedia, the free encyclopedia

#This list of English criminal offences is a partial categorisation of
#English criminal law offences.


##Contents
##1	Offences against the person
##2	Offences against property
##3	Firearms and offensive weapons
##4	Forgery, personation and cheating
##5	Offences against the state
##6	Harmful or dangerous drugs
##7	Offences against religion and public worship
##8	Offences against the administration of public justice
##9	Public order offences
##10	Offences against public morals and public policy
##11	Protection of children and vulnerable adults
##12	Protection of animals and the environment
##13	Road traffic and motor vehicle offences
##14	Participatory and inchoate offences
##15	Other
##16	See also
##17	Notes
##18	References

#Offences against the person

#https://en.wikipedia.org/wiki/Offence_against_the_person

#Offence against the person
#From Wikipedia, the free encyclopedia

#Criminal law
#Elements
#Actus reus Mens rea Causation Concurrence
#Scope of criminal liability
#Complicity Corporate Vicarious
#Severity of offense
#Felony Infraction (also called violation) Misdemeanor
#Inchoate offenses
#Attempt Conspiracy Incitement Solicitation

#Offence against the person
    "Assassination",
    "Assault",
    "Battery",
    "Child abuse",
    "Criminal negligence",
    "Defamation",
    "False imprisonment",
    "Harassment",
    "Home invasion",
    "Homicide",
    "Intimidation",
    "Kidnapping",
    "Manslaughter (corporate)",
    "Mayhem",
    "Murder corporate",
    "Negligent homicide",
    "Invasion of privacy",
    "Robbery",
    "Torture",

#Sexual offences
    "Adultery",
    "Bigamy",
    "Fornication",
    "Incest",
    "Indecent exposure",
    "Masturbation",
    "Obscenity",
    "Prostitution",
    "Rape",
    "Sexual assault",
    "Sodomy",

#Crimes against property
    "Arson",
    "Blackmail",
    "Bribery",
    "Burglary",
    "Embezzlement",
    "Extortion",
    "False pretenses",
    "Forgery",
    "Fraud",
    "Gambling",
    "Intellectual property violation",
    "Larceny",
    "Payola",
    "Pickpocketing",
    "Possessing stolen property",
    "Robbery",
    "Smuggling",
    "Tax evasion",
    "Theft",

#Crimes against justice
    #Compounding
    "Malfeasance in office",
    "Miscarriage of justice",
    "Misprision Obstruction",
    "Perjury",
    "Perverting the course of justice",

#Crimes against the public
    "Apostasy",
    "Begging",
    "Censorship violation",
    "Dueling",
    #"Miscegenation",
    #"Illegal consumption (such as prohibition of drugs, alcohol, and smoking)",
    "Illegal consumption",
    "Terrorism",

#Crimes against animals
    "Cruelty to animals",
    "Wildlife smuggling",
    "Bestiality",

#Crimes against the state
    "Lèse-majesté Treason",

#Defences to liability
#Automatism Consent Defence of property Diminished responsibility Duress Entrapment Ignorantia juris non excusat Infancy Insanity Justification Mistake (of law) Necessity Provocation Self-defence
#Other common-law areas
#Contracts Evidence Property Torts Wills, trusts and estates
#Portals
#Criminal justice Law

#In UK criminal law, the term "offence against the person" usually
#refers to a crime which is committed by direct physical harm or force
#being applied to another person.

#They are usually analysed by division into the following categories:

#Fatal offences
#Sexual offences
#Non-fatal non-sexual offences
#They can be further analysed by division into:

#Assaults
#Injuries

#And it is then possible to consider degrees and aggravations, and
#distinguish between intentional actions (e.g., assault) and criminal
#negligence (e.g., criminal endangerment).

#Offences against the person are usually taken to comprise:

#Fatal offences
    "Murder",
    "Manslaughter",

#Non-fatal non-sexual offences
    "Assault",
    "common assault",
    "Battery",
    "common battery",
    "Wounding",
    "wounding with intent",
    "Poisoning",
    "Assault occasioning actual bodily harm",# (and derivative offences)
    "Inflicting grievous bodily harm",
    "Causing grievous bodily harm with intent", # (and derivative offences)

    #The crimes are usually grouped together in common law countries as a
    #legacy of the Offences against the Person Act 1861.

    #Although most sexual offences will also be offences against the
    #person for various reasons (including sentencing and registration
    #of offenders) sexual crimes are usually categorised separately.
    #Similarly, although many homicides also involve an offence against the
    #person, they are usually categorised under the more serious category.

#England and Wales
#Fatal offences
#See also: Homicide in English law

    "Murder",
    "Manslaughter",
    "Corporate manslaughter, contrary to section 1 of the Corporate Manslaughter and Corporate Homicide Act 2007",
    "Infanticide, contrary to section 1(1) of the Infanticide Act 1938",

    #In section 2(2) of the Law Reform (Year and a Day Rule) Act 1996, "fatal offence" means:
    #"murder, manslaughter, infanticide or any other offence of which one of the elements is causing a person's death",
    "an offence under section 2(1) of the Suicide Act 1961 in connection with the death of a person",
    "an offence under section 5 of the Domestic Violence, Crime and Victims Act 2004.",

#Sexual offences
#Main article: Sexual offences in the United Kingdom
#See also: Rape, Sexual abuse, and Rape in English law

#Non-fatal non-sexual offences
#See also: Non-fatal offences against the person in English law
    "Assault",
    "common assault",
    "Battery",
    "common battery",

#For offences of aggravated assault, see Assault#England and Wales

    "Administering poison, so as to endanger life, contrary to section 23 of the Offences against the Person Act 1861",
    "Administering poison, contrary to section 24 of the Offences against the Person Act 1861",
    "Unlawful wounding or inflicting grievous bodily harm, contrary to section 20 of the Offences against the Person Act 1861",
    "Wounding or causing grievous bodily harm with intent, contrary to section 18 of the Offences against the Person Act 1861",

##Visiting Forces Act 1952
##
##The expression "offence against the person" is used as a term of art
##in section 3 of the Visiting Forces Act 1952 (15 & 16 Geo.6 & 1 Eliz.2
##c.67) and is defined for that purpose by paragraphs 1 (England and
##Wales and Northern Ireland) and 2 (Scotland) of the Schedule to that
##Act.
##
##England and Wales and Northern Ireland
##
##In the application of section 3 of the 1952 Act to England and Wales
##and Northern Ireland it means any of the following offences:
##
##murder, manslaughter, torture, robbery and assault and any offence of aiding, abetting, counselling or procuring suicide or an attempt to commit suicide[8]
##any offence not falling within the foregoing bullet point, being an offence punishable under any of the following enactments:
##the Offences against the Person Act 1861, except section 57 (which relates to bigamy)
##the Criminal Law Amendment Act 1885[why?]
##the Punishment of Incest Act 1908[why?]
##sections 1 to 5 and section 11 of the Children and Young Persons Act 1933, and sections 11, 12, 14 to 16, and 21 of the Children and Young Persons Act (Northern Ireland) 1950
##the Infanticide Act 1938 and the Infanticide Act (Northern Ireland) 1939
##article 3(1)(a) of the Protection of Children (Northern Ireland) Order 1978
##section 1(1)(a) of the Protection of Children Act 1978
##the Child Abduction Act 1984
##the Female Genital Mutilation Act 2003[9]
##the Child Abduction (Northern Ireland) Order 1985
##Part 1 of the Sexual Offences Act 2003[10]
##the Sexual Offences (Northern Ireland) Order 2008[11]
##
##an offence of making such a threat as is mentioned in subsection
##(3)(a) of section 1 of the Internationally Protected Persons Act 1978
##and any of the following offences against a protected person within
##the meaning of that section, namely an offence of kidnapping, an
##offence of false imprisonment and an offence under section 2 of the
##Explosive Substances Act 1883 of causing an explosion likely to
##endanger life
##
##an offence under section 2 of the Nuclear Material (Offences) Act
##1983, where the circumstances are that either in the case of a
##contravention of subsection (2), the act falling within paragraph (a)
##or (b) of that subsection, had it been done, would have constituted an
##offence falling within sub-paragraph (a) or (b) of this paragraph, or
##in the case of a contravention of subsection (3) or (4), the act
##threatened, had it been done, would have constituted such an offence
##
##an offence of making such a threat as is mentioned in section 3 of the
##United Nations Personnel Act 1997 and any of the following offences
##against a UN worker within the meaning of that Act kidnapping false
##imprisonment an offence under section 2 of the Explosive Substances
##Act 1883 of causing an explosion likely to endanger life This list is
##incomplete; you can help by expanding it. It formerly included in
##particular:
##
##rape and buggery[10][12] (presumably including at common law)
##offences of rape and buggery under the law of Northern Ireland[10][13]
##offences punishable under
##section 89 of the Mental Health Act (Northern Ireland) 1948 (which related to certain offences against mentally defective females)[13]
##sections 2 to 28 of the Sexual Offences Act 1956[12]
##section 1 of the Prohibition of Female Circumcision Act 1985[9]
##Scotland
##
##In the application of section 3 of the 1952 Act to Scotland, the
##expression "offence against the person" means any of the following
##offences:
##
##murder, culpable homicide, rape, torture, robbery, assault, incest, sodomy, lewd, indecent and libidinous practices, procuring abortion, abduction, cruel and unnatural treatment of persons, threats to murder or to injure persons
##
##any offence not falling within the last bullet point, being an offence
##punishable under any of the following enactments:
##
##the Criminal Law Amendment Act 1885
##
##section 46 of the Mental Deficiency and Lunacy (Scotland) Act 1913
##(which relates to certain offences against mentally defective females)
##
##sections 12 to 16 and 22 of the Children and Young Persons (Scotland) Act 1937
##
##section 52(1)(a) of the Civic Government (Scotland) Act 1982
##
##an offence of making such a threat as is mentioned in subsection
##(3)(a) of section 1 of the Internationally Protected Persons Act 1978
##and the following offence against a protected person within the
##meaning of that section, namely, an offence under section 2 of the
##Explosive Substances Act 1883 of causing an explosion likely to
##endanger life
##
##an offence under section 2 of the Nuclear Material (Offences) Act
##1983, where the circumstances are that either, in the case of a
##contravention of subsection (2), the act falling within paragraph (a)
##or (b) of that subsection, had it been done, would have constituted an
##offence falling within sub-paragraph (a) or (b) of this paragraph, or,
##in the case of a contravention of subsection (3) or (4), the act
##threatened, had it been done, would have constituted such an offence
##
##an offence of making such a threat as is mentioned in section 3 of the
##United Nations Personnel Act 1997 and an offence of causing an
##explosion likely to endanger life, committed against a UN worker
##(within the meaning of that Act), under section 2 of the Explosive
##Substances Act 1883
##
##See also
##Offences Against the Person Act
##
##Classes of crimes	
##Common law Indictable Either way Summary Regulatory Lesser included
##Elements of crimes	
##Actus reus Causation Mens rea Intention (criminal law) Intention in English law Recklessness Criminal negligence Corporate / Vicarious / Strict liability Omissions Concurrence Ignorantia juris non excusat
##Inchoate offences	
##Encouraging or assisting a crime Conspiracy Accessory Attempt Common purpose
##Defences	
##Self-defence Duress Necessity Marital coercion Consent Medical procedure Prevention of crime Participation in a sporting event Lawful excuse Insanity Diminished responsibility Intoxication Category:Criminal defences

#Offences against the person	

    "Homicide",
    "Murder",
    "Manslaughter",
    "Corporate manslaughter",
    "Infanticide",
    "Unlawful killing",
    "Mayhem",
    "Concealing birth",
    "Child destruction",
    "Wounding or causing grievous bodily harm",
    "Assault occasioning actual bodily harm",
    "Common assault",
    "Attempting to choke, &c. in order to commit any indictable offence",
    "Assault with intent to rob",
    "Robbery",
    "Assault with intent to rape",
    "Assault with intent to resist lawful apprehension",
    "Buggery",
    "Battery",
    "Kidnapping",
    "Child abduction",
    "False imprisonment",
    "Harassment",
    #"Offences Against the Person Act 1861",

#Sexual offences	
    "Rape",
    "Sexual assault",
    #"Sexual Offences Act 2003",

#Public order offences	
    "Riot",
    "Violent disorder",
    "Affray",
    "Unlawful assembly",
    "Fear or provocation of violence",
    "Intentional harassment, alarm or distress",
    "Harassment, alarm or distress",
    #"Public Order Act 1986",
    "Incitement to ethnic or racial hatred",
    "Challenging to a fight",
    "Nuisance",
    "Causing Public nuisance",
    "Outraging public decency",
    "Effecting a public mischief",
    "Keeping a disorderly house",
    "Preventing the lawful burial of a body",
    "Breach of the peace",
    "Treason",
    "High treason",
#    "Common scold",
#    "Nightwalker statute",
    "Rout",
    "Forcible entry",
    #"Accessory (legal term)",
    "Misconduct in a public office",
    "Misfeasance in public office",
    "Abuse of authority",
    "Perjury of oath",
    "Dereliction of duty",

#Offences against property
    "Arson",
    "Dishonesty",
    "Cheating",
    "Burglary",
    "Robbery",
    "Theft",
    "Larceny",
    "Criminal damage",
    "Squatting",
    "Trespass",
    "Taking without owner's consent",
    "Deception",
    "Handling stolen goods",
    "Misappropriation of funds",
    "Blackmail",
    "Extortion",
    "Cybercrime",
    #"Theft Act 1968",
    #"Theft Act 1978",
    #"Fraud Act 2006",
    "Fraud by abuse of position",
    "Conspiracy to defraud",
    "Fare evasion",
    "Webcam blackmail",

#Forgery, personation and cheating	
    "Forgery",
    "Cheating the public revenue",
    "Uttering",

#Offences against justice	
    "Bribery",
    "Perjury",
    "Perverting the course of justice",
    "Embracery",
    "Witness intimidation",
    "Witness tampering",
    "Misprision of treason",
    "Misprision of felony",
    "Compounding a felony",
    "Jury tampering",
    "Assault with intent to resist lawful apprehension",
    "Harboring a fugitive",
    "Encouraging or assisting a crime",
    "Escape from lawful custody",
    "Obstruction of justice",
    "Obstruction of a police officer",
    "Wasting police time",
    "Refusing to assist a constable",
    "Sedition",
    "Espionage",
    "Contempt of the sovereign",
    "Contempt of court",
    "Fabrication of false evidence",
    "Breach of prison",
    "Breaking prison",
    "Rescuing a prisoner",

#Other common law areas	
#Contract Tort Property Wills Trusts and estates Evidence Criminal procedure

#This page was last edited on 14 June 2019, at 01:15 (UTC).
#
#Text is available under the Creative Commons Attribution-ShareAlike
#License; additional terms may apply. By using this site, you agree to
#the Terms of Use and Privacy Policy. 


#Main article: Offence against the person

#Offences against property
#Main articles: Property crime,
#Theft in English law,
#Robbery in English law, and
#Criminal Damage in English law
#See also: Burglary

    "Offences under the Explosive Substances Act 1883",
    "Offences under the Computer Misuse Act 1990",


#Firearms and offensive weapons
#See also: Gun law, Gun politics in the United Kingdom, and Offensive weapon

    "Offences under section 1(1) of the Prevention of Crime Act 1953",
    "Offences under sections 139 and 139A of the Criminal Justice Act 1988",
    "Offences under the Knives Act 1997",


#Forgery, personation and cheating
#See forgery:

    "Offences under Part I of the Forgery and Counterfeiting Act 1981",
    "Falsification of pedigree, contrary to section 183(1)(b) of the Law of Property Act 1925",
    "Improper alteration of the registers, contrary to section 124 of the Land Registration Act 2002",
    "Offences under section 8 of the Non-Parochial Registers Act 1840",
    "Offences under sections 36 and 37 of the Forgery Act 1861",
    "Forgery of passport, contrary to section 36 of the Criminal Justice Act 1925",
    "Offences under sections 133 and 135 of the County Courts Act 1984",
    "Offences under section 13 of the Stamp Duties Management Act 1891; and supplementary offences under sections 14 and 15",
    "Offences under section 6 of the Hallmarking Act 1973",
    "Offences under section 126 of the Mental Health Act 1983",
    "Offences under sections 121 and 122(6) of the Gun Barrel Proof Act 1868",

#Motor vehicle document offences:

    "Offences under section 97AA and 99(5) of the Transport Act 1968",
    "Offences under section 65 of the Public Passenger Vehicles Act 1981",
    "Offences under section 115 of the Road Traffic Regulation Act 1984",
    "Offences under section 173 of the Road Traffic Act 1988",
    "Offences under regulations 11(1) to (3) of the Motor Vehicles (E.C. Type Approval) Regulations 1992 (S.I. 1992/3107) made under section 2(2) of the European Communities Act 1972",
    "Offences under section 44 of the Vehicles Excise and Registration Act 1994",
    "Offences under regulations 10(1) to (3) the Motor Cycle (E.C. Type Approval) Regulations 1995 (S.I. 1995/1531) made under section 2(2) of the European Communities Act 1972",
    "Offences under section 38 of the Goods Vehicles (Licensing of Operators) Act 1995",

#See personation:
    "Personation of a juror",
    "Offences under section 90(1) of the Police Act 1996",
    "Offences under section 30(1) of the Commissioners for Revenue and Customs Act 2005",
    "Offences under section 34 of the Forgery Act 1861",
    "Offences under section 24 of the Family Law Reform Act 1969",
    "Offences under section 60 of the Representation of the People Act 1983",

#See cheating:
    "Offences under section 17 of the Gaming Act 1845",
    "Offences under section 1 of the Fraudulent Mediums Act 1951",

#Offences against the state
    "High treason",
    "Misprision of treason",
    "Compounding treason",
    "Treason felony",
    "Attempting to injure or alarm the Sovereign, contrary to section 2 of the Treason Act 1842",
    "Contempt of the sovereign",
    "Trading with the enemy",
    "Offences under the Official Secrets Acts 1911 to 1989",
    "Offences under the Incitement to Disaffection Act 1934",
    "Causing disaffection, contrary to section 91 of the Police Act 1996",
    "Causing disaffection, contrary to section 6 of the Ministry of Defence Police Act 1987",
    "Incitement to sedition or disaffection or promoting industrial unrest, contrary to section 3 of the Aliens Restriction (Amendment) Act 1919",
    "Offences of procuring and assisting desertion under military law",
    "Offences relating to terrorism",
    "Offences of directing quasi military organisations and wearing uniforms for political purposes under the Public Order Act 1936",
    "Piracy iure gentium",
    "Piracy with violence, contrary to the Piracy Act 1837",
    "Offences under the Slave Trade Act 1824",
    "Offences under the Foreign Enlistment Act 1870",
    "Offences under the Immigration Act 1971",
    "Coinage offences under Part II of the Forgery and Counterfeiting Act 1981",
    "Offences relating to public stores under the Public Stores Act 1875",
    "Offences relating to military stores under military law",
    "Offences against postal and electronic communication services",
    "Misconduct in public office",
    "Refusal to execute public office",
    "Offences of selling public offices under the Sale of Offices Act 1551 and Sale of Offices Act 1809",
    "Purchasing the office of clerk of the peace or under-sheriff, contrary to section 27 of the Sheriffs Act 1887",
    "Cheating the public revenue",
    "Offences under the Customs and Excise Management Act 1979",
    "Tax evasion and money laundering offences",

#See also Offences against military law in the United Kingdom

#Harmful or dangerous drugs
    "Offences under the Misuse of Drugs Act 1971, the Intoxicating Substances (Supply) Act 1985, the Licensing Act 2003, section 7 of the Children and Young Persons Act 1933 and other provisions relating to tobacco, and the Drug Trafficking Act 1994.",
    "Offences under the Psychoactive Substances Act 2016.",
    "Offences against religion and public worship",
    "Offences under sections 75 to 77 of the Marriage Act 1949",
    "Offences of disturbing public worship",

    "Offences under section 2 of the Ecclesiastical Courts Jurisdiction Act 1860",
    "Offences under section 7 of the Burial Laws Amendment Act 1880",
    "Offences under section 59 of the Cemeteries Clauses Act 1847",
    "Offences under articles 18 and 19 of the Local Authorities' Cemeteries Order 1977 (SI 1977/204)",
    "Offences against the administration of public justice",
    "Doing an act tending and intended to pervert the course of public justice - a.k.a. perverting the course of justice, defeating the ends of justice, obstructing the administration of justice",
    "Concealing evidence, contrary to section 5(1) of the Criminal Law Act 1967",
    "Contempt of court a.k.a. criminal contempt",
    "Intimidation, contrary to section 51(1) of the Criminal Justice and Public Order Act 1994",
    "Taking or threatening to take revenge, contrary to section 51(2) of the Criminal Justice and Public Order Act 1994",
    "Perjury, contrary to section 1 of the Perjury Act 1911",
    "Perjury, contrary to section 6 of the Piracy Act 1850",
    "Offences under sections 2 to 4 of the Perjury Act 1911",
    "Making a false statutory declaration, contrary to section 5 of the Perjury Act 1911",
    "Offences under section 6 of the Perjury Act 1911",
    "Fabrication of false evidence",
    "Offences under section 89 of the Criminal Justice Act 1967",
    "Offences under 106 of the Magistrates' Courts Act 1980",
    "Offences under section 11(1) of the European Communities Act 1972",
    #Escape
    #Permitting an escape
    "Assisting a prisoner to escape, contrary to section 39 of the Prison Act 1952",
    "Breach of prison/breaking prison",
    "Rescue/rescuing a prisoner in custody",
    "Harbouring an escaped prisoner, contrary to section 22(2) of the Prison Act 1952",
    "Taking part in a prison mutiny, contrary to section 1(1) of the Prison Security Act 1992",
    "Offences under section 128 of the Mental Health Act 1983",
    "Causing a wasteful employment of the police, contrary to section 5(2) of the Criminal Law Act 1967",
    "Administering an unlawful oath, contrary to section 13 of the Statutory Declarations Act 1835",

#Public order offences
    "Offences under the Public Order Act 1986",
    "Offences under section 31 of the Crime and Disorder Act 1998",
    "Offences under Part V of the Criminal Justice and Public Order Act 1994",
    "Offences under Part II of the Criminal Law Act 1977",
    "Offences under the Protection from Eviction Act 1977",
    "Bomb hoaxes, contrary to section 51 of the Criminal Law Act 1977",

#Offences against public morals and public policy
    "Bigamy, contrary to section 57 of the Offences against the Person Act 1861",
    #See also: Obscenity and Indecency
    "Offences under section 2(1) of the Obscene Publications Act 1959",
    "Offences under section 2(2) of the Theatres Act 1968",
    "Certain offences under the Postal Services Act 2000",
    "Offences under section 1(1) of the Indecent Displays (Control) Act 1981",
    "Offences under section 1(1) of the Protection of Children Act 1978",
    "Offences under section 160 of the Criminal Justice Act 1988",
    "Offences under section 170 of the Customs and Excise Management Act 1979 consisting of importation in breach of the prohibition under section 42 of the Customs Consolidation Act 1876",
    "Offences under the Bribery Act 2010",

#Protection of children and vulnerable adults

#Protection of animals and the environment
#See Cruelty to animals#United Kingdom and Environmental crime

#Road traffic and motor vehicle offences
#Main article: United Kingdom traffic laws

#Participatory and inchoate offences
#See also: Accomplice, Aid and abet, Inchoate offenses, and Inchoate offences in English law
#Encouraging or assisting crime - Part 2 of the Serious Crime Act 2007
    "Soliciting to murder, contrary to section 4 of the Offences against the Person Act 1861",
    #Aiding, abetting, counselling or procuring the commission of an offence
    "Conspiracy, contrary to section 1(1) of the Criminal Law Act 1977",
    "Conspiracy to defraud",
    "Conspiracy to corrupt public morals",
    "Conspiracy to outrage public decency",
    "Attempt, contrary to section 1(1) of the Criminal Attempts Act 1981",

#Parts 1 to 3 of Schedule 3 to the Serious Crime Act 2007 list numerous
#statutory offences of assisting, encouraging, inciting, attempting or
#conspiring at the commission of various crimes.

#Other
#See also: History of English criminal law § Common law offences
    "Mayhem",
    "Kidnapping",
    "False imprisonment",
    "Cheating the public revenue",
    "High treason",
    #"Misprision of treason (disputed - alleged to be statutory)",
    "Compounding treason",
    "Contempt of the sovereign",
    "Misconduct in public office",
    "Refusal to execute public office",
    "Doing an act tending and intended to pervert the course of public justice", # a.k.a. perverting the course of justice, defeating the ends of justice, obstructing the administration of justice",
    "Contempt of court", # a.k.a. criminal contempt",
    "Fabrication of false evidence",
    "Escape",
    "Permitting an escape",
    "Breach of prison/breaking prison",
    "Rescue/rescuing a prisoner in custody",
    "Public nuisance",
    "Outraging public decency",
    "Conspiracy to defraud",
    "Conspiracy to corrupt public morals",
    "Conspiracy to outrage public decency",
    "Common assault", #aka assault (disputed - held to now be statutory, said obiter not to be)
    "battery", #(disputed - held to now be statutory, said obiter not to be)
    "Assault with intent to rob", #(may now be statutory)
    "Rape",
    "Assault with intent to rape", #(continued existence disputed)

#See also
#English criminal law

#This page was last edited on 14 June 2019, at 02:30 (UTC).
#Text is available under the Creative Commons Attribution-ShareAlike
#License; additional terms may apply. By using this site, you agree to
#the Terms of Use and Privacy Policy.

]


#These offnces are 'safe' to use in the unrestricted game - no sexual offences included. 

safe_offences = [

#https://en.wikipedia.org/wiki/List_of_English_criminal_offences
 
#List of English criminal offences
#From Wikipedia, the free encyclopedia

#This list of English criminal offences is a partial categorisation of
#English criminal law offences.


##Contents
##1	Offences against the person
##2	Offences against property
##3	Firearms and offensive weapons
##4	Forgery, personation and cheating
##5	Offences against the state
##6	Harmful or dangerous drugs
##7	Offences against religion and public worship
##8	Offences against the administration of public justice
##9	Public order offences
##10	Offences against public morals and public policy
##11	Protection of children and vulnerable adults
##12	Protection of animals and the environment
##13	Road traffic and motor vehicle offences
##14	Participatory and inchoate offences
##15	Other
##16	See also
##17	Notes
##18	References

#Offences against the person

#https://en.wikipedia.org/wiki/Offence_against_the_person

#Offence against the person
#From Wikipedia, the free encyclopedia

#Criminal law
#Elements
#Actus reus Mens rea Causation Concurrence
#Scope of criminal liability
#Complicity Corporate Vicarious
#Severity of offense
#Felony Infraction (also called violation) Misdemeanor
#Inchoate offenses
#Attempt Conspiracy Incitement Solicitation

#Offence against the person
#    "Assassination",
    "Assault",
    "Battery",
#    "Child abuse",
    "Criminal negligence",
    "Defamation",
    "False imprisonment",
    "Harassment",
    "Home invasion",
#    "Homicide",
    "Intimidation",
    "Kidnapping",
    "Manslaughter (corporate)",
    "Mayhem",
#    "Murder corporate",
    "Negligent homicide",
    "Invasion of privacy",
    "Robbery",
#    "Torture",

#Sexual offences
#    "Adultery",
#    "Bigamy",
#    "Fornication",
#    "Incest",
    "Indecent exposure",
#    "Masturbation",
    "Obscenity",
#    "Prostitution",
#    "Rape",
#    "Sexual assault",
#    "Sodomy",

#Crimes against property
    "Arson",
    "Blackmail",
    "Bribery",
    "Burglary",
    "Embezzlement",
    "Extortion",
    "False pretenses",
    "Forgery",
    "Fraud",
    "Gambling",
    "Intellectual property violation",
    "Larceny",
    "Payola",
    "Pickpocketing",
    "Possessing stolen property",
    "Robbery",
    "Smuggling",
    "Tax evasion",
    "Theft",

#Crimes against justice
    #Compounding
    "Malfeasance in office",
    "Miscarriage of justice",
    "Misprision Obstruction",
    "Perjury",
    "Perverting the course of justice",

#Crimes against the public
    "Apostasy",
    "Begging",
    "Censorship violation",
    "Dueling",
    #"Miscegenation",
    #"Illegal consumption (such as prohibition of drugs, alcohol, and smoking)",
    "Illegal consumption",
    "Terrorism",

#Crimes against animals
    "Cruelty to animals",
    "Wildlife smuggling",
    #"Bestiality",

#Crimes against the state
    "Lèse-majesté Treason",

#Defences to liability
#Automatism Consent Defence of property Diminished responsibility Duress Entrapment Ignorantia juris non excusat Infancy Insanity Justification Mistake (of law) Necessity Provocation Self-defence
#Other common-law areas
#Contracts Evidence Property Torts Wills, trusts and estates
#Portals
#Criminal justice Law

#In UK criminal law, the term "offence against the person" usually
#refers to a crime which is committed by direct physical harm or force
#being applied to another person.

#They are usually analysed by division into the following categories:

#Fatal offences
#Sexual offences
#Non-fatal non-sexual offences
#They can be further analysed by division into:

#Assaults
#Injuries

#And it is then possible to consider degrees and aggravations, and
#distinguish between intentional actions (e.g., assault) and criminal
#negligence (e.g., criminal endangerment).

#Offences against the person are usually taken to comprise:

#Fatal offences
    #"Murder",
    "Manslaughter",

#Non-fatal non-sexual offences
    "Assault",
    "common assault",
    "Battery",
    "common battery",
    "Wounding",
    "wounding with intent",
    "Poisoning",
    "Assault occasioning actual bodily harm",# (and derivative offences)
    "Inflicting grievous bodily harm",
    "Causing grievous bodily harm with intent", # (and derivative offences)

    #The crimes are usually grouped together in common law countries as a
    #legacy of the Offences against the Person Act 1861.

    #Although most sexual offences will also be offences against the
    #person for various reasons (including sentencing and registration
    #of offenders) sexual crimes are usually categorised separately.
    #Similarly, although many homicides also involve an offence against the
    #person, they are usually categorised under the more serious category.

#England and Wales
#Fatal offences
#See also: Homicide in English law

    #"Murder",
    "Manslaughter",
    "Corporate manslaughter, contrary to section 1 of the Corporate Manslaughter and Corporate Homicide Act 2007",
    #"Infanticide, contrary to section 1(1) of the Infanticide Act 1938",

    #In section 2(2) of the Law Reform (Year and a Day Rule) Act 1996, "fatal offence" means:
    #"murder, manslaughter, infanticide or any other offence of which one of the elements is causing a person's death",
    "an offence under section 2(1) of the Suicide Act 1961 in connection with the death of a person",
    "an offence under section 5 of the Domestic Violence, Crime and Victims Act 2004.",

#Sexual offences
#Main article: Sexual offences in the United Kingdom
#See also: Rape, Sexual abuse, and Rape in English law

#Non-fatal non-sexual offences
#See also: Non-fatal offences against the person in English law
    "Assault",
    "common assault",
    "Battery",
    "common battery",

#For offences of aggravated assault, see Assault#England and Wales

    "Administering poison, so as to endanger life, contrary to section 23 of the Offences against the Person Act 1861",
    "Administering poison, contrary to section 24 of the Offences against the Person Act 1861",
    "Unlawful wounding or inflicting grievous bodily harm, contrary to section 20 of the Offences against the Person Act 1861",
    "Wounding or causing grievous bodily harm with intent, contrary to section 18 of the Offences against the Person Act 1861",

##Visiting Forces Act 1952
##
##The expression "offence against the person" is used as a term of art
##in section 3 of the Visiting Forces Act 1952 (15 & 16 Geo.6 & 1 Eliz.2
##c.67) and is defined for that purpose by paragraphs 1 (England and
##Wales and Northern Ireland) and 2 (Scotland) of the Schedule to that
##Act.
##
##England and Wales and Northern Ireland
##
##In the application of section 3 of the 1952 Act to England and Wales
##and Northern Ireland it means any of the following offences:
##
##murder, manslaughter, torture, robbery and assault and any offence of aiding, abetting, counselling or procuring suicide or an attempt to commit suicide[8]
##any offence not falling within the foregoing bullet point, being an offence punishable under any of the following enactments:
##the Offences against the Person Act 1861, except section 57 (which relates to bigamy)
##the Criminal Law Amendment Act 1885[why?]
##the Punishment of Incest Act 1908[why?]
##sections 1 to 5 and section 11 of the Children and Young Persons Act 1933, and sections 11, 12, 14 to 16, and 21 of the Children and Young Persons Act (Northern Ireland) 1950
##the Infanticide Act 1938 and the Infanticide Act (Northern Ireland) 1939
##article 3(1)(a) of the Protection of Children (Northern Ireland) Order 1978
##section 1(1)(a) of the Protection of Children Act 1978
##the Child Abduction Act 1984
##the Female Genital Mutilation Act 2003[9]
##the Child Abduction (Northern Ireland) Order 1985
##Part 1 of the Sexual Offences Act 2003[10]
##the Sexual Offences (Northern Ireland) Order 2008[11]
##
##an offence of making such a threat as is mentioned in subsection
##(3)(a) of section 1 of the Internationally Protected Persons Act 1978
##and any of the following offences against a protected person within
##the meaning of that section, namely an offence of kidnapping, an
##offence of false imprisonment and an offence under section 2 of the
##Explosive Substances Act 1883 of causing an explosion likely to
##endanger life
##
##an offence under section 2 of the Nuclear Material (Offences) Act
##1983, where the circumstances are that either in the case of a
##contravention of subsection (2), the act falling within paragraph (a)
##or (b) of that subsection, had it been done, would have constituted an
##offence falling within sub-paragraph (a) or (b) of this paragraph, or
##in the case of a contravention of subsection (3) or (4), the act
##threatened, had it been done, would have constituted such an offence
##
##an offence of making such a threat as is mentioned in section 3 of the
##United Nations Personnel Act 1997 and any of the following offences
##against a UN worker within the meaning of that Act kidnapping false
##imprisonment an offence under section 2 of the Explosive Substances
##Act 1883 of causing an explosion likely to endanger life This list is
##incomplete; you can help by expanding it. It formerly included in
##particular:
##
##rape and buggery[10][12] (presumably including at common law)
##offences of rape and buggery under the law of Northern Ireland[10][13]
##offences punishable under
##section 89 of the Mental Health Act (Northern Ireland) 1948 (which related to certain offences against mentally defective females)[13]
##sections 2 to 28 of the Sexual Offences Act 1956[12]
##section 1 of the Prohibition of Female Circumcision Act 1985[9]
##Scotland
##
##In the application of section 3 of the 1952 Act to Scotland, the
##expression "offence against the person" means any of the following
##offences:
##
##murder, culpable homicide, rape, torture, robbery, assault, incest, sodomy, lewd, indecent and libidinous practices, procuring abortion, abduction, cruel and unnatural treatment of persons, threats to murder or to injure persons
##
##any offence not falling within the last bullet point, being an offence
##punishable under any of the following enactments:
##
##the Criminal Law Amendment Act 1885
##
##section 46 of the Mental Deficiency and Lunacy (Scotland) Act 1913
##(which relates to certain offences against mentally defective females)
##
##sections 12 to 16 and 22 of the Children and Young Persons (Scotland) Act 1937
##
##section 52(1)(a) of the Civic Government (Scotland) Act 1982
##
##an offence of making such a threat as is mentioned in subsection
##(3)(a) of section 1 of the Internationally Protected Persons Act 1978
##and the following offence against a protected person within the
##meaning of that section, namely, an offence under section 2 of the
##Explosive Substances Act 1883 of causing an explosion likely to
##endanger life
##
##an offence under section 2 of the Nuclear Material (Offences) Act
##1983, where the circumstances are that either, in the case of a
##contravention of subsection (2), the act falling within paragraph (a)
##or (b) of that subsection, had it been done, would have constituted an
##offence falling within sub-paragraph (a) or (b) of this paragraph, or,
##in the case of a contravention of subsection (3) or (4), the act
##threatened, had it been done, would have constituted such an offence
##
##an offence of making such a threat as is mentioned in section 3 of the
##United Nations Personnel Act 1997 and an offence of causing an
##explosion likely to endanger life, committed against a UN worker
##(within the meaning of that Act), under section 2 of the Explosive
##Substances Act 1883
##
##See also
##Offences Against the Person Act
##
##Classes of crimes	
##Common law Indictable Either way Summary Regulatory Lesser included
##Elements of crimes	
##Actus reus Causation Mens rea Intention (criminal law) Intention in English law Recklessness Criminal negligence Corporate / Vicarious / Strict liability Omissions Concurrence Ignorantia juris non excusat
##Inchoate offences	
##Encouraging or assisting a crime Conspiracy Accessory Attempt Common purpose
##Defences	
##Self-defence Duress Necessity Marital coercion Consent Medical procedure Prevention of crime Participation in a sporting event Lawful excuse Insanity Diminished responsibility Intoxication Category:Criminal defences

#Offences against the person	
    "Homicide",
    #"Murder",
    "Manslaughter",
    "Corporate manslaughter",
    #"Infanticide",
    "Unlawful killing",
    "Mayhem",
    #"Concealing birth",
    #"Child destruction",
    "Wounding or causing grievous bodily harm",
    "Assault occasioning actual bodily harm",
    "Common assault",
    "Attempting to choke, &c. in order to commit any indictable offence",
    "Assault with intent to rob",
    "Robbery",
    #"Assault with intent to rape",
    "Assault with intent to resist lawful apprehension",
    #"Buggery",
    "Battery",
    "Kidnapping",
    #"Child abduction",
    "False imprisonment",
    "Harassment",
    #"Offences Against the Person Act 1861",

#Sexual offences	
    #"Rape",
    #"Sexual assault",
    #"Sexual Offences Act 2003",

#Public order offences	
    "Riot",
    "Violent disorder",
    "Affray",
    "Unlawful assembly",
    "Fear or provocation of violence",
    "Intentional harassment, alarm or distress",
    "Harassment, alarm or distress",
    #"Public Order Act 1986",
    #"Incitement to ethnic or racial hatred",
    "Challenging to a fight",
    "Nuisance",
    "Causing Public nuisance",
    "Outraging public decency",
    "Effecting a public mischief",
    "Keeping a disorderly house",
    "Preventing the lawful burial of a body",
    "Breach of the peace",
    "Treason",
    "High treason",
    #"Common scold",
    #"Nightwalker statute",
    "Rout",
    "Forcible entry",
    #"Accessory (legal term)",
    "Misconduct in a public office",
    "Misfeasance in public office",
    "Abuse of authority",
    "Perjury of oath",
    "Dereliction of duty",

#Offences against property	
    "Arson",
    "Dishonesty",
    "Cheating",
    "Burglary",
    "Robbery",
    "Theft",
    "Larceny",
    "Criminal damage",
    "Squatting",
    "Trespass",
    "Taking without owner's consent",
    "Deception",
    "Handling stolen goods",
    "Misappropriation of funds",
    "Blackmail",
    "Extortion",
    #"Cybercrime Theft Act 1968 Theft Act 1978 Fraud Act 2006",
    "Fraud by abuse of position",
    "Conspiracy to defraud",
    "Fare evasion",
    "Webcam blackmail",
#Forgery, personation and cheating	
    "Forgery",
    "Cheating the public revenue",
    "Uttering",

#Offences against justice	
    "Bribery",
    "Perjury",
    "Perverting the course of justice",
    "Embracery",
    "Witness intimidation",
    "Witness tampering",
    "Misprision of treason",
    "Misprision of felony",
    "Compounding a felony",
    "Jury tampering",
    "Assault with intent to resist lawful apprehension",
    "Harboring a fugitive",
    "Encouraging or assisting a crime",
    "Escape from lawful custody",
    "Obstruction of justice",
    "Obstruction of a police officer",
    "Wasting police time",
    "Refusing to assist a constable",
    "Sedition",
    "Espionage",
    "Contempt of the sovereign",
    "Contempt of court",
    "Fabrication of false evidence",
    "Breach of prison",
    "Breaking prison",
    "Rescuing a prisoner",

#Other common law areas	
#Contract Tort Property Wills Trusts and estates Evidence Criminal procedure

#This page was last edited on 14 June 2019, at 01:15 (UTC).
#
#Text is available under the Creative Commons Attribution-ShareAlike
#License; additional terms may apply. By using this site, you agree to
#the Terms of Use and Privacy Policy. 


#Main article: Offence against the person

#Offences against property
#Main articles: Property crime,
#Theft in English law,
#Robbery in English law, and
#Criminal Damage in English law
#See also: Burglary

    "Offences under the Explosive Substances Act 1883",
    "Offences under the Computer Misuse Act 1990",


#Firearms and offensive weapons
#See also: Gun law, Gun politics in the United Kingdom, and Offensive weapon

    "Offences under section 1(1) of the Prevention of Crime Act 1953",
    "Offences under sections 139 and 139A of the Criminal Justice Act 1988",
    "Offences under the Knives Act 1997",


#Forgery, personation and cheating
#See forgery:

    "Offences under Part I of the Forgery and Counterfeiting Act 1981",
    "Falsification of pedigree, contrary to section 183(1)(b) of the Law of Property Act 1925",
    "Improper alteration of the registers, contrary to section 124 of the Land Registration Act 2002",
    "Offences under section 8 of the Non-Parochial Registers Act 1840",
    "Offences under sections 36 and 37 of the Forgery Act 1861",
    "Forgery of passport, contrary to section 36 of the Criminal Justice Act 1925",
    "Offences under sections 133 and 135 of the County Courts Act 1984",
    "Offences under section 13 of the Stamp Duties Management Act 1891; and supplementary offences under sections 14 and 15",
    "Offences under section 6 of the Hallmarking Act 1973",
    "Offences under section 126 of the Mental Health Act 1983",
    "Offences under sections 121 and 122(6) of the Gun Barrel Proof Act 1868",

#Motor vehicle document offences:

    "Offences under section 97AA and 99(5) of the Transport Act 1968",
    "Offences under section 65 of the Public Passenger Vehicles Act 1981",
    "Offences under section 115 of the Road Traffic Regulation Act 1984",
    "Offences under section 173 of the Road Traffic Act 1988",
    "Offences under regulations 11(1) to (3) of the Motor Vehicles (E.C. Type Approval) Regulations 1992 (S.I. 1992/3107) made under section 2(2) of the European Communities Act 1972",
    "Offences under section 44 of the Vehicles Excise and Registration Act 1994",
    "Offences under regulations 10(1) to (3) the Motor Cycle (E.C. Type Approval) Regulations 1995 (S.I. 1995/1531) made under section 2(2) of the European Communities Act 1972",
    "Offences under section 38 of the Goods Vehicles (Licensing of Operators) Act 1995",

#See personation:
    "Personation of a juror",
    "Offences under section 90(1) of the Police Act 1996",
    "Offences under section 30(1) of the Commissioners for Revenue and Customs Act 2005",
    "Offences under section 34 of the Forgery Act 1861",
    "Offences under section 24 of the Family Law Reform Act 1969",
    "Offences under section 60 of the Representation of the People Act 1983",

#See cheating:
    "Offences under section 17 of the Gaming Act 1845",
    "Offences under section 1 of the Fraudulent Mediums Act 1951",

#Offences against the state
    "High treason",
    "Misprision of treason",
    "Compounding treason",
    "Treason felony",
    "Attempting to injure or alarm the Sovereign, contrary to section 2 of the Treason Act 1842",
    "Contempt of the sovereign",
    "Trading with the enemy",
    "Offences under the Official Secrets Acts 1911 to 1989",
    "Offences under the Incitement to Disaffection Act 1934",
    "Causing disaffection, contrary to section 91 of the Police Act 1996",
    "Causing disaffection, contrary to section 6 of the Ministry of Defence Police Act 1987",
    "Incitement to sedition or disaffection or promoting industrial unrest, contrary to section 3 of the Aliens Restriction (Amendment) Act 1919",
    "Offences of procuring and assisting desertion under military law",
    "Offences relating to terrorism",
    "Offences of directing quasi military organisations and wearing uniforms for political purposes under the Public Order Act 1936",
    "Piracy iure gentium",
    "Piracy with violence, contrary to the Piracy Act 1837",
    "Offences under the Slave Trade Act 1824",
    "Offences under the Foreign Enlistment Act 1870",
    "Offences under the Immigration Act 1971",
    "Coinage offences under Part II of the Forgery and Counterfeiting Act 1981",
    "Offences relating to public stores under the Public Stores Act 1875",
    "Offences relating to military stores under military law",
    "Offences against postal and electronic communication services",
    "Misconduct in public office",
    "Refusal to execute public office",
    "Offences of selling public offices under the Sale of Offices Act 1551 and Sale of Offices Act 1809",
    "Purchasing the office of clerk of the peace or under-sheriff, contrary to section 27 of the Sheriffs Act 1887",
    "Cheating the public revenue",
    "Offences under the Customs and Excise Management Act 1979",
    "Tax evasion and money laundering offences",

#See also Offences against military law in the United Kingdom

#Harmful or dangerous drugs
    "Offences under the Misuse of Drugs Act 1971, the Intoxicating Substances (Supply) Act 1985, the Licensing Act 2003, section 7 of the Children and Young Persons Act 1933 and other provisions relating to tobacco, and the Drug Trafficking Act 1994.",
    "Offences under the Psychoactive Substances Act 2016.",
    "Offences against religion and public worship",
    "Offences under sections 75 to 77 of the Marriage Act 1949",
    "Offences of disturbing public worship",

    "Offences under section 2 of the Ecclesiastical Courts Jurisdiction Act 1860",
    "Offences under section 7 of the Burial Laws Amendment Act 1880",
    "Offences under section 59 of the Cemeteries Clauses Act 1847",
    "Offences under articles 18 and 19 of the Local Authorities' Cemeteries Order 1977 (SI 1977/204)",
    "Offences against the administration of public justice",
    "Doing an act tending and intended to pervert the course of public justice - a.k.a. perverting the course of justice, defeating the ends of justice, obstructing the administration of justice",
    "Concealing evidence, contrary to section 5(1) of the Criminal Law Act 1967",
    "Contempt of court a.k.a. criminal contempt",
    "Intimidation, contrary to section 51(1) of the Criminal Justice and Public Order Act 1994",
    "Taking or threatening to take revenge, contrary to section 51(2) of the Criminal Justice and Public Order Act 1994",
    "Perjury, contrary to section 1 of the Perjury Act 1911",
    "Perjury, contrary to section 6 of the Piracy Act 1850",
    "Offences under sections 2 to 4 of the Perjury Act 1911",
    "Making a false statutory declaration, contrary to section 5 of the Perjury Act 1911",
    "Offences under section 6 of the Perjury Act 1911",
    "Fabrication of false evidence",
    "Offences under section 89 of the Criminal Justice Act 1967",
    "Offences under 106 of the Magistrates' Courts Act 1980",
    "Offences under section 11(1) of the European Communities Act 1972",
    #Escape
    #Permitting an escape
    "Assisting a prisoner to escape, contrary to section 39 of the Prison Act 1952",
    "Breach of prison/breaking prison",
    "Rescue/rescuing a prisoner in custody",
    "Harbouring an escaped prisoner, contrary to section 22(2) of the Prison Act 1952",
    "Taking part in a prison mutiny, contrary to section 1(1) of the Prison Security Act 1992",
    "Offences under section 128 of the Mental Health Act 1983",
    "Causing a wasteful employment of the police, contrary to section 5(2) of the Criminal Law Act 1967",
    "Administering an unlawful oath, contrary to section 13 of the Statutory Declarations Act 1835",

#Public order offences
    "Offences under the Public Order Act 1986",
    "Offences under section 31 of the Crime and Disorder Act 1998",
    "Offences under Part V of the Criminal Justice and Public Order Act 1994",
    "Offences under Part II of the Criminal Law Act 1977",
    "Offences under the Protection from Eviction Act 1977",
    "Bomb hoaxes, contrary to section 51 of the Criminal Law Act 1977",

#Offences against public morals and public policy
    "Bigamy, contrary to section 57 of the Offences against the Person Act 1861",
    #See also: Obscenity and Indecency
    "Offences under section 2(1) of the Obscene Publications Act 1959",
    "Offences under section 2(2) of the Theatres Act 1968",
    "Certain offences under the Postal Services Act 2000",
    "Offences under section 1(1) of the Indecent Displays (Control) Act 1981",
    "Offences under section 1(1) of the Protection of Children Act 1978",
    "Offences under section 160 of the Criminal Justice Act 1988",
    "Offences under section 170 of the Customs and Excise Management Act 1979 consisting of importation in breach of the prohibition under section 42 of the Customs Consolidation Act 1876",
    "Offences under the Bribery Act 2010",

#Protection of children and vulnerable adults

#Protection of animals and the environment
#See Cruelty to animals#United Kingdom and Environmental crime

#Road traffic and motor vehicle offences
#Main article: United Kingdom traffic laws

#Participatory and inchoate offences
#See also: Accomplice, Aid and abet, Inchoate offenses, and Inchoate offences in English law
#Encouraging or assisting crime - Part 2 of the Serious Crime Act 2007
    "Soliciting to murder, contrary to section 4 of the Offences against the Person Act 1861",
    #Aiding, abetting, counselling or procuring the commission of an offence
    "Conspiracy, contrary to section 1(1) of the Criminal Law Act 1977",
    "Conspiracy to defraud",
    "Conspiracy to corrupt public morals",
    "Conspiracy to outrage public decency",
    "Attempt, contrary to section 1(1) of the Criminal Attempts Act 1981",

#Parts 1 to 3 of Schedule 3 to the Serious Crime Act 2007 list numerous
#statutory offences of assisting, encouraging, inciting, attempting or
#conspiring at the commission of various crimes.

#Other
#See also: History of English criminal law § Common law offences
    "Mayhem",
    "Kidnapping",
    "False imprisonment",
    "Cheating the public revenue",
    "High treason",
    #"Misprision of treason (disputed - alleged to be statutory)",
    "Compounding treason",
    "Contempt of the sovereign",
    "Misconduct in public office",
    "Refusal to execute public office",
    "Doing an act tending and intended to pervert the course of public justice", # a.k.a. perverting the course of justice, defeating the ends of justice, obstructing the administration of justice",
    "Contempt of court", # a.k.a. criminal contempt",
    "Fabrication of false evidence",
    "Escape",
    "Permitting an escape",
    "Breach of prison/breaking prison",
    "Rescue/rescuing a prisoner in custody",
    "Public nuisance",
    "Outraging public decency",
    "Conspiracy to defraud",
    "Conspiracy to corrupt public morals",
    "Conspiracy to outrage public decency",
    "Common assault", #aka assault (disputed - held to now be statutory, said obiter not to be)
    "battery", #(disputed - held to now be statutory, said obiter not to be)
    "Assault with intent to rob", #(may now be statutory)
    #"Rape",
    #"Assault with intent to rape", #(continued existence disputed)

#See also
#English criminal law

#This page was last edited on 14 June 2019, at 02:30 (UTC).
#Text is available under the Creative Commons Attribution-ShareAlike
#License; additional terms may apply. By using this site, you agree to
#the Terms of Use and Privacy Policy.

]

ADULTMODE = 1

if ADULTMODE == 1:
    offences = all_offences
    #print "Safemode OFF"
else:
    offences = safe_offences
    #print "Safemode ON"


if __name__ == "__main__":
    numcrimes = random.choice(range(1,5))
    charges = ""
    posscrimes = offences
    for f in range(0, numcrimes):
        crim = string.strip(random.choice(posscrimes))
        while crim in ["", None, ","]:
            crim = string.strip(random.choice(posscrimes))
        crim2 = string.replace(crim, ".", "")
        if f == 0:
            charges = "%s" % (crim2)
        elif f == numcrimes-1:
            charges = "%s, and %s. " % (charges, crim2)
        else:
            charges = "%s, %s" % (charges, crim2)
        if crim in posscrimes:
            posscrimes.remove(crim)

    print "%s has been charged with %s" % (random.choice(("He", "She")), charges)
    print

