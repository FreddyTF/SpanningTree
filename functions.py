from classes import Node, Edge


def nodesEintragen(nodeEingabeString, MAX_IDENT, nodes, MAX_NODE_ID):
	i = 0
	for zeile in nodeEingabeString:
		zeile = zeile.replace(' ', "").replace(';','').replace('\n','')
		ortZeichenIstgleich = zeile.find("=")
		nodeName = zeile[0:ortZeichenIstgleich]
		if(len(nodeName) > MAX_IDENT):
			exit()
		nodeID = int(zeile[ortZeichenIstgleich + 1:])
		if not (1 <= nodeID and nodeID <= MAX_NODE_ID):
			exit()
		node = Node(nodeName, nodeID, i)
		nodes.append(node)
		i += 1
	return nodes

def costsEintragen(eingabeGewichteString, MAX_KOSTEN, edgeList):
	for zeile in eingabeGewichteString:

		zeile = zeile.replace(' ', "").replace(';', '').replace('\n', '')
		ortZeichenBindestrich = zeile.find("-")
		ortZeichenDoppelPunkt = zeile.find(":")
		nodeWoher = zeile[0:ortZeichenBindestrich]
		nodeWohin = zeile[ortZeichenBindestrich + 1:ortZeichenDoppelPunkt]
		edgeCosts = int(zeile[ortZeichenDoppelPunkt + 1:])

		if edgeCosts > MAX_KOSTEN:
			exit()
		neuerLink = Edge(edgeCosts, nodeWoher, nodeWohin)
		edgeList.append(neuerLink)

	return edgeList

def every_node_x_times(x, nodes):
	for node in nodes:
		if node.msgCnt < 10:
			return False
	return True