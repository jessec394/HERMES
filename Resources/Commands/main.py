"""
Title: XBEE3 Valve/Vent Unit
Author: Kristoffer Allick
Created: 12/20/2022
Revised: 06/30/2023  by Rick Eason for Valve Open "timers"
Target Device: Vent board XBEE3 SMT
"""

# Imports
import xbee
import machine
from machine import Pin
# from machine import I2C
import time

#Pins
usr_led = Pin(machine.Pin.board.D4, Pin.OUT, value=0)   #Enable pin on XBEE3 set to low initially
asc_led = Pin(machine.Pin.board.D5, Pin.OUT, value=0)   #Enable pin on XBEE3 set to low initially
spkr_pin = Pin(machine.Pin.board.P0, Pin.OUT, value=0)  #Shush chatty monkey
msp_pin = Pin(machine.Pin.board.P7, Pin.OUT)   #Enable pin on XBEE3 set to low initially
heater_pin = Pin(machine.Pin.board.D18, Pin.OUT, value=1)
Hall_pin = Pin(machine.Pin.board.D3, Pin.IN, pull=None)

# # I2C setup
# i2c = I2C(1, freq=100000)
# addresses = i2c.scan()
# press_sense = addresses[1]
#
#
# print(addresses)
#
# print("Vent Control Initialize")
#
#
# def GetPressure():
#     i2c.readfrom(press_sense, nbytes=1, stop=True) #change nbytes later to actually do stuff (pg. 79 of digi micropython
#

def GetCommand():
    packet = None  # Set packet to none
    while packet is None:   # While no packet has come in
        packet = xbee.receive()     # Try to receive packet
    [xbee.receive() for i in range(100)]    # Clear the buffer
    return packet.get('payload').decode('utf-8')[:3]    # Return the last three charters decoded


class ProcessCommand:
    lastCommand = None
    valvetimer = 0

    @staticmethod
    def process_command(Command):
        print(Command)
        if Command == 'PQR':
            if Command != ProcessCommand.lastCommand:
                ProcessCommand.valvetimer += 83 # 5 minute
        elif Command == 'STU':
            if Command != ProcessCommand.lastCommand:
                ProcessCommand.valvetimer += 17 # 1 minute
        elif Command == 'VWX':
            if Command != ProcessCommand.lastCommand:
                ProcessCommand.valvetimer += 33 # 2 minute
        elif Command == 'JKL':
            ProcessCommand.valvetimer = 1
        elif Command == 'MNO':
            ProcessCommand.valvetimer = 0

        if ProcessCommand.valvetimer > 0:
            Valve_Open()
            ProcessCommand.valvetimer -= 1
        else:
            Valve_Close()

        # if Command not in ('ABC', 'DEF'):
        ProcessCommand.lastCommand = Command


ProcessCommand.lastCommand = None
ProcessCommand.valvetimer = 0


# idle
def idle():
    asc_led.value(0)
    msp_pin.value(0)

def Valve_Open():
    msp_pin.value(1)
    Blink(asc_led)

def Valve_Close():
    msp_pin.value(0)
    Blink(asc_led)

def Blink(pin):
    for i in range(5):
        pin.value(1)    #Pin High
        time.sleep_ms(50)   #Do nothing for 1 second
        pin.value(0)    #Pin Low
        time.sleep_ms(50)   #Do nothing for 1 second


#Main Loop
def main():


    while(1):
        time.sleep(3) #need to pause to sync clock, otherwise transmit will be messed up
        ProcessCommand.process_command(GetCommand())
        if Pin.value(Hall_pin)==1:
            Hall_effect="VCR"
            # Hall_effect = str(Pin.value(Hall_pin))  # converts pin value of Hall_pin to a String to use the transmit function later
        else:
            Hall_effect="VOA"
        try:
            xbee.transmit(xbee.ADDR_COORDINATOR, Hall_effect)

        except:
            pass
#-----------------------------------------------------------
main()