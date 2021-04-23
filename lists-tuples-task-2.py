
# exercise 2

# defining a function
def uniform_ages(ages, ages1):
    for x in ages:
        for y in ages1:
            if x == y:
                outcome = True
            elif x != y:
                outcome = False
                return outcome


# calling the pre-defined function
print(uniform_ages([2, 12, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20], [2, 4, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20]))
