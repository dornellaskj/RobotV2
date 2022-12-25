import megaio

def forward() {
    #turn on first 2 switches for forward power
    megaio.set_relays(0,3)
}

def backward() {
    #turn on second two switches for backward power
    megaio.set_relays(0, 12)
}

def off() {
    megaio.set_relays(0, 0)
}