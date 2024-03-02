import obd
import time

class OBDHandler():
    def __init__(self):
        self.connection = obd.OBD("COM4") # auto-connects to USB or RF port
        self.speed = 0
        self.rpm = 0
    
    def get_speed(self):
        cmd = obd.commands.SPEED # select an OBD command (sensor)
        response = self.connection.query(cmd) # send the command, and parse the response
        return response.value.to("mph").magnitude # user-friendly unit conversions

    def get_rpm(self):
        cmd = obd.commands.RPM # select an OBD command (sensor)
        response = self.connection.query(cmd) # send the command, and parse the response
        return response.value.magnitude  # user-friendly unit conversions
    
    def refresh(self):
        self.rpm = self.get_rpm()
        self.speed = self.get_speed()
    
    def get_bass_volume(self):
        bass_percent = self.rpm/7000
        bass_volume = min(bass_percent+0.5, 1)
        return bass_volume
    
    def get_drums_volume(self):
        drums_percent = self.speed/70
        drums_volume = max(min(drums_percent*7 - 1, 1), 0)
        return drums_volume

    def get_other_volume(self):
        other_percent = self.speed/70
        other_volume = max(min(other_percent*7 - 2.5, 1), 0)
        return other_volume
    
    def get_vocals_volume(self):
        vocals_percent = self.speed/70
        vocals_volume = max(min(vocals_percent*7 - 4, 1), 0)
        return vocals_volume
    
    def get_volumes(self):
        volumes = [
            self.get_bass_volume(),
            self.get_drums_volume(),
            self.get_other_volume(),
            self.get_vocals_volume()
        ]
        return volumes


