# Discord and Dice

## Dice rolling and play assitance for Dungeons and Dragons in Discord

## Overview

This version only supports dice rolling in response to requests in discord.

All commands must be prefaced with ! for the bot to response to them.  This is configurable in bot-main.py as command prefix.

Commands supported at this time are:

- !roll  -  rolls dice in XdY+Z formate
- !advantage - rolls 2d20 and takes the higher
- !disadvantage - rolls 2d20 and takes the lower
- !showcontext - shows discord context of input

All of the commands can return more detailed help and examples, by calling them with help as an argument.

## Running

As pushed to git it is designed to be run on Heroku with the ENV variables.  Those are:

- KEY='key string from discord api'
- CHANNELS=['general','dnd']
- DM="DungeonMaster#1234"
- CONTENT="remote/url/"

They KEY is the API bot key from discord.

Channels is a list of channels the bot will respond on.

DM is the discord ID of the dungeon master.  Not used at this time.

Content is the URL where external content can be loaded from.  Not used at this time.

### Running locally

To run locally, create a .env file in the local directory with the 4 required environmental variables.  And uncomment the load dotenv commands in bot-main.py
