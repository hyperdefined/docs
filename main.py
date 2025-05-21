# macros/main.py
def define_env(env):
    @env.macro
    def minimessage_info():
        return '''!!! info "Information"
    This uses MiniMessage to format colors and display (does not use &). You can read more about it [here](https://docs.adventure.kyori.net/minimessage/format.html) and use a visual tool [here](https://webui.adventure.kyori.net/).
'''
