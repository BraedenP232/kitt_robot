"""
Braeden Pelletier December 2022 Smart KITT (Knight Rider)

This is for a Knight Rider themed gas pump build by-
Wil Power's Theme-it 'https://www.themeit.ca/'
Smart Assistant KITT (Knight Industry Two Thousand)
I am using Picovoice, Porcupine wake-word, and Rhino Speech-to-intent
Porcupine references hit-kit.ppn for wake word.
Rhino references kitt.rnh for inferences.
"""

import argparse
import os
import time
import struct
import mutagen
import pygame
import pygame._sdl2 as sdl2
import sys
from threading import Thread
from mutagen.mp3 import MP3

from gpiozero import LED
from picovoice import Picovoice
from pvrecorder import PvRecorder

from .phrases import KittPhrases
from .apa102 import APA102

COLORS_RGB = dict(
    blue=(0, 0, 255),
    green=(0, 255, 0),
    orange=(255, 128, 0),
    pink=(255, 51, 153),
    purple=(128, 0, 128),
    red=(255, 0, 0),
    white=(255, 255, 255),
    yellow=(255, 255, 51),
)

driver = APA102(num_led=12)
power = LED(5)
power.on()
phrases = KittPhrases

recorder = None

pygame.mixer.init(devicename = 'bcm2835 Headphones, bcm2835 Headphones')

