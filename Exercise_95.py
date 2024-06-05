country = input("Enter name of the country: ")
visits = int(input("Enter number of times you have visited: "))
list_of_cities = eval(input())

travel_log = [
    {
        "country" : "France",
        "visits"  : 12,
        "cities" : ["Paris", "Lille", "dijon"]
    },

    {
        "country" : "Germany",
        "visits": 5,
        "cities" : ["Berlin", "Hamburg", "Stuttgart"]
    }
]

def modifier(country,visits,list_of_cities):
   new_country =  {}
   new_country["country"] = country
   new_country["visits"] = visits
   new_country["cities"] = list_of_cities

   travel_log.append(new_country)

modifier(country,visits,list_of_cities)
print(f"I have been to {travel_log[2]['country']}, {travel_log[2]['visits']} times this year ")
print(f"My favourite city is {travel_log[2]['cities'][0]}.")

