from ppadb.client import Client
import time

def adb_connect():
    client = Client(host='127.0.0.1',port=5037)
    find_device = client.device()

    if len(find_device) == 0:
        print('No devices')
        quit()
    
    device = find_devices[0]
    print(f'찾은 디바이스{device}')
    
    return device, client

device, client = adb_connect()

devie.shell('input keyevent 64')
time.sleep(3.0)