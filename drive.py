import megaio
import power

def rightForward():
    megaio.set_relays(0,12)

def rightBackward():
    megaio.set_relays(0,192)