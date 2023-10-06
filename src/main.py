from PiicoDev_RFID import PiicoDev_RFID
from PiicoDev_Unified import sleep_ms
from machine import Pin

RFID_ADDRESS = 0
SDA = Pin(8)
SCL = Pin(9)

rfid = PiicoDev_RFID(bus=RFID_ADDRESS, sda=SDA, scl=SCL)

try:
    while True:
        if rfid.tagPresent():
            id = rfid.readID()
            text = rfid.readText()
            # if text is None:
                # rfid.writeText("this has been written")
                # print(f"Wrote to tag ${id}")
            # else:
            print(text)
        sleep_ms(100)
except KeyboardInterrupt:
    print('exiting')