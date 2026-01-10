#taking total amount as input from user
amount =int(input("please enter amount for withdraw"))
#calculating the number of notes of different dominants
note1 = amount//100
note2 = (amount%100)//50
note3 = ((amount%100)%50)//10
print("note of 100 rupee",note1)
print("note of 50 rupee",note2)
print("note of 10 rupee",note3)