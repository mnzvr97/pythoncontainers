# Exercise 5

#     Iterate over the key: value pairs in home_town and print a string for each item, for example:
#     "city = Arcadia"
#     "state = California"
#     "population = 58000"


def my_home_town_list():
    for key in home_town:
        print(key, '=', home_town[key])

my_home_town_list()

# print("I was born in ", home_town["city"], " ", home_town["state"]," - population of ",home_town["population"])

# print("city = ", home_town["city"])
# print("state = ", home_town["state"])
# print("population = ",home_town["population"])


