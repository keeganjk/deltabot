# deltabot
[![Donate](https://img.shields.io/badge/donate-%24-green.svg)](https://keeganjk.github.io/donate/) <br />
![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg) ![Stable v1.0](https://img.shields.io/badge/stable-v1.0-orange.svg) <br />
~~~
    //\\      ___   ___ .    _____   .    ___   ___  _____
   //  \\    |   \ |    |      |    / \  |   \ /   \   |
  //    \\   |   | |__  |      |   /   \ |___/ |   |   |
 //      \\  |   | |    |      |   |---| |   \ |   |   |
,,========`` |___/ |___ |___   |   |   | |___/ \___/   |
~~~

Simple Discord bot that's easy to understand and change, modify as you wish! 

### Supported platforms:
> <h5>Windows</h5>
> <h5>MacOS</h5>
> <h5>Linux</h5>
### Requirements:
> <h5>Web browser</h5>
> <h5><a href="https://www.python.org/downloads/">Python 3.6+</a> (If on macOS, you will need to run <code>Applications/Python 3.6/Install Certificates.command</code>)</h5>
> <h5><a href="https://github.com/Rapptz/discord.py">discord.py</a> (If on Windows, you will need to use <code>C:/Python36/scripts/pip install discord.py</code> in CMD)</h5>

## Contents
- [What is it?](#what-is-it)
- [How to use it](#how-to-use)
  - [Download](#dl)
  - [Extract files](#extract)
  - [Registering the bot](#reg)
  - [Adding token](#token)
  - [Adding to server](#add)
  - [Editing the bot](#edit)
 - [Credits](#credits)

## What is it? <a id="what-is-it">
Deltabot is a simplistic <a href="discordapp.com">Discord</a> bot that only offers a few features and allows you to change it to your desire. It is made simply for the purpose of people to make their own bots to do anything they want. The basics come pre-coded, so all you need to do is add what you want. Delta (Δ) is a Greek character that represents change in mathematics. This bot is called Deltabot because you are supposed to change it.
## How to use it <a id="how-to-use">
> ### 1. Download <a id="dl">
> Firstly, on any OS, you would navigate to https://github.com/keeganjk/deltabot. Once on this page, click the button that says "Clone or Download" and then "Download as ZIP".
> <br />
> ![Clone or Download](https://github.com/keeganjk/deltabot/blob/master/images/download.gif?raw=true "")
> <br />
> If you are on Unix (Linux, macOS, or BSD), you can type <code>git clone https://github.com/keeganjk/deltabot</code> into the terminal to 
> clone this repository and then <code>mv</code> into the directory. If you do this, skip to step 3.

<hr>

> ### 2. Extract files <a id="extract">
> Nextly, extract the ZIP file and then move into the <code>deltabot</code> folder. <br/><br/>

<hr>

> ### 3a. Register the bot <a id="reg">
> In your web browser, navigate to <a href="https://discordapp.com/developers/applications/me">https://discordapp.com/developers/applications/me</a>.
> Click "New App". 
> Next, give it a name and a description if you'd like.
> Click "Create Bot User" to turn the application into a bot and then confirm it with "Yes, do it!".
> You can select "Public Bot" to make anyone able to add your bot to their server or leave it unchecked so it can only be used with your servers.
> To save your bot, select "Save Changes".
> ![Bot Registration](https://raw.githubusercontent.com/keeganjk/deltabot/master/images/create-bot.gif "")

<hr>

> ### 3b. Add your token <a id="token">
> On your bot's page, scroll down to "App Bot User" and click "click to reveal" next to "Token:" to reveal your token.
> Copy your token.
> Open `deltabot.py` in a text editor and scroll down to the bottom.
> On the last line, `client.run('token')`, replace `token` with your bot's token, leaving it in quotes.
> ![Adding token](https://raw.githubusercontent.com/keeganjk/deltabot/master/images/token.gif "")

> ### 3c. Adding your bot to a server <a id="add">
> To add your bot to a server, you would use this link: https://discordapp.com/api/oauth2/authorize?client_id=CLIENTIDHERE&scope=bot&permissions=1, but you have to get your Client ID. 
> There are two ways of doing this:
> (easiest) 1. Run `deltabot.py`, an authorization link will instantly be generated that you can go to to add your bot to a server.
> (second easiest) 2. Run `deltabot.py`, copy the Client ID and then use the link https://discordapp.com/api/oauth2/authorize?client_id=CLIENTIDHERE&scope=bot&permissions=1, but replace CLIENTIDHERE with your Client ID.
> (least easy) 3. Go to your bot's page at <a href="https://discordapp.com/developers/applications/me">https://discordapp.com/developers/applications/me</a>. Scroll down until you see your bot's Client ID. Copy it, replace CLIENTIDHERE in the link with your Client ID.

<hr>

> ### (optional) 3d. Editing your bot <a id="edit">
> In your text editor, you can edit your bot. There is already a part near the bottom you can un-comment (remove the `#`s from the beginning) and add custom parameters, text, etc.
> You can customize your bot however you'd like!
> Good luck!

## Credits <a id="credits">
[Discord](https://discordapp.com "Discord"), Discord Developers
[discord.py](https://github.com/Rapptz/discord.py "discord.py"), [Rapptz](https://github.com/Rapptz "Rapptz")
