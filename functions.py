from classes import Link, Node



def nodesEintragen(nodeEingabeString, MAX_IDENT, nodes, node_names, MAX_NODE_ID):
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
		node_names.append(nodeName)
	return nodes, node_names

def gewichteEintrange(eingabeGewichteString, MAX_KOSTEN, node_names, links, nodes):
	for zeile in eingabeGewichteString:

		zeile = zeile.replace(' ', "").replace(';', '').replace('\n', '')
		ortZeichenBindestrich = zeile.find("-")
		ortZeichenDoppelPunkt = zeile.find(":")
		node1 = zeile[0:ortZeichenBindestrich]
		node2 = zeile[ortZeichenBindestrich+1:ortZeichenDoppelPunkt]
		kantenGewicht = int(zeile[ortZeichenDoppelPunkt+1:])

		if kantenGewicht > MAX_KOSTEN:
			exit()
		node1position = node_names.index(node1)
		node2position = node_names.index(node2)
		links[node1position][node2position] = Link(kantenGewicht, nodes[node2position].nodeID)
		links[node2position][node1position] = Link(kantenGewicht, nodes[node1position].nodeID)

	return links


def nachrichtenaustausch(nodes, links):
    #for node in nodes:
	reihenfolge = [1,0,2,3,1,2,1]
	for k in reihenfolge:
		node = nodes[k]
		sendeZeileIndex = nodes.index(node)
		zeile = links[sendeZeileIndex]
		listeKanten = []
		for i in range(len(zeile)):
			if zeile[i].kosten > 0:
			   listeKanten.append(i)

		for i in listeKanten: #alle an Node verbundenen Knoten
			neues_angebot_link = links[i][sendeZeileIndex]
			print("neues_angebot_link = " , neues_angebot_link)
			altes_angebot_link = links[sendeZeileIndex][i]
			print("altes_angebot_link = ", altes_angebot_link)

			if neues_angebot_link.rootID < altes_angebot_link.rootID:
				for row_index in range(len(nodes)):
					if links[row_index][i].kosten:
						links[row_index][i].rootID = neues_angebot_link.rootID
						links[row_index][i].summeKosten = neues_angebot_link.summeKosten + links[row_index][i].kosten

			elif neues_angebot_link.rootID == altes_angebot_link.rootID:
				if not altes_angebot_link.summeKosten < neues_angebot_link.summeKosten + altes_angebot_link.kosten:
					links[sendeZeileIndex][row_index].rootID = neues_angebot_link.rootID
					links[sendeZeileIndex][row_index].summeKosten = neues_angebot_link.summeKosten + links[sendeZeileIndex][row_index].kosten
		"""
		if node.nodeID < links[i][sendeZeileIndex].rootID:
			links[i][sendeZeileIndex].rootID = node.nodeID
			links[i][sendeZeileIndex].summeKosten = node.nextHop
		elif node.nodeID <= links[i][sendeZeileIndex].rootID:
			if (node.nextHop + links[i][sendeZeileIndex].kosten) < links[i][sendeZeileIndex].summeKosten:
				links[i][sendeZeileIndex].rootID = node.nodeID
				links[i][sendeZeileIndex].summeKosten = node.nextHop
		"""

	"""
	for i in listeKanten:
		if node.nodeID < links[i][sendeZeileIndex].rootID:
			links[i][sendeZeileIndex].rootID = node.nodeID
			links[i][sendeZeileIndex].summeKosten = node.nextHop
		elif node.nodeID <= links[i][sendeZeileIndex].rootID:
			if (node.nextHop + links[i][sendeZeileIndex].kosten) < links[i][sendeZeileIndex].summeKosten:
				links[i][sendeZeileIndex].rootID = node.nodeID
				links[i][sendeZeileIndex].summeKosten = node.nextHop
	"""

def formatierte_ausgabe(nodes, links, anzahl_nodes):
	print(" " * 7,nodes)
	for i in range(anzahl_nodes):
		print(nodes[i] , links[i])