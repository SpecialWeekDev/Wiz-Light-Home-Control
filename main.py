import asyncio
from pywizlight import wizlight, PilotBuilder, discovery
from config import LIGHTS
from wizcontrol import turn_off, turn_on, set_brightness, get_light

async def main():
    bulbs = await discovery.discover_lights()

    for bulb in bulbs:
        print(bulb)
        print()

    while True:
        command = input("Enter command: ").lower()

        if command == "exit":
            break

        elif command == "on":
            room = input("Which light? (bed/game): ").lower()

            await turn_on(room)

        elif command == "off":
            room = input("Which light? (bed/game): ").lower()

            await turn_off(room)

        elif command == "brightness":
            room = input("Which light? (bed/game): ").lower()
            brightness = int(input("Enter brightness (0-255): "))

            await set_brightness(room, brightness)

asyncio.run(main())