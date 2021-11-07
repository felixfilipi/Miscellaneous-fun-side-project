#!/usr/bin/env python
# coding: utf-8

# In[4]:


import psutil
from pypresence import Presence
import time

client_id = '#'  # Fake ID, put your real one here
RPC = Presence(client_id,pipe=0)  # Initialize the client class
RPC.connect() # Start the handshake loop


while True:  # The presence will stay on as long as the program is running
    cpu_per = round(psutil.cpu_percent(),1) # Get CPU Usage
    mem = psutil.virtual_memory()
    mem_per = round(psutil.virtual_memory().percent,1)# Set the presence
    print(RPC.update(details="Brain performance: "+str(mem_per)+"%", state="Insanity: "+str(cpu_per)+"%"+"\n + Sumpek"))  # Set the presence
    time.sleep(60) # Can only update rich presence every 15 seconds

