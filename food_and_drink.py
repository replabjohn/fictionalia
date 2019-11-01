#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

#food_and_drink.py

__VERSION__ = "0.0.2b"

import random, os, string

TEST = 0



class FastFoodJoint:
    def __init__(self):
        self.name               = None
        self.menu               = None
        self.internal_menu_type         = None
        self.internal_counter_type      = None
        self.internal_counter_image     = None
        self.internal_background_type   = None
        self.internal_background_type   = None
        self.external_brick_type        = None
        self.external_brick_image       = None

        self.customers		= []
        self.staff		= []

    def populate(self):
        exterior_dir = "exteriors"

        self.name = make_fast_food_joint_name()
        self.menu = make_random_menu()
        self.menu_type = random.choice(("light", "dark"))
        self.external_brick_type = random.choice(("Type 01",
                                                  "Type 02",
                                                  "Type 03",
                                                  "Type 04",
                                                  "Type 05",
                                                  "Type 06",
                                                  "Type 07"
                                                  ))

	#The interior view...
	#FAST_FOOD_JOINT_TEST_RENDER_000

	#The exterior view...
        if self.external_brick_type == "Type 01":
            self.external_brick_image = "%s/Houses_Bricks_01_X3.png" % (exterior_dir)

        elif self.external_brick_type == "Type 02":
            self.external_brick_image = "%s/Houses_Bricks_02_X3.png" % (exterior_dir)

        elif self.external_brick_type == "Type 03":
            self.external_brick_image = "%s/Houses_Bricks_03_X3.png" % (exterior_dir)

        elif self.external_brick_type == "Type 04":
            self.external_brick_image = "%s/Houses_Bricks_04_X3.png" % (exterior_dir)

        elif self.external_brick_type == "Type 05":
            self.external_brick_image = "%s/Houses_Bricks_05_X3.png" % (exterior_dir)

        elif self.external_brick_type == "Type 06":
            self.external_brick_image = "%s/Houses_Bricks_06_X3.png" % (exterior_dir)

        elif self.external_brick_type == "Type 07":
            self.external_brick_image = "%s/Houses_Bricks_07_X3.png" % (exterior_dir)


    def add_customer(self,person):
        self.customers.append(person)

    def add_staff(self,person):
        self.staff.append(person)


    def __repr__(self):
        outstring = ""
        for k,v in self.__dict__.iteritems():
            outstring = "%s\n\t%s\t:\t%s\n" % (outstring, k,v)
        return outstring


meaty_pizza_toppings = [
    "bacon",
    "BBQ pulled pork",
    "beef",
    "Canadian bacon",
    "chicken",
    "ham and mushroom",
    "ham and olives",
    "ham and pineapple",
    "ham",
    "meatballs",
    "pepperoni",
    "salami",
    "sausage"#,
    ]

vegetarian_pizza_toppings = [
    "artichoke",
    "basil",
    "black olives",
    "caramelised onions",
    "crushed red pepper",
    "garlic",
    "green bell pepper",
    "green olives",
    "green peppers",
    "jalapenos",
    "mushrooms",
    "olives",
    "onions",
    "pineapple",
    "red bell pepper",
    "red onion",
    "spinach",
    "sun-dried tomatoes",
    "sweetcorn",
    "tomato"#,
    ]

pizza_toppings = [

    #https://www.google.com/amp/s/www.huffpost.com/entry/popular-pizza-toppings_n_4261085/amp
    #The Top 10 Most Popular Pizza Toppings 
    #After analyzing pizza orders from thousands of restaurants in the
    #United States and Canada, Foodler says the top 10 pizza toppings are
    #as follows:
    "pepperoni",
    "mushroom",
    "onions",
    "sausage",
    "bacon",
    "extra cheese",
    "black olives",
    "green peppers",
    "pineapple",
    "spinach",

    #https://www.google.com/amp/s/www.papajohns.co.uk/blog/uks-10-popular-pizza-toppings/amp/
    #The UK's 10 Most Popular Pizza Toppings
    #A 2017 survey by YouGovÂ has definitively established which pizza toppings the UK loves the most. 
    "mushrooms",
    "onions",
    "ham",
    "ham and pineapple",
    "ham and mushroom",
    "ham and olives",
    "pepperoni",
    "pineapple",
    "sweetcorn",
    "tomato",
    "jalapenos",
    "spinach",
    "anchovies",
    "tuna",
    "beef",
    "olives",

    #https://m.ranker.com/list/the-tastiest-pizza-toppings/chef-jen?page=2
    #The Tastiest Pizza Toppings

    #A list of the most delicious pizza topping ideas, ranked and voted on
    #by the pizza lovers of the Internet. What are the best pizza toppings?
    #Among the most popular pizza toppings are pepperoni, olives,
    #mushrooms, and tomatoes. Those tend to be the pizza varieties that
    #appeal to the widest array of taste buds, but that doesn't necessarily
    #mean they're the best.
    "pepperoni",
    "mozzarella",
    "mushroom",
    "bacon",
    "onion",
    "garlic",
    "sausage",
    "crushed red pepper",
    #"Tomato",
    "basil",
    "black olives",
    "pineapple",
    "ham",
    "green bell pepper",
    "Canadian bacon",
    "red onion",
    "chicken",
    "buffalo mozzarella",
    "jalapeno",
    "spinach",
    "salami",
    "red bell pepper",
    "meatballs",
    "feta cheese",
    "sun-dried tomatoes",
    "green olives",
    "caramelised onions",
    "beef",
    "BBQ pulled pork",
    "artichoke",
    "anchovy",
    "sweetcorn",
    "egg",
    "tuna"#,
    ]


fast_food_menu_items = [
    "Burgers",
    "Chicken",
    "Vegetarian Options",
    "Hot Drinks",
    "Cold Drinks",
    "Sides"
    ]


cold_drinks =   ["Cola/Diet Cola",
                 "Lemonade/Diet Lemonade",
                 "Apple Juice",
                 "Orange Juice",
                 "Mineral Water",
                 "Milkshake (Chocolate, Strawberry, Vanilla)",
                 #"Banana Milkshake",
                 "Fruit Smoothie",
                 "Iced Latte",
                 "Iced Caramel Popcorn Latte",
                 "Mocha Iced Frappe",
                 "Caramel Iced Frappe",
                 "Caramel Popcorn Frappe"
                 ]    

hot_drinks  =   [

    #COFFEE
    "Black Coffee",
    "White Coffee",
    "Latte",
    "Latte Macchiato",
    "Toffee Latte",
    "Hot Caramel Popcorn Latte",
    "Caramel Macchiato",
    "Cappuccino",
    "Americano",
    "Flat White",
    "Cortado",
    "Espresso",
    "Espresso Con Panna",
    "Espresso Macchiato",
    "Caffe Mocha",
    "White Chocolate Mocha",

    #TEA
    "Tea",
    "Tea (English Breakfast Tea/Earl Grey Tea)",
    "Herbal Tea (Chamomile, Mint, Jasmine, Chai, Rooibos, Green Tea)",

    #OTHER
    "Hot Chocolate"
    ]

standard_burgers = [
    "Hamburger",
    "Classic Cheeseburger"#,
    ]

vegetarian_options = [
    "Side Salad",
    "Vegan Tofuburger",
    "Turnip Burger",
    "Vegetable Wrap",
    "Avocado Toast",
    "Baked Potato",
    "Sour Cream Baked Potato",
    "Vegan Burger",
    "Superfood Side Salad",
    "Veggie Delight",
    "Fried Zucchini Burger",
    "Plomeek Soup"
    ]

random_burgers = [
    "Big Kahuna Burger",
    "Big Chungus Burger",
    "Double Meat Patty",
    "MRM Spineburger",
    "Pink Slimeburger",
    "Little Mac",
    "Disappointing Cheeseburger",
    "Chungus Burger",
    "Little Chungus Burger",
    "Chungus McBungus",
    "Spam Burger",
    "Star Spangled Burger",
    "Unhealthy Burger",
    "Double Quarter Pounder With Cheese",
    "Kobe Burger",
    "Pretzel Bacon Cheeseburger",
    "Double Grilled Cheese Burger",
    "Buffalo Burger",
    "Zebra Burger",
    "Emu Burger",
    "Meatatarian Burger",
    "Quarter Pounder Deluxe",
    "The Original Double 'n Cheese Steakburger",
    "Mac 'n' Cheese Burger",
    "Zombie Burger",
    "Green Chile Double Cheeseburger",
    "Meat-gasm",
    "Meat-o-geddon",
    "Kangaroo Burger",
    "Spam, Spam and Spam",
    "Spam, Spam, Spam, Spam, Chips and Spam",
    "Full Meaty",
    "Half Meaty",
    "Bacon Meaty"#,
    ]

random_chicken = [
    "Pickle Fried Chicken",
    "Citrus Grilled Chicken Sandwich",
    "Monterey Chicken",
    "Crispy Cheese Chicken",
    "Crispy Chicken Chips",
    "Chicken Tenders",
    "The Best Chicken Tenders You've Ever Had",
    "Buffalo Chicken Wings",
    "Triple Decker Chicken Sandwich",
    "Crispy Chicken",
    "Grilled Chicken",
    ]

random_hotdogs = [
    "Hot Dog"
    "Mac & Cheese Dog",
    "Chilli Dog",
    #"",
    #"",
    ]

standard_sides = [
    "French Fries",
    "Onion Rings",
    ]

random_sides = [
    "Cheesy Bites",
    "Pretzel Chicken Fries",
    "Loaded Chorizo Fries",
    "Pumpkin Spice French Fries",
    "Chocolate-covered Fries",
    "Duck Fat Fries",
    "Chili Cheese Fries",
    "Home Fries",
    "Fully-loaded Fries",
    "Bacon-infused Cheesy Fries",
    "Cheesy Fries",
    "Chicken Tenders",
    "Mozzarella Sticks",
    "Chili",
    "Coleslaw",
    "Hot Dog Bites",
    ]

def make_random_menu():
    ffmi = fast_food_menu_items[:]

    final_menu = "MENU"

    for x in range(0, len(fast_food_menu_items)):
        this_section = random.choice(ffmi)
        ffmi.remove(this_section)
        this_section2 = string.upper(this_section)
        final_menu = "%s\n\n%s" % (final_menu, this_section2)
        if this_section == "Burgers":
            for b in standard_burgers:
                final_menu = "%s\n%s" % (final_menu, b)
            rb = random_burgers[:]
            for f in range(0, len(random_burgers)/2):
                b = random.choice(rb)
                rb.remove(b)
                final_menu = "%s\n%s" % (final_menu, b)
        elif this_section == "Chicken":
            rc = random_chicken[:]
            for f in range(0, len(random_chicken)/2):
                b = random.choice(rc)
                rc.remove(b)
                final_menu = "%s\n%s" % (final_menu, b)
        elif this_section == "Vegetarian Options":
            vo = vegetarian_options[:]
            for f in range(0, len(vegetarian_options)/2):
                b = random.choice(vo)
                vo.remove(b)
                final_menu = "%s\n%s" % (final_menu, b)
        elif this_section == "Hot Drinks":
            hd = hot_drinks[:]
            for f in range(0, len(hot_drinks)/2):
                b = random.choice(hd)
                hd.remove(b)
                final_menu = "%s\n%s" % (final_menu, b)
        elif this_section == "Cold Drinks":
            cd = cold_drinks[:]
            for f in range(0, len(cold_drinks)/2):
                b = random.choice(cd)
                cd.remove(b)
                final_menu = "%s\n%s" % (final_menu, b)

        elif this_section == "Sides":
            for b in standard_sides:
                final_menu = "%s\n%s" % (final_menu, b)
            rs = random_sides[:]
            for f in range(0, len(random_sides)/2):
                b = random.choice(rs)
                rs.remove(b)
                final_menu = "%s\n%s" % (final_menu, b)

    return final_menu

    
