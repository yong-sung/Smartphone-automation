from ppadb.client import Client
import time

# ADB 클라이언트와 연결, 디바이스를 찾는 역할
def adb_connect():
    client = Client(host="127.0.0.1", port=5037) 
    find_devices = client.devices()

    if len(find_devices) == 0:
        print('No devices')
        quit()

    device = find_devices[0]
    print(f'찾은 디바이스: {device}')

    return device, client

device, client = adb_connect()

device.shell('input keyevent 64') # 뒤로 가기 키
time.sleep(2.0) # 2초 동안 대기

xyPosition = "263 163"
device.shell(f'input tap {xyPosition}') # 디바이스 화면에서 특정 좌표를 탭
time.sleep(2.0)

url = "www.naver.com"
device.shell(f'input text {url}')
time.sleep(2.0)

device.shell('input keyevent 66') # 엔터 키
time.sleep(8.0)

result = device.screencap() # 디바이스 화면을 스크린샷으로 가져옴
with open(r"18. 스마트폰 자동화\screen.png", "wb") as fp:
    fp.write(result) # 'screen.png' 파일로 스크린샷 저장