



"""Input

alle Zeilen mit = in einen Array
alle Zeile mit : in einen Array

"""
nodeEingabeString = []
eingabeGewichteString = []

eingabe = open('Input-File', 'r')

for zeile in eingabe:
	if(0 == zeile.__contains__("//")):
		if(zeile.__contains__("=")):
			nodeEingabeString.append(zeile)
		elif(zeile.__contains__("-") and zeile.__contains__(":")):
			eingabeGewichteString.append(zeile)

eingabe.close()

for zeile in nodeEingabeString:
	print(zeile)


for zeile in eingabeGewichteString:
	print(zeile)