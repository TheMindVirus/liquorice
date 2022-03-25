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

# Developer Commentary

```
"Which wire do I have to cut?" the blue one. "There is no blue wire!"

Shorting +5V to GND. Never do it. +5V or +3.3V is known as "High" and GND is known as "Ground",
which would make that situation the "High Ground", and it would be very much over Anakin.
If your board didn't have High Ground Protection it would be bricked with reverse current.
These are just some LED's though, so they can't be "bricked" in the traditional sense with reverse current.

"Hey, Overclockers, this is how you get your Q-Codes": https://github.com/TheMindVirus/liquorice
"POST codes are arbitrary at this point." - I think they're going to stay that way for a long time,
manufacturers aren't going to agree and consumers want control over it...
...well what do you want your POST Code to be, [AA]? [12]? [69]? [88]? [A1]? [B2]?
You just sunk my Battleship!

The USB DBUG Card thing hits a bit of a chicken and the egg situation.
BIOS is for early detection of USB devices but you can't show that
on your USB 7-Segment display because it hasn't been detected in the first place -_(\
It's the same with I2C, it would have to have some very platform specific and
very rudimentary I2C bit-banging until you had proper I2C
control from the Host OS of which hasn't started yet.

Raw GPIO is the way to go, it's considerably less complicated and Raw LED's can be swapped out.
GPIO on Pi is possible, but not as straightforward as it could be.
Instead of writing to 1 register you have to write to 3 per pin to set it up,
but that's the job of a DXE driver. That part has already been written,
as has UART in the same way, but still lots more setup involved than necessary.

What would be really neat is a display powered directly by UART
so you could send "A", "A" and it would update accordingly, or "\n" to clear it.
That would only use 4 pins for any number of digits.
I reckon the StemmaQT/Qwiic Quad-7-Segment Displays can be daisy-chained together,
so chain 4 of them and reserve a Hardware I2C from the Pi to power that...
...never tried it, don't have the kit in front of me.
```
