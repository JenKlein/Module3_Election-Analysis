# #What is the score?
# score = int(input("What is your test score? "))

# # Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# else:
#     if score >= 80:
#         print('Your grade is a B.')
#     elif score >= 70:
#         print('Your grade is a C.')
#     elif score >= 60:
#         print('Your grade is a D.')
#     else:
#         print('Your grade is an F.')


# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")


# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1

# counties_tuple = ["Arapahoe", "Denver", "Jefferson"]

# for county in counties_tuple:
#       print(county)
# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}


# for county in counties_dict:
#     print(county)
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county, voters in voting_data.items():
    print(f"{county} county has {voters} registered voters.")




