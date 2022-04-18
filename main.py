import logging
from classes import Node, Kante
from functions import nodesEintragen, gewichteEintragen, every_node_x_times
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
    MAX_KOSTEN = 100  # Maximales Kantengewicht
    MAX_NODE_ID = 100  # Maximale Konten Id

    """
    Input

    alle Zeilen mit = in einen Array
    alle Zeile mit : in einen Array

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
    eingabeGewichteString = []

    for zeile in inhalt:
        if not "//"in zeile:
            if "=" in zeile:
                nodeEingabeString.append(zeile)
                logging.info("Node hinzugefügt zur passenden Liste")
            elif ("-" in zeile and ":" in zeile):
                eingabeGewichteString.append(zeile)
                logging.info("Kante hinzugefügt zur passenden Liste")


    # Initialisierung der Variablen für die Anzahl der Knoten und Kanten
    anzahl_nodes = len(nodeEingabeString)
    # anzahl_kanten = len(eingabeGewichteString)

    # Initialiserung der Arrays für Nodes und deren zugehörigen Daten
    nodes = []
    node_names = []

    nodes = nodesEintragen(nodeEingabeString, MAX_IDENT, nodes, MAX_NODE_ID)
    liste_kanten = gewichteEintragen(eingabeGewichteString, MAX_KOSTEN)

    for node in nodes:
        for kante in liste_kanten:
            if kante.woher == node.name or kante.wohin == node.name:
                if kante.woher != node.name:
                    kante.kante_tausch()
                node.append_kante(deepcopy(kante))

    for node in nodes:
        node_names.append(node.name)

    # reihenfolge = ["B", "A", "C", "D", "B", "C", "B"]

    # for node_name in reihenfolge:
    counter = 0
    x = 10
    while (counter < 100 and not every_node_x_times(x, nodes)):

        node_index = randint(0, anzahl_nodes - 1)
        logging.info(node_index)
        # node_index = node_names.index(node_name)
        node = nodes[node_index]
        # print(node)
        node.msgCnt += 1

        # angebot raussuchen
        # node.summeKosten
        # node.vermutetRootID

        for kante in node.link:
            empfangerNodeName = kante.wohin
            empfangerNodeIndex = node_names.index(empfangerNodeName)
            empfangerNode = nodes[empfangerNodeIndex]
            if empfangerNode.vermuteteRootID > node.vermuteteRootID:
                empfangerNode.vermuteteRootID = node.vermuteteRootID
                empfangerNode.summeKosten = node.summeKosten + kante.kosten
                empfangerNode.sendeRichtungsName = node.name
                empfangerNode.sendeRichtungsIndex = node.index
            elif empfangerNode.vermuteteRootID == node.vermuteteRootID:
                if node.summeKosten + kante.kosten < empfangerNode.summeKosten:
                    empfangerNode.summeKosten = node.summeKosten + kante.kosten
                    empfangerNode.sendeRichtungsName = node.name
                    empfangerNode.sendeRichtungsIndex = node.index

        counter += 1

    #for node in nodes:
    #    print(node)
    #    print("summekosten", node.summeKosten)
    #    print("vermuteteRootID", node.vermuteteRootID)

    # Endausgabe
    for node in nodes:
        print(node.name, " - ", node.sendeRichtungsName, "(Index ", node.sendeRichtungsIndex, ")")


if __name__ == "__main__":
    main()