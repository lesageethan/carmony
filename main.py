import pygame
import os
import time
from AudioLoop import AudioLoop

def main():
    file_paths = os.listdir("wavs/")
    file_paths = ["wavs/"+file for file in file_paths]
    loop = AudioLoop(file_paths)
    loop.start()

    try:
        while True:
            # Get user input for volume adjustments
            volume_list = []
            for i in range(len(file_paths)):
                volume_input = float(input(f"Enter volume (0.0 to 1.0) for track {file_paths[i]}: "))
                volume_list.append(max(0.0, min(1.0, volume_input)))  # Ensure volume is in the valid range
            loop.adjust_volumes(volume_list)

    except KeyboardInterrupt:
        # Stop the sounds and quit on keyboard interrupt
        pygame.mixer.stop()
        pygame.quit()

if __name__ == "__main__":
    main()