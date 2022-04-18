class Node:
    def __init__(self, name, nodeID, index):
        self.name = name            # Bezeichner des Knotens
        self.nodeID = nodeID        # Knoten ID > 0
        self.link = []              # 1. ZeileListe aller pot.Nachbarknoten
        self.summeKosten = 0        # Kosten um zum Root zu senden
        self.msgCnt = 0             # Zählt mit, wie oft der Knoten bei der Bearbeitung des Algorithmus aufgerufen wird
        self.vermuteteRootID = self.nodeID
        self.sendeRichtungsName = self.name
        self.index = index
        self.sendeRichtungsIndex = index


    def __repr__(self):
        return "Name" + str(self.name) + " ID" + str(self.nodeID) +  " sum" + str(self.summeKosten)

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