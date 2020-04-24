import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# this solution takes on average 0.007 seconds to run, fastest
# # create a new dictionary 
names_count = {}

# iterate over the second list of names 
for name in names_2:
    # save the count of names in the new dict
    names_count[name] = 1

# iterate of the other list of names
for name in names_1:
    # check if name is present in the list
    if names_count.get(name) != None:
        # if so append it to the list of names
        duplicates.append(name)

# STRETCH: using an array instead - takes about 2.7s on average
# list_name_count = list()

# for name in names_2:
#     if name not in list_name_count:
#         list_name_count.append(name)

# for name in names_1:
#     if name in list_name_count:
#         duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
