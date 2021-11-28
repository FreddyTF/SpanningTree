



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
	zeile = zeile.replace(' ', "").replace(';','').replace('\n','')
	ortZeichenIstgleich = zeile.find("=")
	nodeName = zeile[0:ortZeichenIstgleich]
	print("NodeName:---" + nodeName + "---")
	nodeId = zeile[ortZeichenIstgleich+1:]
	print("NodeId:---" + nodeId + "---")




for zeile in eingabeGewichteString:
	print(zeile)
	zeile = zeile.replace(' ', "").replace(';', '').replace('\n', '')
	ortZeichenBindestrich = zeile.find("-")
	ortZeichenDoppelPunkt = zeile.find(":")
	node1 = zeile[0:ortZeichenBindestrich]
	print("Node1:---" + node1 + "---")
	node2 = zeile[ortZeichenBindestrich+1:ortZeichenDoppelPunkt]
	print("Node2:---" + node2 + "---")
	kantenGewicht = zeile[ortZeichenDoppelPunkt:]
	print("Kantengewicht:---" + kantenGewicht + "---")