import asyncio
from pywizlight import wizlight, PilotBuilder, discovery
from config import BEDROOM, GAME_ROOM

async def main():
    bulbs = await discovery.discover_lights()

    for bulb in bulbs:
        print(bulb)
        print()

    lightBR = wizlight(BEDROOM)
    lightGR = wizlight(GAME_ROOM)

    while True:
        command = input("Enter command: ").lower()

        if command == "exit":
            break

        elif command == "on":
            command = input("Which light? (bed/game): ").lower()

            if command == "bed":
                await lightBR.turn_on(PilotBuilder())
            elif command == "game":
                await lightGR.turn_on(PilotBuilder())

        elif command == "off":
            command = input("Which light? (bed/game): ").lower()

            if command == "bed":
                await lightBR.turn_off()
            elif command == "game":
                await lightGR.turn_off()

        elif command == "brightness":
            command = input("Which light? (bed/game): ").lower()
            brightness = int(input("Enter brightness (0-255): "))

            if command == "bed":
                await lightBR.turn_on(PilotBuilder(brightness=brightness))
            elif command == "game":
                await lightGR.turn_on(PilotBuilder(brightness=brightness))

asyncio.run(main())