from flask import Flask, render_template
from wizcontrol import turn_off, turn_on, set_brightness
import asyncio

web = Flask(__name__)

@web.route("/")
def home():
    return render_template("index.html")

@web.route("/on")
def light_on():
    asyncio.run(turn_on("game"))
    return "Light is on"

@web.route("/off")
def light_off():
    asyncio.run(turn_off("game"))
    return "Light is off"

@web.route("/brightness/<int:level>")
def brightness(level):
    asyncio.run(set_brightness("game", level))
    return f"Brightness set to {level}"

if __name__ == "__main__":
    web.run(debug=True)