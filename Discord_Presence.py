import psutil
from pypresence import Presence
import time

client_id = '#'  # Fake ID, put your real one here
RPC = Presence(client_id,pipe=0)  
RPC.connect() 


while True:  # The presence will stay on as long as the program is running
    cpu_per = round(psutil.cpu_percent(),1) 
    mem = psutil.virtual_memory()
    mem_per = round(psutil.virtual_memory().percent,1)
    print(RPC.update(details="Brain performance: "+str(mem_per)+"%", state="Insanity: "+str(cpu_per)+"%"+"\n + Sumpek"))  
    time.sleep(60) 
