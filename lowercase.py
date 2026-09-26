word = input("Enter a word: ")
result = ""

for number in word:
	if number.islower():
		result += number.upper()
	else:
		result += number
print("word is : " + result)
