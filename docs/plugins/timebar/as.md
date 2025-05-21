---
title: "TimeBar/AdvancedSeasons Support"
---
TimeBar supports [AdvancedSeasons](https://www.spigotmc.org/resources/114050/). This configuration file will only appear if you have the plugin installed. The support is still very new, so things might not work correctly!

!!! info "Information"
    Any option that is also present in `config.yml` will be overridden by whatever is set here.

## `timebar-title`
{{ minimessage_info() }}

Set what text appears above the TimeBar. You can use some formatting codes to customize it even more:

- `{TIME}` - Display the time of day. Dawn, afternoon, etc. These names are pulled from the main TimeBar config.
- `{DAYCOUNT}` - Display how many days have passed in the world the TimeBar tracks time in.
- `{DAYPERCENT}`- Percentage of day completion.
- `{SEASON}` - The current season.
- `{TEMP}` - The temperature of the player.

## `seasons`
Change how each season is displayed.

## `colors`
Change the color of the TimeBar for each season.