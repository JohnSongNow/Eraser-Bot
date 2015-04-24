# EraserBot
An open-source IRC bot designed for Twitch.tv made in Python. To have the bot in your channel simply fill out the required forms on the bots field.

If you have any question feel free to leave me a note, I will do my best to address as many issues as I can but no promises.

# Setup
- Python 3.3+
- EraserBot 1.0
- LeagueAPI 1.0
- requests plguin (if you're using the LeagueAPI)

# Features
Eraser bot features anti, spam filters, customiable dilagoue and LeagueAPI intergration.

- Anti Spam Filter
- Easy to customize mod, viewer, and owner bot phrases
- LOL account intergration

# Bot Info
Below is a list of all the required info for the bot to function. Keep in mind that if you do not understand a field simply conduct a google serach.

*Note I recommend that you make a new Twitch Account for your bot to run as
- OWNER = 'ownerNAME'
- NICK = "botName"
- IDENT = "botName"
- REALNAME = "botName"
- CHANNEL = "#channelName"
- PASSWORD = "twitchBotOuathID"
  - Gotten via http://twitchapps.com/tmi/
- RIOT_API_KEY = 'riotAPIKey'
  - Gotten via https://developer.riotgames.com/
- SUMMONER_NAME = 'summonerName'(Optional)

# System Commands
System commands are commands that effect change the system of the bot whether it's the spam filter or other settings. All system commands can only be used by mods with some restricted to only the owner.

- Mod
  - addViewerCommand [commandToken] [Phrase]
  - deleteViewerCommand [commandToken]
- Owner
  - !save
  - !!addModCommand/!addOwnerCommand [commandToken] [Phrase]
  - !deleteViewerCommand/!deleteModCommand/!deleteOwnerCommand [commandToken]
  - !changeSetting [settingName] [newValue]
  - !addMods [modNames]
  - !deleteMods [modNames]
