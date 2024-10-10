def alphabeth(word):
	vowel = ['a', 'e', 'i', 'o', 'u']
	myBoolean = "false"
	for count in range(len(vowel)):
		if word == vowel[count]:
			myBoolean = "True"
	print(myBoolean)

alphabeth('i')


