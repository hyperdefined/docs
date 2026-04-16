---
title: "VelocityBlockVersion/Configuration"
---
How to configure VelocityBlockVersion.

## `mode`
Set the mode for the plugin. This can either be `whitelist` or `blacklist`.

* `whitelist` - Versions on the list CAN join. Versions not on the list are blocked.
* `blacklist` - Versions on the list CAN NOT join. Versions not on the list CAN join.

## `versions`
This is the list of versions to either whitelist/blacklist. You must use the protocol version.

You can see a list of these [here](https://minecraft.wiki/w/Protocol_version).

## `disconnect_message`
{{ minimessage_info() }}
Show this message if a player tries to connect with a version that is blocked.
Use `<versions>` in this message to display which versions your server supports.

## `log_connection_versions`
Enable/disable logging which versions player connect with. This is used for debug mainly. This is off by default so your console won't get spammed.