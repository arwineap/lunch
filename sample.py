import restaurants
import random

def prettyprint(restaurantName, restaurantInfo):
    print restaurantName
    if restaurantInfo['nick']:
        print "AKA: %s" % restaurantInfo['nick']
    print restaurantInfo['location']
    if restaurantInfo['flags']:
        print 'Flags:'
        for flag in restaurantInfo['flags']:
            print "\t%s" % flag

res = restaurants.restaurants()

# add restaurants
res.add('Sorrentos', '5518 Sepulveda Blvd, Culver City, CA', flags=['cheap', 'near', 'closed-on-tuesdays', 'parking-in-rear'])
res.add('Capriottis', '5495 Sepulveda Blvd, Culver City, CA')
res.add('Taco Miendo', '4502 Inglewood Blvd, Culver City, CA')
res.add("Tub's fine chili, and fancy fixins", "4263 Overland Ave, Culver City", flags=['awesome'])
res.add("Mendo", "4724 Admiralty Way  Marina del Rey, CA 90292", flags=['long-lines'])
res.add("Pizza brothers", "4724 Admiralty Way  Marina del Rey, CA 90292")
res.add("Pizzarito", "4371 Glencoe Ave, Marina Del Rey, CA 90292")
res.add("Rutt's", "12114 W Washington Blvd, Los Angeles, CA 90066", flags=['cheap'])
res.add("Great Western Steak and Hoagie", "1720 Lincoln Blvd, Venice, CA", flags=['cash-only'], nick="hot lava")
res.add("Fox hills Mall", "6000 Sepulveda Blvd, Culver City, CA", flags=["choices", "near", "undecisive"])
res.add("islands", "6081 Center Dr #104, Los Angeles, CA", flags=["beer"])
res.add("counter", "4724 Admiralty Way  Marina del Rey, CA 90292", flags=['seating', '$$$', 'big-food'])
res.add("Sachi", "4455 West Slauson Avenue, Los Angeles, CA", flags=['near', 'cash-only'], nick="ghettoaki")
res.add("The Shack", "185 Culver Boulevard Playa del Rey, CA", flags=['distance', 'beer'])
res.add("Lucille's", "6000 Sepulveda Blvd, Culver City, CA")
res.add("Jerry's Deli", "13181 Mindanao Way, Marina del Rey, CA", flags=['$$$', 'too-many-options'])
res.add("Irori", "4371 Glencoe Ave B4, Marina del Rey, CA", flags=['sushi'])
res.add("Rainbow Acres", "13208 West Washington Boulevard, Culver City, CA", nick="hippie market")
res.add("Somosa House", "10700 W Washington Blvd, Culver City, CA")
res.add("Subway", "4949 W Slauson Ave Los Angeles, CA 90056", flags=['walking', 'subway'])
res.add("HoneyBaked", "11405 Jefferson Blvd, Culver City, CA 90230", flags=['close'])
res.add("Mitsuwa", "3760 S Centinela Ave, Los Angeles, CA 90066")
res.add("Curry House", "2130 Sawtelle Blvd #200, Los Angeles, CA 90025")
res.add("Five Guys", "6000 Sepulveda Blvd, Culver City, CA 90230", flags=['calories'])
res.add("California Chicken Cafe", "424 Lincoln Blvd Venice, CA 90291")
res.add("JR's BBQ", "3055 La Cienega, Culver City, CA 90232")
res.add("Mike's Deli", "4859 W Slauson Ave, Los Angeles, CA 90056", flags=['close', 'walking'])
res.add("Ayara Thai", "6245 W 87th St, Los Angeles, CA 90045")
res.add("Normandie Bakery", "3022 S Cochran Ave, Los Angeles, CA 90016", flags=['close'])

# create datafile, load it
res.dumpDataFile('lunchplaces.json')
res.loadDataFile('lunchplaces.json')

# choose restaurant
choice = random.choice(res.restaurants.keys())

# print the randomized choice
# in the followint format:
# Name
# location
# [ optional ]
# Flags:
#   flag1
#   flag2

prettyprint(choice, res.restaurants[choice])

res.mod("Rutt's", location="hell", nick="hawaiikawi", flags=(['all', 'the', 'new', 'flags'], 'a'))
