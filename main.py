import logging
from classes import Node, Edge
from functions import nodesEintragen, costsEintragen, every_node_x_times
from copy import deepcopy

from random import randint

# Logging initialisieren
LOG = logging.getLogger()
LOG.setLevel(logging.DEBUG)


def main():
    """
    Initalisierung der oberen Grenze für bestimmte Parameter
    """

    MAX_IDENT = 5      # Maximallänge für Namen
    MAX_ITEMS = 100    # Maximale Zeilenanzahl für die Eingabedatei
    MAX_COSTS = 100    # Maximales Wegekostes einer Kante
    MAX_NODE_ID = 100  # Maximale Konten Id

    """
    Input

    alle Zeilen mit = in ein Array
    alle Zeile  mit : in ein Array

    """

    # Input File einlesen
    eingabe = open('Input-File', 'r')
    logging.info(eingabe)
    inhalt = []

    for zeile in eingabe:
        inhalt.append(zeile)


    eingabe.close()

    zeilenanzahl = len(inhalt)

    logging.info(f"zeilenanzahl = {zeilenanzahl}")

    # Programmabbruch, wenn Eingabedatei zu groß
    if zeilenanzahl > MAX_ITEMS:
        print("Zeilenanzahl zu gross")
        exit(1)

    # Anlegen von Listen für Node und Gewichte von Verbindungen
    nodeEingabeString = []
    costsEingabeGewichteString = []

    for zeile in inhalt:
        if not "//"in zeile:
            if "=" in zeile:
                nodeEingabeString.append(zeile)
                logging.info("Node hinzugefügt zur passenden Liste")
            elif ("-" in zeile and ":" in zeile):
                costsEingabeGewichteString.append(zeile)
                logging.info("Kante hinzugefügt zur passenden Liste")


    # Initialisierung der Variablen für die Anzahl der Knoten und Kanten
    anzahl_nodes = len(nodeEingabeString)
    # anzahl_kanten = len(eingabeGewichteString)

    # Initialiserung der Arrays für Nodes und deren zugehörigen Daten
    nodeList = []
    nodeNameList = []

    nodeList = nodesEintragen(nodeEingabeString, MAX_IDENT, nodeList, MAX_NODE_ID)
    edgeList = costsEintragen(costsEingabeGewichteString, MAX_COSTS)

    for node in nodeList:
        for edge in edgeList:
            if edge.woher == node.nodeName or edge.wohin == node.nodeName:
                if edge.woher != node.nodeName:
                    edge.kante_tausch()
                node.append_edge(deepcopy(edge))

    for node in nodeList:
        nodeNameList.append(node.nodeName)

    # reihenfolge = ["B", "A", "C", "D", "B", "C", "B"]

    # for node_name in reihenfolge:
    counter = 0
    x = 10
    while (counter < 100 and not every_node_x_times(x, nodeList)):

        node_index = randint(0, anzahl_nodes - 1)
        logging.info(node_index)
        # node_index = node_names.index(node_name)
        node = nodeList[node_index]
        # print(node)
        node.msgCnt += 1

        # angebot raussuchen
        # node.summeKosten
        # node.vermutetRootID

        for edge in node.linkList:
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

    #for node in nodes:
    #    print(node)
    #    print("summekosten", node.summeKosten)
    #    print("vermuteteRootID", node.vermuteteRootID)

    # Endausgabe
    for node in nodeList:
        print(node.nodeName, " - ", node.sendeRichtungsName, "(Index ", node.sendeRichtungsIndex, ")")


if __name__ == "__main__":
    main()