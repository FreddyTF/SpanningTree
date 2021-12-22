import logging
from classes import Node
LOG = logging.getLogger()
LOG.setLevel(logging.DEBUG)


MAX_IDENT = 5     #Maximallänge für Namen
MAX_ITEMS = 100   #Maximale Zeilenanzahl für die Eingabedatei
MAX_KOSTEN = 100  #Maximales Kantengewicht
MAX_NODE_ID = 100 #Maximale Konten Id



"""
Input

alle Zeilen mit = in einen Array
alle Zeile mit : in einen Array

"""

nodeEingabeString = []
eingabeGewichteString = []

eingabe = open('Input-File', 'r')
logging.info(eingabe)
inhalt = []

zeilenanzahl = 0
for zeile in eingabe:
	inhalt.append(zeile)
	zeilenanzahl += 1
logging.info("zeilenanzahl = " + str(zeilenanzahl))


if zeilenanzahl > MAX_ITEMS:
	print("Zeilenanzahl zu gross")
	exit(1)

for zeile in inhalt:
	if not zeile.__contains__("//"):
		if(zeile.__contains__("=")):
			nodeEingabeString.append(zeile)
			logging.info("node hinzugefügt")
		elif(zeile.__contains__("-") and zeile.__contains__(":")):
			eingabeGewichteString.append(zeile)
			logging.info("Kante hinzugefügt")

eingabe.close()


anzahl_nodes  = 0
anzahl_kanten = 0

for zeile in nodeEingabeString:
	anzahl_nodes += 1

for zeile in eingabeGewichteString:
	anzahl_kanten += 1

#dataNodes = [[0 for x in range(anzahl_nodes)] for y in range(2)]
nodes = []

for zeile in nodeEingabeString:
	zeile = zeile.replace(' ', "").replace(';','').replace('\n','')
	ortZeichenIstgleich = zeile.find("=")
	nodeName = zeile[0:ortZeichenIstgleich]
	if(len(nodeName) > MAX_IDENT):
		exit()
	nodeId = int(zeile[ortZeichenIstgleich+1:])
	if not (1 <= nodeId and nodeId <= MAX_NODE_ID):
		exit()
	node = Node(nodeName, nodeId)
	nodes.append(node)

for zeile in eingabeGewichteString:

	zeile = zeile.replace(' ', "").replace(';', '').replace('\n', '')
	ortZeichenBindestrich = zeile.find("-")
	ortZeichenDoppelPunkt = zeile.find(":")
	node1 = zeile[0:ortZeichenBindestrich]
	node2 = zeile[ortZeichenBindestrich+1:ortZeichenDoppelPunkt]
	kantenGewicht = int(zeile[ortZeichenDoppelPunkt+1:])

	if kantenGewicht > MAX_KOSTEN:
		exit()

