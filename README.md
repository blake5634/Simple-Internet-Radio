# Simple Internet Radio

A minimal internet radio with analog input controls for volume and tuning.  The use case is conversion 
of an old analog radio to internet.   The tuning dial's range is mapped into N zones, each zone selects 
a hard-coded radio station.  `vlc` is used in audio only mode to stream the station content.

# Reference Hardware

This code works on the following hardware configuration:

  *  Raspberry Pi Zero
  *  AD1115 Analog input chip (two channels for reading the potentiometers)
  *  Adafruit  [Audio bonnet](https://www.adafruit.com/product/4037?gclid=CjwKCAiAuqHwBRAQEiwAD-zr3aGi_nHOGs2Ol6eyVBbdYg7v8lCJhvojwowAsHldXNX0K86h9EPlBxoCx0QQAvD_BwE)

![Schematic Diagram showing reference hardware.](https://github.com/blake5634/Simple-Internet-Radio/blob/master/Graphics/SchematicSimpleIntRadio.png)

# Dependencies

`Python3, vlc, [SMB library](https://pypi.org/project/smbus-cffi/0.5.1/)`