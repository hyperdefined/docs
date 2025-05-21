---
title: "hyperMOTD/Configuration"
---
How to configure hyperMOTD.

## `type`
Set which mode the MOTD should use. Type can either be `fixed` or `random`.

`fixed` will only show the `fixed-motd`. `random` will pick a MOTD from the `random-motd` list.

## `fixed-motd`
{{ minimessage_info() }}
Used in `fixed` mode.

## `random-motd`
{{ minimessage_info() }}
Used in `random` mode.

## `use-custom-icon`
Use a custom server icon. If set to `true`, place the icon in the `hyperMOTD` folder.

## `custom-icon-filename`
Set the custom server icon file name.