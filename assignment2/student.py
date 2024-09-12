# ---------------- Student List Operations ----------------

# Student List
student_list1 = ["Ravi", "Shree", "Kiran", "Priya"]

# List operations
print("\nThe list of students is:\n", student_list1)

student_list1.append("Manoj")  # append operation
print("\nThe append operation\n", student_list1)

student_list1.insert(1, "Akash")  # insert operation
print("\nThe insert operation at 1st position\n", student_list1)

student_list2 = ["Sara", "Megha"]
student_list3 = student_list1 + student_list2  # list addition (concatenation)
print("\nThis is list addition example\n", student_list3)

# Nested list example
nested_student_list = [student_list1, student_list2, student_list3]
print("\nNested list example\n", nested_student_list)
print("\nThe list at position 2 is:\n", nested_student_list[2])


# ---------------- Student Tuple Operations ----------------

# Student Tuple
student_tuple1 = ("Ravi", "Shree", "Kiran", "Priya")

# Tuple operations
print("\nThe tuple of students is:\n", student_tuple1)

student_tuple1 = student_tuple1 + ("Manoj",)  # append operation
print("\nThe append operation\n", student_tuple1)

student_tuple1 = student_tuple1[:1] + ("Akash",) + student_tuple1[1:]  # insert operation
print("\nThe insert operation at 1st position\n", student_tuple1)

student_tuple2 = ("Sara", "Megha")
student_tuple3 = student_tuple1 + student_tuple2  # tuple addition (concatenation)
print("\nThis is tuple addition example\n", student_tuple3)

# Nested tuple example
nested_student_tuple = (student_tuple1, student_tuple2, student_tuple3)
print("\nNested tuple example\n", nested_student_tuple)


# ---------------- Student Set Operations ----------------

# Student Set
student_set1 = {"Ravi", "Shree", "Kiran", "Priya"}

# Set operations
print("\nThe set of students is:\n", student_set1)

student_set1.add("Manoj")  # add operation
print("\nThe add operation\n", student_set1)

student_set2 = {"Sara", "Megha"}

# Set union
student_set3 = student_set1.union(student_set2)
print("\nThis is set union example\n", student_set3)

# Set difference
student_diff = student_set3.difference(student_set1)
print("\nThis is set difference example\n", student_diff)

# ---------------- Student Dictionary Operations ----------------

# Student Dictionary
student_info = {'name': 'Shree', 'age': 21, 'course': 'Engineering'}

# Dictionary operations
print("\nThe student info is:\n", student_info)
student_info['year'] = 3
print("\nThe updated student info is:\n", student_info)

# Accessing values
print("\nThe student's course is:\n", student_info.get('course'))

# Dictionary keys and values
print("\nThe items in the student dictionary are:\n", student_info.items())
print("\nThe keys in the student dictionary are:\n", student_info.keys())
print("\nThe values in the student dictionary are:\n", student_info.values())