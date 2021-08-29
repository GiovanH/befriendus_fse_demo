init offset = 1
           
init python:
    def bfs_flak_printf(char):
        # initials = char.name[0].upper() + filter(lambda s: s.isupper(), char.name)[0]
        try:
            initials = re.sub(r"(.)[a-z]+([A-Z])[a-z]+", r"\g<1>\g<2>", char.name).upper()
        except:
            if renpy.config.developer:
                raise
            else:
                initials = "??"
        try:
            color = char.show_args['who_color']
            # shout out to fstrings for making strings not look like this in modern python
            return "{color=" + color + "}{b}" + char.name + " [" + initials + "]{/b}{/color}"
        except AttributeError:
            return "{b}" + char.name + " [" + initials + "]{/b}"

init python:
    QuirkStore["flakhack"] = [("\+", "{image={{assets}}/flak/whitneyplus.png}")]


# Todo: Fancy nameboxes. 
# flak-style NVL mode
define __p__flak_borders = Borders(16, 38, 16, 86)

style __p__flak_window:
    align (0.5, 1.0)
    xfill False
    # Measured
    xsize 792
    yminimum 150
    ymaximum 24000  # let it go offscreen
    background Frame("{{assets}}/flak/bg.png", __p__flak_borders)
    padding __p__flak_borders.padding

style bfs_flak_window_cerulean is __p__flak_window:
    background Frame("{{assets}}/flak/bg_cerulean.png", __p__flak_borders)

style bfs_flak_window_fuchsia is __p__flak_window:
    background Frame("{{assets}}/flak/bg_fuchsia.png", __p__flak_borders)

style __p__flak_text:
    font "{{assets}}/whitney-medium.otf"
    # kerning -0.1
    size 16
    color "#1C1C1C"

style __p__flak_who is __p__flak_text:
    bold True

style __p__flak_what is __p__flak_text

screen __p__flak_entry:
    # $ avatar_src = kwargs.get("avatar_src", "{{assets}}/avatar_fail.png")
    # $ who_color = kwargs.get("who_color", "#fff")
    # style_prefix "say"

    default avatar_src = None
    default who_color = "#fff"
    default extend = False
    default system_arrow = False

    default _avatar = None
    python:
        if extend:
            _avatar = None
        elif system_arrow:
            _avatar = "{{assets}}/flak/arrow.png"
        elif avatar_src is not None:
            _avatar = im.AlphaMask(scaleBestFit(avatar_src, 40, 40), "{{assets}}/flak/avatar_mask.png")
        else:
            _avatar = None

    hbox:
        spacing 16
        if _avatar:
            add _avatar pos (0, 2)
        else:
            null width 40

        vbox:
            spacing 2

            if who is not None and not extend:
                text who:
                    id "who"
                    color who_color

            text what:
                id "what"

define bfs_flak = QuirkChar(
    kind=FakeNVLC,
    window_style="__p__flak_window",
    who_style="__p__flak_who",
    what_style="__p__flak_what",
    show_entry_screen="__p__flak_entry",
    show_nvlc_spacing=6,
    show_nvlc_newchar_spacing=3
)

define bfs_flak_sys = QuirkChar(
    kind=bfs_flak,
)


