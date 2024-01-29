import pygame
import os
import time
from AudioLoop import AudioLoop
from OBDHandler import OBDHandler
import obd

def main():
    songname = input("Please enter the name of the folder containing the song you want to play:")
    path = "wavs/" + songname +"/"
    file_paths = os.listdir(path)
    file_paths = [path+file for file in file_paths if file.lower().endswith(".wav")]
    loop = AudioLoop(file_paths)
    loop.start()
    loop.adjust_volumes([0,0,0,0])
    handler = OBDHandler()

    try:
        while True:
            time.sleep(0.1)
            handler.refresh()
            volume_list = handler.get_volumes()
            # volume_list = []
            # for i in range(0, 4):
            #     volume_list.append(float(input("Enter volume for track {}:".format(i))))
            print(volume_list)
            loop.adjust_volumes(volume_list)

    except KeyboardInterrupt:
        # Stop the sounds and quit on keyboard interrupt
        pygame.mixer.stop()
        pygame.quit()

if __name__ == "__main__":
    main()
