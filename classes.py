class Node:
    def __init__(self, name, nodeID):
        self.name = name            # Bezeichner des Knotens
        self.nodeID = nodeID        # Knoten ID > 0
        self.link = []              # Liste aller pot.Nachbarknoten
        self.nextHop = self.name    # Berechneter Link zum nächsten Knoten in Richtung Root
        self.msgCnt = 0             # Zählt mit, wie oft der Knoten bei der Bearbeitung des Algorithmus aufgerufen wird

class Link:
    def __init__(self, kosten = 0):
        # Linkkosten von Node_i -> Node_k
        # kosten = 0: kein Link vorhanden
        # Entspricht ursprüngliche Initialisierung des eingelesenen Graphen
        self.kosten = kosten
        # Über diesen Link erhaltene Nachricht der Nachbarknoten
        # mit Vorschlag der Root incl.Gesamtkosten zur Root
        self.rootID = 0

        self.summeKosten = 0