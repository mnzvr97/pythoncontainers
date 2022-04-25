foods = ("aloo","biryani","kheema","gosht")


# Exercise 3

#     Using a for loop, print just the last two food strings from foods.

for food in foods:
    if food == foods[2] or food == foods[3]:
        print(food)

# for food in foods.reverse():
