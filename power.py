import megaio

def forward():
    off()
    #turn on first 2 switches for forward power
    megaio.set_relays(1,192)


def backward():
    off()
    #turn on second two switches for backward power
    megaio.set_relays(1, 12)


def off():
    megaio.set_relays(1, 0)