class PicovoiceDemo(Thread):
    def __init__(
            self,
            keyword_path,
            context_path,
            access_key,
            device_index,
            porcupine_sensitivity=0.35,
            rhino_sensitivity=0.65,):
        super(PicovoiceDemo, self).__init__()

        def inference_callback(inference):
            return self._inference_callback(inference)

        self._picovoice = Picovoice(
            access_key=access_key,
            keyword_path=keyword_path,
            wake_word_callback=self._wake_word_callback,
            context_path=context_path,
            inference_callback= inference_callback,
            porcupine_sensitivity=porcupine_sensitivity,
            rhino_sensitivity=rhino_sensitivity)

        self._context = self._picovoice.context_info

        self._color = 'red'
        self._device_index = device_index

    @staticmethod
    def _set_color(color):
        for i in range(12):
            driver.set_pixel(i, color[0], color[1], color[2])
        driver.show()

    @staticmethod
    def _say_phrase(self, path):
        global recorder
        pygame.mixer.music.load(path)
        recorder.stop()
        # audio = MP3(path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.5)
        recorder.start()
        pygame.mixer.music.unload()

    @staticmethod
    def _wake_word_callback():
        print('[wake word]\n')

    def _start_up(self):
        self._say_phrase(self, phrases.StartUp2())
        time.sleep(1)
        self._say_phrase(self, phrases.StartUp())

    def _inference_callback(self, inference):
        print('{')
        print("  is_understood : '%s'," % ('true' if inference.is_understood else 'false'))
        if inference.is_understood:
            print("  intent : '%s'," % inference.intent)
            if len(inference.slots) > 0:
                print('  slots : {')
                for slot, value in inference.slots.items():
                    print("    '%s' : '%s'," % (slot, value))
                print('  }')
        else:
            self._set_color(COLORS_RGB[self._color])
            self._say_phrase(self, phrases.BadPhrase())
            self._set_color((0, 0, 0))
        print('}\n')

        if inference.is_understood:
            if inference.intent == 'turnLights':
                if inference.slots['state'] == 'off':
                    self._set_color((0, 0, 0))
                else:
                    self._set_color(COLORS_RGB[self._color])
            elif inference.intent == 'changeColor':
                self._color = inference.slots['color']
                self._set_color(COLORS_RGB[self._color])
            elif inference.intent == 'WhoYou':
                self._set_color(COLORS_RGB[self._color])
                self._say_phrase(self, phrases.WhoAreYou())
                self._set_color((0, 0, 0))
            # if inference.intent == 'WhoYou':
            #     self._set_color(COLORS_RGB[self._color])
            #     self._say_phrase(self, phrases.WhoAreYou())
            #     self._set_color((0, 0, 0))
            elif inference.intent == 'HowYou':
                self._set_color(COLORS_RGB[self._color])
                self._say_phrase(self, phrases.HowAreYou())
                self._set_color((0, 0, 0))
            elif inference.intent == 'Goodbye':
                self._set_color(COLORS_RGB[self._color])
                self._say_phrase(self, phrases.Goodbye())
                self._set_color((0, 0, 0))
            elif inference.intent == 'ThankYou':
                self._set_color(COLORS_RGB[self._color])
                self._say_phrase(self, phrases.ThankYou())
                self._set_color((0, 0, 0))
            elif inference.intent == 'Apology':
                self._set_color(COLORS_RGB[self._color])
                self._say_phrase(self, phrases.Apology())
                self._set_color((0, 0, 0))
            elif inference.intent == 'Greeting':
                self._set_color(COLORS_RGB[self._color])
                self._say_phrase(self, phrases.Greeting())
                self._set_color((0, 0, 0))
            elif inference.intent == 'Anger':
                self._set_color(COLORS_RGB[self._color])
                self._say_phrase(self, phrases.Anger())
                self._set_color((0, 0, 0))
            elif inference.intent == 'Understand':
                self._set_color(COLORS_RGB[self._color])
                self._say_phrase(self, phrases.DoYouUnderstand())
                self._set_color((0, 0, 0))
            elif inference.intent == 'Joke':
                self._set_color(COLORS_RGB[self._color])
                self._say_phrase(self, phrases.Joke())
                self._set_color((0, 0, 0))
            elif inference.intent == 'Reassure':
                self._set_color(COLORS_RGB[self._color])
                self._say_phrase(self, phrases.AreYouSure())
                self._set_color((0, 0, 0))
            elif inference.intent == 'Compliment':
                self._set_color(COLORS_RGB[self._color])
                self._say_phrase(self, phrases.Compliment())
                self._set_color((0, 0, 0))
            elif inference.intent == 'Insult':
                self._set_color(COLORS_RGB[self._color])
                self._say_phrase(self, phrases.Insult())
                self._set_color((0, 0, 0))
            elif inference.intent == 'BadPhrase':
                self._set_color(COLORS_RGB[self._color])
                self._say_phrase(self, phrases.BadPhrase())
                self._set_color((0, 0, 0))
            else:
                raise NotImplementedError()

    def run(self):
        global recorder

        try:
            print('Starting up in 5.....')
            time.sleep(5)
            recorder = PvRecorder(device_index=4, frame_length=self._picovoice.frame_length)
            recorder.start()

            print(self._context)
            print('These are the phrases KITT understands')
            print('~--------------------~')

            print('[Listening ...]')
            PicovoiceDemo._start_up(self)
            while True:
                pcm = recorder.read()
                self._picovoice.process(pcm)

        # Ctrl + C ends the program. Took me forever to figure this out sadly
        # And the ALSA process does not stop if you do not end the program properly
        # which led me to hours and hours of troubleshooting ._.  
        except KeyboardInterrupt:
            sys.stdout.write('\b' * 2)
            print('Stopping ...')
        # Finally, clean up. If Recorder is running, delete process and delete picovoice process
        finally:
            if recorder is not None:
                recorder.delete()

            self._picovoice.delete()


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--access_key',
        help='AccessKey obtained from Picovoice Console (https://picovoice.ai/console/)',
        required=True)
        

    parser.add_argument('--audio_device_index', help='Index of input audio device.', type=int, default=-1)

    args = parser.parse_args()

    o = PicovoiceDemo(
        os.path.join(os.path.dirname(__file__), 'hey-kit.ppn'),
        os.path.join(os.path.dirname(__file__), 'kitt.rhn'),
        args.access_key,
        args.audio_device_index
    )
    o.run()


if __name__ == '__main__':
    main()
