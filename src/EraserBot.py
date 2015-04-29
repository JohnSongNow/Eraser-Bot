# Copyright (c) 2015 Jin (John) Song (rh [at] johnsong.science)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnishedto do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY,WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISIN
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
import socket, time, urllib.request
import RiotAPI, RiotConstants, random

# Connection Constants
HOST = "irc.twitch.tv"
PORT = 6667
OWNER = 'ownerNAME'
NICK = "botName"
IDENT = "botName"
REALNAME = "botName"
CHANNEL = "#channelName"
PASSWORD = "twitchBotOuathID"
readbuffer = ""
GLOBAL_EMOTES_URL = 'https://twitchemotes.com/filters/global'
RIOT_API_KEY = 'riotAPIKey'

# Local Constants
KEY_PHRASE = '!'
MODS = {OWNER, 'thehiddenmage2'}
BANNED_WORDS = set()
EMOTES = set()
EXTRA_VIEWER_COMMANDS = dict()
EXTRA_MOD_COMMANDS = dict()
EXTRA_OWNER_COMMANDS = dict()
LINK_WHITELIST = dict()
AUTO_MESSAGES = dict()
# The Command Followed By It's Clearance
SYSTEM_COMMANDS = {'mods': {'save', 'r9k', 'r9koff', 'addViewerCommand',
                               'deleteViewerCommand'},
                   'owner': {'addmods', 'deletemods', 'addModCommand',
                                'deleteModCommand', 'addOwnerCommand',
                                'deleteOwnerCommand', 'changeSetting'}}

# AUTO_MESSAGE_DELAY is in seconds
SETTINGS = {'MAXIMUM_NON_ASCII_CHARACTERS' : 4,
                'ANTI_SPAM_LENGTH' : 30, 'MAX_EMOTE_OCCURENCE' : 5,
                'AUTO_MESSAGE' : False, 'AUTO_MESSAGE_DELAY' : 300}

# Riot API Constants
API = RiotAPI.RiotAPI(RIOT_API_KEY)
FORMATTER = RiotAPI.RiotFormatter(API)
SUMMONER_NAME = 'summonerName'
SUMMONER_ID = API.get_summoner_by_name(SUMMONER_NAME)

print('Connecting')
t = socket.socket()
t.connect((HOST, PORT))
print("Connected! Logging in")
t.send(bytes("PASS %s\r\n" % PASSWORD, "UTF-8"))
t.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
t.send(bytes("USER %s %s BOT :%s\r\n" % (IDENT, HOST, REALNAME), "UTF-8"))
print("Logged in. Joining Channel")
t.send(bytes("JOIN %s\r\n" % CHANNEL, "UTF-8"))
print("JOINED!")


def execute_command(command, name, line):
    '''
    (Str, Str [Str]) -> NoneType
    Executes a series of commands based on the
    command, name and line.
    '''
    print(name in MODS)
    # You can add indiviudal effects here, but unless it requires something
    # not executable by the send_message(message) do not add
    if(command == 'runes'):
        if(SUMMONER_NAME != 'summonerName'):
            send_message(SUMMONER_NAME + ' is using : ' +
                         str(FORMATTER.format_runepage(
                             API.get_current_runes(SUMMONER_ID))))
    # Extra Viewer Commands
    elif(command in EXTRA_VIEWER_COMMANDS.keys()):
        send_message(EXTRA_VIEWER_COMMANDS[command])

    # If our command is mod-only
    elif(name in MODS):
        # Activiating system commands for mods
        if(command in SYSTEM_COMMANDS['mods']):
            if(command == 'save'):
                save_data()
                send_message('Data has been saved')
            elif(command == 'addViewerCommand'):
                add_command(EXTRA_VIEWER_COMMANDS, line[0], line)
            elif(command == 'deleteViewerCommand'):
                delete_command(EXTRA_VIEWER_COMMANDS, line[0])
            elif(command == 'addAutoMessage'):
                add_command(AUTO_MESSAGES, line[0], line)
            elif(command == 'deleteAutoMessage'):
                delete_command(AUTO_MESSAGES, line[0])
        # Else just a spare mod command
        elif(command in EXTRA_MOD_COMMANDS.keys()):
            send_message(EXTRA_MOD_COMMANDS[command])

        # If it's the owner
        elif(name == OWNER):
            # Activiating system commands for owner only
            if(command in SYSTEM_COMMANDS['owner']):
                # Adding Mod Commands
                if(command == 'addModCommand'):
                    add_command(EXTRA_MOD_COMMANDS, line[0], line)
                # Deleteing Mod Commands
                elif(command == 'deleteModCommand'):
                    delete_command(EXTRA_MOD_COMMANDS, line[0])
                # Deleteing Mods
                elif(command == 'addMods'):
                    for mod in line:
                        MODS.add(mod)
                # Adding Mods
                elif(command == 'deleteMods'):
                    for mod in line:
                        MODS.delete(mod)
                # Adding owner commands
                elif(command == 'addOwnerCommand'):
                    add_command(EXTRA_OWNER_COMMANDS, line[0], line)
                elif(command == 'deleteOwnerCommand'):
                    delete_command(EXTRA_OWNER_COMMANDS, line[0])
                # Adding owner commands
                elif(command == 'addLink'):
                    add_command(LINK_WHITELIST, line[0], line)
                elif(command == 'deleteLink'):
                    delete_command(LINK_WHITELIST, line[0])
                elif(command == 'changeSetting'):
                    # If our wanted setting is valid
                    if(line[0] in SETTING.keys()):
                        try:
                            value = int(line[1])
                            SETTINGS[line[0]] = line[1]
                        except Exception:
                            send_message('Invalid Entry')
            # Activating spare owner commands
            elif(command in EXTRA_OWNER_COMMANDS.keys()):
                send_message(EXTRA_OWNER_COMMANDS[command])


