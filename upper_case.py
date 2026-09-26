word = input("Enter a word: ")
result = ""

for number in word:
	if number.isupper():
		result += number.lower()
	else:
		result += number
print("word is : " + result)
