import logging
from classes import Node, Edge
from functions import nodesEintragen, edgesEintragen, every_node_x_times
from copy import deepcopy

from random import randint

# Logging initialisieren
LOG = logging.getLogger()
LOG.setLevel(logging.DEBUG)


def main():
    """
    Initalisierung der oberen Grenze für bestimmte Parameter
    """

    MAX_IDENT = 5  # Maximallänge für Namen
    MAX_ITEMS = 100  # Maximale Zeilenanzahl für die Eingabedatei
    MAX_COSTS = 100  # Maximales Wegekosten einer Kante
    MAX_NODE_ID = 100  # Maximale Knoten-ID

    """
    Input

    alle Zeilen mit = in eine Liste mit den Zeilen für die Knoten einlesen
    alle Zeile  mit : in eine Liste mit den Zeilen für die Kanten einlesen

    """

    # Input File einlesen
    eingabe = open('Input-File', 'r')
    logging.info(eingabe)

    # Anlegen der Liste mit den Zeilen der Eingabedatei
    inhaltList = []  # Liste mit den Zeilen der Eingabedatei

    for zeile in eingabe:
        inhaltList.append(zeile)

    eingabe.close()

    zeilenanzahl = len(inhaltList)

    logging.info(f"zeilenanzahl = {zeilenanzahl}")

    # Programmabbruch, wenn die Eingabedatei zu groß ist
    if zeilenanzahl > MAX_ITEMS:
        print("Zeilenanzahl zu gross")
        exit(1)

    # Listen mit den Zeilen für Knoten und Kanten erstellen
    nodeEingabeString = []  # Liste mit den Zeilen für die Knoten
    edgeEingabeString = []  # Liste mit den Zeilen für die Kanten

    for zeile in inhaltList:
        if not "//" in zeile:
            if "=" in zeile:
                nodeEingabeString.append(zeile)
                logging.info("Knoten hinzugefügt zur passenden Liste")
            elif ("-" in zeile and ":" in zeile):
                edgeEingabeString.append(zeile)
                logging.info("Kante hinzugefügt zur passenden Liste")

    # Anzahl der Knoten ermitteln
    anzahl_nodes = len(nodeEingabeString)

    # Anlegen der Listen für Knoten, Knotennamen und Kanten
    nodeList = []  # Liste der Knoten
    nodeNameList = []  # Liste der Knotennamen
    edgeList = []  # Liste der Kanten

    # Daten aus den Listen mit den Zeilen für Knoten und Kanten extrahieren

    nodeList = nodesEintragen(nodeEingabeString, MAX_IDENT, nodeList, MAX_NODE_ID)
    edgeList = edgesEintragen(edgeEingabeString, MAX_COSTS, edgeList)

    # Ermittlung der Nachbarknoten und Wegekosten für jeden Knoten

    for node in nodeList:
        for edge in edgeList:
            if edge.woher == node.nodeName or edge.wohin == node.nodeName:
                if edge.woher != node.nodeName:
                    edge.edgeTausch()
                node.append_edge(deepcopy(edge))

    # Erstellung der Liste mit den Knotennamen

    for node in nodeList:
        nodeNameList.append(node.nodeName)

    # Bestimmung des Root-Knotens und des Spanning-Trees nach Bellman Ford

    counter = 0  # Zähler der Schleifendurchläufe
    x = 10  # Minimalanzahl der Durchläufe für jeden Knoten

    while (counter < 100 and not every_node_x_times(x, nodeList)):

        node_index = randint(0, anzahl_nodes - 1)
        logging.info(node_index)
        node = nodeList[node_index]
        node.msgCnt += 1

        # angebot raussuchen
        # node.sumRootCosts
        # node.vermutetRootID

        for edge in node.edgeList:
            empfangerNodeName = edge.wohin
            empfangerNodeIndex = nodeNameList.index(empfangerNodeName)
            empfangerNode = nodeList[empfangerNodeIndex]
            if empfangerNode.vermuteteRootID > node.vermuteteRootID:
                empfangerNode.vermuteteRootID = node.vermuteteRootID
                empfangerNode.sumRootCosts = node.sumRootCosts + edge.costs
                empfangerNode.sendeRichtungsName = node.nodeName
                empfangerNode.sendeRichtungsIndex = node.index
            elif empfangerNode.vermuteteRootID == node.vermuteteRootID:
                if node.sumRootCosts + edge.costs < empfangerNode.sumRootCosts:
                    empfangerNode.sumRootCosts = node.sumRootCosts + edge.costs
                    empfangerNode.sendeRichtungsName = node.nodeName
                    empfangerNode.sendeRichtungsIndex = node.index

        counter += 1

    # for node in nodes:
    #     print(node)
    #     print("sumRootCosts", node.sumRootCosts)
    #     print("vermuteteRootID", node.vermuteteRootID)

    # Endausgabe
    for node in nodeList:
        print(node.nodeName, " - ", node.sendeRichtungsName, "(Index ", node.sendeRichtungsIndex, ")")

    listRootNodes = [node for node in nodeList if node.sumRootCosts == 0]
    for node in listRootNodes:
        print(f"Root Node: {node.nodeName}")

if __name__ == "__main__":
    main()
