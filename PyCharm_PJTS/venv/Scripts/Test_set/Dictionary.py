#     (key)        (value)
enemy= {
    'race'          : 'uruk',
    'location_X'    :   70,
    'location_Y'    :   60,
    'weapon'        : "Sword",
    'image'         :  ['image1.jpg,image2.jpg,image3.jpg,']
    }

enemy['rank']= 'Captan'

print(enemy)
print(enemy['race'])

all_enemies=[]
all_enemies.append(enemy)
print(all_enemies)