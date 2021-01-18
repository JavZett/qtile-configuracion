from libqtile import widget
from settings.theme import colors

base = lambda fg='text', bg='dark': {
    'foreground': colors[fg],
    'background': colors[bg]
}

separator = lambda: widget.Sep(**base(), linewidth=0, padding=5)

icon = lambda fg='color1', bg="dark", fontsize=12, text="?": widget.TextBox(
    **base(fg, bg),
    fontsize=fontsize,
    text=text,
    padding=3
)

powerline = lambda fg="light", bg="dark": widget.TextBox(
    **base(fg, bg),
    text=" ",
    fontsize=15,
    padding=-2
)

workspaces = lambda: [
    separator(),
    widget.GroupBox(
        **base(fg='light'),
        font='UbuntuMono Nerd Font',
        fontsize=12,
        margin_y=3,
        padding_y=8,
        spacing=20,
        borderwidth=1,
        active=colors['active'],
        inactive=colors['inactive'],
        rounded=None,
        highlight_method='block',
        urgent_alert_method='block',
        urgent_border=colors['urgent'],
        this_current_screen_border=colors['dark'],
        this_screen_border=colors['dark'],
        other_current_screen_border=colors['dark'],
        other_screen_border=colors['dark'],
        disable_drag=True
    ),
    separator(),
    widget.WindowName(**base(fg='focus'), fontsize=12, padding=10),
    separator(),
]

primary_widgets = [
    *workspaces(),

    separator(),

    icon(fg="color4", text=' '),
    widget.Memory(**base(fg='color4')),

    powerline('color3'),
    icon(fg="color3", text=' '),
    widget.Net(**base(fg='color3'), interface='enp5s0'),

    powerline('color2'),
    widget.CurrentLayoutIcon(**base(fg='color2'), scale=0.65),
    widget.CurrentLayout(**base(fg='color2'), padding=5),

    powerline('color1'),
    icon(fg="color1", text=' '),
    widget.Clock(**base(fg='color1'), format='%d/%m/%Y - %H:%M '),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    widget.Systray(background=colors['dark'], padding=5),

    powerline('color1'),

    widget.CurrentLayoutIcon(**base(fg='color1'), scale=0.65),

    widget.CurrentLayout(**base(fg='color1'), padding=5),
]

widget_defaults = {
    'font': 'JetBrainsMono Nerd Font Bold',
    'fontsize': 13,
    'padding': 1,
}

extension_defaults = widget_defaults.copy()