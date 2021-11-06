from commands import *
from cycle import Cycle

computers = (
    "",
    "javi@raspberrypi",
    "pi@retropie",
    "javi@zeropi"
    )

myCycle = Cycle(computers)

for i in computers:
    current = Command(i)
    print(current.hostname())
    print(current.cpuload())
    print(current.memory())
    print(current.disk())
    print(current.temperatura())
    current.end()
