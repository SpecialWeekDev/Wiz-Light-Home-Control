import discord
from discord import app_commands
from wizcontrol import turn_on, turn_off, set_brightness
from config import DISCORD_TOKEN

class MyClient(discord.Client):

    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        synced = await self.tree.sync()

        print(f"Synced {len(synced)} commands")
        for command in synced:
            print(command.name)


        print(f"Logged in as {self.user}")

client = MyClient()

@client.tree.command(name="light_on")
@app_commands.describe(room="Which room light?")
async def light_on(
    interaction: discord.Interaction,
    room: str
):
    try:
        await turn_on(room)
        await interaction.response.send_message(
            f"💡 {room}room light turned on!"
        )
    except ValueError as e:
        await interaction.response.send_message(str(e), ephemeral=True)

@client.tree.command(name="light_off")
@app_commands.describe(room="Which room light?")
async def light_off(
    interaction: discord.Interaction,
    room: str
):
    try:
        await turn_off(room)
        await interaction.response.send_message(
            f"🌙 {room}room light turned off!"
        )
    except ValueError as e:
        await interaction.response.send_message(str(e), ephemeral=True)

@client.tree.command(name="brightness")
@app_commands.describe(room="Which room light?", level="Brightness level?")
async def brightness(
    interaction: discord.Interaction,
    room: str,
    level: app_commands.Range[int, 0, 255]
):
    try:
        await set_brightness(room, level)
        await interaction.response.send_message(
            f"💡 {room}room brightness set to {level}!"
        )
    except ValueError as e:
        await interaction.response.send_message(str(e), ephemeral=True)


client.run(DISCORD_TOKEN)