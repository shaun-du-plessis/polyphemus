"""
This module implements a Polyphemus screen reader.
S"""
import ctypes
import pyttsx3


engine = pyttsx3.init()
engine.say("Hello Shaun! Welcome.")
engine.runAndWait()


def check_speaker_volume():
    '''
        Checks the current volume level
    '''
    user32 = ctypes.windll.user32
    volume = user32.GetVolume()
    return volume > 0

age: int
houseNumber: float 6.4
fName: str = 'Shaun'
sName: str = "du Plessis"
child: bool

print(
    f'Hi, {fName} + " " + {sName}. How are you, ' +
    f'do you still live at number {houseNumber}?'
    )


def get_text_for_engine():
    ''' gets text for engine '''
    user_input = ""
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 75)  # Decrease speech rate
    engine.say("This is a slower speech rate.")
    engine.runAndWait()

    while True:
        # pylint: disable=C0103
        user_input = input(
            "Enter some text. I will repeat it to you, 'quit' to exit: "
            )
        if user_input == "quit":
            break
        engine.say(user_input)
        engine.runAndWait()


check_speaker_volume()
get_text_for_engine()
