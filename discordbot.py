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
        await self.tree.sync()
        print(f"Logged in as {self.user}")

client = MyClient()

@client.tree.command(name="light_on")
@app_commands.describe(room="Which light?")
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
@app_commands.describe(room="Which light?")
async def light_off(
    interaction: discord.Interaction,
    room: str
):
    try:
        await turn_off(room)
        await interaction.response.send_message(
            f"🌙 {room} light turned off!"
        )
    except ValueError as e:
        await interaction.response.send_message(str(e), ephemeral=True)

client.run(DISCORD_TOKEN)