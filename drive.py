import megaio
import power

def rightForward():
    megaio.set_relays(0,3)

def rightBackward():
    megaio.set_relays(0,48)