# Combine multiple iterables element-wise:
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['NYC', 'LA', 'Chicago']

pairs = list(zip(names, ages, cities))
print(pairs)

dict_pairs = dict(zip(names, ages))
print(dict_pairs)


unzipNames, unzipAges, unzipCities = zip(*pairs)
print(unzipNames)
print(unzipAges)
print(unzipCities)
