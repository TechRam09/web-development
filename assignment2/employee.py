# ---------------- Employee List Operations ----------------

# Employee List
emp_list1 = ["Ravi", "Shree", "Kiran", "Rahul"]

# List operations
print("\nThe list of employees is:\n", emp_list1)

emp_list1.append("Manoj")  # append operation
print("\nThe append operation\n", emp_list1)

emp_list1.insert(2, "Akash")  # insert operation
print("\nThe insert operation at 2nd position\n", emp_list1)

emp_list2 = ["Sara", "Megha"]
emp_list3 = emp_list1 + emp_list2  # list addition (concatenation)
print("\nThis is list addition example\n", emp_list3)

# Nested list example
nested_emp_list = [emp_list1, emp_list2, emp_list3]
print("\nNested list example\n", nested_emp_list)
print("\nThe list at position 2 is:\n", nested_emp_list[2])

# List operations
print("\nLength of nested list is:\n", len(nested_emp_list))  # len gives length of list
print("\nMax of nested list is:\n", max(nested_emp_list))  # max gives max in list  
print("\nMin of nested list is:\n", min(nested_emp_list))  # min gives min in the list

# Additional list operations
emp_list4 = ["Nithin", "Arya", "Vikas", "Sonia", "Tina", "Fatima"]
print(emp_list4.index("Vikas"))
emp_list4.reverse()
print("\n", emp_list4, "\n")
emp_list4.extend(emp_list3)
print(emp_list4)


# ---------------- Employee Tuple Operations ----------------

# Employee Tuple
emp_tuple1 = ("Ravi", "Shree", "Kiran", "Rahul")

# Tuple operations
print("\nThe tuple of employees is:\n", emp_tuple1)

emp_tuple1 = emp_tuple1 + ("Manoj",)  # append operation
print("\nThe append operation\n", emp_tuple1)

emp_tuple1 = emp_tuple1[:2] + ("Akash",) + emp_tuple1[2:]  # insert operation at 2nd position
print("\nThe insert operation at 2nd position\n", emp_tuple1)

emp_tuple2 = ("Sara", "Megha")
emp_tuple3 = emp_tuple1 + emp_tuple2  # tuple addition (concatenation)
print("\nThis is tuple addition example\n", emp_tuple3)

# Nested tuple example
nested_emp_tuple = (emp_tuple1, emp_tuple2, emp_tuple3)
print("\nNested tuple example\n", nested_emp_tuple)
print("\nThe tuple at position 2 is:\n", nested_emp_tuple[2])

# ---------------- Employee Set Operations ----------------

# Employee Set
emp_set1 = {"Ravi", "Shree", "Kiran", "Rahul"}

# Set operations
print("\nThe set of employees is:\n", emp_set1)

emp_set1.add("Manoj")  # add operation
print("\nThe add operation\n", emp_set1)

emp_set2 = {"Sara", "Megha"}

# Set union
emp_set3 = emp_set1.union(emp_set2)
print("\nThis is set union example\n", emp_set3)

# Set difference
emp_diff = emp_set3.difference(emp_set1)
print("\nThis is set difference example\n", emp_diff)

# ---------------- Employee Dictionary Operations ----------------

# Employee Dictionary
employee_info = {'name': 'Ravi', 'age': 28, 'branch': 'IT'}

# Dictionary operations
print("\nThe employee info is:\n", employee_info)

# Adding a new key-value pair
employee_info['salary'] = 40000
print("\nThe updated employee info with salary is:\n", employee_info)

# Updating an existing value
employee_info['age'] = 29
print("\nThe updated employee age is:\n", employee_info)

# Accessing a value using a key
print("\nThe employee's branch is:\n", employee_info['branch'])

# Using get() to access a value (safe access)
print("\nUsing get() to access salary:\n", employee_info.get('salary'))

# Removing a key-value pair using pop()
removed_value = employee_info.pop('salary')
print("\nThe salary has been removed, and its value was:", removed_value)
print("The updated employee info is:\n", employee_info)

# Removing the last key-value pair using popitem()
removed_item = employee_info.popitem()
print("\nThe last key-value pair removed is:\n", removed_item)
print("The updated employee info is:\n", employee_info)

# Adding multiple key-value pairs using update()
employee_info.update({'position': 'Manager', 'department': 'Operations'})
print("\nThe updated employee info with multiple values:\n", employee_info)

# Checking if a key exists
if 'name' in employee_info:
    print("\nKey 'name' exists in employee_info")

# Getting all keys
print("\nAll keys in the employee dictionary:\n", employee_info.keys())

# Getting all values
print("\nAll values in the employee dictionary:\n", employee_info.values())

# Getting all key-value pairs
print("\nAll key-value pairs in the employee dictionary:\n", employee_info.items())

# Clearing the dictionary
employee_info.clear()
print("\nThe employee dictionary after clear operation:\n", employee_info)
