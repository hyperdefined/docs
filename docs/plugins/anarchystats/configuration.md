---
title: "AnarchyStats/Configuration"
---
How to configure AnarchyStats.

## `info-command-override`
Allows you to change the command to something else. If another plugin uses `/info`, you can change the command here so they do not overlap.

Requires a full server restart.

## `date`
The date your server started.

Must be formatted: `MM/DD/YYYY`.

You must include zeros for single digits. Example: 06, 02, 01, etc. For example, do not do `5/27/2019`. You would instead use `05/27/2019`. Notice the zero filling in the gap.

## `date-format`
This lets you choose how dates are formatted. The default option is Month/Day/Year. If you wish to change it, refer to [this chart](https://www.digitalocean.com/community/tutorials/java-simpledateformat-java-date-format#java-simpledateformat) for formatting codes.

- `M/dd/yyyy`
- `dd/MM/yyyy`

## `worlds-to-use`
These are the worlds that will be included in the world size calculation. You shouldn't need to change this if you don't have any other worlds or did not change the default name. For the few people out there, you can change the world names here. You can also add more if you have more worlds.

## `command-message`
{{ minimessage_info() }}
Change the command’s format here. There are some keywords to use.

- `{{STARTDATE}}` – Shows the formatted start date.
- `{{DAYS}}` – Shows how many days passed since the start date.
- `{{WORLDSIZE}}` – Shows the world size.
- `{{TOTALJOINS}}` – Shows total unique joins.

## `use-permission-node`
Do you want the command to require certain permissions to run? Set this to `true` if so.

## `permission-node`
If you wish to require certain permissions to run the command, set the permission node here. You shouldn't need to change this, but you can. Whatever is set here is what you give to players.