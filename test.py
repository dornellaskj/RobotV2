import megaio
import time
import power

def test(pin):
    
    power.forward()
    megaio.set_relays(0,pin)
    time.sleep(.4)
    power.backward()
    time.sleep(.2)
    power.off()
    megaio.set_relays(0,0)
   