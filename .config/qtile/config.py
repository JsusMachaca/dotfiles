from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Focus apps.
    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
    
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Resize MonadTall
    Key([mod, "control"], "left", lazy.layout.grow()),
    Key([mod, "control"], "right", lazy.layout.shrink()),
    Key([mod], "s", lazy.window.toggle_floating()),
    
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

#                       CUSTOM
    # Rofi
    Key([mod], "d", lazy.spawn("rofi -show drun")),
    
    # Screen Capture
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui")),

    # Audio Control
    Key([], "XF86AudioLowerVolume", lazy.spawn(
            "pactl set-sink-volume @DEFAULT_SINK@ -5%"
        )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
            "pactl set-sink-volume @DEFAULT_SINK@ +5%"
        )),
    Key([], "XF86AudioMute", lazy.spawn(
            "pactl set-sink-mute @DEFAULT_SINK@ toggle"
        )),

    # Brightness Control
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]

groups = [Group(i) for i in [" 󰈹  ", " 󰨞  ", "   ", " 󱙋  ", "   ", "   ",]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
            # Switch to workspace N
            Key([mod], actual_key, lazy.group[group.name].toscreen()),
            # Send window to workspace N
            Key([mod, "shift"], actual_key, lazy.window.togroup(group.name, switch_group=True)),
            Key([mod, "control"], actual_key, lazy.window.togroup(group.name, switch_group=False)),
        ]
    )

layouts = [
    layout.MonadTall(border_focus_stack=["#0f101a", "#0f101a"], border_focus=["#5d5d5d", "#5d5d5d"], border_width=1, margin=7),
    layout.MonadWide(border_focus_stack=["#0f101a", "#0f101a"], border_focus=["#5d5d5d", "#5d5d5d"], border_width=1, margin=7),
    layout.Max(border_focus_stack=["#0f101a", "#0f101a"], border_focus=["#5d5d5d", "#5d5d5d"], border_width=0),
]

widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
#       WIDGETS ARCH LOGO    .
                widget.TextBox(
                    text='   ',
                    #foreground=["#ff0055", "#ff0055"],
                    foreground=["#d8dee9", "#d8dee9"],
                    background=["#0f101a", "#0f101a"],
                    fontsize=22,
                ),

                widget.Sep(
                    foreground=["#f1ffff", "#f1ffff"],
                ),

                widget.Spacer(
                    length=20,
                    background=["#0f101a", "#0f101a"],
                ),

#       WIDGETS GROUPS     .
                widget.GroupBox(
                    foreground=["#f1ffff", "#f1ffff"],
                    background  =["#0f101a", "#0f101a"],
                    font='UbuntuMono Nerd Font',
                    fontsize=20,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=["#f1ffff", "#f1ffff"],
                    inactive=["#525050", "#525050"],
                    rounded=False,
                    highlight_method='block',
                    #this_current_screen_border=["#f07178", "#f07178"],
                    this_current_screen_border=["#2c2c36", "#2c2c36"],
                    this_screen_border=["#5c5c5c", "#5c5c5c"],
                    other_current_screen_border=["#0f101a", "#0f101a"],
                    other_screen_border=["#0f101a", "#0f101a"],
                ),

                widget.WindowName(
                    #foreground=["#f07178", "#f07178"],

                    foreground=["#4c566a", "#4c566a"],
                    background=["#0f101a", "#0f101a"],
                ),

                widget.Sep(
                    background=["#0f101a", "#0f101a"],
                    foreground=["#0f101a", "#0f101a"],
                ),


#                                   WIDGETS RIGHT BAR                 .

#       WIDGETS UPDATES     .
                widget.TextBox(
                    text="󱈙 ",
                    padding=-10.5,
                    fontsize=37,
                    #foreground=["#0f101a", "#0f101a"],
                    #background=["#ffd47e", "#ffd47e"],
                    
                    foreground=["#0f101a", "#0f101a"],
                    background=["#1f223b", "#1f223b"],
                ),

                widget.TextBox(
                    text=" ",
                    #foreground=["#000000", "#000000"],
                    #background=["#ffd47e", "#ffd47e"],

                    foreground=["#d8dee9", "#d8dee9"],
                    background=["#1f223b", "#1f223b"],
                ),

                widget.CheckUpdates(
                    #foreground=["#000000", "#000000"],
                    #background=["#ffd47e", "#ffd47e"],

                    foreground=["#d8dee9", "#d8dee9"],
                    background=["#1f223b", "#1f223b"],

                    display_format='{updates}',
                    colour_have_updates=["#d8dee9", "#d8dee9"],
                    custom_command='checkupdates',
                    update_interval=2400,
                ),


