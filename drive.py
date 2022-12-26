import megaio
import power

def rightForward():
    megaio.set_relays(1,3)

def rightBackward():
    megaio.set_relays(1,48)