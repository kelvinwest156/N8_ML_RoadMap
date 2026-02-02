numbers =[1, 2, 3, 4]
numbers2 =[8, 3, 2, 9]
numbers3 =[3, 6, 6, 7]


# def square(x):
#     return x**2
#
# squared = list(map(square, numbers))
# print(squared)

squared = list(map(lambda x,y,z: x+y+z, numbers, numbers2, numbers3))
print(squared)