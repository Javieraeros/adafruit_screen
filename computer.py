from commands import *
from cycle import Cycle

computers = (
    "",
    "javi@zero2pi",
    "javi@raspberrypi",
    "pi@retropie",
)

mycycle = Cycle(computers)
current = mycycle.current()
computer = Command(current)

def current_computer(buttonPrev, buttonNext):
    global computer
    if buttonPrev.value and not buttonNext.value:
        computer.end()
        current = mycycle.prev()
        computer = Command(current)
    elif buttonNext.value and not buttonPrev.value:
        computer.end()
        current = mycycle.next()
        computer = Command(current)
    return computer