IGNORE_ME= """
Randomly Generated Menu
Items Include 
Whatter?

Bacon Ranch Monster Taco
Beefy Fritos Burrito
(Dave's) (Massive) Tripple patty (Burger) (Special)
The Jasperiser 
Mini Bacon Quesadilla 



China Dry Pork And Seaweed (Burger)

Bacon, Macaroni And Cheese Toastie
Crayfish Seafood Deluxe
black pepper-mixed beef patty 




s, , and chicken nuggets

classic cheeseburger on a sesame seed bun 

Meaty Breakfast Burrito

tiny egg wrap

Honey Mustard & Chipotle Barbecue Snack Wraps



Chef Lou's Famous Idaho Ice Cream Potato

pork tenderloin sandwich

Roast Beef Sandwich

The fillings can include, but are not limited to, french fries,
chicken tenders, mozzarella sticks, cheesesteak meat, Italian sausage,
marinara sauce, ranch dressing, and onion rings


PICKLE RICK!


Illegal Burrito

Pepperoni & Cheese Potato from the Potato Place


Pastrami & Cheese from Primanti Bros.


Chicken Grilled Burrito from Taco John's


cheeseburger or a hot dog or a sausage

Cheddar Rounds from Pal's Sudden Service

Hash brown bites with real cheddar cheese inside. Yum!

43. Texas â Trailer Park Tacos from Torchy's Tacos

You can't go wrong with a fried chicken taco.



45. Vermont â The Georgia Burger from Beansie's Bus

instagram.com
Bacon cheeseburger on a glazed doughnut!

âAmy K.

46. Virginia â The Greg Brady from Jack Brown's Beer and Burger Joint

yelp.com
It's topped with mac 'n' cheese and barbecue potato chips. Enough said.

âlizs4da0ab953

47. West Virginia â The Duke from Tudor's Biscuit World

You can get just about anything you can think of on a biscuit there. America!


48. Washington â SW Ranch Taco Burger from Miner's Drive-In Restaurant

Their burgers are bigger than your whole head!


49. Wisconsin â Cheese Curds from Dairy Queen

You can get cheese curds just about anywhere in Wisconsin, from Culver's to Dairy Queen!


50. And Wyoming â Super Potato OlÃ©s from Taco John's

This is about as crazy as fast food gets out here!



15 Fast Food Items So Disgusting Theyâre Amazing
Gregory Austin Gregory Austin
2 years ago

Burgers

Over the past few years, youâve likely noticed a particular trend
regarding the online fast food conversation. This trend involves
reviewers, bloggers and opinionated unknowns across the country who
single out the most âoutside the boxâ menu items and proceed to
trash them for being disgusting.

When dissected, this practice is simply an easy attack on the lowest
of hanging fruits. When you step into a fast food restaurant (or some
select sit-down dining establishments), you know what youâre getting
into. Youâre basically signing an invisible contract allowing the
proprietors to fill your belly with portions of questionable nutrition
and, in return, youâre spared from having to cook and from spending
a lot of money.

So, when you turn around and blast cheap food joints for serving you
something that isnât the pinnacle of wholesome goodness, youâre
kind of breaking an unwritten trust. Fast food isnât supposed to be
good for you, you numbskulls!

However, after stripping aside your fabricated air of supremacy, you
just might realize how amazing these unique menu choices can be.
Hereâs a list of a 15 amazing anomalies and what makes them great.

15. Double Down (KFC):

KFC Double Down

The Double Down is the granddaddy of food weâre supposed to be
horrified by. Even though it has only been around since 2010, there
are more scathing online reviews about this sandwich than there are
about marine life species (which, by the way, is estimated at over 2
million of them).

But whatâs so bad about it, really? If youâre walking into a KFC,
youâre probably thinking about getting fried chicken, right? Well,
the Double Down is two pieces of chicken wrapped around bacon. It
comes with sauce and two types of cheese. So, youâre getting what
you came for (probably less, considering KFCâs smallest meal is
comprised of eight pieces), plus a few extras. And, you avoid the
extra bread carbs and you donât have to worry about those pesky
bones.

14. Hot Dog Bites Pizza (Pizza Hut):

Pizza Hut

Pizza Hut isn't anybodyâs favorite pizza joint, unless of course,
you live on a secluded military base or in certain parts of rural
Nebraska where there are no other options within a 50-mile radius. But
Pizza Hut keeps their lights on by offering hot, cheap, passable
pizza. So, why not hot dogs on a pizza?

Besides, this hot dog pizza only exists because of public demand. Not
direct demand, obviously; who would ask for hot dogs on a pizza? But
the mega-minds at Pizza Hut corporate arenât interested in giving
you the pizza you want, but rather the pizza you need.

Since Pizza Hut gave the world the Stuffed Crust pizza in 1995, the
next 20 years were exclusively spent on figuring out what else could
be added to crust. And up until this pie, the best pizza scientists
came up with was pepperoni. So, if youâve ever eaten even the
tiniest slice of Stuffed Crust pizza, you indirectly supported the
eventual making of this delicacy known as Hot Dog Bites Pizza.

13. Halloween Whopper (Burger King):

Black Whopper

Disliking the black-bunned Halloween Whopper is just silly. If you
enjoy the traditional Whopper, you should be perfectly fine with the
Halloween Whopper because itâs the exact same sandwich, only a shade
darker. If the unnaturally shaded bun isnât aesthetically pleasing
to you, you can simply close your eyes while biting into your meal and
youâll never know the difference.

And if youâre concerned about the rumor going around that
verdant-colored fecal matter may occur after consuming a Halloween
Whopper, please know, the rumor is indeed 100% true. But hey; so what,
who cares? It is Halloween, after all.

12. 3-Point Bloominâ Onion (Outback):

Bloomin' Onion

While not technically a fast food restaurant, Outback Steakhouseâs
3-Point Bloominâ Onion earned its place on this list the same way
those 64 teams earned a spot in the NCAA college basketball
tournament. This appetizer made it through sheer persistence.

Now, some people would say a deep fried Bloominâ Onion is already a
gigantic appetizer and should never be consumed immediately before a
full steak and two fixings anyway. But those naysayers probably never
considered loading that massive onion with 
and bite-sized sirloin tips. And thatâs probably because those
people either hate steak, or freedom, or the invisible hand of the
capitalist market. Because this baby is certain to net Outback a cool
mint.

11. Spicy Sriracha Burger (Jack in the Box):

Spicy Sriracha Burger

A wise man once said: âIf you canât get a burger loaded with
Sriracha, then that burger ainât getting got!â I never got that
wise manâs name, but he was standing in front of me at Jack in the
Box and after he ordered two Spicy Sriracha Burgers with a large fry
and coke, I decided to order the exact same thing. Funny story, I was
initially there just to ask for directions to the Convention Center.
Anyway, upon leaving the restaurant, I saw that same man doing nitrous
shots out of a half dozen cans of whipped cream. It was at that point
I realized he might not be such a wise man after all. Those Spicy
Sriracha Burgers were delicious, though.

10. Whopper Poutine/Poutine a la Burger (Burger King):

BK Beef Poutine

In most Canadian Burger Kings you can get a side of poutine, which if
youâre unfamiliar, consists of regular fries smothered in cheese
curds and gravy. But for a while back in 2014-15 (at select locations)
you could get a chopped up Whopper sprinkled atop your already
delicious poutine treat. And back in 2014-15, times were good.

So why did BKCA abruptly end this delightful delicacy? Because of
negative backlash on the internet, thatâs why. People claimed it had
too many calories, too much fat and waaaaaay too much sodium. When did
whiners on the internet turn this world into a nanny state? Also, when
will other people realize that the sane citizens of this planet enjoy
eating things they like on top of other things they like?

9. Hula Burger (McDonaldâs):

Hula Burger

Hereâs one from the way-back machine. The Hula Burger was introduced
by Ray Kroc (yes, the Ray Kroc) in the 1960s in order to please
Catholics on Fridays, during lent. It was a simple design: a big olâ
slice of pineapple and two half slices of cheese on a bun. It didnât
last long because its alternative, the Filet oâ Fish, proved to be
far more popular even though it only came with one half slice of
cheese.  If you ever worked at McDonaldâs youâll know that at the
end of the day this meant throwing out a ton of wasted half slices of
cheese. Also, about 20 pounds of dehydrated onions, which has nothing
to do with the Hula Burger or Filet oâ Fish, but is still quite
wasteful.

8. 3Ã3 â 100Ã100 (In-N-Out Burger):

In-N-Out Burger is a popular fast food chain that began in California
and now serves parts of Arizona, Texas, Nevada, Utah and Oregon.
Theyâre best known for paying their employees a living wage and
refusing to franchise or go public. But the true In-N-Out loyalists
know them for their 3Ã3 burgers and beyond. Basically, on the regular
menu they have a Double-Double burger consisting of two patties, two
pieces of cheese, lettuce, tomato, etc. But on the (not so) secret
menu you can add burgers and cheese slices till your hearts content.
It got to a point where somebody once ordered a 100Ã100 and they
actually made it for him, thus ending the practice once and for all.
Restaurants like Burger King claim theyâll âmake it your way.â
But In-N-Out had the gall to follow through on their neighborâs
promise.

7. Mac ân Cheese Big Daddy Patty Melt (Dennyâs):

Most of the time Dennyâs tends to fly under the radar. Most likely
because whoever goes into their establishment is drunk at 4:17 AM and
has no recollection of what they ordered, or if they, in fact, went to
Dennyâs at all. Their old ad campaign from back in the 90s even had
people mistaking the restaurantâs name for Lennyâs.

All that changed a few years back when they started serving up this
patty melt with some very unnaturally cheesy âmac and cheeseâ. But
was it as much of a game changer as the photos suggest. Sadly, nobody
will ever know, because anybody who ever ordered it has no
recollection of the experience, or if they in fact, went to Dennyâs
at all.

6. Glazed Donut Breakfast Sandwich (Dunkinâ Donuts):

This little guy is a no-brainer. Eggs, bacon and glazed donuts
separately are the greatest breakfast options known to man. The
question everybody should be asking is: why hasnât anybody attempted
this before? Also, how can this world praise a combination croissant
and doughnut and briefly elect it mayor of New York City, while at the
same time condemn this 360 calorie, light sandwich? I mean, what did
everyone expect from Dunkinâ Donuts? A breakfast sandwich not
consisting of at least 1/3 doughnut? Now if somebody would just create
a breakfast sandwich consisting of the second greatest breakfast items
known to man, oatmeal, cherry danish and mimosa, weâd be all set.

5. Enormous Omelet Sandwich (Burger King):

Hereâs another breakfast wonder that didnât even last a year. It
started out just fine with eggs, sausage, bacon, cheese, another layer
of eggs, all atop Burger Kingâs patented torpedo-shaped bun that
they use for most non-Whopper sandwiches. But cries of excess sodium
and cholesterol sent this egg behemoth back to roost. Again, who are
these people to determine what you ingest? A lot of people work long,
grueling hours in horrendous offices and factories, just to make ends
meet. And hereâs the thing, some of these companies barely give
people time for lunch, forcing many employees to choose between having
a meal, going to the bathroom, or calling their children whom they
hardly ever see. If only they could find a breakfast meal with enough
kick to get them through these monstrous days. Sorry, hard-working
citizens, the internet ruined it for you.


4. Waffle Taco (Taco Bell):

Believe it or not, the Waffle Taco is no longer available at Taco Bell
restaurants. Instead, theyâve replaced it with the Biscuit Taco,
which sounds about 1/8th as appetizing. When Taco Bell first announced
their breakfast menu, the public was ecstatic and the Waffle Taco was
the most talked about and anticipated offering. And then it was taken
away for no apparent reason. In this case, there was no outcry that
this item was unhealthy or disgusting, and it was massively popular to
boot. Any reasonable human being should view this calculated move as a
form of self-sabotage. Why, Taco Bell? Why? Â¡Yo quiero un
explanation!

3. The Crave Case (White Castle):

The beauty of the Crave Case can be boiled down to raw, unadulterated
math. This package consists of 30 beef sliders, each with five holes
in the patty, served in one sleek box at a cost of around $20. And in
the end the equation comes out to a commendable 4,200 calories, which,
if youâre a calorie counter at heart, you would know thatâs around
double the daily recommended intake for both men and woman (2,500 and
2,000, respectively). Now, why would almost double what youâre
entitled ever be considered beneficial? Think back to college, when
you had to cram for an exam for 48 straight hours, or perhaps youâve
experienced something similar with deadlines at your job. With a 48
hour deadline, you donât have time to stop at a diner and hem and
haw over the menu. Itâs far easier to just grapple onto your trusty
Crave Case and get to work.

2. Grilled Cheese Burger Melt (Friendlyâs):

Has this ever happened to you? The only thing on your mind is a hearty
grilled cheese sandwich; however, youâre sitting at a diner with
friends and canât justify ordering just a grilled cheese. Then
again, youâre having a Trainspotting level craving for cheese melted
onto toasted breadâ¦ but what would people say? Friendlyâs
understands this conundrum consummately. Thatâs why they offered the
GCBM with such vigor, until (like many other novelty sandwiches) they
were shamed into discontinuing the item. However, for a few short
years it was the perfect dietary compromise. A burger patty for them
and two mouth-watering grilled cheeses for you.

1. Buffalo Crunch Doughnut (Tim Hortons):

The last sandwich on this list isnât a sandwich at all. And, unlike
many of the other items on this list, was never available in its
companyâs chain restaurants. Tim Hortonsâ Buffalo Crunch Doughnut
gave its consumer all the greatness of a Buffalo chicken wing, only in
doughnut form. And it was exclusively available at the Tim Hortonsâ
booth at the New York State Fair (located in Syracuse, NY) back in
2014. What became of this modern marvel? Nobody knows for sure, but it
appears that the world wasnât quite ready for the worldâs perfect
doughnut. Not yetâ¦




Fortune Subscribe
RETAIL	FAST FOOD
11 Secret Fast Food Menu Items You Need to Order
Michal Addady
March 3, 2016


Fast food restaurants keep offering crazier new options, but some of
their craziest foods arenât even on the menu.

With the help of Hack the Menu, we found 11 secret items that you
might be shocked to know exist. As the website warns, some of these
may be so secret that not even the people working there know what they
are, but if you describe what you want nicely they just might make it
for you.

Arbyâs Meat Mountain

This is exactly what it sounds likeâa mountain of every type of meat
that Arbyâs offers, topped off with some Swiss cheese and cheddar
(because why not?). At $10 itâs the most expensive thing you can get
at Arbyâs, but itâs a pretty good deal considering you probably
wonât want to eat for about a week after.

Burger Kingâs Suicide Burger

This secret menu item is also known as the âQuad Stacker.â Itâs
a burger with four beef patties and four slices of cheese with bacon
and special sauce. If youâre already throwing caution to the wind
and eating something with a name that suggests itâll kill you, you
might as well top your order off with a side of Fringsâhalf fries,
half onion rings.

Chick-Fil-Aâs Blueberry Cheesecake Milkshake
Hack the Menu warns that this dessert isnât available at all
Chick-Fil-A locations, but go ahead and ask them to blend a slice of
blueberry cheesecake into a vanilla milkshake and see what they say.

Chipotleâs Burritodilla
This is the Quesaritoâs âdiet friendlyâ twin. The Quesarito,
which isnât much a secret anymore, is basically a burrito with a
quesadilla in place of the standard tortilla. The Burritodilla is a
quesadilla filled with about half the contents of a burrito, giving
you the same flavors as the first, but much less aggressively.


Five Guysâ Double Grilled Cheese Burger
If youâre not a vegetarian, the only time itâs acceptable to order
a grilled cheese at Five Guys Burgers & Fries is when youâre loading
two of them up with burger patties and toppings.

KFCâs Triple Down

Youâve heard of the Double Down. Now add an extra layer of chicken,
cheese, and bacon to get this triple decker âsandwich.â

McDonaldâs Land, Sea & Air Burger

Canât choose between a Big Mac, McChicken, and Filet-O-Fish?
Donât. Get a Big Mac and add McChicken and Filet-O-Fish patties to
get this very appropriately named secret menu item. If youâre not a
Filet-O-Fish fan but really love chicken, go for the Big McChickenâa
Big Mac with McChicken patties in place of buns.

Shake Shackâs Peanut Butter & Bacon ShackBurger

According to Hack the Menu, Shake Shack had this on its menu for a
single weekend. It was removed due to concern about allergy
cross-contamination, but luckily ordering it is as simple as getting a
ShackBurger with bacon and peanut butter sauce on the side.

Sonicâs Purple Sprite

What makes this Sprite purple? Mixing it with lemonade, Powerade, and
Cranberry juice. As for who came up with this concoction and why,
thatâs still a secret.

Taco Bellâs The Incredible Hulk

Hack the Menu describes this as âone of Taco Bellâs healthy secret
menu items.â Itâs made by replacing the nacho cheese in a 5 layer
burrito with guacamole, which does technically make it healthier. If
you donât really care about the nutrition aspect of the Incredible
Hulk, add Taco Bellâs lava sauce.

Wendyâs Meat Cube

This is probably the least appetizing name of any of these secret menu
items, but it may be the most accurate. Itâs a regular burger, but
with a full pound of hamburger patties. And it looks very much like a
cube of meat.



Â© 2019 Fortune Media IP Limited. All Rights Reserved. Use of this
site constitutes acceptance of our Terms of Use and Privacy Policy
(Your California Privacy Rights).



We Present: America's 20 Most Unhealthy Fast Food Chains

BY CALEB PENNINGTON  â ON JUL 07, 2018  IN FOOD
 
In the past year there has been a lot of talk about what the United
States contributes to the international community. One aspect of
American culture that has certainly spread to other countries is our
obsession with fast food. There was a time when there were only a
handful of fast food corporations jockeying for our dinner money but
now it seems like there is a different franchise on every block.

The influx of fast food places has taken a noticeable toll on the
health of the American public. The United States has a major problem
with obesity and fast food consumption is one of the primary causes.
As such, this list will countdown America's 20 most unhealthy fast
food chains.

Most of these you will have heard of but some of them may have escaped
your notice. Some regional chains are only available in certain parts
of the country, while others, like McDonalds, are available worldwide.
The only thing that these fast food chains have in common is that the
majority of their menu is incredibly unhealthy. If you can think of
any unhealthy fast food chains that didnât make our list, feel free
to mention them in the comments.


https://www.thetravel.com/we-present-americas-20-most-unhealthy-fast-food-chains/

20
SMASHBURGER - A DECENT PRICE FOR A NOT SO DECENT MEAL

They recently opened a Smashburger in my city, so I stopped by to see
what the fuss was about. Smashburger bills itself as the fastest
growing fast food chain in the country and I realized why immediately
upon entering their restaurant. Fast food prices have experienced
significant spikes in the past decade but this restaurant has
apparently avoided the trend. Despite selling more high-quality
products than Burger King or McDonalds, Smashburgerâs prices were
only slightly higher than either of these giant corporations.

With Smashburgerâs prices being so low, it raises the chance that
customers will overeat.

Therefore, even though their food itself might not be as bad as some
other entries, the overall result is the same.

19
MCDONALDS - EVEN IF ITâS NOT SUPERSIZED

Believe it or not, there was a time when people didnât know how
unhealthy McDonalds was. This was until a documentary called Supersize
Me. The man in the documentary only ate McDonalds, for every meal, for
several weeks and he got so sick that they had to end the experiment
early or risk his life. McDonalds made several changes to their menu
in response to the backlash from this film. The most famous of these
changes was when they abandoned their âsupersize meâ program.
Despite these changes, McDonalds still isnât very healthy.

It is consistently ranked as one of the worst offending fast food
places in the entire country.

18
QUIZNOS - IT ISNâT JUST FRIES

When most people think of fast food restaurants they think of places
that sell burgers and french fries. This is usually accompanied by a
misconception that burger restaurants are more unhealthy than other
types of fast food. This is not universally true. A good example of
this is Quiznos. Quiznos is often compared to Subway but this is only
because they both sell subs. While Subway has consciously made its
food increasingly healthier, however, Quiznos product is anything but.

Their food is incredibly greasy and the way that they prepare their
subs is meant to harness all of this grease.

17
HAROLD AND KUMAR GET FAT AT WHITE CASTLE

White Castle is a weird restaurant. People who havenât lived in New
Jersey or Philadelphia have probably never been to White Castle but
almost everyone under the age of 35 has heard of this fast food chain.
Part of this can be attributed to the cult classic Harold and Kumar Go
to White Castle, but there is also something to the unique experience
that White Castle provides.

This restaurant isnât known for its full burger, it is famous for
its sliders. These little burgers trick people into thinking they
havenât eaten that much food when, in reality, they have just
scarfed down the equivalent of three full-sized burgers with a single
serve of sliders.

16
GETTING SHOOK AT SHAKE SHACK

Many of the restaurants on this list are especially unhealthy because
they offer something (besides the standard fast food fare) that isn't
good for their customers. In the case of Shake Shack, I am talking
about alcohol.

Shake Shack first began to gain national notoriety because they
offered hard milkshakes. I can personally attest that Shake Shack's
regular milkshakes are very good, so I can see how people could over
indulge in them.

Therefore, even though the actual food at Shake Shack may be healthier
than the food at other fast food restaurants, they still deserve a
spot on this list.

15
5 GUYS AND A STOMACHACHE

A recent survey found that Five Guys is the most popular fast food
restaurant in America. This ranking system was not based on how many
people eat there every year (this ranking is obviously dominated by
McDonalds), it was based on how people who ate fast food a lot ranked
the restaurants based on 5 criteria.

Five Guys is also the favorite fast food restaurant of this author.
Five Guys might be winning the eye of the public but it isn't winning
over health critics. They consistently rank it as one of the
unhealthiest meals that people can eat.

14
DAIRY QUEEN- THE QUEEN OF UNHEALTHY FOOD

Dairy Queen makes this list because it offers something that most
other fast food places don't: ice cream.

Sure, you can get a cone or a flurry at most large chains, but nowhere
else can you sample the wide array of sugary treats that DQ has to
offer.

A couple of years ago, I saw a commercial for a triple later Oreo pie.
There is no way that this is a healthy eating option.

I am guilty of enjoying Dairy Queen's $5 lunch deal but I will try to
go there less after compiling this list.

13
WENDY'S - THE SNEAKY RED-HEAD

If there was any entry on this list that was my Achilles heel, it
would be Wendyâs. All of their food is great but I especially love
that I can get chili as a side instead of french fries. I was
therefore devastated when I learned how incredibly unhealthy Wendyâs
food is (even by fast food standards). Even my beloved chili is full
of things that a person shouldnât be eating on a regular basis.

I would be lying if I said that I had sworn off Wendyâs all together
but I have certainly cut back since I've learned about all the health
risks related to eating their food.

12
BURGER KING - SECOND FIDDLE IS STILL BAD

Can you imagine being a lifelong Burger King employee? As if itâs
not bad enough that youâve dedicated your life to a giant fast food
conglomerate, you are constantly stuck playing second fiddle to those
clowns (pun intended) at McDonalds.

It seems like everything Burger King does is a step behind their top
competitor and the company never achieved the iconic status that the
golden arches have.

One area where BK was able to get a leg up on its competitors was its
healthy food division. But even the 100-calorie menu at Burger King
isnât entirely healthy. Itâs only healthier in comparison to the
normal menu.

11
IN-N-OUT - AND OUT AGAIN

Most Americans have never experienced In-N-Out burger because it only
has restaurant locations on the west coast. Those who have tasted this
legendary burger are generally happy with their experience but their
digestive tracks are not.

From what I have read about In-N-Out is that the name describes how
easy it is to get your food and go. But it also describes the food's
interaction with your digestion...

In-N-Out is incredibly greasy, and eating it comes with all the
negative consequences that always come with eating greasy food. This
is one aspect of the west coast that the east coast would be better
without.

10
ARBYâS - CAN'T TRUST THOSE CURLY FRIES

Unlike some other entries on this list, Arby's is very forthcoming
about the ingredients for their famous roast beef sandwiches. While we
applaud this fast food chain for their honesty, after looking at said
ingredients, I cannot label Arby's food as anything other than
unhealthy.

There are a lot of health concerns with Arby's product but the thing
that I found most disturbing was that almost everything on the menu
had an extremely high salt content. Eating there is just a heart
attack waiting to happen. It doesnât help that their food is so
delicious that you find yourself wanting second helpings.

9
PIZZA HUT - FAST FOOD OR NOT?

I had an internal debate over whether any (or all) pizza can be
considered fast food. It can be prepared with a quickness that
corresponds with fast food but pizza seems like its own, distinct
industry. If pizza can be considered a fast food, Pizza Hut is
certainly the fast foodiest. The Hut is all about cutting cost and
standardization, two pillars of the fast food industry. Another reason
why Pizza Hut resembles fast food is how unhealthy it is.

There are more calories in a single slice of Pizza Hut pizza than
there are in several items from McDonalds dollar menu.

8
CHARLIEâS CHEESESTEAKS - 12 INCHES OF HEART ATTACK

The restaurant Charlieâs Cheesesteaks is an anomaly to me. I have
never seen one in a normal location, I have only seen them in food
courts at shopping malls or airports. I have eaten there, and the food
is good, so that isnât what keeps Charlies from expanding past the
food court market.

I have a theory: Charlieâs is so unhealthy that only people who are
almost forced to eat it (such as at airports with limited options)
will choose to do so regularly.

I found Charlieâs delicious, but even I have to admit that the food
tasted incredibly unhealthy.

7
CHICK-FIL-A - MONDAY THROUGH FRIDAY

When I attended college at West Virginia University, one of the best
things about the school was their food court. We could use our meal
swipes at several chain restaurants, including Chick-fil-A.

I liked Chick-fil-A, but not as much as some of my friends did. One
kid, in particular, ate it just about every day for lunch and dinner.
By the end of the semester he was hospitalized for being malnourished.

I know that there aren't practically any foods that are healthy enough
for someone to eat every day but this story leaves a lasting
impression of Chick-fil-Aâs health benefits.

6
CHIPOTLE - A BUFFET OF ARTERY BLOCKERS

I was in college when the Chipotle craze hit America. The Hispanic
food server was very popular among kids my age, meaning it was
constantly displayed all over social media. This led to even more
people trying it and Chipotle began building new stores to meet this
demand. But is it good for you? The short answer is no.

Chipotle isn't as dependent on grease as some of the other foods on
this list but they still use a lot of artificial flavors and extracts
that aren't good for our bodies.

Also, the buffet style that Chipotle uses encourages overeating.

5
SONIC - NOT EVEN FIT FOR A HEDGEHOG

The coolest thing about Sonic is the unique eating experience that it
provides. Instead of ordering food at the counter like you would at a
normal fast food restaurant, Sonic allows its customers to pull up to
a parking station, order over an intercom, and have their food brought
out to them.

This is totally different from any other fast food place that I have
ever been to. One thing that isnât different about Sonic is the
quality of their food. They push the same greasy dribble that ever
other burger and fries place does. The only exception is their
milkshakes, which are also unhealthy.

4
PANDA EXPRESS - GREASE, SICKNESS, AND CULTURAL DIFFERENCES

For a longtime, Panda Express held a mythical place in the back of my
mind. I love fast food and I love Chinese food, so why wouldnât I
like a place that incorporates both. I tried Panda Express for the
first time last year and I was not impressed. I could taste the grease
on the food and I felt incredibly bloated and tired afterwards.

Chinese food isnât supposed to be healthy anyways, at least not the
way we eat it. The food was designed for the smaller portions that
they eat in Asia, so when Americans gorge themselves on it, it can be
very fattening.

3
TACO BELL - FAKE MEAT BUT REAL FAT

I honestly have no idea what the meat at Taco Bell is made out of.
Even worse, Iâm not sure if I want to know.

The founders of Taco Bell were able to build a multi-billion-dollar
company selling a âmeat likeâ substance covered in cheap toppings.

This is certainly an impressive accomplishment but it does not bode
well for the health of people who eat Taco Bell on a daily basis.
Ignoring the suspicious nature of their meat product, almost every
item on Taco Bellâs menu has an extremely high fat and sodium
content. Many people enjoy Taco Bell but they probably will not enjoy
the heart problems that go with it.

2
KFC - NOT ACTUALLY MADE IN KENTUCKY

I abhor Kentucky Fried Chicken. My siblings loved it, so when I was
growing up, I was always outvoted and made to go there for dinner. As
I have grown older, my feelings toward the Colonelâs secret blend of
herbs and spices has not grown. My own biases aside, KFC is not good
for you.

It is owned by the same company that owns Pizza Hut and Taco Bell and
that should tell you everything that you need to know about the
quality of their chicken.

KFC pitches their product as a home-cooked meal, as opposed to
traditional fast food, making it all the more dangerous.

1
CINNABON - MY DREAM COME TRUE

I have never been to a Cinnabon before but it is certainly on my
bucket list. You may have already figured out that I actually like
fast food. I am also an avid eater of cinnamon rolls. To me, this
sounds like Cinnabon and myself were a match made in heaven. The only
obstacle? Cinnabonâs food is very bad for you.

Their pastries are made up almost entirely of sugar and carry almost
no nutritional value. This will not stop me from sampling their wares
someday, but it will prevent me from letting it become an everyday
habit.


 
The 33 Craziest New Fast Foods Of 2014
Rachel Sanders
Rachel Sanders
BuzzFeed Staff
 View 36 comments
 
Another year is nearing its end, and here we are with another crop of inexplicable fast food menu items to look back on in fondness and confusion.

There are some patterns you can spot amidst all the cheese: Pizza Hut continues to gleefully troll the world, KFC is WAY more fun outside the U.S., Jack in the Box understands that 90% of its customer base is stoners, and Taco Bell maintains an uncanny knack for formulating exactly which Franken-foods will cause Twitter to freak out the most.

Behold what humans worldwide leave in our greasy wake this year:

1. 7-Eleven's Doritos Loaded (U.S.)

The love child of a Dorito and a mozzarella stick that we definitely
never asked for but will totally eat when drunk.


2. Taco Bell's Waffle Breakfast Taco (U.S.)

After months of whispers and rumors, it finally arrived this spring.

3. Subway's Fritos Chicken Enchilada Melt (U.S.)

"It's a nice change up if you eat at Subway a lot and find yourself
getting sick of cured meats."

4. Domino's Starburst Chocolate Lava Cake (Australia)

On a scale from one to no-longer-capable-of-speech, how high was the
Domino's R&D team when they came up with this?

5. Pizza Hut's Doritos-Crust Pizza (Australia)

AUSTRALIA WOULD.

6. McDonald's Black & White Pie (China)

With coconut filling and a fried chocolate shell. Would definitely eat!

7. KFC's Crispy Cheese Chicken (Philippines)

Apparently "marinated" in cheese and then covered in crispy cheese
bits. Admit it, you're intrigued.

8. Burger King's Burger-Topped Poutine (Canada)

Poutine to the People, no doubt, but not convinced this is the way to
go about it.

9. Carl's Jr's Bisnut (U.S.)

This is pretty much what you think it is: a wannabe-Cronut biscuit
with a hole in the middle, topped with icing and sprinkles.

10. Pizza Hut's Surf & Turf Pizza with Dessert-Stuffed Crust (South Korea)

How did it take humanity so long to come up with a pizza that combines
shrimp, calamari, sausage, bacon, steak, cranberry (or apple) and
cream cheese?

11. Jack in the Box's Hella-PeÃ±o Burger

Yes, that is a burger topped with stuffed jalapeÃ±o poppers and cheese
sauce. And yes, explicitly marketing fast food to stoners is a
brilliant strat.

12. KFC's Popcorn Chicken Nacho Box (Australia)

This was MADE for America. It's a travesty that it's only available
Down Under.

13. Papa John's Frito Chili Cheese Pizza (U.S)

Doesn't seem like the worst idea in the world, TBH.

14. Taco Bell's Starburst Strawberry Freeze (U.S)

At last, you can have your candy in slush form!

15. Pizza Hut's Chili Dog Stuffed Crust Pizza (New Zealand)

Â¯\_(ã)_/Â¯

16. Burger King's Premium Berry Burger (Japan)

With cranberry spread and blueberries on top. Sounds almost as
appetizing as the "Mush 'n' Cheese"! BERRY KRISTMUSH TO ALL!!!

17. Church's Chicken & Waffle Bites (U.S.)

Legit brilliant.

18. Del Taco's Bun Taco (U.S.)

(LOL). This was one of three "throwback" menu items resurrected to
commemorate Del Taco's 50th anniversary.

19. Domino's Specialty Chicken (U.S.)

What is it? Literally just fried chicken chunks covered with cheese
and other stuff. Why does it exist? We may never know.

20. KFC's Dipping Fries (Romania)

Clearly, Eastern Europeans understand the need for a higher
condiment:fry ratio.

21. Carl's Jr.'s Double Loaded Omelet Biscuit (U.S.)

Also at Hardee's. Two omelets with sausage, ham, bacon, American, Jack
AND cheddar cheese is a great thing to have for breakfast if you want
to be passed out for the rest of the day!

22. Jack in the Box's Chick-N-Tater Melt (U.S)

You can get this miraculous monster of a sandwich (chicken, hash
brown, cheese, bacon, cheese sauce, and ranch on a croissant) in one
of the chain's late-night Munchie Meals.

23. KFC's Creamed Corn Chicken Sandwich (Brazil)

Nope!

24. Domino's Subwich (India)

A bean or chicken patty between two triangles of pizza dough. This
just makes me want actual pizza.

25. McDonald's McSbrinz Burger (Switzerland)

Sbrinz is apparently a kind of Swiss cheese that is served in adorable
little rolls. Why put in on a burger, you ask? Well, uh, why not?

26. KFC's Double Down King (South Korea)

The original Double Down was apparently NOT ENOUGH for South Korea,
where KFC went ahead and slapped a hamburger in there too.

27. Pizza Hut's Pretzel Piggy Pizza (U.S.)

This pie boasts bacon, mushrooms and spinach with a salted pretzel
crust and balsamic drizzle. It's part of Pizza Hut's big, bewildering
American menu revamp.

28. Pizza Hut's Sausage Roll Crust Pizza (Luxembourg)

If you put a pizza surrounded by pigs-in-a-blanket in front of me, I'm
not going to NOT eat it.

29. Taco Bell's Quesarito (U.S.)

Your eyes do not deceive you; that is, in fact, a burrito wrapped in a
quesadilla.

30. Subway's Flatizza (U.S.)

What is that, a piece of frickin' matzoh? NOT A THING.

31. White Castle's Waffle Breakfast Sandwiches (U.S.)

In the words of Businessweek, who eats breakfast at White Castle?

32. Pizza Hut's Quesadilla, Burrito & Nacho Pizzas (New Zealand)

Pizza Hut is DEFINITELY the place I turn to for authentic, flavorful
Mexican food.

33. Tim Horton's Buffalo Crunch Doughnut (U.S.)

God willing, these doughnuts (which were served for only a week at the
New York State Fair this summer) will pop up at some regular Tim
Horton's locations in the future.


December 18, 2014, at 11:50 p.m.
A previous version of this post included a fictional milkshake which was incorrectly presented as real. I wanted to believe.

Get all the best Tasty recipes in your inbox! Sign up for the Tasty newsletter today!



We Present: America's 20 Most Unhealthy Fast Food Chains

BY CALEB PENNINGTON  â ON JUL 07, 2018  IN FOOD
 
In the past year there has been a lot of talk about what the United
States contributes to the international community. One aspect of
American culture that has certainly spread to other countries is our
obsession with fast food. There was a time when there were only a
handful of fast food corporations jockeying for our dinner money but
now it seems like there is a different franchise on every block.

The influx of fast food places has taken a noticeable toll on the
health of the American public. The United States has a major problem
with obesity and fast food consumption is one of the primary causes.
As such, this list will countdown America's 20 most unhealthy fast
food chains.

Most of these you will have heard of but some of them may have escaped
your notice. Some regional chains are only available in certain parts
of the country, while others, like McDonalds, are available worldwide.
The only thing that these fast food chains have in common is that the
majority of their menu is incredibly unhealthy. If you can think of
any unhealthy fast food chains that didnât make our list, feel free
to mention them in the comments.


https://www.thetravel.com/we-present-americas-20-most-unhealthy-fast-food-chains/

20
SMASHBURGER - A DECENT PRICE FOR A NOT SO DECENT MEAL

They recently opened a Smashburger in my city, so I stopped by to see
what the fuss was about. Smashburger bills itself as the fastest
growing fast food chain in the country and I realized why immediately
upon entering their restaurant. Fast food prices have experienced
significant spikes in the past decade but this restaurant has
apparently avoided the trend. Despite selling more high-quality
products than Burger King or McDonalds, Smashburgerâs prices were
only slightly higher than either of these giant corporations.

With Smashburgerâs prices being so low, it raises the chance that
customers will overeat.

Therefore, even though their food itself might not be as bad as some
other entries, the overall result is the same.

19
MCDONALDS - EVEN IF ITâS NOT SUPERSIZED

Believe it or not, there was a time when people didnât know how
unhealthy McDonalds was. This was until a documentary called Supersize
Me. The man in the documentary only ate McDonalds, for every meal, for
several weeks and he got so sick that they had to end the experiment
early or risk his life. McDonalds made several changes to their menu
in response to the backlash from this film. The most famous of these
changes was when they abandoned their âsupersize meâ program.
Despite these changes, McDonalds still isnât very healthy.

It is consistently ranked as one of the worst offending fast food places in the entire country.

18
QUIZNOS - IT ISNâT JUST FRIES

When most people think of fast food restaurants they think of places
that sell burgers and french fries. This is usually accompanied by a
misconception that burger restaurants are more unhealthy than other
types of fast food. This is not universally true. A good example of
this is Quiznos. Quiznos is often compared to Subway but this is only
because they both sell subs. While Subway has consciously made its
food increasingly healthier, however, Quiznos product is anything but.

Their food is incredibly greasy and the way that they prepare their
subs is meant to harness all of this grease.

17
HAROLD AND KUMAR GET FAT AT WHITE CASTLE

White Castle is a weird restaurant. People who havenât lived in New
Jersey or Philadelphia have probably never been to White Castle but
almost everyone under the age of 35 has heard of this fast food chain.
Part of this can be attributed to the cult classic Harold and Kumar Go
to White Castle, but there is also something to the unique experience
that White Castle provides.

This restaurant isnât known for its full burger, it is famous for
its sliders. These little burgers trick people into thinking they
havenât eaten that much food when, in reality, they have just
scarfed down the equivalent of three full-sized burgers with a single
serve of sliders.

16
GETTING SHOOK AT SHAKE SHACK

Many of the restaurants on this list are especially unhealthy because
they offer something (besides the standard fast food fare) that isn't
good for their customers. In the case of Shake Shack, I am talking
about alcohol.

Shake Shack first began to gain national notoriety because they
offered hard milkshakes. I can personally attest that Shake Shack's
regular milkshakes are very good, so I can see how people could over
indulge in them.

Therefore, even though the actual food at Shake Shack may be healthier
than the food at other fast food restaurants, they still deserve a
spot on this list.

15
5 GUYS AND A STOMACHACHE

A recent survey found that Five Guys is the most popular fast food
restaurant in America. This ranking system was not based on how many
people eat there every year (this ranking is obviously dominated by
McDonalds), it was based on how people who ate fast food a lot ranked
the restaurants based on 5 criteria.

Five Guys is also the favorite fast food restaurant of this author.
Five Guys might be winning the eye of the public but it isn't winning
over health critics. They consistently rank it as one of the
unhealthiest meals that people can eat.

14
DAIRY QUEEN- THE QUEEN OF UNHEALTHY FOOD

Dairy Queen makes this list because it offers something that most
other fast food places don't: ice cream.

Sure, you can get a cone or a flurry at most large chains, but nowhere
else can you sample the wide array of sugary treats that DQ has to
offer.

A couple of years ago, I saw a commercial for a triple later Oreo pie.
There is no way that this is a healthy eating option.

I am guilty of enjoying Dairy Queen's $5 lunch deal but I will try to
go there less after compiling this list.

13
WENDY'S - THE SNEAKY RED-HEAD

If there was any entry on this list that was my Achilles heel, it
would be Wendyâs. All of their food is great but I especially love
that I can get chili as a side instead of french fries. I was
therefore devastated when I learned how incredibly unhealthy Wendyâs
food is (even by fast food standards). Even my beloved chili is full
of things that a person shouldnât be eating on a regular basis.

I would be lying if I said that I had sworn off Wendyâs all together
but I have certainly cut back since I've learned about all the health
risks related to eating their food.

12
BURGER KING - SECOND FIDDLE IS STILL BAD

Can you imagine being a lifelong Burger King employee? As if itâs
not bad enough that youâve dedicated your life to a giant fast food
conglomerate, you are constantly stuck playing second fiddle to those
clowns (pun intended) at McDonalds.

It seems like everything Burger King does is a step behind their top
competitor and the company never achieved the iconic status that the
golden arches have.

One area where BK was able to get a leg up on its competitors was its
healthy food division. But even the 100-calorie menu at Burger King
isnât entirely healthy. Itâs only healthier in comparison to the
normal menu.

11
IN-N-OUT - AND OUT AGAIN

Most Americans have never experienced In-N-Out burger because it only
has restaurant locations on the west coast. Those who have tasted this
legendary burger are generally happy with their experience but their
digestive tracks are not.

From what I have read about In-N-Out is that the name describes how
easy it is to get your food and go. But it also describes the food's
interaction with your digestion...

In-N-Out is incredibly greasy, and eating it comes with all the
negative consequences that always come with eating greasy food. This
is one aspect of the west coast that the east coast would be better
without.

10
ARBYâS - CAN'T TRUST THOSE CURLY FRIES

Unlike some other entries on this list, Arby's is very forthcoming
about the ingredients for their famous roast beef sandwiches. While we
applaud this fast food chain for their honesty, after looking at said
ingredients, I cannot label Arby's food as anything other than
unhealthy.

There are a lot of health concerns with Arby's product but the thing
that I found most disturbing was that almost everything on the menu
had an extremely high salt content. Eating there is just a heart
attack waiting to happen. It doesnât help that their food is so
delicious that you find yourself wanting second helpings.

9
PIZZA HUT - FAST FOOD OR NOT?

I had an internal debate over whether any (or all) pizza can be
considered fast food. It can be prepared with a quickness that
corresponds with fast food but pizza seems like its own, distinct
industry. If pizza can be considered a fast food, Pizza Hut is
certainly the fast foodiest. The Hut is all about cutting cost and
standardization, two pillars of the fast food industry. Another reason
why Pizza Hut resembles fast food is how unhealthy it is.

There are more calories in a single slice of Pizza Hut pizza than
there are in several items from McDonalds dollar menu.

8
CHARLIEâS CHEESESTEAKS - 12 INCHES OF HEART ATTACK

The restaurant Charlieâs Cheesesteaks is an anomaly to me. I have
never seen one in a normal location, I have only seen them in food
courts at shopping malls or airports. I have eaten there, and the food
is good, so that isnât what keeps Charlies from expanding past the
food court market.

I have a theory: Charlieâs is so unhealthy that only people who are
almost forced to eat it (such as at airports with limited options)
will choose to do so regularly.

I found Charlieâs delicious, but even I have to admit that the food
tasted incredibly unhealthy.

7
CHICK-FIL-A - MONDAY THROUGH FRIDAY

When I attended college at West Virginia University, one of the best
things about the school was their food court. We could use our meal
swipes at several chain restaurants, including Chick-fil-A.

I liked Chick-fil-A, but not as much as some of my friends did. One
kid, in particular, ate it just about every day for lunch and dinner.
By the end of the semester he was hospitalized for being malnourished.

I know that there aren't practically any foods that are healthy enough
for someone to eat every day but this story leaves a lasting
impression of Chick-fil-Aâs health benefits.

6
CHIPOTLE - A BUFFET OF ARTERY BLOCKERS

I was in college when the Chipotle craze hit America. The Hispanic
food server was very popular among kids my age, meaning it was
constantly displayed all over social media. This led to even more
people trying it and Chipotle began building new stores to meet this
demand. But is it good for you? The short answer is no.

Chipotle isn't as dependent on grease as some of the other foods on
this list but they still use a lot of artificial flavors and extracts
that aren't good for our bodies.

Also, the buffet style that Chipotle uses encourages overeating.

5
SONIC - NOT EVEN FIT FOR A HEDGEHOG

The coolest thing about Sonic is the unique eating experience that it
provides. Instead of ordering food at the counter like you would at a
normal fast food restaurant, Sonic allows its customers to pull up to
a parking station, order over an intercom, and have their food brought
out to them.

This is totally different from any other fast food place that I have
ever been to. One thing that isnât different about Sonic is the
quality of their food. They push the same greasy dribble that ever
other burger and fries place does. The only exception is their
milkshakes, which are also unhealthy.

4
PANDA EXPRESS - GREASE, SICKNESS, AND CULTURAL DIFFERENCES

For a longtime, Panda Express held a mythical place in the back of my
mind. I love fast food and I love Chinese food, so why wouldnât I
like a place that incorporates both. I tried Panda Express for the
first time last year and I was not impressed. I could taste the grease
on the food and I felt incredibly bloated and tired afterwards.

Chinese food isnât supposed to be healthy anyways, at least not the
way we eat it. The food was designed for the smaller portions that
they eat in Asia, so when Americans gorge themselves on it, it can be
very fattening.

3
TACO BELL - FAKE MEAT BUT REAL FAT

I honestly have no idea what the meat at Taco Bell is made out of.
Even worse, Iâm not sure if I want to know.

The founders of Taco Bell were able to build a multi-billion-dollar
company selling a âmeat likeâ substance covered in cheap toppings.

This is certainly an impressive accomplishment but it does not bode
well for the health of people who eat Taco Bell on a daily basis.
Ignoring the suspicious nature of their meat product, almost every
item on Taco Bellâs menu has an extremely high fat and sodium
content. Many people enjoy Taco Bell but they probably will not enjoy
the heart problems that go with it.

2
KFC - NOT ACTUALLY MADE IN KENTUCKY

I abhor Kentucky Fried Chicken. My siblings loved it, so when I was
growing up, I was always outvoted and made to go there for dinner. As
I have grown older, my feelings toward the Colonelâs secret blend of
herbs and spices has not grown. My own biases aside, KFC is not good
for you.

It is owned by the same company that owns Pizza Hut and Taco Bell and
that should tell you everything that you need to know about the
quality of their chicken.

KFC pitches their product as a home-cooked meal, as opposed to
traditional fast food, making it all the more dangerous.

1
CINNABON - MY DREAM COME TRUE

I have never been to a Cinnabon before but it is certainly on my
bucket list. You may have already figured out that I actually like
fast food. I am also an avid eater of cinnamon rolls. To me, this
sounds like Cinnabon and myself were a match made in heaven. The only
obstacle? Cinnabonâs food is very bad for you.

Their pastries are made up almost entirely of sugar and carry almost
no nutritional value. This will not stop me from sampling their wares
someday, but it will prevent me from letting it become an everyday
habit.



https://www.thetravel.com/we-present-americas-20-most-unhealthy-fast-food-chains/
 
10 Short-Lived Fast Food Items That Deserve a Comeback
By Chris Morgan  |  April 25, 2017  |  12:25pm

10 Short-Lived Fast Food Items That Deserve a Comeback

A couple of short-run fast food items from the days of yore took over
the internet recently. Thereâs an entire podcast dedicated to the
brief period of time McDonaldâs served pizza, and thanks to Rick and
Morty, people were suddenly obsessed with McDonaldâs âSzechuan
Sauceâ that was served coinciding with the Disney movie Mulan. Of
course, there was nothing authentic about Mickey Dâs sauce, which
had little if anything to do with Sichuan cuisine (For starters, the
top-listed ingredient in their Szechuan Sauce was high fructose corn
syrup). However, this confluence of events serves as a nice jumping
off point to discuss some other short-lived fast food items we would
like to see get another chance.


1. Taco Bellâs Bacon Club Chalupa 

First off, I just wanted to address the Bell Beefer, since it is a
staple of internet clamoring for discontinued menu items. We donât
need the Bell Beefer back. Itâs just a burger, only interesting for
the novelty of getting a burger from Taco Bell. However, as I delved
into writing this list, I was reminded of the existence of the Bacon
Club Chalupa, and I was instantly taken back to my memories of eating
these. It was good enough to pull me away from my traditional gordita
eating. I didnât like the chalupa shell nearly as much, but I was
all about a taco that included chicken, bacon, and a tasty ranch
sauce. When they brought it back in 2015 briefly, a time in which I
did not partake in eating it again, apparently they made it an avocado
ranch sauce. That sounds like an improvement.

2. Jack in the Boxâs Cheesy Macaroni Bites 

Jack in the Box is primarily a West Coast chain, which is why I spent
much of my life unfamiliar with their menu. However, said menu is
basically completely insane, and there was a period of time where
their ads were literally solely catering to an audience of stoned
people who wanted to eat weird stuff. The Cheesy Macaroni Bites
arenât that odd, to be fair. They were basically just deep-fried
globs of macaroni and cheese. Thatâs something you donât find at a
lot of places, and it also is something a fast food place manages to
do well. By the way, you can currently get a sandwich consisting of
chicken, hash browns, bacon, cheese and ranch dressing on a croissant
on their âMunchie Mealâ menu. You know, if you are stoned and
hungry.

3. Burger Kingâs Western Whopper 

The Whopper is a solid burger. Itâs not great, but it gets the job
done, which makes it the perfect trademark burger for a fast food
restaurant. The Western Whopper took that solid base, and added bacon
(before bacon got played out) and sauce with a âWesternâ tang.
Basically, it was BBQ sauce, but BBQ sauce is wonderful on a burger,
especially when you throw in bacon as well.

4. Wendyâs Classic Greek Pita 

Sometimes, you arenât in the mood for a traditional sandwich. In
that instance, some fast food places now offer wraps, but what about a
classic pita-style sandwich? Wendyâs released three pita sandwiches
in the mid-90s: one veggie, one Chicken Caesar and one Classic Greek.
The Greek was the best, although that may be influenced by a general
lack of interest in Chicken Caesar Salad. The Greek one, though, had
feta cheese, and it just makes sense to have a Greek sandwich on a
pita. It was basically like eating a chicken gyro, and who doesnât
enjoy a chicken gyro?


5. Subwayâs Orchard Chicken Salad Sub 

I had just moved to Los Angeles, and, naturally, I had gotten lost on
my way home from a studio I was doing some work at. To try and
alleviate my frustration, I decided to stop at a Subway to pick up a
footlong of this new sandwich I had been seeing advertised. That
sandwich was the Orchard Chicken Salad. In addition to the chicken,
and the mayo, it had cranberries raisins, apples and celery. If they
still had the Orchard Chicken Salad available, it would be my go to
order. Instead, Iâm pretty sure it only existed for a month or two
that summer.

6. Pizza Hutâs Bigfoot Pizza 

These days, fast food pizza places trumpet the quality of their
ingredients. Papa Johnâs has been doing the whole âBetter
ingredients, better pizzaâ thing for a while, and Dominos built an
entire ad campaign on apologizing for how garbage their pizza had
been. This is a good thing, but I occasionally feel a twinge of
fondness for the days when pizza places were trumpeting quantity over
quality. The king of that era was Pizza Hutâs Bigfoot Pizza. The
Bigfoot was a rectangular pizza that was three feet long. Apparently,
you could get it with three toppings for only $10.99 back in 1993.
Rare are the occasions when you would need that much pizza, and you
could always just order a couple normal size pizzas. Still, thereâs
something about seeing a delivery guy with a giant rectangular box.

7. Taco Bellâs Cheesarito 

Look, if weâre being honest, the best thing about Taco Bellâs food
is the melted cheese. The best item they ever introduced was the
Cheesy Gordita Crunch, and the reason for that is the taste and
mouthfeel of the melted cheese between the gordita wrap and the hard
taco shell. The Cheesarito is basically just one big opportunity to
enjoy some melted cheese. It was a soft tortilla stuffed with cheese
and taco sauce.

8. McDonaldâsâ Arch Deluxe 

The Arch Deluxe was a burger for âadults,â an attempt to provide a
âmatureâ option for people bringing their kids in to eat Happy
Meals. This was apparently lost on me as a kid, because I ate several
Arch Deluxes. It had a weird piece of circular bacon that was
inorganic looking even by fast food standards, but maybe they could
replace that with strips of peppered bacon if it were to return. One
thing is for sure; the sauce they used for the Arch Deluxe was quite
tasty, and it also had ketchup on it, which they wisely put on the
bottom bun so it didnât mix with the Arch Deluxe sauce.

9. Burger Kingâs Enormous Omelet Sandwich 

Look, the Enormous Omelet Sandwich was kind of repulsive. However, it
was repulsive in that way fast food can be sometimes, which is to say
it was gloriously repulsive. It was so big and so heavy, which is to
say when you ate one itâd weigh on you. One sandwich was 730
calories and 47 grams of fat. It was a long sandwich, filled with
eggs, an uncannily long sausage patty, bacon,and a ton of American
cheese. It was almost a novelty sandwich, not something you could â
or should â eat with any regularity. Itâs also the kind of thing
that is missing from modern fast food. Give America the opportunity to
shove a revolting among of breakfast food down their gullet in
sandwich form again, BK!

10. McDonaldâsâ Cheddar Melt 

Not everything McDonaldâs has done over the years has been a
success, but a lot of things, like the McDLT, just didnât make
practical sense. I remember eating what I believe were bratwursts from
Mickey Dâs sometime around when I graduated from high school, for
example. I thought about going with the Hula Burger, which was a
meat-free Lent option built around a pineapple slice. Sure, Iâve
never eaten it, but Iâd like the chance. However, the Cheddar Melt
is just a more practical, and more enticing, option. It had onions
sautÃ©ed in teriyaki sauce (which make any burger better) and also it
came on a rye bun. The Cheddar Melt was just different enough from
McDonaldâs traditional options to make it intriguing. It certainly
deserves a return more than those Salad Shakers McDonaldâs used to
offer. We certainly donât need to see the return of salad in a cup.

Chris Morgan is the author of The Comic Galaxy of Mystery Science
Theater 3000 and the new novel The Ash Heap of History. Heâs also on
Twitter.


Grilled stuffed burrito
Â£5 chicken nachos box
Beefy melt griller
Fajitas burrito

Chocodilla
Cocomarsh melt 


The Most Ridiculous New Fast Food Menu Items of 2018
   
SHAY SPENCEPosted on December 21, 2018 5:02PM

ARBY'S
ARBY'S ARBYNATOR

The roast beef chain gave us what we didn't know we wanted, putting
their famed seasoned curly fries directly on a sandwich. You can also
take it a step further by going for the Half-Pound Arbynator, which
comes with an absolutely ridiculous amount of meat.

CARLS. JR
CARL'S JR./HARDEE'S FROOT LOOP DONUTS

These colorful, bite-size donuts were released for a limited time in
August and taste exactly like the classic sugary breakfast cereal.

MCDONALD'S
MCDONALD'S TRIPLE STACK BREAKFAST SANDWICHES

With their first new addition to the breakfast menu since 2013,
McDonald's now gives you the option to order their McMuffins,
McGriddles, and breakfast biscuits piled with two sausage patties and
bacon.


SONIC PICKLE JUICE SLUSHIE

This polarizing menu item all-but broke the internet when it was
announced in March. The bright-green beverage boasted a
sweet-and-tangy flavor that was a little more subtle than the name
would lead you to believe.

POPEYES' GOLD-DUSTED CHICKEN

Before they were serving emotional support chickens for holiday
travelers, the fried chicken chain pulled a more glamorous stunt:
champagne-battered, 24-karat-gold-coated chicken wings for one day
only to celebrate their 3,000th location.

KFC
KFC'S WAFFLE DOUBLE DOWN

The KFC Double Downâa breakfast sandwich that has two pieces of
fried chicken in lieu of a bunâis one of the most iconic fast food
innovations of all time. This year, KFC in Canada took it to the next
level by putting a whole belgian waffle smothered in maple aioli in
the middle.


CHILI'S
CHILI'S BOSS BURGER

This 1,650 calorie burger is not for the faint of heart. The bottom
bun is smothered in BBQ sauce and ranch, and then topped with lettuce,
tomato, a beef patty and cheddar cheese. Next, the burger is loaded
with four other meatsâbrisket, pulled ribs, jalapeÃ±o sausage, and
baconâbefore being completed with a top bun.

CHILI'S
BURGER KING'S 'NIGHTMARE KING'

Another meat on meat on meat situation: BK's green bun burger,
released in October for Halloween, features a quarter-pound of beef, a
crispy chicken fillet, melted American cheese, thick-cut bacon,
mayonnaise and onions on a glazed green sesame seed bun.

CHILI'S
DUNKIN'S COSMIC COOLATTAS

Taking a page from Starbucks' unicorn frappuccinos from 2017, Dunkin
released these "galaxy-inspired" colorful frozen beverages in April,
along with a matching donut.


PANERA BREAD
PANERA'S DOUBLE BREAD BOWL

For the indecisive carb loader, the fast-casual chain tested these in
July at their Philadelphia locations, letting customers mix and match
two different soup or mac-and-cheese options in the same loaf of
bread.

OLIVE GARDEN
OLIVE GARDEN'S LOADED PASTA CHIPS

Lightly fried pasta dough is topped with meat sauce, three Italian
cheeses, Alfredo sauce and hot peppers in this nacho-like dish, which
debuted in February.

IHOP
IHOP'S GRINCH PANCAKES

In tandem with the new Dr. Seuss' The Grinch movie, the breakfast
chain released these bright green pancakes with red candy Grinch
hearts (and a matching hot chocolate option).



RETAIL
These were the biggest menu flops in fast food
Jessica Tyler Jul 17, 2018, 9:16 AM ET

BK shake em up fries
YouTubeFast food has seen its share of flops over the years.
Fast-food chains often experiment with their menus to try to appeal to new customers or offer healthier options.
Even though some of these items take off, many of them end up huge failures.
Other items that have been long discontinued include Taco Bell's Seafood Salad, McDonald's Hula Burger, and Wendy's Frescata.
Not every fast-food option can be a best seller.

Some experimental menu items actually end up costing chains millions,
like McDonald's Arch Burger, a "gourmet" burger that aimed to appeal
to a more adult crowd but failed miserably. McDonald's spent an
estimated $150 million to $200 million advertising the Arch Deluxe's
rollout, which, at the time, was the most expensive promotional
campaign in fast-food history, The New York Times reported.

Other menu items failed because they were just unappetizing, like Taco
Bell's Seafood Salad or Domino's Oreo Pizza.

Here are some fast-food items that didn't make it:

McDonald's: Pizza

McDonald's Pizza took years to develop. It required developing a
quick-cook oven, remodeling kitchens to fit the new equipment, and
expanding drive-thru windows to accommodate pizza boxes. Even after
all of that work, customers still complained that the wait was too
long and the price was too high. The pizza began disappearing from
menus not long after it was added.

McDonald's: Mozzarella Sticks

McDonald's launched mozzarella sticks in late 2015, but customers were
furious when they found most of their mozzarella sticks didn't
actually have cheese in them. They were sold at three for $1 but were
discontinued not long after they launched.


Burger King: Yumbo

In 2014, Burger King relaunched the Yumbo sandwich, a ham-and-cheese
sandwich that was originally removed from the menu in 1974. The chain
promoted it with nostalgic, '70s-themed ads and commercials, but it
has since been discontinued again.

McDonald's: Hula Burger

The Hula Burger, introduced in the 1960s, was intended to be a
meat-free option for Catholic customers who couldn't eat meat on
Fridays during Lent. Positioned to compete against the Filet-o-Fish,
the pineapple-and-cheese burger ultimately failed and was pulled from
the menu because the Filet-o-Fish was much more popular.


McDonald's: Fish McBites

Fish McBites were also added to the menu as another fish option, but
they failed to do anything to help McDonald's sales and were
eventually taken off the menu in 2013.

McDonald's: McAfrika

The McAfrika was one of McDonald's worst PR disasters because it was
launched in Norway, one of the world's wealthiest countries, when
millions in South Africa were starving. The sandwich was made with
beef, cheese, and vegetables on a pita, and was quickly pulled from
the menu in 2002.


McDonald's: McStuffins

McStuffins, which look a lot like Hot Pockets, were made from French
bread filled with ingredients like pepperoni or teriyaki chicken.
McDonald's attempt at Hot Pockets lasted less than a year and were
removed from the menu in 1993.

McDonald's: McDLT

The McDLT, short for McDonald's Lettuce Tomato, separated the lettuce
and tomato from the burger, placing them in separate styrofoam
containers for "maximum freshness." It was taken off the menu in 1991
after receiving backlash from environmental activists.


McDonald's: McSalad Shakers

Introduced in 2000, McSalad Shakers didn't last too long on the
McDonald's menu, perhaps because not enough people were interested in
buying a shakeable salad. There's a Facebook group full of fans
advocating to bring back the Salad Shakers, but it hasn't been active
since 2016.

McDonald's: Mighty Wings

McDonald's Mighty Wings failed for a few reasons, mainly that they
were too expensive and too spicy for McDonald's customers' tastes. The
were on the menu from 1990 to 2003.


McDonald's: Chicken Fajitas/Breakfast Burritos

McDonald's briefly tried selling Mexican food, but the fajitas and
breakfast burritos were pulled from the menu in the 1990s, most likely
because they couldn't complete with Taco Bell's offerings. There's a
Facebook group advocating to bring them back, but it only has about
650 likes.

McDonald's: Arch Deluxe

The Arch Deluxe, which was introduced in 1996, was one of the most
expensive failures ever for McDonald's. The advertising budget was
upwards of $150 million, according to The New York Times. Even though
the Arch Deluxe cost McDonald's millions and was discontinued in the
late '90s, the Arch sauce - a mustard-mayo combination - is in testing
again, on a new fresh-beef burger called the Archburger.


McDonald's: McSpaghetti

McSpaghetti was introduced in the 1970s. Even though it was
discontinued in the United States, it's still on the menu
internationally in the Philippines.

McDonald's: McHotdog

Even though McDonald's founder Ray Kroc said in his autobiography that
the chain would never sell hot dogs because of quality concerns,
McDonald's launched the McHotdog in 1995 anyway. It didn't go over
well with customers and was later pulled from the menu.

Taco Bell: Waffle Taco

Taco Bell's Waffle Tacos - scrambled eggs and sausage inside of a
folded waffle - received a lot of attention when they were first
announced in 2013, but they were eventually replaced by similarly
constructed biscuit tacos.

Taco Bell: Seafood Salad

As a response to fish-fillet sandwiches from other fast-food
restaurants, Taco Bell launched the seafood salad in the 1980s. The
salad made with shrimp, whitefish, and snow crab did not go over well
with customers and was eventually removed from the menu.

Burger King: Burger Shots

Burger King repeatedly tried to sell sliders, first as Burger Bundles,
then as Burger Buddies, and eventually as Burger Shots, which were
unpopular and eventually discontinued in 2004.

Burger King: Enormous Omelette Sandwich

The Enormous Omelette sandwich from Burger King, introduced to the
menu in 2005, was mainly discontinued because of health concerns - it
had 330 milligrams of cholesterol and 1,940 milligrams of sodium.

Burger King: Satisfries

Satisfries were a low-calorie alternative to Burger King's traditional
fries, but they sold poorly because people preferred the regular
french fries. They were discontinued in 2014.

Burger King: Shake Em Up Fries

Fast food has seen its share of flops over the years.

Shake 'Em Up fries, launched in 2002, came with a packet of cheese
powder that customers had to pour into the bag and shake to make
cheese fries.

McDonald's: McLean Deluxe

The McLean Deluxe claimed to have 91% less fat than a Big Mac and had
seaweed extract in place of fatty content. It was dropped from the
menu in 1996.

Dairy Queen: Dairy Queen Breeze

The Dairy Queen Breeze launched in 1990 as a frozen yogurt alternative
to the Blizzard, but it was discontinued in 2000 because sales were
disastrous.

Wendy's: Frescata

This deli-style sandwich was pulled in 2007 after just one year on the
menu because it wasn't selling well.

Wendy's: Superbar

Wendy's used to have an all-you-can-eat salad bar/buffet, but it
wasn't quite fast food and eventually proved unsuccessful before being
pulled in 1998.

Jack In The Box: Frings

Frings, introduced in 1979, were a french fry/onion ring combo that
was discontinued shortly after being released.

Sonic: Pickle O's

Pickle O's were initially introduced in 1968 and brought back to the
menu in 2003. Even though these fried pickles were officially
discontinued, people claim you can still order them simply by asking
for fried pickles.

Domino's: Oreo Dessert Pizza

First offered in 2007, this dessert pizza was quickly discontinued
because people claimed it was too sweet.

Pizza Hut: Priazzo

Made in 1985 to resemble a Chicago-style deep-dish pizza, the Priazzo
failed because it took too long to prepare for a fast-food
establishment.

* Copyright Â© 2018 Insider Inc. All rights reserved. Registration on
or use of this site constitutes acceptance of our Terms of Service and
Privacy Policy.




14 of the most outlandish fast food abominations of 2017
JENNIFER MACHINNov 27, 2017
     
2017 has been challenging for many reasons, but we didn't expect fast
food to be one of them. Sadly, here we are.

Don't believe me? Just take a look at this year's most bizarre
creations â anything from chicken scented bath bombs to chicken
coffee. All of that actually happened this year, and they weren't even
the worst.

Take a look at a few of the atrocities that fast food companies rolled
out in this sad, sad year.

1. Volcano Crispy Chicken Chips

Taco Bell tested out these spicy triangular fried chicken chips in the
Knoxville, Tennessee, area around January.

They are chips. Made of chicken.



2. The Naked Chicken Chalupa 

About a week later, they announced a chicken shell.



3. Naked Chicken Chips aka Nuggets

Months later, Taco Bell released the chip version of the Naked Chicken
Chalupa which was basically chicken nuggets with their signature Nacho
cheese dipping sauce.

4. Sweet & Crunchy Tenders

Popeyes released their Sweet & Crunchy Tenders made with shortbread
cookie coating.

5. Lucky Charms Shake

Burger King introduced this sweet shake made of soft vanilla ice
cream, syrup, and Lucky Charms.

6. Minions Everything

McDonald's released Minion-themed food and toys in Singapore
locations. That included banana pie, Minion-shaped potatoes, spicy
chicken nuggets, and banana ice cream.

Make it end.



 7. Zinger Meteorite

KFC's specialty website, KFC Limited, was selling a $20,000 meteorite
shaped like a Zinger Chicken Sandwich.


8. Firecracker Burrito 

Taco Bell introduced the Firecracker Burrito which is made up of rice,
cheese, beef, tortilla strips, and spicy pop rocks. Yes, as in the
candy.

9. Naked Egg Taco

Taco Bell continuously pushes the bar with weird foods and this time it was a fried egg as a shell. 
You could also, quite easily, think of it as a vertical omelet. 
Because that's what it is.



10. Chocoladilla

After testing it out in the UK, Taco Bell brought the Kit Kat
Quesadilla to the U.S.

11. KFC Bath Bombs




12. Rick and Morty's Szechuan sauce 

Select McDonald's locations gave away the classic Szechuan sauce, in a
nod to the Cartoon Network show, only on Oct. 7. It was a shit show.



13. Buffalo-flavored latte

Tim Hortons released a "zesty buffalo seasoning" coffee drink in two
stores in Buffalo, New York.



14. McVegan 
McDonald's tested out their own vegan burger in Tampere, Finland. 

OK, this one doesn't sound so bad. 



The 10 Craziest Fast Food Items That Broke The Internet In 2017

Constantine Spyrou
Dec 16, 2017

When it comes down to who made the craziest fast food items, chains
really upped their game in 2017. Everybody was crafting concoctions
that bordered sheer insanity, whether it be for their looks, calorie
content, or how much it drove fans berserk. Not all items generated
hype from the major fast food players this year, but these ten were
the ones that pushed the limits of total absurdity.

Unicorn Frappuccino - Starbucks

To be honest, I'm not sure whether this wacky drink broke baristas
more than it did the internet. Still, the color-changing,
terrible-tasting frappuccino went viral everywhere for its looks,
which made it a huge hit on Instagram. This epitome of unicorn food
was only sold for a few days, but that was enough to leave a lasting
impact.

Firecracker Burrito - Taco Bell
spicy pop rocks burrito is back

You'd think Pop Rocks and burritos wouldn't go well together, but Taco
Bell found a way to make it happen with this eye-popping item. The
spicy Pop Rocks added a whole new level of texture that was
unprecedented in terms of fast food items. While it was only available
as a test item this year, the hype surrounding it could lead to bigger
launches in the future.

Cookie Dough Tenders - Popeyes

Another mashup between the realms of sweet and savory, Popeyes crusted
some of their chicken tenders in shortbread cookie dough. These Sweet
& Crunchy tenders drew long lines the instant they came out, and drew
some high praise from our fried chicken expert, Reach. It also pushed
the bounds of just what could be used as fried chicken batter, making
us wonder what's coming next.

McVegan - McDonald's

McDonald's is now the first major fast food burger joint to offer a
full vegan burger, and this McVegan actually received praise from
PETA. It's insane how long it took for this item to surface, but the
plant-based meat movement was in full swing during 2017. While it's
only in Sweden and Finland for now, initial tests are doing very well,
so it may spread even further next year.

Arbynator - Arby's

 WOW THIS LOOKS GROSS
(as I wait til everyone falls asleep so I can sneak away and eat 3 arbynator's at 1am)

The Arbynator may have just come out last week, but its gargantuan
size is enough to vault it into this top ten. At a half pound of meat,
curly fries, and multiple sauces on the inside, there's only one other
sandwich as gluttonous as this one that came out this year.

Farmhouse King - Burger King

Burger King's contribution to this list involves it's most caloric
burger of all time. At 1,220 calories per sandwich, this fried egg,
bacon, and crispy onion double cheeseburger is easily enough to
require an extra week at the gym. No fast food addition this year came
close to beating the Farmhouse King in terms of unhealthiness.

Kit Kat Quesadilla - Taco Bell

 I was just at my local Taco Bell, and they had a Kit Kat Quesadilla
 for $1. Which is odd, because thereâs nothing online about it in
 the US.


Dessert quesadillas, anyone? At just a buck each, Taco Bell began
testing Kit Kat AND Twix Quesadillas this year. The sweet candy fusion
turned a ton of heads and led to customer demands nationwide. We'll
have to see if this delirious dessert will show up next year or not.

Cherry Pie Frappuccino - Starbucks

While the Unicorn Frappuccino was crazy on a whole bunch of different
levels, it didn't have one insane addition that this drink did: A pie
crust lid. Starbucks Japan sold the Cherry Pie Frappuccino for the
whole month of April, and fans were drawn to it, both for the sweet
flavors inside and the innovative pastry on the outside. We've never
seen anything like it here in the U.S., but the crunchy add-on would
definitely be a dope menu option.

Naked Chicken Chalupa - Taco Bell

When Taco Bell first announced their fried chicken taco shell, fans
went absolutely nuts. The hyped continued throughout the year with its
national launch, along with its return as a Bacon Ranch Naked Chicken
Chalupa. The concept led Taco Bell to innovate even further with
protein taco shells, with their breakfast Naked Egg Taco being an
example of their continual envelope pushing. There was nothing normal
about the Naked Chicken Chalupa at first, but now that it's arrived,
the norms have clearly changed.

Szechuan Sauce - McDonald's

While Szechuan Sauce isn't exactly new, having been released for a
limited time in the 90s, its Rick & Morty-fueled return escalated to
extreme levels of excitement. Hardcore fans demanded the condiment,
then once they got it, called for more. McDonald's couldn't keep up
with the growing hype of the Szechuan Sauce, as their ultra-limited
release pissed off some fans to the point of police being called. No
2017 item was obsessed over more than the Mulan McNugget Sauce, that's
for sure.

"""


