import subprocess
import time
import os
import datetime

scripts = [
    "suhkumi.py",
    "nightlight.py",
    "1okktubre.py",
    "2slimey.py",
    "christ_blunt.py",
    "corpsekyo.py",
    "elek.py",
    "giuliano.py",
    "helabrokeangel.py",
    "hellsing_glock_boyz.py",
    "kk.py",
    "knsevenkay.py",
    "moneynumb.py",
    "my_little_pony.py",
    "naxowo.py",
    "nekkropsy.py",
    "ocelot.py",
    "pistolero2k.py",
    "putrid.py",
    "sexadlibs.py",
    "slattuhs.py",
    "suban.py",
    "tnnn.py",
    "unixzo.py",
    "vampireosamagang666.py",
    "vritni.py",
    "war6aw.py",
    "xartinreligion.py",
    "xoly.py",
    "xtendo.py",
    "yoi.py",
    "young_piri.py",
    "zatru.py"
]

processes = {}

def start_script(script):
    return subprocess.Popen(["python3", script])

def wait_until_15_arg():
    while True:
        # Argentina = UTC-3
        now = datetime.datetime.utcnow() - datetime.timedelta(hours=3)
        print("Hora Argentina:", now.strftime("%H:%M"))
        
        if now.hour == 15 and now.minute == 0:
            print("Son las 15:00, iniciando todos...")
            return
        
        time.sleep(20)

# Esperar hasta las 15:00
wait_until_15_arg()

print("Matando procesos viejos...")
os.system("pkill -f python3")

print("Iniciando todos los scrobblers al mismo tiempo...")
for script in scripts:
    processes[script] = start_script(script)
    print("Iniciado:", script)

# Auto-restart
while True:
    for script, process in processes.items():
        if process.poll() is not None:
            print("Reiniciando:", script)
            processes[script] = start_script(script)
    time.sleep(20)
