---
title: "AutoWhitelistRemove/Configuration"
---
How to configure AutoWhitelistRemove.

## `inactive-period`
Set how long a player has to be offline in order to be removed from the whitelist. This option has a specific format.

- `<number><time duration>`

Time durations:

- `w` - weeks
- `d` - days
- `m` - months

Examples: `30d`, `2w`, `1m`

## `extra-commands`
Run the commands in order when we remove a player.

- `%player%` - player's name. Might not be accurate if they changed their name since they were online.
- `%uuid%` - player's UUID.

## `autoremove-on-start`
Do you want to automatically remove inactive players from the whitelist when the server starts? If you set this to false, you must manually do `/awr check` to remove inactive players.

## `save-whitelist-removals`
When we remove players, should we save who we removed to a file? This helps you later down the line if you want to re-add players and forgot who was removed. This saves to `removals.json`.