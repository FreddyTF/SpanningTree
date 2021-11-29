MAX_IDENT = 5     #Maximallänge für Namen
MAX_ITEMS = 100   #Maximale Zeilenanzahl für die Eingabedatei
MAX_KOSTEN = 100  #Maximales Kantengewicht
MAX_NODE_ID = 100 #Maximale Konten Id



"""Input

alle Zeilen mit = in einen Array
alle Zeile mit : in einen Array

"""
nodeEingabeString = []
eingabeGewichteString = []

eingabe = open('Input-File', 'r')
zeilenanzahl = 0

for zeile in eingabe:
	zeilenanzahl += 1

if zeilenanzahl > MAX_ITEMS:
	print("Zeilenanzahl zu gross")
	exit(1)

for zeile in eingabe:
	if not zeile.__contains__("//"):
		if(zeile.__contains__("=")):
			nodeEingabeString.append(zeile)
		elif(zeile.__contains__("-") and zeile.__contains__(":")):
			eingabeGewichteString.append(zeile)

eingabe.close()


anzahl_nodes  = 0
anzahl_kanten = 0

for zeile in nodeEingabeString:
	anzahl_nodes +=  1

for zeile in eingabeGewichteString:
	anzahl_kanten += 1

for zeile in nodeEingabeString:
	print(zeile)
	zeile = zeile.replace(' ', "").replace(';','').replace('\n','')
	ortZeichenIstgleich = zeile.find("=")
	nodeName = zeile[0:ortZeichenIstgleich]
	if(len(nodeName) > MAX_IDENT):
		exit()
	print("NodeName:---" + nodeName + "---")
	nodeId = int(zeile[ortZeichenIstgleich+1:])
	if not (1 <= nodeId and nodeId <= MAX_NODE_ID):
		exit()
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
	kantenGewicht = int(zeile[ortZeichenDoppelPunkt:])
	if kantenGewicht > MAX_KOSTEN:
		exit()
	print("Kantengewicht:---" + kantenGewicht + "---")