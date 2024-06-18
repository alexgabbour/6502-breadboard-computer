#!/bin/python3

rom = bytearray([0xea] * 32768)

with open('eeprom_code.bin', 'wb') as file:
    file.write(rom)
    