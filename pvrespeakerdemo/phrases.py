"""
Braeden Pelletier December 2022 Smart KITT (Knight Rider)

Phrases categorized and randomized for output
Ex. When you tell KITT an insult, it will pull one of the responses
at random. Likewise for greetings, compliments, and so on.
If no inference is recognized, BadPhrase() is pulled.
*Rhino Speech-to-Intent*
"""
import random
import secrets

class KittPhrases:
    # Phrases in response of a "Who are you"-type question
    def WhoAreYou():
        # Contain all full paths in an array
        phrases = [
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/WhoAreYou/kitt-sure-enough.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/WhoAreYou/I am KITT.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/WhoAreYou/I am a Knight Industries.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/WhoAreYou/I am the voice.mp3'
            ]
        # var path is a random full path of one of the above
        path = secrets.choice(phrases)
        return path
    def ThankYou():
        phrases = [
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/ThankYou/De nada.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/ThankYou/Dont mention it.mp3'
        ]
        path = secrets.choice(phrases)
        return path
    def Joke():
        phrases = [
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Joke/I stopped for gas the other day....mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Joke/Im definitely dark and handsome....mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Joke/When I was a kid....mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Joke/Can a Rolls-Royce do computer scans_.mp3'
        ]
        path = secrets.choice(phrases)
        return path
    def Insult():
        phrases = [
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Insult/You must be joking.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Insult/Why_.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Insult/The things Im forced to put up with.mp3'
            ]
        path = secrets.choice(phrases)
        return path
    def Idle():
        phrases = [
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Youre awfully quiet.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Idle/Ehum.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Idle/Are you there....mp3'
        ]
        path = secrets.choice(phrases)
        return path
    def HowAreYou():
        phrases = [
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/HowAreYou/Not now, I have a headache.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/HowAreYou/As a machine.mp3'
        ]
        path = secrets.choice(phrases)
        return path
    def Greeting():
        phrases = [
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Greeting/Hello.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Greeting/Hello!.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Greeting/You again_.mp3'
        ]
        path = secrets.choice(phrases)
        return path
    def Goodbye():
        phrases = [
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Goodbye/Bon voyage.mp3'
        ]
        path = secrets.choice(phrases)
        return path
    def DoYouUnderstand():
        phrases = [
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/DoYouUnderstand/I certainly hope so.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/DoYouUnderstand/I dont think so.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/DoYouUnderstand/I suppose so.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/DoYouUnderstand/I think so.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/DoYouUnderstand/Im afraid not.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/DoYouUnderstand/In a word, no.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/DoYouUnderstand/No comment.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/DoYouUnderstand/Not exactly.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/DoYouUnderstand/Probably.mp3'
        ]
        path = secrets.choice(phrases)
        return path
    def Compliment():
        phrases = [
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Compliment/Definitely possible.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Compliment/Dont mention it.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Compliment/I agree.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Compliment/Its good to hear your voice.mp3'
        ]
        path = secrets.choice(phrases)
        return path
    def AreYouSure():
        phrases = [
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/AreYouSure/I certainly hope not.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/AreYouSure/I have no idea.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/AreYouSure/If you say so.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/AreYouSure/Im afraid so.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/AreYouSure/Negative.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/AreYouSure/Not a chance.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/AreYouSure/Of course.mp3'
        ]
        path = secrets.choice(phrases)
        return path
    def Apology():
        phrases = [
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Apology/Are you alright1.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Apology/Did you hear that_.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Apology/Im sorry I try.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Apology/Where are your pants_.mp3'
        ]
        path = secrets.choice(phrases)
        return path
    def Anger():
        phrases = [
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Anger/How very unproductive.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Anger/I detect a certain tone in your voice.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Anger/Surely youre not serious.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Anger/Well thats a new one.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Anger/Your palms are clammy.mp3'
        ]
        path = secrets.choice(phrases)
        return path
    def BadPhrase():
        phrases = [
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/BadPhrase/Good heavens! And I thought Michael was difficult.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/BadPhrase/I beg your pardon.mp3'
        ]
        path = secrets.choice(phrases)
        return path
    def Affection():
        # Todo, 'I love you (kit)'
        phrases = [
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Affection/Youve probably begun.mp3',
            '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Affection/Tell me about it.mp3'
        ]
        path = secrets.choice(phrases)
        return path
    def StartUp():
        return '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/WhoAreYou/I am the voice.mp3'
    
    def StartUp2():
        return '/home/pi/.virtualenvs/py3.7/lib/python3.7/site-packages/pvrespeakerdemo/sounds/Greeting/Hello!.mp3'