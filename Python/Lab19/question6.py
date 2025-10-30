#!/usr/bin/python3
# #(6) Write a function called cell_metabolism that takes the number of glucose and oxy-gen
# molecules, that contains an inner function energy_output() to calculate ATP yield
# (assume 1 glucose+6 oxygen gives 38 ATP). The function should return the total ATP
# produced.
def cell_metabolism():
    glucose = int(input("Enter number of glucose molecules: "))
    oxygen = int(input("Enter number of oxygen molecules: "))

    def energy_output(g, o):
        atp_per_glucose = 38
        max_reactions = min(g, o // 6)
        return max_reactions * atp_per_glucose

    return energy_output(glucose, oxygen)

# Call the function and print the result
atp = cell_metabolism()
print("ATP produced:", atp)

