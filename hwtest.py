#!/usr/bin/python3
import board, time
from digitalio import DigitalInOut, Direction
OUTPUT = Direction.OUTPUT

pinout = \
{
    "E1": [None, board.D23, OUTPUT],
    "D1": [None, board.D24, OUTPUT],
    "C1": [None, board.D25, OUTPUT],
    ".1": [None, board.D16, OUTPUT],
    "E2": [None, board.D20, OUTPUT],
    "D2": [None, board.D21, OUTPUT],
    "G2": [None, board.D13, OUTPUT],
    "C2": [None, board.D19, OUTPUT],
    ".2": [None, board.D26, OUTPUT],
    "B2": [None, board.D6,  OUTPUT],
    "A2": [None, board.D5,  OUTPUT],
    "F2": [None, board.D12, OUTPUT],
    "B1": [None, board.D22, OUTPUT],
    "A1": [None, board.D27, OUTPUT],
    "G1": [None, board.D17, OUTPUT],
    "F1": [None, board.D4,  OUTPUT],
}

for pin in pinout:
    pinout[pin][0] = DigitalInOut(pinout[pin][1])
    pinout[pin][0].direction = pinout[pin][2]

for pin in pinout:
    pinout[pin][0].value = True
    time.sleep(0.1)

for pin in pinout:
    pinout[pin][0].value = False
    time.sleep(0.1)

pins = ["E1","F1","G1","A1","B1","C1","E2","F2","G2","A2","B2","C2"]

for pin in pins:
    pinout[pin][0].value = True

