# liquorice
```diff
- Strawberry Liquorice DBUG Card for displaying UEFI POST codes for Raspberry Pi Windows -
```
Currently in Prototype Phase and as yet untested, but the theory is that 7-Segment Displays \
can be connected directly to GPIO pins without an I2C Microcontroller for easier debugging \
from a baremetal setting such as [pftf-rpi4](https://github.com/pftf/rpi4) UEFI. POST codes are arbitrary at this point.

This may also be useful to Overclockers to get the absolute maximum performance possible \
out of the Raspberry Pi running AMI-BIOS and UEFI-ACPI compliant Operating Systems.

# Pinout
This pinout may vary between revisions of the board and different 7-Segment Displays.
| Board Pin | Physical Pin | GPIO Pin | Comment |
| --- | --- | --- | --- |
| 1 (E1) | 16 | GPIO23 | - |
| 2 (D1) | 18 | GPIO24 | - |
| 3 (C1) | 22 | GPIO25 | - |
| 4 (.1) | 36 | GPIO16 | - |
| 5 (E2) | 38 | GPIO20 | - |
| 6 (D2) | 40 | GPIO21 | - |
| 7 (G2) | 33 | GPIO13 | - |
| 8 (C2) | 35 | GPIO19 | - |
| 9 (.2) | 37 | GPIO26 | - |
| 10 (B2) | 31 | GPIO6 | Adjacent to Header |
| 11 (A2) | 29 | GPIO5 | Adjacent to Header |
| 12 (F2) | 32 | GPIO12 | - |
| 13 (\_2) | 25 | GND | Common Ground, Adjacent to Header |
| 14 (\_1) | 25 | GND | Common Ground |
| 15 (B1) | 15 | GPIO22 | Adjacent to Header |
| 16 (A1) | 13 | GPIO27 | - |
| 17 (G1) | 11 | GPIO17 | - |
| 18 (F1) | 7 | GPIO4 | 1-Wire Interface |
| UART (\_) | 6 | GND | Common Ground |
| UART (TX) | 8 | GPIO14 | Serial Transmission from Pi |
| UART (RX) | 10 | GPIO15 | Serial Reception into Pi |
| FAN (\_) | 1 | GND | Common Ground, Adjacent to Header |
| FAN (+V) | 2 | +5V | Do Not Short to GND |

The Dual 7-Segment Display in use here is the LB-602VK2 337Y from ROHM Semiconductor \
Also compatible with LBP-602A-K2: https://www.mouser.co.uk/datasheet/2/348/lbp-602ak2-e-1874551.pdf

![Pinout](https://github.com/themindvirus/liquorice/blob/main/pinout.png)

# Prototyping

This is what a hand-built prototype will end up looking like on veroboard. It must have at least one Dual-7-Segment \
display for 8-bit POST Codes and anywhere up to 4 Quad-7-Segment displays for 64-bit POST Codes.

![IMG_5350](https://github.com/themindvirus/liquorice/blob/main/IMG_5350.jpg)

The idea came straight after having successfully obtained a list of Q-Codes from ASUS Q-Code Logger \
and displaying it on an Adafruit Macropad RP2040. I designed a quick pencil schematic (upside-down in-reverse).

![IMG_5342](https://github.com/themindvirus/liquorice/blob/main/IMG_5342.jpg)

Once I had decided which arrangement of GPIO pins was easiest to wire by hand, I set about safely \
cutting traces on some veroboard, cut and filed to size. Then I commenced hand-soldering lots of tiny red wires.

![IMG_5344](https://github.com/themindvirus/liquorice/blob/main/IMG_5344.jpg)

Prototyping this way is not the best way to do it and neither is connecting ground with lines of solder. \
A PCB would be better. I also couldn't help noticing the wiring looked a bit like a Menorah, Happy Hanukkah!

![IMG_5345](https://github.com/themindvirus/liquorice/blob/main/IMG_5345.jpg)

You may also have noticed that I decided to break out the UART and +5V rails at the last minute, \
by looking at the schematic. When debugging UEFI I often used the UART and a small cooling fan.

![IMG_5347](https://github.com/themindvirus/liquorice/blob/main/IMG_5347.jpg)

Finally, all the wiring was finished! That was a tricky job and it passed a quick electrical safety test \
with no shorts as detected by a beeping Multimeter. It's not ideal to run it on a metal surface though.

![IMG_5349](https://github.com/themindvirus/liquorice/blob/main/IMG_5349.jpg)

I connected up a spare black 40-pin GPIO ribbon cable and the combination of stringy red wiring and \
black lace flex started to remind me of a classic candy sweet called Liquorice, along with everything else.

![IMG_5351](https://github.com/themindvirus/liquorice/blob/main/IMG_5351.jpg)

The prototype has been built but currently the support for this pinout of POST Code Display is \
awaiting a UEFI PEI/DXE/BDS Driver and EFI calls to `PostCode(0xAA);` for it to be a useful device.
