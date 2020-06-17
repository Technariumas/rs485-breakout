# rs485 valve controller

Pins MISO and SCL on the 10 pin header are programmed as general purpose IO. Two least significant bits written to register 5 allows to control the state of these pins:

```
import minimalmodbus as mm

instrument = mm.Instrument(SERIAL_PORT, ADDRESS)

print("Setting 00")
instrument.write_register(5, 0b00000000, functioncode=6);
sleep(0.1)

print("Setting 01")
instrument.write_register(5, 0b00000001, functioncode=6);
sleep(0.1)

print("Setting 10")
instrument.write_register(5, 0b00000010, functioncode=6);
sleep(0.1)

print("Setting 11")
instrument.write_register(5, 0b00000011, functioncode=6);

```

