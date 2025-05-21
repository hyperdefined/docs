---
title: "ToolStats/Commands"
---
These are all commands used by ToolStats.

## `/toolstats reset`
Permission: `toolstats.reset`

Allows the player to reset their tool's lore if it's incorrect. This will remove all lore and re-apply it based on the stats/origin of the held item.

## `/toolstats reset confirm`
Permission: `toolstats.reset.confirm`

Confirm the reset command.

## `/toolstats reload`
Permission: `toolstats.reload`

Reloads the configuration.

## `/toolstats givetokens`
Permission: `toolstats.givetokens`

Usage: `/toolstats givetokens <player> <token-type> <amount>`

Used for giving players tokens. If no amount is specified, only 1 will be given.

## `/toolstats edit`
Permission: `toolstats.edit`

Usage: `/toolstats edit <stat> <new-value>`

Edit the stat of an item. You must be holding the item and the item must have the stat tracked already.

## `/toolstats remove`
Permission: `toolstats.remove`

Usage: `/toolstats remove <stat>`

Remove the stat of an item.