#       WIDGETS MEMORY   .
                widget.TextBox(
                    text="󱈙 ",
                    padding=-12,
                    fontsize=37,
                    #foreground=["#ffd47e", "#ffd47e"],
                    #background=["#f07178", "#f07178"],

                    foreground=["#1f223b", "#1f223b"],
                    background=["#1b1b25", "#1b1b25"],
                ),

                widget.TextBox(
                    text='󰍛 ',
                    #foreground=["#000000", "#000000"],
                    #background=["#f07178", "#f07178"],

                    foreground=["#d8dee9", "#d8dee9"],
                    background=["#1b1b25", "#1b1b25"],
                ),

                widget.Memory(
                    format="{MemUsed:.0f}{mm} / {MemTotal:.0f}{mm}",
                    #foreground=["#000000", "#000000"],
                    #background=["#f07178", "#f07178"],

                    foreground=["#d8dee9", "#d8dee9"],
                    background=["#1b1b25", "#1b1b25"],
                ),

                widget.Sep(
                    #foreground=["#f07178", "#f07178"],
                    #background=["#f07178", "#f07178"],

                    foreground=["#1b1b25", "#1b1b25"],
                    background=["#1b1b25", "#1b1b25"],
                ),

#       WIDGETS LAYOUT    .
                widget.TextBox(
                    text="󱈙 ",
                    padding=-12,
                    fontsize=37,
                    #foreground=["#f07178", "#f07178"],
                    #background=["#ff0055", "#ff0055"],

                    foreground=["#1b1b25", "#1b1b25"],
                    background=["#283144", "#283144"],
                ),

                widget.CurrentLayoutIcon(
                    scale = 0.6,
                    #background=["#ff0055", "#ff0055"],

                    background=["#283144", "#283144"],
                ),

                widget.CurrentLayout(
                    #foreground=["#000000", "#000000"],
                    #background=["#ff0055", "#ff0055"],

                    foreground=["#d8dee9", "#d8dee9"],
                    background=["#283144", "#283144"],
                ),

#       WIDGETS CLOCK   . 
                widget.TextBox(
                    text="󱈙 ",
                    padding=-12,
                    fontsize=37,
                    #foreground=["#ff0055", "#ff0055"],
                    #background=["#b900ff", "#b900ff"],

                    foreground=["#283144", "#283144"],
                    background=["#1c2332", "#1c2332"],
                ),

                widget.TextBox(
                    text='󰃰 ',
                    #foreground=["#000000", "#000000"],
                    #background=["#b900ff", "#b900ff"],

                    foreground=["#d8dee9", "#d8dee9"],
                    background=["#1c2332", "#1c2332"],
                ),

                widget.Clock(
                    format="%d/%m/%Y ",
                    #foreground=["#000000", "#000000"],
                    #background=["#b900ff", "#b900ff"],

                    foreground=["#d8dee9", "#d8dee9"],
                    background=["#1c2332", "#1c2332"],
                ),

                widget.Sep(
                    #foreground=["#000000", "#000000"],
                    #background=["#b900ff", "#b900ff"],

                    foreground=["#d8dee9", "#d8dee9"],
                    background=["#1c2332", "#1c2332"],
                ),

                widget.Clock(
                    format=" %I:%M %p",
                    #foreground=["#000000", "#000000"],
                    #background=["#b900ff", "#b900ff"],

                    foreground=["#d8dee9", "#d8dee9"],
                    background=["#1c2332", "#1c2332"],
                ),

                widget.Sep(
                    #foreground=["#b900ff", "#b900ff"],
                    #background=["#b900ff", "#b900ff"],

                    foreground=["#1c2332", "#1c2332"],
                    background=["#1c2332", "#1c2332"],
                ),

#       WIDGETS SYSTRAY   
                widget.TextBox(
                    text="󱈙 ",
                    padding=-11,
                    fontsize=37,
                    #foreground=["#b900ff", "#b900ff"],
                    #background=["#0f101a", "#0f101a"],

                    foreground=["#1c2332", "#1c2332"],
                    background=["#0f101a", "#0f101a"],
                ),
                
                widget.Systray(
                    background=["#0f101a", "#0f101a"],
                ),
            ],
            21,
            opacity=0.99,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False 
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="Pavucontrol"), # Pantalla de control de audio
        Match(wm_class="Lightdm-gtk-greeter-settings"), # Configuración de Lightdm
        Match(wm_class="Lxappearance"), # Configuración de temas
        Match(wm_class="Nitrogen"), # Configuracion de fondos de pantalla
    ],
    border_focus="#5d5d5d",
    border_width=1,
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
