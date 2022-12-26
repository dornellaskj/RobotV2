import megaio

def forward():
    off()
    #turn on first 2 switches for forward power
    megaio.set_relays(0,3)


def backward():
    off()
    #turn on second two switches for backward power
    megaio.set_relays(0, 48)


def off():
    megaio.set_relays(0, 0)
