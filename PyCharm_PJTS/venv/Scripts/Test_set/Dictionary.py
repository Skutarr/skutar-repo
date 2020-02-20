#------------------------------------------СЛОВАРИ-----------------
import json

filename = "enemies_list"
myfile = open(filename, mode="w", encoding="Latin-1")

#     (key)        (value)
enemy1 = {'race': 'uruk', 'location_X': 70, 'location_Y': 60, 'weapon': "Sword",
          'image': ['image1.jpg,image2.jpg,image3.jpg,'], 'rank': 'Captan'}

enemy2 = {'race': 'ork', 'location_X': 23, 'location_Y': 6, 'weapon': "Bow",
          'image': ['image4.jpg,image5.jpg,image6.jpg,'], 'rank': 'soldier'}

# print(enemy1)
# print(enemy1['race'])

all_enemies = []
all_enemies.append(enemy1)
all_enemies.append(enemy2)

# print(all_enemies)
# ------------------- SAVE by JSON --------------------
json.dump(all_enemies,myfile)
myfile.close()

# ------------------- LOAD by JSON --------------------
myfile = open(filename, mode="r", encoding="Latin-1")
json_data=json.load(myfile)

for enemy in json_data:
    print("Enemy Type - " + str(enemy['race']))

