import smbus
import time

#  for gain = +/1 2.048V
ADC0 = 0xC4
ADC1 = 0xD4
ADC2 = 0xE4
ADC3 = 0XF4


#  for gain = +/1 4.096V
ADC0 = 0xC2
ADC1 = 0xD2
ADC2 = 0xE2
ADC3 = 0XF2


def smbus_init(busnum):
    # Get I2C bus
    bus = smbus.SMBus(busnum)
    return bus


def get_Ain(bus,chan):
    # ADS1115 address, 0x48(72)
    # Select configuration register, 0x01(01)
    #		0xC483(50307)	AINP = AIN0 and AINN = GND, +/- 2.048V
    #				Continuous conversion mode, 128SPS
    data = [chan,0x83]
    bus.write_i2c_block_data(0x48, 0x01, data)
    #time.sleep(0.5)
    time.sleep(0.010)  # should work at 128SPS

    # ADS1115 address, 0x48(72)
    # Read data back from 0x00(00), 2 bytes
    # raw_adc MSB, raw_adc LSB
    data = bus.read_i2c_block_data(0x48, 0x00, 2)

    # Convert the data
    raw_adc = data[0] * 256 + data[1]

    if raw_adc > 32767:
        raw_adc -= 65535
    return raw_adc


def test_AD(bus,chan):
    for i in range(50):
        v = get_Ain(bus,chan)
        print('raw A/D value: {}'.format(v))
        
if __name__=='__main__':
    bus = smbus_init(1)
    
    test_AD(bus,ADC1)
    
