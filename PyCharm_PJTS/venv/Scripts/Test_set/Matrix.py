cities=["MinasTirith","HelmsDeep"]
print(type(cities))

countries={"Gondor","Rohan"}
print(type(countries))
# city=str(cities[1])
# print("city_name  "+city)
#
cities.append("Edoras") # расширение массива
# print(cities)
cities.insert(3,"Asgiliath")
# print(cities)
# del cities[-1]
# print(cities)
# можно сортировать sort по алфавиту
for x in cities:
    print(x)
    # print(x.upper()) # строчные -> заглавные