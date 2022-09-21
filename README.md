# Simple Internet Radio

A minimal internet radio with analog input controls for volume and tuning.  The use case is conversion 
of an old analog radio to internet.   The tuning dial's range is mapped into N zones, each zone selects 
a hard-coded radio station.  `vlc` is used in audio only mode to stream the station content.

# Reference Hardware: a [Tivoli Audio Model One](https://www.radiomuseum.org/r/tivoli_pal_henry_kloss.html) Conversion  
[Photo Gallery](https://github.com/blake5634/Simple-Internet-Radio/blob/master/PhotoGallery.md)

This code works on the following hardware configuration:

  *  Raspberry Pi Zero
  *  AD1115 Analog input chip (two channels for reading the potentiometers)
  *  Adafruit  [Audio bonnet](https://www.adafruit.com/product/4037?gclid=CjwKCAiAuqHwBRAQEiwAD-zr3aGi_nHOGs2Ol6eyVBbdYg7v8lCJhvojwowAsHldXNX0K86h9EPlBxoCx0QQAvD_BwE)
  * Custom 3D printed mount plate to adapt potentiometer to original tuning knob. (see 
  `POT\ Mount\ for\ Tivoli\ Model\ One.stl`)


Wiring Diagram
![Schematic Diagram showing reference hardware.](https://github.com/blake5634/Simple-Internet-Radio/blob/master/Graphics/SchematicSimpleIntRadio.png)

# Pi Audio Basics
   * A simple test: `cvlc --no-video http://kcrw.streamguys1.com/kcrw_192k_mp3_on_air`

Above should play a stream from KCRW if vlc is installed and configured right. 

# Runtime Notes
 * When you power up, it takes a minute or two for the rPi to boot.  This is a *feature* - it gives a nice old-time vacuume tube feel to the experience.
 * Not as nice is the lag in response to volume change.   That is an explicit tradeoff of how frequently you want the rPi to be wasting cycles 
 checking the analog inputs for changes. 

# Dependencies for this software
`Python3`, [vlc](https://www.videolan.org/vlc/), 
[SMB library](https://pypi.org/project/smbus-cffi/0.5.1/)
[Python-vlc package](https://stackoverflow.com/questions/46758360/how-to-play-streaming-audio-from-internet-radio-on-python-3-5-3)
