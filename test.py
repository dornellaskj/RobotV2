import megaio
import time
import power

def test(pin):
    
    power.forward()
    megaio.set_relays(0,pin)
    time.sleep(.2)
    power.backward()
    time.sleep(.2)
    power.off()
    megaio.set_relays(0,0)

def down(pin):
    megaio.set_relays(0,pin)
    power.backward()
    time.sleep(.2)
    power.off()
    megaio.set_relays(0,0)

def up(pin):
    megaio.set_relays(0,pin)
    power.forward()
    time.sleep(.2)
    power.off()
    megaio.set_relays(0,0)
   