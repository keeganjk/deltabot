#!/usr/bin/env python3

# deltabot.py
# By keeganjk

# To create a Discord bot, go to https://discordapp.com/developers/applications/me
# Click "New App".
# Add a name (required) and a description and profile picture if you'd like.
# Click "Create a Bot User" to turn this application into a bot and confirm with "Yes, do it!".
# You can find the Client ID near the top of the page under "APP DETAILS".
# To add the bot to a server, go to https://discordapp.com/api/oauth2/authorize?client_id=CLIENTIDHERE&scope=bot&permissions=1
# This link will be generated when you run this script, assuming that you've put in your token.
# Lastly, at the bottom of the page, you will see a line that says "client.run('token')".
# Find your token near the bottom of your bot's page under "Bot".
# You will have to click "click to reveal".
# Copy the token and put it in the bottom line of the page, where it says client.run('token'). LEAVE YOUR TOKEN IN QUOTES.

# Imports modules required for the bot
import discord, random

# Creates a variable, "client", that performs the bot's functions
client = discord.Client()

# Starts a list of command prefixes
prefixes = []

# Detect if the client (bot) has an event
@client.event
# When the bot is ready, run this function below:
async def on_ready():
    user    = str(client.user)                 # The bot's name + Discord tag
    name    = client.user.name                 # The bot's name
    user_id = client.user.id                   # The bot's ID
    prefixes.append('<@' + user_id + '> ')     # Add's "@[bot name] " as a prefix
    print("Logged in as : " + name)            # The bot is logged in as [its name]
    print("Client ID    : " + user_id)         # The bot prints its ID
    print('=' * 50)                            # Makes a line out of ='s that is 50 characters long
    print("To add this bot to a server, use:") # Displays a link that can be used to add bot to server
    print("https://discordapp.com/api/oauth2/authorize?client_id=" + user_id + "&scope=bot&permissions=1")
    print('=' * 50)                            # Makes a line out of ='s that is 50 characters long

# Creates variables/lists
defPrefix     = '!!'                   # Sets default prefix, character that determines if you are talking to the bot or not
prefixes.append(defPrefix)             # Adds the default prefix to the list of prefixes
logStr        = ''                     # Makes a list to put history in if log is enabled
log           = 1                      # Whether the bot records logs or not. 1 or True = on, 0 or False is off.
msg           = ''                      # Declares variable used for replies
usr_greetings = ['hi', 'hey', 'hello'] # Known greetings to expect from a user
bot_greetings = []                     # A list of a bot's known greetings to reply with
for i in usr_greetings:                # For every item in usr_greetings,
    bot_greeting = i.capitalize()      # Capitalize it
    bot_greetings.append(bot_greeting) # and add it to the bot's list of greetings

# Detect if the client (bot) has an event
@client.event
# If someone says something, run this function below:
async def on_message(message):
    author    = message.author                         # Author of the message
    auth_name = message.author.name                    # Author's name
    channel   = message.channel                        # Channel that the message is on
    server    = message.server                         # Server that the message is on
    original  = message.content                        # Original message
    digested  = original.lower()                       # "Digested" version of the message, comprehended so that the bot will understand
    global defPrefix, logStr, log, msg, usr_greetings # Globalizes variables so they can be accessed.

    if log == 1 or log == True:                              # If log is enabled
        logStr = logStr + '\n' + auth_name + ': ' + original # Add latest message to log.

    while len(logStr) >= 1000:   # While the length of the log (string) is greater than or equal to 1000,
        logStr  = logStr[:900]   # Log as string trimmed to 900 characters

    for prefix in prefixes:                                  # For every prefix,

        for i in usr_greetings:                              # For item in usr_greetings:
            if digested.startswith(prefix + i):              # If the message starts with [prefix][item]:
                msg = random.choice(bot_greetings)           # Choose a random choice from the bot's known greetings
                msg = msg + ', ' + '**' + str(author) + '**' # Set reply to "[greeting], [message author]"
                await client.send_message(channel, msg)      # Send message.

        if digested.startswith(prefix + "log"):         # If the message starts with [prefix]log,
            digested = digested.replace(prefix, '')     # Get rid of prefix
            if "off" in digested or '0' in digested:    # If "off" is in the message,
                log = 0                                 # Disable logging.
                msg = "Log disabled"                    # Set message to "Log disabled"
                await client.send_message(channel, msg) # Send message
            elif "on" in digested or '1' in digested:   # Otherwise, if "on" is in the message,
                log = 1                                 # Enable logging.
                msg = "Log enabled"                     # Set message to "Log enabled"
                await client.send_message(channel, msg) # Send message.
            elif "stat" in digested:                    # Otherwise, if "stat" is in the message,
                msg = "Log status: " + str(log)         # Set the status of the logger as the reply
                await client.send_message(channel, msg) # Send a message with the status of the logger
            elif "clear" in digested:                   # Otherwise, if "clear" is in the message,
                logStr  = ''                            # Clear log as string
                msg     = "Log cleared"                 # Set message to "Log cleared"
                await client.send_message(channel, msg) # Send message.
            else:                                       # Otherwise,
                msg    = "```" + logStr + "```"         # Puts log in code format so it's easier to read
                await client.send_message(channel, msg) # Sends specified message.
                
        elif digested.startswith(prefix + "help"): # Otherwise, if the message starts with [prefix]help,
            msg = ("INSERT\n"                      # Put a help message here
                   "HELP\n"
                   "MESSAGE\n"
                   "HERE")
            await client.send_message(channel, msg) # Sends specified message

        elif digested.startswith(prefix + "info"): # Otherwise, if the message starts with [prefix]info,
            msg = ("INSERT\n"                      # Put an info message here
                   "INFO\n"
                   "MESSAGE\n"
                   "HERE")
            await client.send_message(channel, msg) # Sends specified message

        elif digested.startswith(prefix + "set"):          # Otherwise, if message starts with [prefix]set,
            if "prefix " in digested:                      # If "prefix" is also in the message,
                digested  = digested.replace("set", '')    # Get rid of all unnecessary parts of message
                digested  = digested.replace("prefix", '') # Get rid of all unnecessary parts of message
                digested  = digested.replace(prefix, '')   # Get rid of all unnecessary parts of message
                digested  = digested.replace(' ', '')      # Get rid of all unnecessary parts of message
                oldPrefix = defPrefix                      # Save old prefix so it can be removed
                defPrefix = str(digested)                  # Change prefix to what is left of the message
                while oldPrefix in prefixes:               # Until oldPrefix is not in prefixes at all,
                    prefixes.remove(oldPrefix)             # Remove every occurrence of prefixes.
                prefixes.append(defPrefix)                 # Add the (new) default prefix to prefixes
                msg      = "Prefix changed to " + prefix   # Set message to "Prefix changed to [prefix]"
                await client.send_message(channel, msg)    # Send message

        #elif digested.startswith(prefix + "command_name_here"): # Uncomment these lines and add your own custom commands!
        #    msg = "INSERT MESSAGE HERE"                         # Uncomment these lines and add your own custom commands!
        #    await client.send_message(channel, msg)             # Uncomment these lines and add your own custom commands!

# Allows the bot to connect using it's token. Put your token below, leaving it in quotes.
# You can find your bot's token at https://discordapp.com/developers/applications/me/
client.run('token')
