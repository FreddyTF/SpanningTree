class Node:
    def __init__(self, name, nodeID):
        self.name = name            # Bezeichner des Knotens
        self.nodeID = nodeID        # Knoten ID > 0
        self.link = []              # 1. ZeileListe aller pot.Nachbarknoten
        self.nextHop2Root = name    # Name des Node an den er sendet
        self.summeKosten = 0        # Kosten um zum Root zu senden
        self.msgCnt = 0             # Zählt mit, wie oft der Knoten bei der Bearbeitung des Algorithmus aufgerufen wird
        self.vermuteteRootID = self.nodeID

    def __repr__(self):
        return "Name" + str(self.name) + " ID" + str(self.nodeID) + " nH2R" + str(self.nextHop2Root) + " sum" + str(self.summeKosten)

    def append_kante(self, kante):
        self.link.append(kante)


class Kante:
    def __init__(self, kosten, wohin, woher):
        self.kosten = kosten
        self.wohin = wohin
        self.woher = woher

    def kante_tausch(self):
        (self.wohin, self.woher) = (self.woher, self.wohin)
        return

    def __repr__(self):
        return  "woher" + str(self.woher) + " wohin" + str(self.wohin) + " kosten" + str(self.kosten)