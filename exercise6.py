# Exercise 6

#     Create an empty list named cohort.

#     Using a for loop, add one dictionary to the cohort list for each student name. Each dictionary should have this shape:

#     {
#       'student': 'Tina',
#       'fav_food' 'Cheeseburger'
#     }

#     Iterate over cohort printing out each element.


names = ["Mohammad", "Mansur", "Ali", "Khan"]

foods = ("aloo","biryani","kheema","gosht")

cohort = []
for name in enumerate(names):
    student_obj = { 'student': name[1], 'fav_food': foods[name[0]] }
    cohort.append(student_obj)

print(cohort)


for person in cohort:
    print(f"{person['student']}'s favorite food is {person['fav_food']}")

