import subprocess
import time
import os

os.environ["LIBNFC_INTRUSIVE_SCAN"] = "true"

def nfc_raw():
    lines=subprocess.check_output("/usr/bin/nfc-poll", stderr=open('/dev/null','w'))
    return lines

def read_nfc():
    lines=nfc_raw()
    return lines

try:
    while True:
        myLines=read_nfc()
        buffer=[]
        for line in myLines.splitlines():
            line_content=line.split()
            if(not line_content[0] =='UID'):
                pass
            else:
                buffer.append(line_content)

        str=buffer[0]
        id_str=[]
        
        for i in range(2,len(str)):
            id_str.append(str[i])
            
        uid="".join(id_str)
        print ("UID adalah : {}").format(uid)
        #print (buffer)


except KeyboardInterrupt:
        pass
