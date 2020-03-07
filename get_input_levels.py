import AD1115_readSMB as ad 
import time as t


bus = ad.smbus_init(1)  # i2c bus #1

def get_pot_val(chan):
    #################3
    #
    #
    rv = ad.get_Ain(bus, chan)
    return  rv

while True:
    tuneval = get_pot_val(ad.ADC1)

    volval = get_pot_val(ad.ADC0)

    print('vol: {} tune: {}'.format(volval,tuneval))

    t.sleep(0.500)