def make_fast_food_joint_name():

    #make Type 2 less common - it's a bit boring
    #name_type = random.choice(("Type 1", "Type 1M", "Type 2", "Type 3")) #, "Type 4"))
    name_type = random.choice(("Type 1", "Type 1M", "Type 2", "Type 3",
        "Type 1", "Type 1M", "Type 3",
        "Type 1", "Type 1M", "Type 3"))
    if name_type == "Type 1":
        #simplest version...
        real_places = ["Pizza Hut", "Shake Shack", "Chicken Cottage"]
        word_1 = ["Burger", "Chicken", "Fast Food", "Hamburger", "Fried Chicken"]
        word_2 = ["Hut", "Shack", "Cottage", "Shack", "Cabin", "Shed",
                  "Den", "Lodge", "Box", "House", "Joint", "Palace"]
        jointname = "%s %s" % (random.choice(word_1), random.choice(word_2))
        while jointname in real_places:
            jointname = "%s %s" % (random.choice(word_1), random.choice(word_2))
    elif name_type == "Type 1M":
        #Mc"simplest version"
        real_places = ["Pizza Hut", "Shake Shack", "Chicken Cottage"]
        word_1 = ["Burger", "Chicken", "FastFood", "Hamburger", "Chicken"]
        word_2 = ["Hut", "Shack", "Cottage", "Shack", "Cabin", "Shed",
                  "Den", "Lodge", "Box", "House", "Joint", "Palace"]
        jointname = "Mc%s%s" % (random.choice(word_1), random.choice(word_2))
        while jointname in real_places:
            jointname = "%s %s" % (random.choice(word_1), random.choice(word_2))
    elif name_type == "Type 2":
        #KFC analogue
        letter = random.choice(string.uppercase)
        while letter in "KFC":
            letter = random.choice(string.uppercase)
        jointname = random.choice(("%sFC" % letter,
                                  "%sFC" % letter,
                                  "%s F C" % letter,
                                  "%s.F.C" % letter))
    elif name_type == "Type 3":
        #Kentucky Fried Chicken analogue
        #U.S. State Capitals
        #source": "Wikipedia: List of U.S. state capitals"
        state_capitals = ["Montgomery", "Juneau", "Phoenix", "Little Rock", "Sacramento",
                          "Denver", "Hartford", "Dover", "Tallahassee", "Atlanta", "Honolulu",
                          "Boise", "Springfield", "Indianapolis", "Des Moines", "Topeka",
                          # "Frankfort",
                          "Baton Rouge", "Augusta", "Annapolis", "Boston", "Lansing",
                          "Saint Paul", "Jackson", "Jefferson City", "Helena", "Lincoln",
                          "Carson City", "Concord", "Trenton", "Santa Fe", "Albany",
                          "Raleigh", "Bismarck", "Columbus", "Oklahoma City", "Salem",
                          "Harrisburg", "Providence", "Columbia", "Pierre", "Nashville",
                          "Austin", "Salt Lake City", "Montpelier", "Richmond", "Olympia",
                          "Charleston", "Madison", "Cheyenne"
                          ]

        states = [ "Alabama", "Alaska", "Arizona", "Arkansas", "California",
                   "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii"
                   "Idaho", "Illinois", "Indiana", "Iowa", "Kansas",
                   # "Kentucky"
                   "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                   "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska",
                   "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
                   "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                   "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee"
                   "Texas", "Utah", "Vermont", "Virginia", "Washington"
                   "West Virginia", "Wisconsin", "Wyoming"
                   ]
        jointname = random.choice(("%s Fried Chicken" % random.choice(state_capitals),
                                   "%s Fried Chicken" % random.choice(states)))

    #elif name_type == "Type 4":


    return jointname


