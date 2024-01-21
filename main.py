import pygame
import os
import time
from AudioLoop import AudioLoop
from OBDHandler import OBDHandler
import obd

def main():
    file_paths = os.listdir("wavs/")
    file_paths = ["wavs/"+file for file in file_paths]
    loop = AudioLoop(file_paths)
    loop.start()
    loop.adjust_volumes([0,0,0,0,0,0])
    handler = OBDHandler()

    try:
        while True:
            time.sleep(0.05)
            handler.refresh()
            volume_list = handler.get_volumes()
            print(volume_list)
            loop.adjust_volumes(volume_list)

    except KeyboardInterrupt:
        # Stop the sounds and quit on keyboard interrupt
        pygame.mixer.stop()
        pygame.quit()

if __name__ == "__main__":
    main()
