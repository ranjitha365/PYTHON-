

    # nested dictionary finding highest one
city_information = {
    1: {'place' :'banglore', 'famouse': 'job', 'rating': 45 },
    2: {'place' : 'dharwad', 'famouse ' : 'sweet', 'rating' : 50},
}

highest = max(city_information.values() , key = lambda x : x ['rating'])
print("top:", highest["place"], "famouse for sweet:", highest["rating"])