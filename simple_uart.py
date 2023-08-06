print("Sensors and Actuators")

import time
import serial.tools.list_ports
try:
    ser = serial.Serial(port="COM4", baudrate=9600)
    print("mo cong COM thanh cong")
except:
    print("Can not open the port")
def sendcommand(cmd):
    ser.write(cmd.encode())
    #todo
mess=""
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
def processData(data,client):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    if splitData[1] == "T":
        client.publish("sensor1", splitData[2])
    elif splitData[1] == "H":
        client.publish("sensor2", splitData[2])

# while True:
#     readSerial()
#     time.sleep(1)

# while True:
#     sendcommand("0")
#     time.sleep(5)
#     sendcommand("1")
#     time.sleep(5)
#     sendcommand("2")
#     time.sleep(5)
#     sendcommand("3")
#     time.sleep(5)