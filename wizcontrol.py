from pywizlight import wizlight, PilotBuilder
from config import BEDROOM, GAME_ROOM

lightBR = wizlight(BEDROOM)
lightGR = wizlight(GAME_ROOM)

async def turn_on(room):
    if room == "bed":
        await lightBR.turn_on(PilotBuilder())
    elif room == "game":
        await lightGR.turn_on(PilotBuilder())

async def turn_off(room):
    if room == "bed":
        await lightBR.turn_off()
    elif room == "game":
        await lightGR.turn_off()

async def set_brightness(room, brightness):
    if room == "bed":
        await lightBR.turn_on(PilotBuilder(brightness=brightness))
    elif room == "game":
        await lightGR.turn_on(PilotBuilder(brightness=brightness))