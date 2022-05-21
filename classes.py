class Node:
    def __init__(self, nodeName, nodeID, index):
        self.nodeName = nodeName  # Knotenname
        self.nodeID = nodeID  # Knoten ID > 0
        self.edgeList = []  # Liste der Kanten zu allen Nachbarknoten
        self.sumRootCosts = 0  # Kosten, um zum Root zu senden
        self.msgCnt = 0  # Zählt mit, wie oft der Knoten bei der Bearbeitung des Algorithmus aufgerufen wird
        self.index = index  # Index des Knotens in der Liste der Knoten
        self.vermuteteRootID = self.nodeID  # Vermutete nodeID des Root-Knotens
        self.sendeRichtungsName = self.nodeName  # Name des Knotens, an den gesendet wird
        self.sendeRichtungsIndex = self.index  # Index des Knotens, an den gesendet wird

    def __repr__(self):
        return "Name" + str(self.nodeName) + " ID" + str(self.nodeID) + " sum" + str(self.sumRootCosts)

    def append_edge(self, edge):
        self.edgeList.append(edge)


class Edge:
    def __init__(self, costs, wohin, woher):
        self.woher = woher  # nodeName des Startknotens der Kante
        self.wohin = wohin  # nodeName des Endknotens der Kante
        self.costs = costs  # Wegekosten der Kante

    def edgeTausch(self):
        (self.wohin, self.woher) = (self.woher, self.wohin)
        return

    def __repr__(self):
        return "woher" + str(self.woher) + " wohin" + str(self.wohin) + " costs" + str(self.costs)
