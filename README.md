# deltabot
# MOVED TO ![https://gitlab.com/keeganjk/deltabot]("https://gitlab.com/keeganjk/deltabot") !
[![Donate](https://img.shields.io/badge/donate-%24-green.svg)](https://keeganjk.github.io/donate/)

![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg) ![Stable v1.0](https://img.shields.io/badge/stable-v1.0-orange.svg)

```
    //\\      ___   ___ .    _____   .    ___   ___  _____
   //  \\    |   \ |    |      |    / \  |   \ /   \   |
  //    \\   |   | |__  |      |   /   \ |___/ |   |   |
 //      \\  |   | |    |      |   |---| |   \ |   |   |
,,========`` |___/ |___ |___   |   |   | |___/ \___/   |
```

Simple Discord bot that's easy to understand and change, modify as you wish!

### Supported platforms:
>  Windows

>  MacOS

>  Linux
### Requirements:
>  Web browser

>  [Python 3.6](https://www.python.org/downloads "Python 3.6") (If on macOS, you will need to run `Applications/Python 3.6/Install Certificates.command`)

>  [discord.py](https://github.com/Rapptz/discord.py "discord.py") (If on Windows, you will need to use `C:/Python36/scripts/pip install discord.py` in CMD)

## Contents
- [What is it?](#what-is-it)
- [How to use it](#how-to-use)
  - [Download](#dl)
  - [Extract files](#extract)
  - [Registering the bot](#reg)
  - [Adding token](#token)
  - [Adding to server](#add)
  - [Editing the bot](#edit)
 - [Defaults](#defs)
 - [Credits](#credits)

## What is it? (#what-is-it)
Deltabot is a simplistic [Discord](discordapp.com "Discord") bot that only offers a few features and allows you to change it to your desire. It is made simply for the purpose of people to make their own bots to do anything they want. The basics come pre-coded, so all you need to do is add what you want. Delta (Δ) is a Greek character that represents change in mathematics. This bot is called Deltabot because you are supposed to change it.
## How to use it (#how-to-use)
> ### 1. Download (#dl)
> Firstly, on any OS, you would navigate to https://github.com/keeganjk/deltabot. Once on this page, click the button that says "Clone or Download" and then "Download as ZIP".
>

> ![Clone or Download](https://github.com/keeganjk/deltabot/blob/master/images/download.gif?raw=true "")
>

> If you are on Unix (Linux, macOS, or BSD), you can type `git clone https://github.com/keeganjk/deltabot` into the terminal to
> clone this repository and then `mv` into the directory. If you do this, skip to step 3.

---


> ### 2. Extract files (#extract)
> Nextly, extract the ZIP file and then move into the `deltabot` folder.



---


> ### 3a. Register the bot (#reg)
> In your web browser, navigate to [https://discordapp.com/developers/applications/me](https://discordapp.com/developers/applications/me).
> Click "New App".
> Next, give it a name and a description if you'd like.
> Click "Create Bot User" to turn the application into a bot and then confirm it with "Yes, do it!".
> You can select "Public Bot" to make anyone able to add your bot to their server or leave it unchecked so it can only be used with your servers.
> To save your bot, select "Save Changes".
> ![Bot Registration](https://raw.githubusercontent.com/keeganjk/deltabot/master/images/create-bot.gif "")

---


> ### 3b. Add your token (#token)
> On your bot's page, scroll down to "App Bot User" and click "click to reveal" next to "Token:" to reveal your token.
> Copy your token.
> Open `deltabot.py` in a text editor and scroll down to the bottom.
> On the last line, `client.run('token')`, replace `token` with your bot's token, leaving it in quotes.
> ![Adding token](https://raw.githubusercontent.com/keeganjk/deltabot/master/images/token.gif "")

> ### 3c. Adding your bot to a server (#add)
> To add your bot to a server, you would use this link: https://discordapp.com/api/oauth2/authorize?client_name=CLIENTIDHERE&scope=bot&permissions=1, but you have to get your Client ID.
> There are two ways of doing this:
> (easiest) 1. Run `deltabot.py`, an authorization link will instantly be generated that you can go to to add your bot to a server.
> (second easiest) 2. Run `deltabot.py`, copy the Client ID and then use the link https://discordapp.com/api/oauth2/authorize?client_name=CLIENTIDHERE&scope=bot&permissions=1, but replace CLIENTIDHERE with your Client ID.
> (least easy) 3. Go to your bot's page at [href="https://discordapp.com/developers/applications/me](https://discordapp.com/developers/applications/me). Scroll down until you see your bot's Client ID. Copy it, replace CLIENTIDHERE in the link with your Client ID.

---


> ### (optional) 3d. Editing your bot (#edit)
> In your text editor, you can edit your bot. There is already a part near the bottom you can un-comment (remove the `#`s from the beginning) and add custom parameters, text, etc.
> You can customize your bot however you'd like!
> Good luck!

---
---


> ### Defaults: (#defs)
>
> ```
>
> Default prefix       : !! or @botname  or @botname#....
>
> Default commands     :
>
> hi, hey, hello, etc. : bot responds to greeting (from list of greetings (usr_greetings))
>
> log.                 : shows log
>
> log on/1/off/0       : enables/disables log
>
> log stat             : shows log status (enabled/disabled)
>
> log clear            : clears log
>
> help                 : displays custom help message
>
> info                 : displays custom info message
>
> set prefix [prefix]  : changes default prefix to a prefix of your choice

> ```

## Credits (#credits)
[Discord](https://discordapp.com "Discord"), Discord Developers

[discord.py](https://github.com/Rapptz/discord.py "discord.py"), [Rapptz](https://github.com/Rapptz "Rapptz")
