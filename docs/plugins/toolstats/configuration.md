---
title: "ToolStats/Configuration"
---
How to configure ToolStats.

## `tokens`
See [Token System](tokens.md).

## `enabled`
This section is used to enable/disable which data gets tracked on each item. It's best if you test the plugin and decide which data you do not want.

- `crafted-by`: This tag is used for tracking who crafts any tool/armor pieces.
- `crafted-date`: This tag is used for tracking when someone crafts any tool/armor piece.
- `fished-by`: This tag is used for tracking who fishes any tool/armor piece.
- `fished-on`: This tag is used for tracking when someone fishes any tool/armor piece.
- `looted-by`: This tag is used for tracking who loots any tool/armor piece from an unlooted chest.
- `looted-on`: This tag is used for tracking when someone loots any tool/armor piece from an unlooted chest.
- `traded-by`: This tag is used for tracking who trades any tool/armor piece from a villager.
- `traded-on`: This tag is used for tracking when someone trades any tool/armor piece from a villager.
- `damage-done`: This tag is used for tracking how much damage a weapon has done.
- `player-kills`: This tag is used for tracking player kills on weapons.
- `mob-kills`: This tag is used for tracking mob kills on weapons.
- `blocks-mined`: This tag is used for tracking blocks mined on various tools.
- `fish-caught`: This tag is used for tracking how many successful catches from a fishing rod.
- `sheep-sheared`: This tag is used for tracking how many sheep were sheared from shears.
- `armor-damage`: This tag is used for tracking damage taken with armor.
- `dropped-by`: This tag is used for tracking where a tool/armor piece drops from.
- `dropped-on`: This tag is used for tracking when a tool/armor piece drops from a mob.
- `elytra-tag`: This tag is used for finding new Elytras in end cities.
- `arrows-shot`: This tag is used for tracking arrows shot from bows/crossbows.
- `flight-time`: This tag is used for tracking elytra flight time.
- `crops-harvested`: This tag is used for tracking how many crops are broken with a hoe.

## `messages`
This section let's you set how the lore is displayed on the items.

Each section is easy to understand. Make sure to keep the placeholder codes in order for the lore to show correctly. Some placeholders cannot be used for other sections.

!!! danger "Warning"
    You should set these values **once**. The plugin tries to match this lore in order to update it on items. If you change it, it will fail to match resulting in duplicate lore.

    It's highly recommended to test what format works best before using on a production server.

!!! info "Information"
    These messages support either legacy formatting codes (using `&`) and [MiniMessage](https://docs.advntr.dev/minimessage/format.html).

- `{player}`: Player's name.
- `{date}`: The date of that action.
- `{fish}`: The total caught fish.
- `{kills}`: The total mob/player kills.
- `{blocks}`: The total blocks mined.
- `{sheep}`: The total of sheep sheared.
- `{name}`: Player/mob name.
- `{damage}`: The total damage taken.
- `{crops}`: The total crops mined.
- `{arrows}`: The total arrows shot.
- `{years}`/`{months}`/`{days}`/`{hours}`/`{minutes}`/`{seconds}`: Time for elytra flight.

## `date-format`
This lets you choose how dates are formatted. The default option is Month/Day/Year. If you wish to change it, refer to [this chart](https://www.digitalocean.com/community/tutorials/java-simpledateformat-java-date-format#java-simpledateformat) for formatting codes.

- `dd/MM/yyyy` - Day/Month/Year
- `M/dd/yyyy` - Month/Day/Year

## `number-formats`
If you ever want to change how numbers are formatted, you can do it here. **You probably do not need to change this.**

## `generate-hash-for-items`
When items are created (only items we want to track), we can add a hash to the item. Right now, this does not have a purpose. However, it can be used in the future to detect duplication glitches.

## `normalize-time-creation`
This forces item creation times to be set at 12:00 AM on the day. This means 2 items created on the same day but hours apart will have the exact same creation time (same day at midnight). This is used to "normalize" creation dates for better compatibility.

## `allow-creative`
Allow stats and origin tracking if you are in creative mode.