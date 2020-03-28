import AD1115_readSMB as ad 
import time as t


bus = ad.smbus_init(1)  # i2c bus #1

def get_pot_val(chan):
    #################3
    #
    #
    rv = ad.get_Ain(bus, chan)
    return  rv

Nreads = 500 
nloop = int(Nreads/4)

print(' Starting time test NOW with {} reads'.format(Nreads))    
tstart = t.time()
# how much time does it take to read the ADC 1000 times?
for i in range(nloop):
    x = get_pot_val(ad.ADC1)
    x = get_pot_val(ad.ADC0)
    x = get_pot_val(ad.ADC1)
    x = get_pot_val(ad.ADC0)
    
tend = t.time()

readspersec = Nreads/(tend-tstart)

print('{:8.1f} ADC per sec'.format(readspersec))
