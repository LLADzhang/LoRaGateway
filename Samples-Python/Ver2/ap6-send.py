# www.ifroglab.com
# -*- coding: utf8 -*-
# coding=UTF-8
# * iFrogLab IL-LORA1272  www.ifroglab.com
# *
# * 功能,             USB to TTL , IFROGLAB LORA
# * 電源VDD,          3.3V       ,Pin 3
# * 接地GND,          GND        ,Pin 1
# * 接收反應Host_IRQ,  null       , Pin 2
# * UART,             RX         ,UART_RX  Pin 7
# * UART,             TX         ,UART_TX  Pin 8



import serial

def Fun_CRC(data):
    crc=0
    for i in data:
        crc=crc^i
    return crc

def Fun_OS():
    OSVersion=platform.system()
    port_path="/dev/cu.usbserial"
    print OSVersion
    if OSVersion=="Darwin":              #MAC Port
        port_path="/dev/cu.usbserial"
    elif OSVersion=="Linux":            #Linux Port
        port_path="/dev/ttyUSB0"
    return port_path




#ser = serial.Serial ("/dev/ttyAMA0")    # Raspbeeey Pi port
#ser = serial.Serial ("/dev/cu.usbserial")    #MAC port
portPath=Fun_OS()
ser = serial.Serial (portPath)    #MAC port
ser.baudrate = 115200                     #Set baud rate to 9600

#讀取F/W版本及Chip ID
array1=[0x80,0x00,0x00,0]
array1[3]=Fun_CRC(array1)
print array1
ser.write(serial.to_bytes(array1))
data = ser.read(10)
print data.encode('hex')



# 重置 & 初始化
array2=[0xc1,0x01,0x00,0]
array2[3]=Fun_CRC(array2)
print array2
ser.write(serial.to_bytes(array2))
data = ser.read(5)
print data.encode('hex')



# 讀取設定狀態
array3=[0xc1,0x02,0x00,0]
array3[3]=Fun_CRC(array3)
print array3
ser.write(serial.to_bytes(array3))
data = ser.read(12)
print data.encode('hex')


#設定模式與頻率
#array4=[0xC1,0x3,0x5,0x3,0x1,0x65,0x6C,0x3,0]
array4=[0xC1,3,5,2,1,0x65,0x6C,0x3,0]
array4[8]=Fun_CRC(array4)
print array4
ser.write(serial.to_bytes(array4))
data = ser.read(5)
print data.encode('hex')

#寫入資料
array5=[0xC1,0x5,0x5,0x61,0x62,0x63,0x64,0x65,0]
array5[8]=Fun_CRC(array5)
print array5
ser.write(serial.to_bytes(array5))
data = ser.read(5)
print data.encode('hex')

