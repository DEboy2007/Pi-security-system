# Pi-security-system
An easy-to-use and cheap home security system.<br>
**Still a work-in-progress!**

### Features
- Remote control through discord
- On demand image of what the camera sees
- Motion detection
- Alert and asleep modes so you only get notifications when needed

### Image of current features
![image](https://user-images.githubusercontent.com/66331423/122826428-fc511900-d297-11eb-9d6c-356fc78f98a8.png)

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
- Install discord.py:
```pip install discord.py```
- Download the python files and in bot.py, replace the token and channel ID with your bot's token and the channel where you would like security alerts
- Transfer bot.py and motion_detection.py to your Pi and run bot.py (Make sure all files are in the same directory)
- Connect your Pi camera to the Pi and put the camera where you want to monitor
- Congratulations! You now have a remotely accessible home security system! (use $info for help)
