---
title: "TimeBar/RealisticSeasons Support"
---
!!! danger "Warning"
    You must use RealisticSeasons version 10.5.1+ due to API changes.

TimeBar supports [RealisticSeasons](https://www.spigotmc.org/resources/93275/). This configuration file will only appear if you have the plugin installed. The support is still very new, so things might not work correctly!

!!! info "Information"
    Any option that is also present in `config.yml` will be overridden by whatever is set here.

## `use-24h-format`
Set if you wish to use 24hr time formatting of the title.

## `timebar-title`
{{ minimessage_info() }}

Set what text appears above the TimeBar. You can use some formatting codes to customize it even more:

- `{TIME}` - The current world time, 7:20 am, etc.
- `{TIME-WORD}` - The time to display. Dawn, afternoon, etc.
- `{DAYCOUNT}` - How many total days in game have passed.
- `{DAYPERCENT}`- Percentage of day completion.
- `{SEASON}` - The current season.
- `{DATE}` - The current date.
- `{DAY}` - The current day.
- `{MONTH}` The current month.

## `date-format`
This lets you choose how dates are formatted. The default option is Month/Day/Year. If you wish to change it, refer to [this chart](https://www.digitalocean.com/community/tutorials/java-simpledateformat-java-date-format#java-simpledateformat) for formatting codes.

- `M/dd/yyyy`
- `dd/MM/yyyy`

## `times`
Set time of day wording.
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

## `month`
Set the time of days for each month. Because each month is different in time, you can adjust them here. These are set in 24hr time. **Make sure to use 2 digits for hours and minutes (don't use 7 for 7am, use 07).**

The `name` option for each month is how that month is displayed using the `{MONTH}` placeholder. The `title` option will allow you to set a title for that month only. You can use the placeholders above also. You can add the `title` option to each month to do this.
```yaml
month:
  january:
    name: "January"
    dawn: "06:00"
    morning: "08:30"
    noon: "12:00"
    afternoon: "15:00"
    sunset: "16:30"
    night: "18:30"
    midnight: "00:00"
    #title: "This title will show in January only."
  february:
    name: "February"
    dawn: "05:25"
    morning: "08:00"
    noon: "12:00"
    afternoon: "15:35"
    sunset: "17:00"
    night: "18:50"
    midnight: "00:00"
    #title: "This title will show in February only."
  march:
    name: "March"
    dawn: "05:00"
    morning: "07:30"
    noon: "12:00"
    afternoon: "16:00"
    sunset: "17:45"
    night: "19:15"
    midnight: "00:00"
  april:
    name: "April"
    dawn: "04:30"
    morning: "07:00"
    noon: "12:00"
    afternoon: "16:30"
    sunset: "18:20"
    night: "19:45"
    midnight: "00:00"
  may:
    name: "May"
    dawn: "04:00"
    morning: "06:30"
    noon: "12:00"
    afternoon: "17:00"
    sunset: "18:55"
    night: "20:05"
    midnight: "00:00"
  june:
    name: "June"
    dawn: "03:35"
    morning: "06:00"
    noon: "12:00"
    afternoon: "17:30"
    sunset: "19:30"
    night: "20:30"
    midnight: "00:00"
  july:
    name: "July"
    dawn: "03:10"
    morning: "05:30"
    noon: "12:00"
    afternoon: "18:00"
    sunset: "20:00"
    night: "21:00"
    midnight: "00:00"
  august:
    name: "August"
    dawn: "03:35"
    morning: "06:00"
    noon: "12:00"
    afternoon: "17:30"
    sunset: "19:30"
    night: "20:30"
    midnight: "00:00"
  september:
    name: "September"
    dawn: "04:00"
    morning: "06:30"
    noon: "12:00"
    afternoon: "17:00"
    sunset: "18:55"
    night: "20:05"
    midnight: "00:00"
  october:
    name: "October"
    dawn: "04:30"
    morning: "07:00"
    noon: "12:00"
    afternoon: "16:30"
    sunset: "18:20"
    night: "19:45"
    midnight: "00:00"
  november:
    name: "November"
    dawn: "05:00"
    morning: "07:30"
    noon: "12:00"
    afternoon: "16:00"
    sunset: "17:45"
    night: "19:15"
    midnight: "00:00"
  december:
    name: "December"
    dawn: "05:30"
    morning: "08:00"
    noon: "12:00"
    afternoon: "15:35"
    sunset: "17:00"
    night: "18:50"
    midnight: "00:00"
```