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
    megaio.set_relays(0,16)
    megaio.set_relays(1,195)    
    time.sleep(move_time)
    power.off()
    megaio.set_relays(0,0)

def driveBackward(move_time):
    megaio.set_relays(0,16) 
    megaio.set_relays(1,60)
    time.sleep(move_time)
    power.off()
    megaio.set_relays(0,0)

def turnRight(move_time):
    megaio.set_relays(0,16) 
    megaio.set_relays(1,15)
    time.sleep(move_time)
    power.off()
    megaio.set_relays(0,0)

def turnLeft(move_time):
    megaio.set_relays(0,16) 
    megaio.set_relays(1,240)
    time.sleep(move_time)
    power.off()
    megaio.set_relays(0,0)