# Python 3.10 Match statement, similar to switch in other langs

import random
from enum import Enum
class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2
    NONE = False

color = Color(random.randint(0, 2))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
    case _:
        print(f"No color detected: {color}")
