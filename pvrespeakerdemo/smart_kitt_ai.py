# 
# Made by Braeden Pelletier 2022
# This is for a Knight Rider themed gas pump
# I am using Picovoice, Porcupine wake-word, and Rhino Speech-to-intent
#

import argparse
import os
import time
import struct
import sys
from threading import Thread

from gpiozero import LED
from pydub import AudioSegment
from pydub.playback import play
from playsound import playsound
from picovoice import Picovoice
from pvrecorder import PvRecorder

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

# pull file for playback
fname = "/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Hello!.mp3"
mysound = AudioSegment.from_wav(fname)

class PicovoiceDemo(Thread):
    def __init__(
            self,
            keyword_path,
            context_path,
            access_key,
            device_index,
            porcupine_sensitivity=0.75,
            rhino_sensitivity=0.25):
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
    def _say_phrase():
        play(mysound)

    @staticmethod
    def _wake_word_callback():
        print('[wake word]\n')

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
                self._say_phrase()
            elif inference.intent == 'HowYou':
                self._say_phrase()
            elif inference.intent == 'Goodbye':
                self._say_phrase()
            elif inference.intent == 'ThankYou':
                self._say_phrase()
            elif inference.intent == 'Apology':
                self._say_phrase()
            elif inference.intent == 'Greeting':
                self._say_phrase()
            elif inference.intent == 'Anger':
                self._say_phrase()
            elif inference.intent == 'Understand':
                self._say_phrase()
            elif inference.intent == 'Joke':
                self._say_phrase()
            elif inference.intent == 'Reassure':
                self._say_phrase()
            elif inference.intent == 'Compliment':
                self._say_phrase()
            elif inference.intent == 'Insult':
                self._say_phrase()
            else:
                raise NotImplementedError()

    def run(self):
        recorder = None

        try:
            recorder = PvRecorder(device_index=self._device_index, frame_length=self._picovoice.frame_length)
            recorder.start()

            print(self._context)

            print('[Listening ...]')

            while True:
                pcm = recorder.read()
                self._picovoice.process(pcm)
        except KeyboardInterrupt:
            sys.stdout.write('\b' * 2)
            print('Stopping ...')
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
