---
title: "CustomLauncherRewrite/Uninstall"
description: "CustomLauncherRewrite is a custom launcher for Toontown Rewritten written in Java."
---
It's recommended to first migrate things over if you go back to the official launcher. This includes:

- Screenshots
- Game settings
- Resource packs

If you want to migrate, follow these steps. Otherwise skip this section.

1. Install the official TTR launcher. If you did not change the install directory, head over to `C:\Program Files (x86)\Toontown Rewritten`. If you did, head over to that location instead.
2. Copy these files from `ttr-files` to `C:\Program Files (x86)\Toontown Rewritten`. Replace any files.
    - `settings.json` - This file holds your settings.
    - `resources` - This folder holds your resource packs.
    - `screenshots` - This folder holds your screenshots.

## Windows
Simply delete your CustomLauncherRewrite folder, that is all! No other steps are needed.

## Linux
Open up a terminal and run this command:
```
curl -s https://raw.githubusercontent.com/hyperdefined/CustomLauncherRewrite/master/linux/uninstaller.sh | bash
```
Running random scripts on the internet is scary, please double check this script before running! This script will handle the uninstallation.