#SPAM0

#Have Randomly Generated Cocktail Names In The Pub/ Lounge Bar.

#Multiple, Slippery, Screaming, Wet, LONG ISLAND, Classic, Old, Dirty, Drunken, Fearless, Liquid 
#Tropical, Naked, Fuzzy, Fiery, Crazy, Crouching, Flaming, Flying, Super, Long, Slow, Comfortable

#[COLOUR]
#Pink, Red, Blue, White, Black

#Nipple, Orgasm, Gorilla, Elf, Redneck, Zombie, Russian, Bee, Tiger, Elephant, Grasshopper

#AGAINST THE WALL, ON THE BEACH, Juice

def make_random_cocktail_name(mode=None):
    #Have Randomly Generated Cocktail Names In The Pub/ Lounge Bar.
    if mode == "clean":
        first_words = (
                           "Alien",
                           "Atomic",
                           #"Bloody",
                           "Cheeky",
                           "Caribbean",
                           "Classic",
                           "Comfortable",
                           "Crafty",
                           "Crazy",
                           "Creamy",
                           "Crouching",
                           "Dirty",
                           #"Drunken",
                           "Fearless",
                           "Fiery",
                           "Flaming",
                           "Flying",
                           "Foggy",
                           "Fuzzy",
                           "Hillbilly",
                           "Hot",
                           #"Juicy",
                           "Jungle",
                           "Liquid",
                           "Lonely",
                           "Long Island",
                           "Long",
                           "Lost",
                           "Mexican",
                           "Multiple",
                           #"Naked",
                           "Naughty",
                           "Nuclear",
                           "Old",
                           "Prairie",
                           "Quick",
                           "Royal",
                           "Rusty",
                           "Sandy",
                           "Screaming",
                           #"Sex",
                           #"Sexy",
                           "Short",
                           "Slippery",
                           "Slow",
                           "Strawberry",
                           "Super",
                           "Three-Legged",
                           "Tropical",
                           #"Wet",
                           #"Soft",
                           #"Hard",
                           "Double",
                           "Single",
                           "Wicked",
                           "Big",
                           "Massive",
                           #"Horny",
                           "Dancing",
                           "Happy",
                           "Clockwork",
                           "Sunset",
                           "Cynical",
                           #"Obscene",
                           "Negative",
                           "Flying",
                           "Laser",
                           "Space",
                           "Photon",
                           "Hairy",
                           "Wild",
                           #"Bikini",
                           "Muddy",
                           "Quantum",
                           #"Slutty",
                           "Fizzy"#,
                            )

        word_1 = random.choice(first_words)
        #[COLOUR]
        colour_word = random.choice(("Pink",
                                 "Red",
                                 "Blue",
                                 #"White",
                                 #"Black",
                                 "Golden",
                                 #""
                                 ))
                                 
        last_word = random.choice((
                           #"",
                           "Alien",
                           "Bee",
                           #"Bottom",
                           "Butterfly",
                           "Cat",
                           "Dwarf",
                           "Earthquake",
                           "Elephant",
                           "Elf",
                           "Girl Scout",
                           "Girl",
                           "Gorilla",
                           "Grasshopper",
                           #"Hooker",
                           "Hurricane",
                           "Kool Aid",
                           "Lady",
                           "Lady",
                           "Librarian",
                           "Machine",
                           #"Mexican",
                           "Midget",
                           "Monkey",
                           #"Nipple",
                           #"Orgasm",
                           "Potion",
                           "Redneck",
                           "Russian",
                           "Sailor",
                           "Secretary",
                           #"Slut",
                           #"Stripper",
                           "Tiger",
                           "Volcano",
                           #"Wench",
                           "Zombie",
                                 #""
                           #"Innuendo",
                           "Robot",
                           "Death",
                           "Nun",
                           "Thing",
                           "Wedgie",
                           "Tornado",
                           "Squirrel",
                           "Blonde"#,
                                 ))

        suffix = random.choice((
                           "Against The Wall",
                           #"Between the Sheets",
                           "In The Bush",
                           #"in the Crack",
                           #"in the Sack",
                           "in the Woods",
                           "On The Beach",
                           #"in Bed",
                           "in the Park",
                           "in the Dark",
                           "in the Rain",
                           "After Dark",
                           "Juice",
                           "Juice",
                           "Juice",
                           "Special",
                           "Special",
                           "Special",
                           "",
                           ""
                                 #"",
                                 #""
                                 ))
        
    else:
        first_words = (
                           "Alien",
                           "Atomic",
                           "Bloody",
                           "Cheeky",
                           "Caribbean",
                           "Classic",
                           "Comfortable",
                           "Crafty",
                           "Crazy",
                           "Creamy",
                           "Crouching",
                           "Dirty",
                           "Drunken",
                           "Fearless",
                           "Fiery",
                           "Flaming",
                           "Flying",
                           "Foggy",
                           "Fuzzy",
                           "Hillbilly",
                           "Hot",
                           "Juicy",
                           "Jungle",
                           "Liquid",
                           "Lonely",
                           "Long Island",
                           "Long",
                           "Lost",
                           "Mexican",
                           "Multiple",
                           "Naked",
                           "Naughty",
                           "Nuclear",
                           "Old",
                           "Prairie",
                           "Quick",
                           "Royal",
                           "Rusty",
                           "Sandy",
                           "Screaming",
                           "Sex",
                           "Sexy",
                           "Short",
                           "Slippery",
                           "Slow",
                           "Strawberry",
                           "Super",
                           "Three-Legged",
                           "Tropical",
                           "Wet",
                           #""
                           "Soft",
                           "Hard",
                           "Double",
                           "Single",
                           "Wicked",
                           "Big",
                           "Massive",
                           "Horny",
                           "Joy",
                           "Dancing",
                           "Happy",
                           "Clockwork",
                           "Sunset",
                           "Cynical",
                           "Obscene",
                           "Negative",
                           "Flying",
                           "Laser",
                           "Space",
                           "Photon",
                           "Hairy",
                           "Wild",
                           "Bikini",
                           "Muddy",
                           "Quantum",
                           "Slutty",
                           "Fizzy"#,
                            )

        word_1 = random.choice(first_words)
        #[COLOUR]
        colour_word = random.choice(("Pink",
                                 "Red",
                                 "Blue",
                                 "White",
                                 "Black",
                                 "Golden",
                                 #""
                                 ))
                                 
        last_word = random.choice((
                           #"",
                           "Alien",
                           "Bee",
                           "Bottom",
                           "Butterfly",
                           "Cat",
                           "Dwarf",
                           "Earthquake",
                           "Elephant",
                           "Elf",
                           "Girl Scout",
                           "Girl",
                           "Gorilla",
                           "Grasshopper",
                           "Hooker",
                           "Hurricane",
                           "Kool Aid",
                           "Lady",
                           "Lady",
                           "Librarian",
                           "Machine",
                           #"Mexican",
                           "Midget",
                           "Monkey",
                           "Nipple",
                           "Orgasm",
                           "Potion",
                           "Redneck",
                           "Russian",
                           "Sailor",
                           "Secretary",
                           "Slut",
                           "Stripper",
                           "Tiger",
                           "Volcano",
                           "Wench",
                           "Zombie",
                                 #""
                           "Innuendo",
                           "Robot",
                           "Death",
                           "Nun",
                           "Thing",
                           "Wedgie",
                           "Tornado",
                           "Squirrel",
                           "Blonde"#,
                                 #""
                                 #""
                                 #""
                                 #""
                                 ))

    suffix = random.choice((
                           "Against The Wall",
                           "Between the Sheets",
                           "In The Bush",
                           "in the Crack",
                           "in the Sack",
                           "in the Woods",
                           "On The Beach",
                           "in Bed",
                           "in the Park",
                           "in the Dark",
                           "in the Rain",
                           "After Dark",
                           "Juice",
                           "Juice",
                           "Juice",
                           "Special",
                           "Special",
                           "Special",
                           "",
                           ""
                                 #"",
                                 #""
                                 ))

    #AGAINST THE WALL, ON THE BEACH, Juice
    #cocktail_type = random.choice((1,1,1,1, 2,2,2, 3,3,4,4, 5,6,7,8))
    cocktail_type = random.choice((1,1,1,1, 2,2,2, 3,3,4,4, 5,8))
    if cocktail_type == 1:
        return "%s %s" % (word_1, last_word)
    elif cocktail_type == 2:
        word_1a = random.choice(first_words)
        while word_1a == word_1:
            word_1a = random.choice(first_words)
        return "%s %s %s" % (word_1, word_1a, last_word)
    elif cocktail_type == 3:
        return "%s %s %s" % (word_1, colour_word, last_word)
    elif cocktail_type == 4:
        return "%s %s" % (colour_word, last_word)

    elif cocktail_type == 5:
        return "%s %s %s" % (word_1, last_word, suffix)
    elif cocktail_type == 6:
        word_1a = random.choice(first_words)
        while word_1a == word_1:
            word_1a= random.choice(first_words)
        return "%s %s %s %s" % (word_1, word_1a, last_word, suffix)
    elif cocktail_type == 7:
        return "%s %s %s %s" % (word_1, colour_word, last_word, suffix)
    elif cocktail_type == 8:
        return "%s %s %s" % (colour_word, last_word, suffix)


