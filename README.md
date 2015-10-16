# EraserBot
Eraserbot is an IRC bot written in Python (**3.3+**) designed for to moderate Twitch.tv channels. EraserBot is a simple and customizable bot editable both manually using the options file or using the Twitch.tv chat when the bot is running. To run the bot EraserBot should be ran in an Python IDE. To have the bot in your channel simply fill out the required forms on the bots field.

If you have any question feel free to leave me a note, I will do my best to address as many issues as I can but no promises.

# Setup
To setup your bot you need the following. Running the bot is fairly simple, simply run the script using your Python IDE of choice and fill out the required forms. Don't forget to mod EraserBot as well.

- Python 3.3+
- EraserBot
- A Python IDE (Not needed if you are running the script directly)

# Features
Eraser bot features anti, spam filters, customiable dilagoue and LeagueAPI intergration.

- Anti Spam Filter
- Easy to customize mod, viewer, and owner bot phrases
- Social Media Intergration with FB and Twitter

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
