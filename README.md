```
   ____                                       
  / ___|__ _ _ __ _ __ ___   ___  _ __  _   _ 
 | |   / _` | '__| '_ ` _ \ / _ \| '_ \| | | |
 | |__| (_| | |  | | | | | | (_) | | | | |_| |
  \____\__,_|_|  |_| |_| |_|\___/|_| |_|\__, |
                                        |___/
```

# Carmony
A work-in-progress open source version of Mercedes' MBUX Sound Drive

## Demo
[See a demo of the script in action here](https://www.youtube.com/watch?v=vxGZE5MImc0)

[See the original Mercedes Sound Drive demonstration here](https://www.youtube.com/shorts/NfBV0JRV3dU)

## Credits
Music Files/Loops: [ModeAudio on YouTube](https://www.youtube.com/watch?v=8b_Mv0cUEsc)

Music Control: [PyGame](https://github.com/pygame/pygame)

OBD Reading: [Python-OBD](https://python-obd.readthedocs.io/en/latest/)

## Requirements

- [An ELM327 OBD Reader like this](https://www.amazon.co.uk/dp/B07MQ8GHG3?psc=1&ref=ppx_yo2ov_dt_b_product_details) (Not an affiliate link)
- [PyGame](https://github.com/pygame/pygame)
- [Python-OBD](https://python-obd.readthedocs.io/en/latest/)
- A car with an OBD2 port
- A laptop or Raspberry Pi

## How it Works
The aim for this repo is to enable a musical loop to be controlled using inputs from a car's OBD port, similarly to the effect of Mercedes' Sound Drive.

When the program is ran, any song, broken down into four stems, will play. The four stems are as follows: ```bass.wav```, ```drums.wav```, ```other.wav```, and ```vocals.wav```. These can be generated for any song for free using [Spleeter](https://github.com/deezer/spleeter).

As adjustments are made to the car's current state (RPM, Speed, and Throttle), the volumes of each of the five loops will change. They change in accordance with this graph:

<img src="github-images/volume-curves.png" style="width:500px">

This chart shows volume of instrument on the Y axis, and percentage activation of the measured heuristic (Speed or RPM) on the X axis. RPM is represented as a number from 0.0-1.0, corresponding to values from 0-7000rpm. Speed is also represented as a number from 0.0-1.0 representing speeds from 0-70mph.

Currently, the script works for any song split into four stems for any song. A more ambitious version would be to split and play different samples from the song at custom intervals depending on the state of the car.

## Set Up

If you want to set this up for yourself, you will need to download the files listed in this repo onto a laptop or Raspberry Pi. Then, you will need an [ELM327 OBD2 reader like this](https://www.amazon.co.uk/dp/B07MQ8GHG3?psc=1&ref=ppx_yo2ov_dt_b_product_details).  

Simply connect the USB OBD2 reader to your computer's COM4 USB port (This will need to be adjusted manually if using a different port, Linux, or a wireless OBD reader). Then run the script. If all goes well, it should start to work after a few seconds.