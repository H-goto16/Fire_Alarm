import machine
import urequests
import utime

pin36 = machine.Pin(34, machine.Pin.IN)
pin32 = machine.Pin(32, machine.Pin.IN)

TOKEN = '***' 
URL = 'https://notify-api.line.me/api/notify'
headers = {'Content-Type':'application/x-www-form-urlencoded','Authorization': 'Bearer ' + TOKEN}

def submit(message):
    msg='message=' + message
    msgutf = msg.encode('utf-8')
    r = urequests.post(URL , headers=headers, data=msgutf)
    print(r.content)

def detectSensorAnalog():
    gasAL = machine.ADC(pin36)
    gasAL.atten(machine.ADC.ATTN_11DB)
    gas_val = gasAL.read()
    return gas_val
    
def detectSensorDigital():
    return pin32.value()

try:
    submit("\n起動しました。")
    while True:
        if(detectSensorDigital() == 0):
            submit("\n煙を検知しました。\n濃度は"+ str(detectSensorAnalog()) + "です。")
            utime.sleep(2)
except Exception as e:
    submit("\n \n====== \nERROR! \n====== \n \n" + str(e) +" \n ")
    
submit("\n終了します。")
