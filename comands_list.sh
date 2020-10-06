#!/bin/bash

cat bot.py | egrep -oE "@bot.command\(name=.*[a-z]" | sed "s/^@bot.command(name=\|name)/\!/" | sed "s/'\|\!name//" > files/commands.txt

exit 0