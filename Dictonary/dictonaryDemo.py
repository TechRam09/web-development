student = {"name":"shree","age":20,"branch": "cse"}
# print(student)
# print(type(student))


# add  value
student["college"] = "VVIET"
# print(student)

# add a list   
student["marks"] = [48,55,56,60,53]
# print(student)

#access
# print(student['marks'])

# print(student.get("age"))


#update existing value
student["age"] = 23
# print(student)

#remove the element 
del student["college"]
# print(student)


#items() => print all items in value of tuples
print(student.items())

#keys() => returns only keys
print(student.keys())

#values() => returns only.values
print(student.values())

#pop() => pop the topest element from the dictionary
student.pop()
print()

#clear() => returns a empty dictionary
student.clear()
print(student)