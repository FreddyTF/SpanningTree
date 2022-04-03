from classes import Node, Kante


def nodesEintragen(nodeEingabeString, MAX_IDENT, nodes, MAX_NODE_ID):
	i = 0
	for zeile in nodeEingabeString:
		zeile = zeile.replace(' ', "").replace(';','').replace('\n','')
		ortZeichenIstgleich = zeile.find("=")
		nodeName = zeile[0:ortZeichenIstgleich]
		if(len(nodeName) > MAX_IDENT):
			exit()
		nodeId = int(zeile[ortZeichenIstgleich+1:])
		if not (1 <= nodeId and nodeId <= MAX_NODE_ID):
			exit()
		node = Node(nodeName, nodeId, i)
		nodes.append(node)
		i += 1
	return nodes

def gewichteEintragen(eingabeGewichteString, MAX_KOSTEN):
	liste_links = []
	for zeile in eingabeGewichteString:

		zeile = zeile.replace(' ', "").replace(';', '').replace('\n', '')
		ortZeichenBindestrich = zeile.find("-")
		ortZeichenDoppelPunkt = zeile.find(":")
		node1 = zeile[0:ortZeichenBindestrich]
		node2 = zeile[ortZeichenBindestrich+1:ortZeichenDoppelPunkt]
		kantenGewicht = int(zeile[ortZeichenDoppelPunkt+1:])

		if kantenGewicht > MAX_KOSTEN:
			exit()
		neuerLink = Kante(kantenGewicht, node1, node2)
		liste_links.append(neuerLink)

	return liste_links

def every_node_x_times(x, nodes):
	for node in nodes:
		if node.msgCnt < 10:
			return False
	return True