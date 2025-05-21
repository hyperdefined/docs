---
title: "AutoWhitelistRemove/Commands"
---
These are all commands used by AutoWhitelistRemove.

## `/awr help`
Permission: `autowhitelistremove.command`

Shows the help menu.

## `/awr ignore`
Permission: `autowhitelistremove.ignore`

Allows you to add/remove ignored players from being removed (see the list in the config). You can specify UUIDs or player names.
```
/awr ignore add hyperdefined
/awr ignore add 311be5cd-d17c-49b3-bf47-f781fdbcc929
/awr ignore remove hyperdefined
/awr ignore remove 311be5cd-d17c-49b3-bf47-f781fdbcc929
```

## `/awr check`
Permission: `autowhitelistremove.check`

This will check all whitelisted players and see who would be removed.

## `/awr check confirm`
Permission: `autowhitelistremove.check.confirm`

This will actually remove the players from the whitelist.

## `/awr reload`
Permission: `autowhitelistremove.reload`

Reloads the configuration.