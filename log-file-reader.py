# Entwickeln Sie ein Python-Programm, welches (automatisiert) Logs aus den Systemen Windows
# und Linux ausliest und in eine neue Datei auf Ihrem USB-Stick kopiert.
# Die kopierten Log-Daten sollen nach Wunsch des Anwenders gefiltert und entsprechend
# aufbereitet werden (bspw. in Excel). Hierbei soll es dem Nutzer auch möglich sein,
# ausschließlich einen bestimmten Zeitraum zu betrachten oder bestimmte Events
# anzeigen zu lassen.

import os
import shutil

def trenner(anzahl):
    for i in range(anzahl):
        print("*", end="")
    print()

# Liste zum Speichern der einzelnen Zeilen des Logs
log_lines = []

trenner(50)
print("Willkommen beim Log File Reader")
trenner(50)
betriebssystem = input("Welches Betriebssystem nutzen Sie (mac/win): ")

if betriebssystem == "mac":
    # Einlesen der Datei
    logfile = open("/var/log/wifi.log", "r")
elif betriebssystem == "in":
    # Einlesen der Datei
    logfile = open("C:\Windows\System32\winevt\Logs\system.log", "r") # TODO: Pfad muss noch geprüft werden

# Zeilenweises Durchgehen der Datei und speichern in Liste
for zeile in logfile:
    log_lines.append(zeile)
    
# Ausgeben der Liste
print(log_lines)
