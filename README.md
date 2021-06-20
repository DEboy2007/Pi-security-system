# Pi-security-system
An easy-to-use and cheap home security system.
**Still a work-in-progress!**

### Features
- Remote control through discord
- Face recognition
- Motion detection
- Alert and asleep modes so you only get notifications when needed

### Requirements

#### Hardware
- Raspberry Pi
- Raspberry Pi charger
- Raspberry Pi Camera

#### Software
- Discord
- Raspbian installed on your Pi
- discord.py library installed on your Pi

### Setup
- Create a discord bot (You can follow this guide: https://www.freecodecamp.org/news/create-a-discord-bot-with-python/)
- Download the python files and in bot.py, replace the token and channel ID with your bot's token and the channel where you would like security alerts
- Transfer bot.py and motion_detection.py to your Pi and run both of them.
- Connect your Pi camera to the Pi and put the camera where you want to monitor
- Congratulations! You now have a remotely accessible home security system!