def add_command(target, command_name, line):
    '''
    (Dict(Str, Str), Str, [Str]) -> NoneType
    Adds the command to teh targgeted dictionary.
    '''
    if(len(line) > 1):
        target[command_name] = list_to_str(line[1:])
        send_message('Command ' + line[0] + ' has been added.')
    else:
        send_message('Invalid Entry')


def delete_command(target, command_name):
    '''
    (Dict, Str) -> NoneType
    Deletes the command with the name at the targeted dictionary.
    '''
    if(command_name in target):
        del target[command_name]
        send_message('Command ' + command_name +
                     ' has been deleted.')
    else:
        send_message('Command ' + command_name + ' does not exist.')


def send_message(message):
    '''
    (Str) -> NoneType
    Sends a message to the IRC chat based on
    with the login info as a global
    '''
    t.send(bytes('PRIVMSG ' + CHANNEL + ' :' + message  + '\r\n', 'UTF-8'))


def time_out(username, time=300):
    '''
    (Str) -> NoneType
    Times out the username.
    '''
    send_message('/timeout ' + username + ' ' + str(time))


def ASCII_Filter(message):
    '''
    ([Str]) -> Bool
    Returns whether this line will
    be filtered based on the number of non ASCII
    characters
    '''
    # Something going wrong
    if(isinstance(message, list)):
        non_ASCII = 0
        for word in message:
            for letter in word:
                if(ord(letter) > 126):
                    non_ASCII += 1
                    # MAXIMUM_NON_ASCII_CHARACTERS is a global constant within
                    # SETTINGS
                    if(non_ASCII > SETTINGS['MAXIMUM_NON_ASCII_CHARACTERS']):
                        return True;
    return False;


def emote_filter(message):
    '''
    (Str) -> bool
    Checks if the current str does not obey the maxmium
    number of emotes allowed.
    '''
    # Something going wrong
    if(isinstance(message, list)):
        emotes_occurence = 0
        for word in message:
            if(word in EMOTES):
                emotes_occurence += 1
            # MAXIMUM_NON_ASCII_CHARACTERS is a global constant
            if(emotes_occurence > SETTINGS['MAX_EMOTE_OCCURENCE']):
                return True
    return False


def link_filter(message):
    '''
    (Str) -> bool
    Checks if the current str contains a non whitelisted link
    '''
    return False
    for word in message:
        if(word):
            return True
    return False

def check_spam(message, username):
    '''
    (Str, Str) -> bool
    Checks if the current str obeys all of the chat rules
    (Emote / ASCII Spam and message length). Returns
    whether the message is filtered or not
    '''
    # Checking the length first
    if(len(message) > SETTINGS['ANTI_SPAM_LENGTH']):
        time_out(username, 10)
        send_message("Your message is too long : " + username)
        return True

    # Banned Words Filter
    for word in BANNED_WORDS:
        if(word in message):
            time_out(username, 10)
            send_message("No profanity or unallowed" +
                         " words please : "  + username)
            return True

    # Then checking the ASCII filter
    if(False):
        if(ASCII_Filter(message) == True):
            time_out(username, 10)
            send_message("ASCII spam detected : " + username)
            return True

    # Then checking the emote filter
    if(emote_filter(message) == True):
        time_out(username, 10)
        send_message("Emote spam detected : " + username)
        return True

    # Link Filter
    if(link_filter(message) == True):
        time_out(username, 10)
        send_message("Linked is not from a whitelisted source : " + username)
    return False


def auto_message():
    '''
    () -> ()
    Sends periodic random messages through twitch chat
    '''
    new_key = random.choice(AUTO_MESSAGES)
    current_key = ''
    while True:
        # Making sure the next message is not the same as our current
        # Maybe a global cosntantw ould work better here hmm...
        while(current_key != new_key and len(AUTO_MESSAGES > 1)):
            new_key = random.choice(AUTO_MESSAGES.keys())
        current_key = new_key

        send_message(AUTO_MESSAGE[current_key])
        # Sleep the thread
        time.sleep(SETTINGS['AUTO_MESSAGE_DELAY'])


