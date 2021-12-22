class Node:
    def __init__(self, name, nodeID):
        self.name = name            # Bezeichner des Knotens
        self.nodeID = nodeID        # Knoten ID > 0
        self.link = []              # Liste aller pot.Nachbarknoten
        self.nextHop = 0            # Berechneter Link zum nächsten Knoten in Richtung Root
        self.msgCnt = 0             # Zählt mit, wie oft der Knoten bei der Bearbeitung des Algorithmus aufgerufen wird

class Link:
    def __init__(self, kosten = 0, rootID = 0, summeKosten = 0):
        # Linkkosten von Node_i -> Node_k
        # kosten = 0: kein Link vorhanden
        # Entspricht ursprüngliche Initialisierung des eingelesenen Graphen
        self.kosten = kosten
        # Über diesen Link erhaltene Nachricht der Nachbarknoten
        # mit Vorschlag der Root incl.Gesamtkosten zur Root
        self.rootID = rootID
        self.summeKosten = summeKosten

    def __repr__(self):
        string_summeKosten = str(self.summeKosten)
        string_rootID = str(self.rootID)
        return string_rootID.rjust(3) + ":" + string_summeKosten.ljust(3)

def nachrichtenaustausch(nodes, links):
    for node in nodes:
        sendeZeileIndex = nodes.index(node)
        zeile = links[sendeZeileIndex]
        listeKanten = []
        for i in range(len(zeile)):
            if zeile[i].kosten > 0:
               listeKanten.append(i)

        for i in listeKanten:
            if node.nodeID < links[i][sendeZeileIndex].rootID:
                links[i][sendeZeileIndex].rootID = node.nodeID
                links[i][sendeZeileIndex].summeKosten = node.nextHop
            elif node.nodeID <= links[i][sendeZeileIndex].rootID:
                if (node.nextHop + links[i][sendeZeileIndex].kosten) < links[i][sendeZeileIndex].summeKosten:
                    links[i][sendeZeileIndex].rootID = node.nodeID
                    links[i][sendeZeileIndex].summeKosten = node.nextHop
