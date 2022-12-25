import talk
import time
import power

def startup():
    talk.whoami()
    power.forward()
    time.sleep(2)
    power.backward()
    time.sleep(2)
    power.off()
