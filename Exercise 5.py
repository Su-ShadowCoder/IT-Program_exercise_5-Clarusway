# # Excercise 1
# my_lst = [1, 2, 3, 4, 5, 6]
# my_lst.remove(1)
# my_lst.remove(3)
# my_lst.remove(4)
# print(my_lst)

# # Excercise 2
# tuple_1 = (1,2,3)
# tuple_2 = (4,5,6)
#
# tuple_3 = tuple_1 + tuple_2
# print(tuple_3)

# # Excercise 3.1
# my_lst = [1,2,3,4,5]
# midpoint = len(my_lst) // 2
# tuple_1 = my_lst[:midpoint]
# tuple_2 = my_lst[midpoint:]
# print(f"Tuple 1 is: {tuple_1}\n"
#       f"Tuple 2 is: {tuple_2})")

# # Excercise 3.2

# my_tuple = (1, 2, 3, 4, 5)
#
# # Splitting the tuple into two tuples of the same size
# tuple1 = tuple(x for x in my_tuple if x % 2 == 0)
# tuple2 = tuple(x for x in my_tuple if x % 2 != 0)
#
# print("Tuple with even numbers:", tuple1)
# print("Tuple with odd numbers:", tuple2)

# Side bar exercises for for loops.
# Exercise one
# lst_10 = range(1, 11)
# for lst_10 in lst_10:
#     print(lst_10)
#
# # Exercise two
# names = ["Alice", "Bob", "Claire", "David", "Emily", "Frank", "Grace",
#          "Henry", "Isabella", "Jack"]
# for names in names:
#     print(f"Goodmorning! {names}")
# Ending side bar exercises for for loop

# Side bar for generator expression

# Generate a tuple containing the first 5 multiples of 4
# Use a generator expression with variable x
# multiples_of_4_tuple = tuple(x * 4 for x in range(1, 6))
# print(f"Tuple of multiples of 4: {multiples_of_4_tuple}")

# Ending side bar exercises for generator expression

# # Excercise 4
# tuples_list = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
# sorted_list = sorted(tuples_list, key = lambda x: x[-1])
#
# print(sorted_list)

# # Excercise 5.1
# numb = [20, 30, 40, 50, 60]
#
# total = sum(numb)
# avarage = total / len(numb)
#
# print(f"Avarage is : {avarage}")
#
# # # Excercise 5.2
# desired_average = 5
# # Original list of numbers
# numb = [20, 30, 40, 50, 60]
#
# # Calculate the current sum of numbers in the list
# current_total = sum(numb)
#
# # Calculate the number of elements in the list
# num_elements = len(numb)
#
# # Calculate the total sum required to achieve the desired average
# required_total = desired_average * (num_elements + 1)
#
# # Calculate the number to be added to the list
# number_to_add = required_total - current_total
#
# # Add the number to the list
# numb.append(number_to_add)

# Recalculate the average
# new_total = sum(numb)
# new_average = new_total / len(numb)
#
# print("Updated list of numbers:", numb)
# print(f"New average is : {new_average}")

#Exercise 6
# matrix = [[3] * 6] *6
# print(matrix)
