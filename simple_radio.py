
#
#   Digital I/O setup (do not break i2S audio)
#          (i2S uses 18,19,21)
import vlc
import time as t

import AD1115_readSMB as ad 


urls = {}
urls['kcrw']='http://kcrw.streamguys1.com/kcrw_192k_mp3_on_air_internet_radio'
urls['kexp']='http://live-aacplus-64.kexp.org/kexp64.aac' 
#KEXP_support_email.txt:http://live-mp3-128.kexp.org:8000/listen.pls
#KEXP_support_email.txt:http://live-mp3-32.kexp.org:8000/listen.pls
urls['wfmt']='http://stream.wfmt.com/main'
urls['kuow']='https://playerservices.streamtheworld.com/api/livestream-redirect/KUOWFM_AAC.aac'
urls['kiro'] = 'http://14093.live.streamtheworld.com:3690/KIROFM_SC'  # but commercial first!

stlist =  ['wfmt','kcrw','kexp','kuow','kiro']
#stlist =  ['wfmt','kcrw','kexp','kuow']

# init the I2C AD1115 chip
bus = ad.smbus_init(1)  # i2c bus #1

#define VLC instance
instance = vlc.Instance()
#Define VLC player
player=instance.media_player_new()

def get_tune(list):

    tune_levels = [23900, 18400, 12600, 6250]
    #tune_levels = [23900, 18400, 12600]   # drop lowest station
    tune_control = get_pot_val(ad.ADC1)
    #print('tune level: ', tune_control)
    for i in range(len(tune_levels)):
        if tune_control < tune_levels[i]:
            next
        else:
            #print('get_tune: level: {} sta:{}'.format(tune_control,list[i]))
            return list[i]        
    #print('returning default: {}'.format(list[i+1]))
    return list[i+1] 

def get_vol():
    pval = get_pot_val(ad.ADC0)
    vol =  29 + int(69 * pval/float(30000)) 
    if vol > 100:
        vol = 100
    if vol < 0:
        vol = 0
    #print('get_vol: level: {} vol:{}'.format(pval,vol))
    return vol

def get_pot_val(chan, n=3):
    #################3
    #
    #
    rv = 0
    for i in range(n):
        rv += ad.get_Ain(bus, chan)
        t.sleep(0.010)  # 10 ms
    return  int(rv/n)


pst = 'wfmt'
vol = 75
pvol = vol
# set volume according to knob
player.audio_set_volume(get_vol())
stations = {}
# open all stations
for s in stlist:
    stations[s] = instance.media_new(urls[s])
# tune initial station as tuned by dial
player.set_media(stations[get_tune(stlist)])
# ready to rock and roll!!
#Play the media
player.play()
while (1):
    st = get_tune(stlist)
    #st = 'kcrw'
    if st != pst:
        #print ('Playing '+st)
        #Define VLC media
        player.set_media(stations[st])
        #Play the media
        player.play()
        pst = st      # store current station
    vol =  get_vol()
    if vol != pvol:
       player.audio_set_volume(vol)
       pvol = vol
    t.sleep(1)

player.stop()            
player.audio_set_volume(100)
quit()
