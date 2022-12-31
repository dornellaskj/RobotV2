import time
from pygame import mixer

def whoami():
    mixer.init()
    mixer.music.load("./gun_robot.mp3")
    mixer.music.play()
    # while mixer.music.get_busy():  # wait for music to finish playing
    #     time.sleep(1)

