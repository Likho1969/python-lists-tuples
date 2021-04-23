
# exercise 1

ages = [2, 12, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20]  # creating a list

final_list = set(ages)  # removing duplicates

print(final_list)   # getting a list without duplicates

print("-------------------------------------------------------------------------------------")

# option for exercise 1
ages = [2, 12, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20]  # creating a list
temp_list = []   # creating an empty but temporary list

# looping through a list
for i in ages:
    if i not in temp_list:
        temp_list.append(i)

ages = temp_list

print(ages)
