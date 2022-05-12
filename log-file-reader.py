# Entwickeln Sie ein Python-Programm, welches (automatisiert) Logs aus den Systemen Windows
# und Linux ausliest und in eine neue Datei auf Ihrem USB-Stick kopiert.
# Die kopierten Log-Daten sollen nach Wunsch des Anwenders gefiltert und entsprechend
# aufbereitet werden (bspw. in Excel). Hierbei soll es dem Nutzer auch möglich sein,
# ausschließlich einen bestimmten Zeitraum zu betrachten oder bestimmte Events
# anzeigen zu lassen.

import pandas as pd
import platform

def trenner(anzahl):
    for i in range(anzahl):
        print("*", end="")
    print()
    
def setOS():
    if platform.system() == 'Darwin':
        return "/var/logs"
    elif platform.sytem == 'Linux':
        return "/var/logs"
        


# Liste zum Speichern der einzelnen Zeilen des Logs
log_lines = []
date_data = []
time = []
event = []

logfile = open("/var/log/wifi.log", "r")

# Iterate through log
for zeile in logfile:
    log_lines.append(zeile)

# First line is, why so ever, trash    
# log_lines.pop(0)

# Parsing of the list
for i in log_lines:
    date_data.append(i[0:10])
    time.append(i[10:19])
    
logs = pd.DataFrame({
    "Datum": date_data,
    "Uhrzeit": time
})


print(getOS())
