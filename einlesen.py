import logging
from classes import Node, Kante
from functions import nodesEintragen, gewichteEintrange

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

eingabe = open('Input-File2', 'r')
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
			logging.info("node hinzugefügt zur passenden Liste")
		elif(zeile.__contains__("-") and zeile.__contains__(":")):
			eingabeGewichteString.append(zeile)
			logging.info("Kante hinzugefügt zur passenden Liste")

eingabe.close()


anzahl_nodes  = 0
anzahl_kanten = 0

for zeile in nodeEingabeString:
	anzahl_nodes += 1

for zeile in eingabeGewichteString:
	anzahl_kanten += 1

nodes = []
node_names = []

nodes = nodesEintragen(nodeEingabeString, MAX_IDENT, nodes, node_names, MAX_NODE_ID)
liste_kanten = gewichteEintrange(eingabeGewichteString, MAX_KOSTEN, nodes)


for node in nodes:
	#print(node)
	for kante in liste_kanten:
		if kante.woher == node.name or kante.wohin == node.name:
			if kante.woher != node.name:
				kante.kante_tausch()
			node.append_kante(kante)
			#print(kante)

#print("Ende")
# for kante in liste_kanten:
# 	print(kante)

#
for node in nodes:
	print(node)
	for kante in node.link:
		print(kante)

