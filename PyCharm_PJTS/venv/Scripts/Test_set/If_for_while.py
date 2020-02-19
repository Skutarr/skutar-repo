
num = input ("Введите число: ")

if int (num) > 0:
	if int (num) > 10:
		print ("Вы ввели число больше 10")
		if int (num) >= 50:
			print ("Вы ввели число больше 50")
	else:
		print ("Вы ввели число меньше 10 и больше 0")
elif int (num) < -10:
	print ("Вы ввели число меньше -10")
else:
	print ("Вы ввели число меньше 0 и больше -10")
print ("All is okay!")
print()
name = input ()
A = 'Yes' if name != "Test" else 'No'
print (A)

#------------------------------------- WHILE_FOR----------------------------
i = 1000
while i > 100:
	print (i)
	i /= 2

for j in 'hello world':
	if j == 'w':
		break
else:
	print ("Буквы а нету в слове")