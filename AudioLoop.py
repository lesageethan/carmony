import pygame
import os

class AudioLoop():
    def __init__(self, file_paths):
        pygame.init()
        pygame.mixer.set_num_channels(len(file_paths))
        self.sounds = [self.load_sound(file_path) for file_path in file_paths]
        
    def load_sound(self, file):
        sound = pygame.mixer.Sound(file)
        return sound
    
    def start(self):
        for sound in self.sounds:
            sound.play(loops=-1)
    
    def adjust_volumes(self, volume_list):
        for i in range(0, len(self.sounds)):
            pygame.mixer.Channel(i).set_volume(volume_list[i])