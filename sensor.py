import time
import serial.tools.list_ports

try:
    ser = serial.Serial(port = "COM12", baudrate = 9600)
    print("Open COM successfully")
except:
    print('Can not open the port')

relay1_ON = [0,6,0,0,0,255,200,91]
relay1_OFF = [0,6,0,0,0,0,136,27]

relay2_ON = [15,6,0,0,0,255,200,164]
relay2_OFF = [15,6,0,0,0,0,136,228]

def set_device1(state):
    if state == True:
        ser.write(relay1_ON)
    else:
        ser.write(relay1_OFF)
    # time.sleep(1)
    # return serial_read_data(ser)

def set_device2(state):
    if state == True:
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

while True:
    print("TEST RELAY")
    set_device1(True)
    time.sleep(10)
    set_device1(False)
    time.sleep(10)
    set_device2(True)
    time.sleep(10)
    set_device2(False)
    time.sleep(10)
    print("TEST SENSOR")
    print(readMoisture())
    time.sleep(1)
    print(readTemperature())
    time.sleep(1)
import time
import serial.tools.list_ports
# from main import client
try:
    ser = serial.Serial(port = "COM12", baudrate = 9600)
    print("Open COM successfully")
except:
    print('Can not open the port')

def send_command(cmd):
    ser.write(cmd.encode())
    #TODO

mess = ""
def processData(data, client):
    print(data)
    data = data.replace("!", "")
    print(data)
    data = data.replace("#", "")
    print(data)
    splitData = data.split(":")
    print(splitData)
    if splitData[1] == "T":
        client.publish("sensor1", splitData[2])
    elif splitData[1] == "H":
        client.publish("sensor2", splitData[2])


def readSerial(client):
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")

        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(mess[start:end + 1], client)
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end + 1:]

while True:
    send_command("0");
    time.sleep(3)
    send_command("1");
    time.sleep(3)
    send_command("2");
    time.sleep(3)
    send_command("3");
    time.sleep(3)
    readSerial()
    time.sleep(1)
def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB Serial Device" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    return commPort