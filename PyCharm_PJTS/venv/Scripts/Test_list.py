cities=["1","2"]
print(type(cities))

countries={"3","4"}
print(type(countries))
city=str(cities[1])
print("city_name  "+city)

cities.append("3") # расширение массива
print(cities)
cities.insert(3,"4")
print(cities)
del cities[-1]
print(cities)
# можно сортировать sort по алфавиту 