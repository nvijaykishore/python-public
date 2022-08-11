capitals = {
    "France":"Paris",
    "Germany":"Berlin",
    "India":"New Delhi"
    }

#Nesting lists in a dictionary
travel_log = {
    "France":["Paris","Lille","Dijon"],
    "Germany":["Berlin","Stutgart","Hamburg"],
    }

#nesting dictionary in a dictonary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visited": 12},
     "Germany":{"cities_visited": ["Berlin", "Stutgart", "Hamburg"], "total_visited": 6}
     }

country = travel_log["France"]
print(country["cities_visited"])