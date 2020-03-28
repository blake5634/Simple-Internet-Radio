import AD1115_readSMB as ad 
import time as t

TEST = 'ADC'
TEST = 'SCALING'
#TEST = 'BOTH'

bus = ad.smbus_init(1)  # i2c bus #1

def get_pot_val(chan):
    #################3
    #
    #
    rv = ad.get_Ain(bus, chan)
    return  rv


#  SCALING only
def get_vol():
  #  pval = get_pot_val(ad.ADC0)
    pval = 16500
    vol =  29 + int(69 * pval/float(30000)) 
    if vol > 100:
        vol = 100
    if vol < 0:
        vol = 0
    #print('get_vol: level: {} vol:{}'.format(pval,vol))
    return vol

def get_vol2():
    pval = get_pot_val(ad.ADC0)
  #  pval = 16500
    vol =  29 + int(69 * pval/float(30000)) 
    if vol > 100:
        vol = 100
    if vol < 0:
        vol = 0
    #print('get_vol: level: {} vol:{}'.format(pval,vol))
    return vol

Nreads = 40 
nloop = int(Nreads/4)

print(' Starting {} time test NOW with {} reads'.format(TEST,Nreads))    
tstart = t.time()
# how much time does it take to read the ADC 1000 times?
for i in range(nloop):
    if TEST== 'ADC':
        x = get_pot_val(ad.ADC1)
        x = get_pot_val(ad.ADC0)
        x = get_pot_val(ad.ADC1)
        x = get_pot_val(ad.ADC0)
    if TEST=='SCALING':
        x = get_vol()
        x = get_vol()
        x = get_vol()
        x = get_vol()
    if TEST=='BOTH':
        x = get_vol2()
        x = get_vol2()
        x = get_vol2()
        x = get_vol2()
    
tend = t.time()

readspersec = Nreads/(tend-tstart)

print('{:8.1f} {} per sec'.format(readspersec,TEST))
