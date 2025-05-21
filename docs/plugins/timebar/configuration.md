---
title: "TimeBar/Configuration"
---
How to configure TimeBar.

## `worlds`
Set which worlds track time and which worlds display those times.
```yaml
# Set which worlds track time and which worlds show that time.
worlds:
  # Set a TimeBar for "world".
  world:
    # Display the TimeBar for "world" in these worlds below.
    - world
    - world_nether
    - world_the_end
  # Set a TimeBar for "world2".
  world2:
    # Display the TimeBar for "world2" in these worlds below.
    - world2
    - world2_nether
    - world2_the_end
```
If you have multiple worlds on your server, you can define multiple TimeBars.

## `titlebar-color`
Set what color the TimeBar should be. These are the colors it supports:

- `blue`
- `green`
- `pink`
- `purple`
- `red`
- `white`
- `yellow`

## `timebar-title`
{{ minimessage_info() }}

Set what text appears above the TimeBar. You can use some formatting codes to customize it even more:

- `{TIME}` - Display the time of day. Dawn, afternoon, etc.
- `{DAYCOUNT}` - Display how many days have passed in the world the TimeBar tracks time in.
- `{DAYPERCENT}`- Percentage of day completion.

## `bar-update-frequency`
How often should the title update. This uses ticks, 20 ticks = 1 second.

## `hold-clock-to-show`
Instead of the TimeBar always showing 100% of the time (unless turned off), this requires players to hold a clock in order for it to show. If they stop holding a clock, it disappears. This is a more vanilla style option.

## `times`
Set the time of day wording.
```yaml
times:
  dawn: "Dawn"
  morning: "Morning"
  noon: "Noon"
  afternoon: "Afternoon"
  sunset: "Sunset"
  night: "Night"
  midnight: "Midnight"
```

## `times-of-day`
Set when each time of day happens. This is in game ticks. You can see by using `/time query daytime`.
```yaml
times-of-day:
  dawn: 23000
  morning: 1000
  noon: 6000
  afternoon: 10500
  sunset: 12250
  night: 13800
  midnight: 18000
```