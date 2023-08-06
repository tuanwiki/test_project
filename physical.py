print("xin chao")
import time
import serial.tools.list_ports
try:
    ser = serial.Serial(port="COM3", baudrate=9600)
    print("mo cong COM thanh cong")
except:
    print("Can not open the port")

relay1_ON=[0,6,0,0,0,255,200,91]
relay1_OFF=[0,6,0,0,0,0,136,27]
relay2_ON=[15,6,0,0,0,255,200,164]
relay2_OFF=[15,6,0,0,0,0,136,228]
def setDevice1(state):
    if state==True:
        ser.write(relay1_ON)
    else:
        ser.write(relay1_OFF)
def setDevice2(state):
    if state==True:
        ser.write(relay2_ON)
    else:
        ser.write(relay2_OFF)
def serial_read_data(ser):
    bytesToRead = ser.inWaiting()
    if bytesToRead > 0:
        out = ser.read(bytesToRead)
        data_array = [b for b in out]
        print(data_array)
        if len(data_array) >= 7:
            array_size = len(data_array)
            value = data_array[array_size - 4] * 256 + data_array[array_size - 3]
            return value
        else:
            return -1
    return 0
soil_temperature =[1, 3, 0, 6, 0, 1, 100, 11]
def readTemperature():
    serial_read_data(ser)
    ser.write(soil_temperature)
    time.sleep(1)
    return serial_read_data(ser)

soil_moisture = [1, 3, 0, 7, 0, 1, 53, 203]
def readMoisture():
    serial_read_data(ser)
    ser.write(soil_moisture)
    time.sleep(1)
    return serial_read_data(ser)

# while True:
#     print("TEST RELAY1")
#     setDevice1(True)
#     time.sleep(2)
#     setDevice1(False)
#     time.sleep(2)
#     print("TEST RELAY2")
#     setDevice2(True)
#     time.sleep(2)
#     setDevice2(False)
#     time.sleep(2)
#     print("TEST SENSOR")
#     print(readMoisture())
#     time.sleep(1)
#     print(readTemperature())
#     time.sleep(1)
