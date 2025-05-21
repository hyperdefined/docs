---
title: "SimplePlayTime/Configuration"
---
How to configure SimplePlayTime.

## `afk-timeout`
Set how long a player must be AFK for in order to not count playtime. This time is in seconds.

## `messages`
{{ minimessage_info() }}
Here you can change the format of the messages.

- `players-only` - Set the "this command is for players only" message.
- `playtime-start` - When a new player joins the server, send them this message. This is used to tell them their playtime is being tracked.
- `playtime-command` - When a player uses `/playtime`. Use `%days%`, `%hours%`, `%minutes%`, and `%seconds%` for placeholders.