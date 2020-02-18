race = input("Enter Enemy's race ")
print("Enemy's race - " + str(race))

message=""
counter=5
while counter>0:
    message = input("Eneter something   ")
    if message == "Correct":
        break
    counter=counter-1
    print("Not correct")

print("Correct")