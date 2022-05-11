# Danke Eddi
# python -m pip install pywin32
import win32evtlog

logtype= 'System'
server = 'localhost' # name of the target computer to get event logs
hand = win32evtlog.OpenEventLog(server,logtype)
flags = win32evtlog.EVENTLOG_SEQUENTIAL_READ|win32evtlog.EVENTLOG_BACKWARDS_READ

total = win32evtlog.GetNumberOfEventLogRecords(hand)
print(f"{total} Events gefunden.")
