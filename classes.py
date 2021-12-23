class Node:
    def __init__(self, name, nodeID, nextHop):
        self.name = name            # Bezeichner des Knotens
        self.nodeID = nodeID        # Knoten ID > 0
        self.link = []              # Liste aller pot.Nachbarknoten
        self.nextHop = nextHop      # Berechneter Link zum nächsten Knoten in Richtung Root
        self.msgCnt = 0             # Zählt mit, wie oft der Knoten bei der Bearbeitung des Algorithmus aufgerufen wird

    def __repr__(self):
        return (str(self.name) + " " +  str(self.nodeID) + " " + str(self.nextHop)).center(7)

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