spirits_list = [
        'Passoa "The Passion Drink" Liqueur',
        "151 Rum",
        "151-proof Rum",
        "Absolut Citron Vodka",
        "Amaretto Almond Liqueur",
        "Amaretto",
        "Amarula Cream",
        "Aperol",
        "Apple Pucker",
        "Aristocrat Triple Sec",
        "Bacardi 151",
        "Bacardi Carta Blanca Superior White Rum",
        "Bacardi Golden Rum",
        "Bailey's Irish Cream",
        "Banana Liqueur",
        "Barrow's Intense Ginger Liqueur",
        "Blackbeard Spiced Rum",
        "Blue Curacao",
        "Bourbon",
        "Brandy",
        "Brut Champagne",
        "Butterscotch Schnapps",
        "Campari",
        "Captain Morgan Rum",
        "Cava",
        "Chambord",
        "Champagne",
        "Cherry Liqueur",
        "Cherry Vodka",
        "Cinnamon Schnapps",
        "Coconut Rum",
        "Coffee Liqueur",
        "Cognac",
        "Cointreau",
        "Creme de Almond",
        "Creme De Banane Liqueur",
        "Creme De Menthe",
        "Crown Royal Canadian Whiskey",
        "Crown Royal",
        "Curacao",
        "Dark Rum",
        "DeKuyper Buttershots Liqueur",
        "Drambuie",
        "Dry Vermouth",
        "Fireball Cinammon Whiskey",
        "Frangelico Hazelnut Liqueur",
        "Galliano",
        "Gin",
        "Gold Rum",
        "Goldschlager Cinnamon Schnapps",
        "Goldschlager",
        "Grain Alcohol",
        "Hazelnut Liqueur",
        "Hpnotiq Liqueur",
        "Irish Cream",
        "Irish Liqueur",
        "Jack Daniels",
        "Jacquin's Orange Flavoured Gin",
        "Jagermeister",
        "Jameson",
        "Jim Beam Black Label Bourbon",
        "Jim Beam",
        "Johnnie Walker Black",
        "Jose Cuervo Gold Tequila",
        "Kahlua Coffee Liqueur",
        "Kahlua Liqueur",
        "Kahlua",
        "Ketel One Vodka",
        "Lemon Vodka",
        "Light Rum",
        "Malibu Coconut Rum",
        "Malibu Rum",
        "Mango Vodka",
        "Maraschino Liqueur",
        "Melon Liqueur",
        "Mezcal",
        "Midori Liqueur",
        "Midori Melon Liqueur",
        "Midori",
        "Oloroso Sherry",
        "Orange Curacao Liqueur",
        "Orange Curacao",
        "Orange Liqueur",
        "Orange Rum",
        "Passoa Liqueur",
        "Peach Schnapps",
        "Peppermint Liqueur",
        "Peppermint Schnapps",
        "Pernod",
        "Pina Colada Schnapps",
        "Pomegranate Vodka",
        "Prickly Pear-Infused Mezcal",
        "Prosecco",
        "Rakija", # fruit brandy popular in the Balkans
        "Raspberry Liqueur",
        "Raspberry Vodka",
        "Rum",
        "Rumple Minze Peppermint Liqueur",
        "Rye Whiskey",
        "Sambuca",
        "Scotch",
        "Sherry",
        "Silver Tequila",
        "Sloe Gin",
        "Smirnoff Vodka",
        "Sour Apple Pucker",
        "Southern Comfort Peach Liqueur",
        "Southern Comfort",
        "Spiced Rum",
        "Stolichnaya Vodka",
        "Strawberry Schnapps",
        "Sweet Vermouth",
        "Tequila Rose strawberry cream liqueur",
        "Tequila",
        "Triple Sec",
        "Vanilla Vodka",
        "Vodka",
        "Whisky",
        "White Creme de Cacao",
        "White Rum",
        "Wild Berry Schnapps"#,
        ]