def load_data():
    '''
    () -> ()
    Loads all the apparoate data from disk onto the bot
    '''
    # Loading mods and banned words
    load_set(BANNED_WORDS, 'banned_words.txt')
    load_set(MODS, 'mods.txt')

    # Loading Emotes
    temp_emotes = []
    load_list(temp_emotes, 'global_emotes.txt')
    for emote in temp_emotes:
        EMOTES.add(emote[:len(emote) - 1])

    # Loading all the dicts
    load_dict(EXTRA_VIEWER_COMMANDS, 'extra_viewer_commands.txt')
    load_dict(EXTRA_MOD_COMMANDS, 'extra_mod_commands.txt')
    load_dict(EXTRA_OWNER_COMMANDS, 'extra_owner_commands.txt')
    load_dict(AUTO_MESSAGES, 'auto_messages.txt')
    load_dict(LINK_WHITELIST, 'link_whitelist.txt')
    load_dict(SETTINGS, 'settings.txt')
    for key, value in SETTINGS.items():
        SETTINGS[key] = int(value)


def save_data():
    # Saving mods and banned words
    save_set(BANNED_WORDS, 'banned_words.txt')
    save_set(MODS, 'mods.txt')

    # Loading all the dicts
    save_dict(EXTRA_VIEWER_COMMANDS, 'extra_viewer_commands.txt')
    save_dict(EXTRA_MOD_COMMANDS, 'extra_mod_commands.txt')
    save_dict(EXTRA_OWNER_COMMANDS, 'extra_owner_commands.txt')
    save_dict(AUTO_MESSAGES, 'auto_messages.txt')
    save_dict(LINK_WHITELIST, 'link_whitelist.txt')
    save_dict(SETTINGS, 'settings.txt')


def load_dict(target, file_name):
    '''
    (Dict, Str) -> NoneType
    Loads the dictionary up with all of commands in the file.
    Note that any commands with dupelicate keys will be overridden.
    '''
    try:
        file = open(file_name, 'r')
        for line in file:
            # Finding the split index
            index = line.index(':')
            key = line[:index]
            value = line[index + 1:]
            target[key] = value
    except FileNotFoundError:
        print('File : ' + file_name + ' not found!')
    except Exception:
        print('Something else went wrong')


def load_set(target, file_name):
    '''
    (Set, Str) -> NoneType
    Loads the set up with all of commands in the file.
    Note that any commands with dupelicate keys will be overridden.
    '''
    try:
        file = open(file_name, 'r')
        for line in file:
            target.add(line.replace('\n', ''))
    except FileNotFoundError:
            print('File : ' + file_name + ' not found!')


def load_list(target, file_name):
    '''
    (list, Str) -> NoneType
    Loads the set up with all of commands in the file.
    Note that any commands with dupelicate keys will be overridden.
    '''
    file = open(file_name, 'r')
    for line in file:
        target.append(line)


def save_dict(data, file_name):
    '''
    (Dict, Str) -> NoneType
    Saves the dictionary up with all of commands in the file.
    Note that any commands with dupelicate keys will be overridden.
    '''
    try:
        file = open(file_name, 'w')
        for key, value in data.items():
            file.write(str(key) + ':' + str(value))
            file.write('\n')
    except FileNotFoundError:
        print('File : ' + file_name + ' not found!')


def save_set(data, file_name):
    '''
    (Set, Str) -> NoneType
    Saves the set up with all of commands in the file.
    Note that any commands with dupelicate keys will be overridden.
    '''
    try:
        file = open(file_name, 'w')
        for value in data:
            file.write(value)
            file.write('\n')
    except FileNotFoundError:
            print('File : ' + file_name + ' not found!')


def list_to_str(message):
        result_message = ''

        for word in message:
            result_message += word + ' '
        length = len(result_message) - 1
        result_message = result_message[:length]
        return result_message


# Main Loop
load_data()

if(SETTINGS['AUTO_MESSAGE']):
    try:
        thread.start_new_thread(auto_message, ())
    except:
        print('Something went wrong')

while True:
    readbuffer = readbuffer + t.recv(1024).decode("UTF-8")
    temp = readbuffer.split("\n")
    readbuffer = temp.pop()

    # Parsing the line
    for line in temp:
        line = line.rstrip()
        line = line.split()

        if(line[0] == "PING"):
            t.send(bytes("PONG %s\r\n" % line[1], "UTF-8"))

        # If this is a line
        if(line[1] == 'PRIVMSG'):
            name = line[0].split('!')[0].strip(':')
            line[3] = line[3][1:]

            # Checking Spam
            if(check_spam(line[3:], name) == False):
                # Checking if we have a command
                if(len(line) > 3):
                    command = line[3].strip(':').strip()
                    # Command executor
                    if(command[0] != ''):
                        if(command[0] == KEY_PHRASE):
                            execute_command(command[1:], name, line[4:])
        print(line)