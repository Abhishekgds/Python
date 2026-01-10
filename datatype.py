#lets check the data type value of different variables
a=5
print("type of a: ", type(a))
b=5.6
print("type of b: ", type(b))
c="coding"
print("type of c: ", type(c))
d= True
print("type of d: ", type(d))
#input a word
text=str(input("Enter a string: "))
#reverse string
#using step value as -1 to literate in reverse
revText = text[::-1]
text = revText
print("reverse of given string is:")
print(text)