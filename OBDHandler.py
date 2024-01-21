import obd
import time

class OBDHandler():
    def __init__(self):
        self.connection = obd.OBD("COM4") # auto-connects to USB or RF port
        self.speed = 0
        self.rpm = 0
        self.accel_pos = 0
    
    def get_speed(self):
        cmd = obd.commands.SPEED # select an OBD command (sensor)
        response = self.connection.query(cmd) # send the command, and parse the response
        return response.value.to("mph").magnitude # user-friendly unit conversions

    def get_rpm(self):
        cmd = obd.commands.RPM # select an OBD command (sensor)
        response = self.connection.query(cmd) # send the command, and parse the response
        return response.value.magnitude  # user-friendly unit conversions
    
    def get_accel_pos(self):
        cmd = obd.commands.ACCELERATOR_POS_D # select an OBD command (sensor)
        response = self.connection.query(cmd) # send the command, and parse the response
        response_percent = (response.value.magnitude-31.5)*2.127
        if response_percent<0:
            return 0
        return response_percent# user-friendly unit conversions
    
    def refresh(self):
        self.rpm = self.get_rpm()
        self.speed = self.get_speed()
        self.accel_pos = self.get_accel_pos()

    def get_pad_volume(self):
        rpm_percent = self.rpm/7000
        if rpm_percent<0.08:
            return 0
        return (rpm_percent-0.08)*2
    
    def get_bass_volume(self):
        bass_percent = self.accel_pos/100
        return bass_percent

    def get_synth_volume(self):
        synth_percent = self.speed/70
        if synth_percent < 0.17:
            return 0
        return float(((synth_percent-0.17)**0.7).real)
    
    def get_drums_volume(self):
        drums_percent = self.speed/70
        drums_percent = -5.76+(41.6*drums_percent)-(64*drums_percent)**2
        if drums_percent < 0:
            return 0
        return float(((drums_percent-0.20)**0.2).real)

    def get_guitar_volume(self):
        guitar_percent = self.speed/70
        if guitar_percent < 0.3:
            return 0
        return float(((guitar_percent-0.40)**0.2).real)
    
    def get_drums_2_volume(self):
        drums_percent = self.speed/70
        if drums_percent < 0.4:
            return 0
        return float(((drums_percent-0.45)**0.2).real)
    
    def get_volumes(self):
        volumes = [
            self.get_bass_volume()*0.5,
            self.get_pad_volume(),
            self.get_synth_volume()*0.5,
            self.get_guitar_volume()*0.5,
            self.get_drums_volume(),
            self.get_drums_2_volume(),
        ]
        return volumes


