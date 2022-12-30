import megaio
import power
import time

def rightForward(move_time):
    megaio.set_relays(1,3)
    time.sleep(move_time)
    megaio.set_relays(1,0)


def rightBackward(move_time):
    megaio.set_relays(1,48)
    time.sleep(move_time)
    megaio.set_relays(1,0)

def leftBackward(move_time):
    power.backward()
    megaio.set_relays(0,16)
    time.sleep(move_time)
    power.off()
    megaio.set_relays(0,0)

def leftForward(move_time):
    power.forward()
    megaio.set_relays(0,16)
    time.sleep(move_time)
    power.off()
    megaio.set_relays(0,0)

def driveForward(move_time):
    power.forward()
    megaio.set_relays(0,16)
    time.sleep(.02)
    megaio.set_relays(1,3)
    time.sleep(move_time)
    power.off()
    megaio.set_relays(1,0)
    megaio.set_relays(0,0)

def driveBackward(move_time):
    leftBackward(move_time)
    rightBackward(move_time)   