mixers_list = [
        "7 Up",
        "a Maraschino Cherry",
        "Benadictine",
        "Cherry Juice",
        "Citrus Soda",
        "Club Soda",
        "Coconut Cream",
        "Coconut",
        "Cola",
        "Cranberry Juice",
        "Cranberry-Raspberry Juice",
        "Cream",
        "Double Cream",
        "Fernet-Branca",
        "Fresh Banana",
        "Fresh Lemon Juice",
        "Fresh Lime Juice",
        "Freshly Brewed Espresso",
        "Frozen Pink Lemonade",
        "Frozen Strawberries",
        "Fruit Punch",
        "Ginger Ale",
        "Grapefruit Juice",
        "Grenadine Syrup",
        "Grenadine",
        "Half And Half Cream",
        "Half-and-Half",
        "Honey",
        "Lemon Juice",
        "Lemon-Lime Soda",
        "Lemon",
        "Lemonade",
        "Lime Juice",
        "Lime Soda Water",
        "Lime",
        "Lychee Liqueur",
        "Mango Nectar",
        "Maraschino Cherries",
        #"Milk",
        "Mint",
        "No Fear Energy Drink",
        "One Whole Lime",
        "Orange Juice",
        "Passion Fruit Juice",
        "Passion Fruit",
        "Pineapple Juice",
        "Pineapple",
        "Pink Lemonade",
        "Pomegranate",
        "Raspberry-Lime Sorbet",
        "Red Bull",
        "Soda Water",
        "Sprite",
        "Star Fruit",
        "Strawberries",
        "Strawberry Daiquiri Mix",
        "Sugar Syrup",
        "Sugar",
        "Sweet and Sour Mix",
        "Switchel", # water mixed with vinegar, and often seasoned with ginger
        "Tabasco Sauce",
        "Thai Basil",
        "Tomato Juice",
        "Tonic Water",
        "Vanilla Sugar Syrup",
        "Whipped Cream",
        "Worcestershire Sauce"#,
        ]

poss_glasses = [
                #"beer mug",
                "beer stein",
                "cocktail glass",
                "collins glass",
                "highball glass",
                "hurricane glass", 
                "old fashioned glass",
                "pilsner glass", 
                "rocks glass",
                "shot glass",
                "wine glass",
    ]

poss_garnishes = [
                "orange slice",
                "skewered slice of orange",
                "candied ginger",
                "lime",
                "cherry",
                "lime wedge",
                "orange peel",
                #"candy cane",
                "mint leaves",
                "lemon wedge",
                "lemon twist",

    ]

#SPAM10

