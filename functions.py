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

def gewichteEintrange(eingabeGewichteString, MAX_KOSTEN, node_names, links):
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
		links[node1position][node2position] = Link(kantenGewicht)
		links[node2position][node1position] = Link(kantenGewicht)

	return links
