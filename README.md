# Eraser-Bot
Eraser-Bot is an IRC bot written in specifically designed to moderate Twitch.tv channels. It's a simple and customizable bot 
designed to ensure a smooth chat experience. Eraser bot features anti-spam and profanity filters, customizable commands, and is easy to use.

# Setup
Running the bot is fairly simple, fill out the required forms and then run the script using a Python IDE or through a cmd prompt/shell  Don't forget to mod Eraser-Bot as well.

- Python (**3.3+**) 
- A modded Twitch.tv account for Eraser-Bot to use
- Python IDE(Not needed but recommended if using shell/cmd prompt)

# Bot Info
Fill out the info below with the required info to run Eraser-Bot. I recommend making a dedicated Twitch.tv account for your bot.

- OWNER = "ownerNAME"
- NICK = "botName"
- IDENT = "botName"
- REALNAME = "botName"
- CHANNEL = "#channelName"
- PASSWORD = "twitchBotOuathID"
  - [Login in with your bot account here](http://twitchapps.com/tmi/)
- KEY_PHRASE = "!"
  - I don't recommend changing this unless you have a specific reason

# Commands
Commands are called from the Twitch.tv chat, and they range from adding and deleting commands to changing the system settings. Certain commands are set to ensure that only mods and/or the owner can call them. New commands can also be added both manually by editing the text files or through Eraser-Bot by a mod or owner.

By default the key phrase is '!', you can change it but it is not recommended.
To call a command simply put the keyphrase, the command name then the params. Note the last param
will take into account every word until the end is reached.

Example 1
```
!addViewerCommand [commandToken] [Phrase]

!addViewerCommand facebook Here is a link to facebook! https://facebook.com
```

Second example 2
```
!changeSetting [settingName] [settingValue]

!changeSetting greetingMessage "Welcome to (Insert Name Here)'s Channel!

Notice how all values past the param are considered to be part of 
```

- Mod
  - addViewerCommand [commandToken] [Phrase]
  - deleteViewerCommand [commandToken]
- Owner
- save : Saves the currnet commands to local text files  
- reload : Reloads all current commands from local text files  
- add|Mod/Owner|Command [commandToken] [Phrase] : Adds a mod/owner phrase with a keyword
- delete|Mod/Owner|Command [commandToken] : Deletes a mod/owner phrase with a keyword
- changeSetting [settingName] [newValue] : Changes the given setting to a new value
- addMods [modNames] : Adds a mod to the bot-mod list
- deleteMods [modNames] : Deletes a mod from the bot-mod list 

For any questions please visit [Eraser-Bot](johnsong.science/projects/eraser-bot)