real_cocktails = {

#The 10 Most Bizarre Cocktail Names
    "Juicy Lucy":               {"name":            "Juicy Lucy",
                                "ingredients":  [   "Vodka",
                                                    "Gin",
                                                    "Blue Curacao",
                                                    "Orange Juice",
                                                    "Sprite"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "collins glass",
                                 "garnish":         "orange slice",
                                 "ice":             "yes"
                },

    "Drunken Sailor":           {"name":            "Drunken Sailor",
                                "ingredients":  [   "Rum",
                                                    "Gin",
                                                    "Ginger Ale",
                                                    "Lime Juice"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           "pilsner glass", #"copper mug",
                                 "garnish":         ["skewered slice of orange", "candied ginger", "lime", "cherry"],
                                 "ice":             "yes"
                },

    "Dances with Wenches":      {"name":       "Dances with Wenches",
                                "ingredients":  [   "Blackbeard Spiced Rum",
                                                    "Cranberry Juice"],
                                 "name type":       "clean",
                                 "colour":          None, #pink!
                                 "glass":           "collins glass",
                                 "garnish":         "lime wedge",
                                 "ice":             "yes"
                },

    "A Short Trip to Hell":      {"name":       "A Short Trip to Hell",
                                "ingredients":  [   "Peach Schnappps",
                                                    "Strawberry Schnappps",
                                                    "Wild berry Schnappps",
                                                    "Red Bull",
                                                    "Jagermeister"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           "collins glass", #"highball glass"
                                 "garnish":         None,
                                 "ice":             "yes"
                },

    "Voodoo":      {"name":       "Voodoo",
                                "ingredients":  [   "Amber Rum",
                                                    "Red Vermouth",
                                                    "Apple Juice",
                                                    "Lime Juice",
                                                    "Sugar Syrup"],
#                                "ingredients":  [   "Mint",
#                                                    "Mango vodka",
#                                                    "Mango nectar"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           "highball glass", #"collins glass",
                                 "garnish":         None,
                                 "ice":             "yes"
                },

    "Mikey's Breakfast Banger":      {"name":       "Mikey's Breakfast Banger",
                                "ingredients":  [   "Club Soda",
                                                    "Orange Juice",
                                                    "Amaretto"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           "wine glass",
                                 "garnish":         "orange peel",
                                 "ice":             "no"
                },

    "Drunken Elf":      {"name":       "Drunken Elf",
                                "ingredients":  [   "Bacardi Golden Rum",
                                                    "Pink Lemonade"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           "old fashioned glass",
                                 "garnish":         "candy cane",
                                 "ice":             "no"
                },

    "Fearless Redneck":      {"name":       "Fearless Redneck",
                                "ingredients":  [   "Jim Beam Black Label Bourbon",
                                                    "No Fear Energy Drink"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           "beer stein", #"beer mug"
                                 "garnish":         "mint leaves",
                                 "ice":             "no"
                },

    "Sand in the Crack":      {"name":       "Sand in the Crack",
                                "ingredients":  [   "Malibu Coconut Rum",
                                                    "Captain Morgan Rum",
                                                    "Pineapple Juice",
                                                    "Cranberry Juice"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "hurricane glass", #"highball glass"
                                 "garnish":         None,
                                 "ice":             "yes"
                },

    "Hop, Skip, and Go Naked":      {"name":       "Hop, Skip, and Go Naked",
                                "ingredients":  [   "Lemon Vodka",
                                                    "Grapefruit Juice",
                                                    "Beer"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "collins glass",
                                 "garnish":         "lemon wedge", # ["lemon zest, "lime zest"]
                                 "ice":             "yes"
                },
    #10 REALLY BIZARRE COCKTAIL NAMES
    "Fuzzy Navel":      {"name":       "Fuzzy Navel",
                                "ingredients":  [   "Peach Schapps",
                                                    "Orange Juice"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           "highball glass",
                                 "garnish":         "orange slice",
                                 "ice":             "yes"
                },

    "B.A.F.":      {"name":       "B.A.F.", 
                                "ingredients":  [   "Aperol",
                                                    "Sherry",
                                                    "Scotch"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           "rocks glass",
                                 "garnish":         None, #"lemon twist",
                                 "ice":             "yes"
                },


##    "A Lonely Island Lost in the Middle of a Foggy Sea":      {"name":       "A Lonely Island Lost in the Middle of a Foggy Sea",
##                                "ingredients":  [   "
##
##Finding a cocktail with an 11-word name is a rare treat. This cocktail
##from Chicago-based bartender Paul McGee turns the fun-loving culture
##of tiki drinking on its head with a deeply somber name."]
##                },
##
##
##
##
##    "Sex on the Beach":      {"name":       "Sex on the Beach",
##                                "ingredients":  [   "
##
##What would this list be without mentioning this classic vacation
##cocktail? Born in Florida, this cocktail has remained a Spring Break
##staple since its invention in the 1970s."]
##                },



    "Redheaded Slut":      {"name":       "Redheaded Slut",
                                "ingredients":  [   "Jagermeister",
                                                    "Peach Schnapps",
                                                    "Cranberry Juice"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "rocks glass", #"shot glass",
                                 "garnish":         None,
                                 "ice":             "yes"
                },

    "Monkey Gland":      {"name":       "Monkey Gland",
                                "ingredients":  [   "Gin",
                                                    "Pernod",
                                                    "Orange Juice",
                                                    "Grenadine"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 #"glass":           "old fashioned glass", # "cocktail glass"
                                 "glass":           "cocktail glass", #"old fashioned glass"
                                 "garnish":         "orange slice",
                                 "ice":             "no"
                },

    "Afternoon Delight":      {"name":       "Afternoon Delight",
                                "ingredients":  [   "Vodka",
                                                    "Blue Curacao",
                                                    "Creme de Peche",
                                                    "Malibu",
                                                    "Pineapple Juice"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           "collins glass",
                                 "garnish":         "orange slice",
                                 "ice":             "yes"
                },


##
##    "Goat's Delight":      {"name":       "Goat's Delight",
##                                "ingredients":  [   "
##
##Usually, goats and cocktails do not go together. (Or so we hear.)
##Created before prohibition, itâs still a mystery how this forgotten
##recipe gained its name. One thing is for sure: Do not give this drink
##to your goat."]
##                },
##
##
##
##
##    "A.M.F.":      {"name":       "A.M.F.",
##                                "ingredients":  [   "
##
##With four different types of liquor involved, this cocktail will no
##doubt knock you out for the night. Say Adios to the bartender and
##hello to your hangover."]
##                },

    "Bullfrog":      {"name":       "Bullfrog",
                                "ingredients":  [   "Gin",
                                                    "Tequila",
                                                    "Vodka",
                                                    "White Rum",
                                                    "Blue Curacao",
                                                    "Red Bull"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           "tall glass", #"pint glass"
                                 "garnish":         ["lemon slice", "cherry"],
                                 "ice":             "yes"
                },

    "Red Death":      {"name":       "Red Death",
                                "ingredients":  [   "Southern Comfort",
                                                    "Vodka",
                                                    "Amaretto",
                                                    "Triple Sec",
                                                    "Sloe Gin",
                                                    "Lime Juice",
                                                    "Orange Juice"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           "collins glass", #"highball glass", "tumbler"
                                 "garnish":         "orange Slice",
                                 "ice":             "yes"
                },

    "Brass Monkey":      {"name":       "Brass Monkey",
                                "ingredients":  [   "Vodka",
                                                    "Rum",
                                                    "Orange Juice"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           "highball glass",
                                 "garnish":         "orange slice",#"lemon slice",
                                 "ice":             "yes"
                },

    "Fat Like Buddha":      {"name":       "Fat Like Buddha",
                                "ingredients":  [   "Rum",
                                                    "Cointreau",
                                                    "Benadictine"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           "cocktail glass", #"rocks glass",
                                 "garnish":         "orange twist",
                                 "ice":             "no"
                },

##    "Set the New Year on Fire":      {"name":       "Set the New Year on Fire",
##                                "ingredients":  [   "
##
##Itâs not too often that a cocktail name offers a command. This
##uncommon New Year cocktail takes its name literally, with a flaming
##lime peel garnish. When the clock tolls midnight, listen to your drink
##and flame on."]
##                },
##

##
##Facets of Screwdriver
##A screwdriver (drink) with equal parts of vanilla vodka and Blue Curacao topped with lemon-lime soda is a "Sonic Screwdriver".
##A screwdriver with equal parts of vodka and Mountain Dew is a "Dew Driver".
##A screwdriver with one part of Southern Comfort and two parts of orange juice is a "Comfortable Screw".
##For some of us, a house full of guests is mere happiness. Arranging a get-together or a party will be a great way to gain joy. Selecting the drinks to be served for such an event is equally important, considering the age group and the party themes. Here is a fun-filled list of drinks that you can choose from, to thrill your guests.
##List of Funny Drink Names
##The Non-alcoholic Ones
##Planning to throw a party this weekend? Alcoholic cocktails would top the list, but the party welcomes kids and pregnant women too; or may be some who aren't in the mood of getting drunk.
##Make some colorful and fun-named drinks. Some quick-to-prepare and less costly (due to lack of liqueur) funny drink names include:
##
##â¢ Crazy cow
##â¢ Mickey mouse
##â¢ Pussy foot
##Pussy foot drink
##
##The Alcoholic Ones
##Alcoholic beverages serve the most popular drinking medium. For celebrations, parties, or whatever excuse we can find to drink, the alcoholic drinks don't really need a reason to fit in. The funnier ones add a little more fun to them. These are:
##
##â¢ Bee's knees drink
##â¢ Cement mixer
##â¢ Crouching tiger
##â¢ Elephant shake
##â¢ Flaming gorilla
##â¢ Flying Fair brother
##â¢ Fire hammer drink
##â¢ Grasshopper
##Grasshopper drink

##
##â¢ Hair of the dog
##â¢ RumChata
##â¢ Screwdriver
##â¢ Voodoo
##â¢ Swimming pool cocktail
##Swimming pool cocktail
##
##â¢ Strawberry cosmopolitan
##Strawberry drink
##
##â¢ The Bahama Mama cocktail
##â¢ Tom and Jerry drink
##The Energy Drinks
##Stay sharp, focused, and energetic all the time. For a quick pick-me-up during a slow afternoon at the office, or a booster dose while playing, let's have a look at the funny list below:
##

##â¢ Betty Boop Juice
##â¢ PAC-man energy drink
##â¢ Duracell
##â¢ Super Mario
##List of Bizarre Drinks
##These unusual drink names may seem interesting, but are a big deal to have them.
##
##â¢ Flaming volcano
##â¢ Earthquake
##â¢ Hurricane
##â¢ Mudslide
##Few Easy Non-alcoholic Drinks

    "Atomic Cat":      {"name":       "Atomic Cat",
                        #Atomic Cat, a non-alcoholic drink, is a refreshing cocktail; a perfect drink to cheer your mood.
                                "ingredients":  [   "Orange Juice",
                                                    "Tonic Water"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           "highball glass", #"collins glass", 
                                 "garnish":         "orange wheel",
                                 "ice":             "yes"
                },

    "Bora Bora":      {"name":       "Bora Bora",
                                "ingredients":  [   "Pineapple juice",
                                                    "passion fruit juice",
                                                    "lemon juice",
                                                    "grenadine syrup"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           "highball glass", #"hurricane glass", #"collins glass"
                                 "garnish":         ["cherry", "pineapple wedge"],#["cherry", "lime wheel"], 
                                 "ice":             "yes"
                },

    "Crouching Tiger":      {"name":       "Crouching Tiger",
                                "ingredients":  [   "Lychee Liqueur",
                                                    "Silver Tequila"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           "shot glass",
                                 "garnish":         None,
                                 "ice":             "no"
                },

    "Iron Butterfly":      {"name":       "Iron Butterfly",
                                "ingredients":  [   "Vodka",
                                                    "Kahlua Coffee Liqueur",
                                                    "Irish cream"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           "old fashioned glass",
                                 "garnish":         None,#filbert nuts (optional)
                                 "ice":             "yes"
                },

    "Screwdriver":      {"name":       "Screwdriver",
                                "ingredients":  [   "Orange Juice",
                                                    "Vodka"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           "highball glass",
                                 "garnish":         "orange slice",#"orange wedge",
                                 "ice":             "yes"
                },

    #7 Hilariously Named Cocktails from Bars Across the Country

    "Sometimes You Gotta Work a Little To Ball a Lot":      {"name":       "Sometimes You Gotta Work a Little To Ball a Lot",
                                #Where to find it: Hank's Oyster Bar, Washington, D.C.
                                "ingredients":  [   "Bourbon",
                                                    "Honey",
                                                    "Switchel",
                                                    "Lemon",
                                                    "Mint"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None, #???
                                 "garnish":         None, #???
                                 "ice":             None  #???
                },

    "Aloha Felicia":      {"name":       "Aloha Felicia", 
                                #Where to find it: Three Dots and a Dash, Chicago, IL
                                "ingredients":  [   "Rum",
                                                    "coconut",
                                                    "pineapple",
                                                    "Thai basil"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           "tall glass", #???
                                 "garnish":         ["pineapple slice", "paper umbrella"], #['Pineapple slices or lime slices']
                                 "ice":             "yes"
                },

    "Nip Slip":      {"name":       "Nip Slip", #SPAM
                                #Where to find it: Butter & Scotch, New York, NY
                                "ingredients":  [   "Cava",
                                                    "Barrow's Intense Ginger Liqueur",
                                                    "raspberry-lime sorbet"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Pho-King Champ":      {"name":       "Pho-King Champ",
                                #Where to find it: Midnight Rambler, Dallas, TX
                                "ingredients":  [   "Vodka",
                                                    "Oloroso Sherry",
                                                    "aromatized beef stock",
                                                    "cilantro leaf"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Grow a Pear":      {"name":       "Grow a Pear",
                                #Where to find it: Horchata, New York, NY
                                "ingredients":  [   "Prickly pear-infused mezcal",
                                                    "pomegranate",
                                                    "lime"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    #Drinks with Dirty Names
    "Between The Sheets":      {"name":       "Between The Sheets",
                                "ingredients":  [   "Cognac",
                                                    "Triple Sec",
                                                    "Light Rum",
                                                    "Fresh lemon juice"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "cocktail glass", #martini glass
                                 "garnish":         "lemon twist", #"orange peel",
                                 "ice":             "no"
                },

    "Pink Silk Panties":      {"name":       "Pink Silk Panties",
                                "ingredients":  [   "Vodka",
                                                    "Peach Schnapps",
                                                    "Cranberry Juice"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "cocktail glass", #martini glass
                                 "garnish":         "cherry",
                                 "ice":             "no"
                },

    "Dirty Whore's Bath Water":      {"name":       "Dirty Whore's Bath Water",
                                "ingredients":  [   "Vodka",
                                                    "Apple Pucker",
                                                    "Lemonade"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "shot glass",
                                 "garnish":         None,
                                 "ice":             "no"
                },

    "Bend Over Shirley":      {"name":       "Bend Over Shirley",
                                "ingredients":  [   "Raspberry Vodka",
                                                    "Grenadine Syrup",
                                                    "Sprite"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "collins glass",
                                 "garnish":         "cherry", #two Maraschino Cherries
                                 "ice":             "yes"
                },

    "Blow Job":      {"name":       "Blow Job",
                                "ingredients":  [   "Amaretto",
                                                    "Irish Cream",
                                                    "Whipped Cream"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "shot glass",
                                 "garnish":         "whipped cream",
                                 "ice":             "no"
               },

    "Dirty Banana":      {"name":       "Dirty Banana",
                                "ingredients":  [   "Bacardi Carta Blanca Superior White Rum",
                                                    "Coffee Liqueur",
                                                    "Creme de Banane Liqueur",
                                                    "Half and Half Cream",
                                                    "Milk",
                                                    "Fresh Banana"],
                                 "name type":       "clean", #-ish
                                 "colour":          None,
                                 "glass":           "collins glass", #"hurricane glass", #"martini glass", "cocktail glass",
                                 "garnish":         ["banana slice", "cherry"], #["unpeeled banana slice", "maraschino cherry"]
                                 "ice":             "no"
                },

    "Porn Star":      {"name":       "Porn Star", #SPAM99
                                "ingredients":  [   "Passion Fruit",
                                                    "Ketel One Vodka",
                                                    'Passoa "The Passion Drink" liqueur',
                                                    "Vanilla Sugar Syrup",
                                                    "Fresh Lime Juice",
                                                    "Brut champagne"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Red Headed Slut":      {"name":       "Red Headed Slut",
                                "ingredients":  [   "Cranberry Juice",
                                                    "Peach Schnapps",
                                                    "Jagermeister"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "rocks glass", #"shot glass",
                                 "garnish":         None,
                                 "ice":             "yes"
                },

    "Screaming Orgasm":      {"name":       "Screaming Orgasm",
                                "ingredients":  [   "Vodka",
                                                    "Coffee Liqueur",
                                                    "Amaretto",
                                                    "Bailey's Irish Cream",
                                                    "Half and Half Cream",
                                                    "Milk"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "old fashioned glass", #"cocktail glass",#tall tumbler,#"hurricane glass"
                                 "garnish":         "cherry",
                                 "ice":             "yes"
                },

    "Leg Spreader":      {"name":       "Leg Spreader",
                                "ingredients":  [   "Spiced Rum",
                                                    "Peach Schnapps",
                                                    "Malibu Coconut Rum",
                                                    "Pineapple Juice",
                                                    "Star Fruit"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         "strawberry",
                                 "ice":             "yes"
                },

    "Sex In The Driveway":      {"name":       "Sex In The Driveway",
                                "ingredients":  [   "Peach Schnapps",
                                                    "Blue Curacao",
                                                    "Vodka",
                                                    "Sprite"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "highball glass",
                                 "garnish":         "lemon wheel",
                                 "ice":             "yes"
                },

    "Angel's Tit":      {"name":       "Angel's Tit", 
                                "ingredients":  [   "White Creme de Cacao",
                                                    "Maraschino Liqueur",
                                                    "Whipped Cream",
                                                    "a maraschino cherry"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "cocktail glass", #"shot glass",
                                 "garnish":         "cherry",
                                 "ice":             "no"
                },

    "Naughty Girl Scout":      {"name":       "Naughty Girl Scout",
                                "ingredients":  [   "Kahlua",
                                                    "Bailey's Irish Cream",
                                                    "Creme de Menthe"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "highball glass", #"cocktail glass", #"martini glass"
                                 "garnish":         "mint",
                                 "ice":             "yes"
                },

    "Pop My Cherry":      {"name":       "Pop My Cherry",
                                "ingredients":  [   "Triple Sec",
                                                    "Orange Juice",
                                                    "Cherry Vodka"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "shot glass",
                                 "garnish":         "strawberry",
                                 "ice":             "no"
                },

    "Panty Ripper":      {"name":       "Panty Ripper", #SPAM99
                                "ingredients":  [   "Coconut Rum",
                                                    "Pineapple Juice",
                                                    "a Maraschino Cherry"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Royal Fuck":      {"name":       "Royal Fuck",
                                "ingredients":  [   "Crown Royal Canadian Whiskey",
                                                    "Peach Schnapps",
                                                    "Cranberry Juice"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Naked Lady":      {"name":       "Naked Lady",
                                "ingredients":  [   "Rum",
                                                    "Sweet Vermouth",
                                                    "Rakija",
                                                    "Lemon Juice",
                                                    "Grenadine"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Suck, Bang, and Blow":      {"name":       "Suck, Bang, and Blow",
                                "ingredients":  [   "Jose Cuervo Gold Tequila",
                                                    "Smirnoff Vodka",
                                                    "Absolut Citron Vodka",
                                                    "Jagermeister",
                                                    "Rumple Minze Peppermint Liqueur",
                                                    "Jacquin's Orange Flavored Gin",
                                                    "Goldschlager Cinnamon Schnapps",
                                                    "Hpnotiq Liqueur",
                                                    "Aristocrat Triple Sec",
                                                    "One Whole Lime",
                                                    "Strawberry Daiquiri Mix",
                                                    "Cranberry Juice"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },


    "Sex on my Face":      {"name":       "Sex on my Face",
                                "ingredients":  [   "Crown Royal Canadian Whiskey",
                                                    "Coconut Rum",
                                                    "Southern Comfort",
                                                    "Banana Liqueur",
                                                    "Cranberry Juice",
                                                    "Orange Juice",
                                                    "Pineapple Juice"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Liquid Viagra":      {"name":       "Liquid Viagra",
                                "ingredients":  [   "Jagermeister",
                                                    "Red Bull"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Slippery Nipple":      {"name":       "Slippery Nipple",
                                "ingredients":  [   "Grenadine Syrup",
                                                    "Irish Cream",
                                                    "DeKuyper Buttershots Liqueur"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Hanky Panky":      {"name":       "Hanky Panky",
                                "ingredients":  [   "Gin",
                                                    "Sweet Vermouth",
                                                    "Fernet-Branca"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Fat Hooker":      {"name":       "Fat Hooker",
                                "ingredients":  [   "Vodka",
                                                    "Coconut Rum",
                                                    "Peach Schnapps",
                                                    "Orange Juice"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    #4 Sexual Innuendo Cocktails to Get (Un)comfortable With

    "Sloe Comfortable Screw":      {"name":       "Sloe Comfortable Screw",
                                "ingredients":  [   "Vodka",
                                                    "Sloe Gin",
                                                    "Southern Comfort"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "collins glass", #"highball glass", 
                                 "garnish":         "orange slice",  #"orange wheel", 
                                 "ice":             "yes"
                },

    "Slippery Nipple":      {"name":       "Slippery Nipple",
                                "ingredients":  [   "Sambuca",
                                                    "Irish Cream"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Frozen Pink Panties":      {"name":       "Frozen Pink Panties",
                                "ingredients":  [   "Gin",
                                                    "Frozen Pink Lemonade",
                                                    "Frozen Strawberries"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Sex on the Beach":      {"name":       "Sex on the Beach",
                                "ingredients":  [   "Vodka",
                                                    "Peach Schnapps",
                                                    "Orange Juice"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "highball glass",
                                 "garnish":         ["orange slice", "cherry"],
                                 "ice":             "no"
                },

    #16 DIRTY DRINK RECIPES: COCKTAIL NAMES THAT SHOULD NOT BE UTTERED AT A WORK CONFERENCE
    "Bend Over Shirley":      {"name":       "Bend Over Shirley",
                                "ingredients":  [   "Raspberry Vodka",
                                                    "Sprite",
                                                    "Grenadine Syrup"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "collins glass",
                                 "garnish":         "cherry", #two Maraschino Cherries
                                 "ice":             "yes"
                },

    #Exotic Drinks with dirty names (open at your own risk !)
    "Buttery Nipple":      {"name":       "Buttery Nipple",
                                "ingredients":  [   "DeKuyper Buttershots liqueur",
                                                    "Irish cream"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Sex on the Beach":      {"name":       "Sex on the Beach",
                                "ingredients":  [   "Vodka",
                                                    "Peach Schnapps",
                                                    "Cranberry Juice",
                                                    "Orange Juice"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "highball glass",
                                 "garnish":         ["orange slice", "cherry"],
                                 "ice":             "no"
                },

    "Blowjob":      {"name":       "Blowjob",
                                "ingredients":  [   "Bailey's Irish Cream",
                                                    "Amaretto"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "shot glass",
                                 "garnish":         "whipped cream",
                                 "ice":             "no"
                },

    "Between the Sheets":      {"name":       "Between the Sheets",
                                "ingredients":  [   "Brandy",
                                                    "Light Rum",
                                                    "Triple Sec",
                                                    "Sweet and Sour Mix"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "cocktail glass",
                                 "garnish":         "lemon twist", #"orange peel",
                                 "ice":             "no"
                },

    "Liquid viagra":      {"name":       "Liquid Viagra",
                                "ingredients":  [   "Jagermeister",
                                                    "Red Bull"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Slippery Nipple":      {"name":       "Slippery Nipple",
                                "ingredients":  [   "Bailey's Irish Cream",
                                                    "Butterscotch Schnapps"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Screaming Orgasm":      {"name":       "Screaming Orgasm",
                                "ingredients":  [   "Vodka",
                                                    "Bailey's Irish Cream",
                                                    "Kahlua Coffee Liqueur"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "old fashioned glass", #"cocktail glass",#tall tumbler,#"hurricane glass"
                                 "garnish":         "cherry",
                                 "ice":             "yes"
                },

    "Slow Comfortable Screw":      {"name":       "Slow Comfortable Screw",
                                "ingredients":  [   "Sloe Gin",
                                                    "Southern Comfort Peach Liqueur",
                                                    "Orange Juice"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "highball glass", #"collins glass", 
                                 "garnish":         "orange wheel", #"orange slice",
                                 "ice":             "yes"
                },

    "Sex Machine":      {"name":       "Sex Machine",
                                "ingredients":  [   "Coffee Liqueur",
                                                    "Irish Cream"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Sit On My Face":      {"name":       "Sit On My Face",
                                "ingredients":  [   "Kahlua Coffee Liqueur",
                                                    "Frangelico Hazelnut Liqueur",
                                                    "Bailey's Irish Cream"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Deep Throat":      {"name":       "Deep Throat",
                                "ingredients":  [   "Bailey's Irish Cream",
                                                    "Kahlua Coffee Liqueur",
                                                    "Whipped Cream"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Creamy Pussy":      {"name":       "Creamy Pussy",
                                "ingredients":  [   "Bailey's Irish Cream",
                                                    "Tequila Rose strawberry cream liqueur"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Harvey Wallbanger":      {"name":       "Harvey Wallbanger",
                                "ingredients":  [   "Vodka",
                                                    "Hazelnut Liqueur",
                                                    "Orange Juice"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           "collins glass",
                                 "garnish":         ["orange slice", "cherry"],
                                 "ice":             "yes"
                },

    "Pop My Cherry ":      {"name":       "Pop My Cherry",
                                "ingredients":  [   "Cherry Vodka",
                                                    "Triple Sec",
                                                    "Orange Juice"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "shot glass",
                                 "garnish":         "strawberry",
                                 "ice":             "no"
                },

    "Bend Over Shirley":      {"name":       "Bend Over Shirley",
                                "ingredients":  [   "Raspberry Vodka",
                                                    "Sprite",
                                                    "Grenadine Syrup"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "collins glass",
                                 "garnish":         "cherry", #two Maraschino Cherries
                                 "ice":             "yes"
                },

    "Wyoming Legspreader":      {"name":       "Wyoming Legspreader",
                                "ingredients":  [   "Cola",
                                                    "Grain Alcohol",
                                                    "Raspberry Liqueur"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Three-Legged Monkey":      {"name":       "Three-Legged Monkey",
                                "ingredients":  [   "Crown Royal Canadian Whisky",
                                                    "Amaretto Almond Liqueur",
                                                    "Pineapple Juice"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Dr. Pecker":      {"name":       "Dr. Pecker",
                                "ingredients":  [   "Rye Whiskey",
                                                    "Cola",
                                                    "Cranberry-Raspberry Juice"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Penile Colarous":      {"name":       "Penile Colarous",
                                "ingredients":  [   "Banana Liqueur",
                                                    "Coconut Rum",
                                                    "Peach Schnapps",
                                                    "Pina Colada Schnapps",
                                                    "Pineapple Juice"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Tight Snatch":      {"name":       "Tight Snatch",
                                "ingredients":  [   "Vodka",
                                                    "Peach Schnapps",
                                                    "Orange Juice",
                                                    "Cranberry Juice"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },


    "Strawberry Stripper":      {"name":       "Strawberry Stripper",
                                "ingredients":  [   "Orange Juice",
                                                    "7 Up",
                                                    "Grenadine",
                                                    "Strawberry Schnapps"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },


    "Orange Bush":      {"name":       "Orange Bush",
                                "ingredients":  [   "Vodka",
                                                    "Orange Juice"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Fuzzy navel":      {"name":       "Fuzzy Navel",
                                "ingredients":  [   "Peach Schnapps",
                                                    "Orange Juice",
                                                    "Lemonade"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           "highball glass",
                                 "garnish":         "orange slice",
                                 "ice":             "yes"
                },

    "Dirty Mother":      {"name":       "Dirty Mother",
                                "ingredients":  [   "Brandy",
                                                    "Kahlua Coffee Liqueur"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Golden Shower":      {"name":       "Golden Shower",
                                "ingredients":  [   "Stolichnaya Vodka",
                                                    "Orange Juice",
                                                    "Fresh Lemon Juice",
                                                    "Triple Sec",
                                                    "Ginger Ale"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Red Balls":      {"name":       "Red Balls",
                                "ingredients":  [   "Pomegranate Vodka",
                                                    "Coconut Rum",
                                                    "Creme de Almond",
                                                    "Sweet Vermouth",
                                                    "Lime Juice"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Royal Fuck":      {"name":       "Royal Fuck",
                                "ingredients":  [   "Crown Royal Canadian Whiskey",
                                                    "Sour Apple Pucker",
                                                    "Cranberry Juice"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Grape KneeLength":      {"name":       "Grape KneeLength",
                                "ingredients":  [   "Club Soda",
                                                    "Vodka",
                                                    "Chambord"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

##heading down for a "Dirty Fort Girl" right now.
##"Dirty Fort Girl"? Ooh - inquiring minds want to know!
##"Dirty Fort Girl"? Ooh - inquiring minds want to know!
##
##Fat ass in a glass, Mainers favorite I hear. LOL
##
##Fat ass in a glass, Mainers favorite I hear. LOL
##Fat Ass in a Glass.. The Down East Panty Dropper, The Lewiston Martini.. 
##
##Liquid Panty Remover...what the hell makes Allen's so popular in Maine? That stuff is skunkbait! lol
##I'm guessing because it's sweet and it's cheap

    #Top 10 Inappropriately Named Cocktails

    "Sex with an alligator":      {"name":       "Sex With An Alligator",
                                "ingredients":  [   "Chambord",
                                                    "Jagermeister",
                                                    "Midori",
                                                    "Pineapple Juice"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "rocks glass", #"shot glass" #"cocktail glass"
                                 "garnish":         None,
                                 "ice":             "no"
                },

    "Miscarriage":      {"name":       "Miscarriage",
                                "ingredients":  [   "Vodka",
                                                    "Cherry Juice",
                                                    "Tabasco"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Monte's Sex Potion":      {"name":       "Monte's Sex Potion",
                                "ingredients":  [   "Coconut Rum",
                                                    "Chambord",
                                                    "Lemon Juice"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "PS I love you":      {"name":       "PS I love you",
                                "ingredients":  [   "Dark Rum",
                                                    "Amaretto",
                                                    "Kahlua",
                                                    "Amarula Cream",
                                                    "Double Cream"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Journalist":      {"name":       "Journalist",
                                "ingredients":  [   "Gin",
                                                    "Sweet Vermouth",
                                                    "Dry Vermouth",
                                                    "Curacao",
                                                    "Lemon Juice"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Lady Diana":      {"name":       "Lady Diana",
                                "ingredients":  [   "Campari",
                                                    "Gin",
                                                    "Lime Juice"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Broken Heart Zombie Mai Tai":      {"name":       "Broken Heart Zombie Mai Tai",
                                "ingredients":  [   "Gold Rum",
                                                    "Orange Rum",
                                                    "151 Rum",
                                                    "Triple Sec",
                                                    "Orange Curacao Liqueur",
                                                    "Orange Juice",
                                                    "Grenadine Syrup",
                                                    "Lime Soda Water"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Blood of Satan":      {"name":       "Blood of Satan",
                                "ingredients":  [   "Bailey's Irish Cream",
                                                    "Jack Daniels",
                                                    "Jagermeister",
                                                    "Goldschlager"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },
 
    #9 NAUGHTY COCKTAIL NAMES AND RECIPES

    "Redheaded Slut":      {"name":       "Redheaded Slut",
                                "ingredients":  [   "Jagermeister",
                                                    "Peach Schnapps",
                                                    "Cranberry Juice"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "rocks glass", #"shot glass",
                                 "garnish":         None,
                                 "ice":             "yes"
                },

    "Sex With an Alligator":      {"name":       "Sex With an Alligator",
                                "ingredients":  [   "Raspberry Liqueur",
                                                    "Melon Liqueur",
                                                    "Jagermeister"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "cocktail glass", #"shot glass", #"rocks glass"
                                 "garnish":         None,
                                 "ice":             "no"
                },

    "Angel's Tit":      {"name":       "Angel's Tit",
                                "ingredients":  [   "White Creme de Cacao",
                                                    "Cherry Liqueur",
                                                    "Half-and-Half",
                                                    "Maraschino Cherries"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "shot glass",
                                 "garnish":         "cherry",
                                 "ice":             "no"
                },

    "Leg Spreader":      {"name":       "Leg Spreader",
                                "ingredients":  [   "Midori Melon Liqueur",
                                                    "Malibu Rum",
                                                    "Pineapple Juice",
                                                    "7 Up"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         "strawberry",
                                 "ice":             "yes"
                },

    "Blow-job":      {"name":       "Blow-job",
                                "ingredients":  [   "Bailey's Irish Cream",
                                                    "Amaretto",
                                                    "Kahlua",
                                                    "Whipped Cream"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "shot glass",
                                 "garnish":         "whipped cream",
                                 "ice":             "no"
                },

    "Screaming Orgasm":      {"name":       "Screaming Orgasm",
                                "ingredients":  [   "Vodka",
                                                    "Bailey's Irish Cream",
                                                    "Kahlua"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "old fashioned glass", #"cocktail glass",#tall tumbler,#"hurricane glass"
                                 "garnish":         "cherry",
                                 "ice":             "yes"
                },

    "Bend Over Shirley":      {"name":       "Bend Over Shirley",
                                "ingredients":  [   "Raspberry Vodka",
                                                    "Sprite",
                                                    "Grenadine Syrup",
                                                    "Maraschino Cherries"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "collins glass",
                                 "garnish":         "cherry", #two Maraschino Cherries
                                 "ice":             "yes"
                },

    "Quick Fuck":      {"name":       "Quick Fuck",
                                "ingredients":  [   "Bailey's Irish Cream",
                                                    "Midori liqueur",
                                                    "Kahlua"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "The Slippery Nipple":      {"name":       "The Slippery Nipple",
                                "ingredients":  [   "Bailey's Irish Cream",
                                                    "Sambuca"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    #The 7 Worst Cocktail Names

    "Bloody Mary":      {"name":       "Bloody Mary",
                                "ingredients":  [   "Vodka",
                                                    "Tomato Juice",
                                                    "Tabasco Sauce",
                                                    "Worcestershire Sauce"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Rusty Nail":      {"name":       "Rusty Nail",
                                "ingredients":  [   "Drambuie",
                                                    "Scotch"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Flirtini":      {"name":       "Flirtini",
                                "ingredients":  [   "Champagne",
                                                    "Vodka",
                                                    "Pineapple Juice"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Salty Dog":      {"name":       "Salty Dog",
                                "ingredients":  [   "Gin",
                                                    "Grapefruit Juice"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },


    "Harvey Wallbanger":      {"name":       "Harvey Wallbanger",
                                "ingredients":  [   "Vodka",
                                                    "Galliano",
                                                    "Orange Juice"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           "collins glass",
                                 "garnish":         ["orange slice", "cherry"],
                                 "ice":             "yes"
                },

    "Sex On The Beach":      {"name":       "Sex On The Beach",
                                "ingredients":  [   "Peach Schnapps",
                                                    "Vodka",
                                                    "Orange Juice",
                                                    "Cranberry Juice"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "highball glass",
                                 "garnish":         ["orange slice", "cherry"],
                                 "ice":             None
                },

    "Sex on Fire":      {"name":       "Sex on Fire",
                                "ingredients":  [   "Peach Schnapps",
                                                    "Vodka",
                                                    "Orange Juice",
                                                    "Cranberry Juice",
                                                    "Fireball Cinammon Whiskey"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    #10 drink names that are oh so wrong

    "Fiery German":      {"name":       "Fiery German",
                                "ingredients":  [   "Jagermeister",
                                                    "Cinnamon Schnapps"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Screaming Orgasm":      {"name":       "Screaming Orgasm",
                                "ingredients":  [   "Vodka",
                                                    "Irish Cream",
                                                    "Kahlua"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           "old fashioned glass", #"cocktail glass",#tall tumbler,#"hurricane glass"
                                 "garnish":         "cherry",
                                 "ice":             "yes"
                },

    "Alien Nipple":      {"name":       "Alien Nipple",
                                "ingredients":  [   "Butterscotch Schnapps",
                                                    "Irish Liqueur",
                                                    "Melon Liqueur"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Hillbilly Kool Aid":      {"name":       "Hillbilly Kool Aid",
                                "ingredients":  [   "Grain Alcohol",
                                                    "Lemon-Lime Soda",
                                                    "Fruit Punch"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Slap Your Mama":      {"name":       "Slap Your Mama",
                                "ingredients":  [   "Citrus Soda",
                                                    "Orange Juice",
                                                    "Spiced Rum"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Charlie Manson":      {"name":       "Charlie Manson",
                                "ingredients":  [   "Ginger Ale",
                                                    "Spiced Rum",
                                                    "Rye Whiskey"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Heaven's Gate":      {"name":       "Heaven's Gate",
                                "ingredients":  [   "Coconut Rum",
                                                    "Spiced Rum",
                                                    "Orange Liqueur",
                                                    "Raspberry Liqueur",
                                                    "Pineapple Juice",
                                                    "Lemon-lime Soda"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Bloody Mary":      {"name":       "Bloody Mary",
                                "ingredients":  [   "Vodka",
                                                    "Tomato Juice",
                                                    "Tabasco Sauce",
                                                    "Worcestershire Sauce"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },


    #The 10 worst cocktails ever created

    "Bath Cure":      {"name":       "Bath Cure",
                                "ingredients":  [   "White Rum",
                                                    "Gold Rum",
                                                    "Light Rum",
                                                    "151-proof Rum",
                                                    "Brandy",
                                                    "Vodka",
                                                    "Orange Juice",
                                                    "Grenadine"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },
 
    "Cement Mixer":      {"name":       "Cement Mixer",
                                "ingredients":  [   "Lime Juice",
                                                    "Baileys"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Prairie Oyster":      {"name":       "Prairie Oyster",
                                "ingredients":  [   "Bourbon",
                                                    "Tabasco Sauce",
                                                    "Worcestershire Sauce",
                                                    "Raw Egg Yolk",
                                                    "salt and pepper"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Bloody Tampon":      {"name":       "Bloody Tampon",
                                "ingredients":  [   "Whisky",
                                                    "Vodka",
                                                    "Tequila",
                                                    "Tomato Juice",
                                                    "Lemon Juice",
                                                    "Baileys"],
                                 "name type":       "dirty",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Four Horsemen of the Apocolypse":      {"name":       "Four Horsemen of the Apocolypse",
                                "ingredients":  [   "Jim Beam",
                                                    "Jack Daniels",
                                                    "Jameson",
                                                    "Johnnie Walker Black",
                                                    "Bacardi 151"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

##    "Hot Mexican Hooker
##    Hot Mexican Hooker
##    This one is both horrid and hilarious. Tequila, Tabasco sauce and the juice from a tin of tuna. Mmmm, fishy.

    "Motor Oil":      {"name":       "Motor Oil",
                                "ingredients":  [   "Jagermeister",
                                                    "Peppermint Schnapps",
                                                    "Cinnamon Schnapps",
                                                    "Coconut Rum"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    #https://www.bbcgoodfood.com/howto/guide/top-10-most-popular-cocktail-recipes
 
    "Mojito":      {"name":       "Mojito",
                                "ingredients":  [   "White Rum",
                                                    "Sugar",
                                                    "Lime",
                                                    "Soda Water"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           "collins glass",
                                 "garnish":         "mint",
                                 "ice":             "yes"
                },

    "Espresso Martini":      {"name":       "Espresso Martini",
                                "ingredients":  [   "Freshly Brewed Espresso",
                                                    "Coffee Liqueur"
                                                    "Gin",
                                                    "Dry Vermouth"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

##    "Pimm's":      {"name":       "Pimm's",
##                                "ingredients":  [   "
##
##"],
##                                 "name type":       "clean"
##                },
##
##
##It wouldn't be British summertime without a glass of fruity Pimm's
##punch. Make a pitcher for your next gathering with friends, and add
##plenty of mint leaves, cucumber, orange and strawberries for a
##fruitier flavour. Turn this sensational summer cup into a Pimm's
##slushie to keep everyone cool or add a splash of juice and a
##sprinkling of seeds to make our pomegranate Pimm's.
 
    "Passion Fruit Martini":      {"name":       "Passion Fruit Martini",
                                "ingredients":  [   "Passion Fruit Pulp",
                                                    "Vanilla Vodka",
                                                    'Passoa "The Passion Drink" Liqueur',
                                                    "Lime Juice",
                                                    "Sugar Syrup",
                                                    "Prosecco"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Pina Colada":      {"name":       "Pina Colada",
                                "ingredients":  [   "White Rum",
                                                    "Pineapple Juice",
                                                    "Coconut Cream"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Frozen Strawberry Daiquiri":      {"name":       "Frozen Strawberry Daiquiri",
                                "ingredients":  [   "Strawberries",
                                                    "Rum",
                                                    "Lime Juice"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Rum Punch":      {"name":       "Rum Punch",
                                "ingredients":  [   "Orange Juice",
                                                    "Lime Juice",
                                                    "Golden Rum",
                                                    "Sugar syrup",
                                                    "Grenadine Syrup",
                                                    "Angostura Bitters",
                                                    "a Maraschino Cherry"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Cosmopolitan":      {"name":       "Cosmopolitan",
                                "ingredients":  [   "Vodka",
                                                    "Cointreau",
                                                    "Cranberry Juice",
                                                    "Lime Juice"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Negroni":      {"name":       "Negroni",
                                "ingredients":  [   "Campari",
                                                    "Gin",
                                                    "Sweet Vermouth"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },


    "Aperol Spritz":      {"name":       "Aperol Spritz",
                                "ingredients":  [   "Aperol",
                                                    "Soda Water",
                                                    "Prosecco"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Classic Gin Martini":      {"name":       "Classic Gin Martini",
                                "ingredients":  [   "Gin",
                                                    "Dry Vermouth",
                                                    "Angostura Bitters"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Black Russian":      {"name":       "Black Russian",
                                "ingredients":  [   "Vodka",
                                                    "Kahlua",
                                                    "Cola"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "White Russian":      {"name":       "White Russian",
                                "ingredients":  [   "Vodka",
                                                    "Kahlua",
                                                    "Cream"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                },

    "Mimosa":      {"name":       "Mimosa",
                                "ingredients":  [   "Champagne",
                                                    "Orange Curacao",
                                                    "Orange Juice"],
                                 "name type":       "clean",
                                 "colour":          None,
                                 "glass":           None,
                                 "garnish":         None,
                                 "ice":             None
                }


#TO ADD
#SEA BREEZE
#ALABAMA SLAMMER
#TROPICAL SUNSET
#MINT JULEP

    }

def pick_pizza_topping():
    return random.choice(pizza_toppings)

def make_pizza():
    topping1 = pick_pizza_topping()
    topping2 = pick_pizza_topping()
    while topping1 == topping2:
        topping2 = pick_pizza_topping()
    return "%s and %s" % (topping1, topping2)


def make_random_cocktail():
    name = make_random_cocktail_name()
    num_spirits = random.choice((1,1,2,2,2,2,2,3,3,3,3,3,3,3,4,4,5))
    num_mixers = random.choice((1,1,2,2,2,2,2,3,3,3,3,3))
    ingredients = []
    for f in range(0, num_spirits):
        this_spirit = random.choice(spirits_list)
        while this_spirit in ingredients:
            this_spirit = random.choice(spirits_list)
        ingredients.append(this_spirit)
    for f in range(0, num_mixers):
        this_mixer = random.choice(mixers_list)
        while this_mixer in ingredients:
            this_mixer = random.choice(mixers_list)
        ingredients.append(this_mixer)
    retvar = "%s (" % name
    for f in ingredients:
        if f == ingredients[0]:
            retvar = "%s%s" % (retvar, f)
        elif f == ingredients[-1]:
            retvar = "%s and %s)" % (retvar, f)
        else:
            retvar = "%s, %s" % (retvar, f)
    return retvar
    

def get_real_cocktail():
    rc = random.choice(real_cocktails.keys())
    name = real_cocktails[rc]["name"]
    ingredients = real_cocktails[rc]["ingredients"]
    name_type = real_cocktails[rc]["name type"]
    retvar = "%s (" % name
    for f in ingredients:
        if f == ingredients[0]:
            retvar = "%s%s" % (retvar, f)
        elif f == ingredients[-1]:
            retvar = "%s and %s)" % (retvar, f)
        else:
            retvar = "%s, %s" % (retvar, f)
    return retvar

def make_cocktail_name():
    pass

def make_fast_food_menu():
    pass

def pick_real_cocktail():
    pass


def make_cocktail_list():
    num_real_cocktails = random.choice(range(2,5))
    num_random_cocktails = random.choice(range(2,5))

    cocktail_menu = ""
    cocktail_menu_list = []
    
    for f in range(0, num_real_cocktails):
        this_cocktail = get_real_cocktail()
        while this_cocktail in cocktail_menu_list:
            this_cocktail = get_real_cocktail()
        if cocktail_menu == "":
            cocktail_menu = "%s" % this_cocktail
        else:
            cocktail_menu = "%s\n%s" % (cocktail_menu, this_cocktail)
        cocktail_menu_list.append(this_cocktail)

    for f in range(0, num_random_cocktails):
        this_cocktail = make_random_cocktail()
        while this_cocktail in cocktail_menu_list:
            this_cocktail = make_random_cocktail()
        #if cocktail_menu == "":
        #    cocktail_menu = "%s" % this_cocktail
        #else:
        #    cocktail_menu = "%s\n\n%s" % (cocktail_menu, this_cocktail)
        cocktail_menu = "%s\n%s" % (cocktail_menu, this_cocktail)
        cocktail_menu_list.append(this_cocktail)
        
    return cocktail_menu

def do_test():
    cks = real_cocktails.keys()
    cks.sort()
    all_cocktails_count = len(cks)
    empty_details_count = 0
    empty_details_list = []
    for c in cks:
        name = real_cocktails[c]["name"]
        #print "name: '%s'" % name
        if real_cocktails[c]["colour"] == None:
            if real_cocktails[c]["glass"] == None:
                if real_cocktails[c]["garnish"] == None:
                    if real_cocktails[c]["ice"] == None:
                        empty_details_list.append(name)
                        empty_details_count = empty_details_count + 1
    print "%s (of %s) cockatils missing all details" % (empty_details_count, all_cocktails_count)
    for f in empty_details_list:
        print "\t - %s" % f

if __name__ == "__main__":
    print "sample pizza:"
    print "%s" % make_pizza()
    print
    print "sample real cocktail:"
    print get_real_cocktail()
    #print
    print "sample random cocktail:"
    print make_random_cocktail()
    print
    print "================"
    print
    print "COCKTAIL MENU"
    print
    print make_cocktail_list()
    print
    print "================"
    print

    jointname = string.upper(make_fast_food_joint_name())
    print "%s\n%s\n\n" % (jointname, "="*len(jointname))
    print make_random_menu()

    if TEST == 1:
        do_test()


    f = FastFoodJoint()
    f.populate()
    print f
