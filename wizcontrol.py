from pywizlight import wizlight, PilotBuilder
from config import LIGHTS

def get_light(room):
    ip = LIGHTS.get(room)

    if ip is None:
        raise ValueError(f"Unknown room: {room}")
    return wizlight(ip)

async def turn_on(room):
    light = get_light(room)
    await light.turn_on(PilotBuilder())

async def turn_off(room):
    light = get_light(room)
    await light.turn_off()

async def set_brightness(room, brightness):
    light = get_light(room)
    await light.turn_on(PilotBuilder(brightness=brightness))
