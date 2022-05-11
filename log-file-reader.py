# Entwickeln Sie ein Python-Programm, welches (automatisiert) Logs aus den Systemen Windows
# und Linux ausliest und in eine neue Datei auf Ihrem USB-Stick kopiert.
# Die kopierten Log-Daten sollen nach Wunsch des Anwenders gefiltert und entsprechend
# aufbereitet werden (bspw. in Excel). Hierbei soll es dem Nutzer auch möglich sein,
# ausschließlich einen bestimmten Zeitraum zu betrachten oder bestimmte Events
# anzeigen zu lassen.

import os
import shutil
import pandas as pd

def trenner(anzahl):
    for i in range(anzahl):
        print("*", end="")
    print()

# Liste zum Speichern der einzelnen Zeilen des Logs
log_lines = []
date_data = []
time = []
event = []

trenner(50)
print("Willkommen beim Log File Reader")
trenner(50)

logfile = open("/var/log/wifi.log", "r")

# Zeilenweises Durchgehen der Datei und speichern in Liste
for zeile in logfile:
    log_lines.append(zeile)
    
# Parsen der Liste
for i in log_lines:
    date_data.append(i[0:7])
    time.append(i[7:15])

logs = pd.DataFrame({
    'Datum': date_data,
    'Uhrzeit': time
})
print(logs)