from re import T
import serial.tools.list_ports

ports = serial.tools.list_ports.comports();
newSerial = serial.Serial();
listOfPorts = []

for port in ports:
    listOfPorts.append(str(port))
    print(str(port))

print("Select USB Serial Device")
val = input("COM")

for com in range(0,len(listOfPorts)):
    if listOfPorts[com].startwith("COM"+str(val)):
        portValue = "COM"+str(val)

serialInst.baudrate = 9600
serialInst.port = portValue
serialInst.open()

while True:
    if serialInst.in_waitting:
        packet = serialInst.realTime()

