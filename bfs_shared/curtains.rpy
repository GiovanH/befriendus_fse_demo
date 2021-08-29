init offset = 2

# Welcome to my annotated curtain animation! hope you enjoy your stay
# <3 ~gio

# Sequences:

# Fade in on closed curtains
# Animate curtains opening
# Zoom in on stage

# Zoom out to open curtains
# Animate curtains closing
# Fade out on closed curtains

# The top bit, static.
# Layers are drawn in order, so the front needs to come last.
# All this does is display three images at once on layers.
transform bfs_curtains_top:
    contains:
        "{{assets}}/curtains/top_c.png"
    contains:
        "{{assets}}/curtains/top_b.png"
    contains:
        "{{assets}}/curtains/top_a.png"

# The top bit, but during movement.
# The two main parts shuffle slightly, then don't move.
# Because there's no `repeat` statement, this will just play once.
transform bfs_curtains_top_shuffle:
    contains:
        "{{assets}}/curtains/top_c.png"
    contains:
        "{{assets}}/curtains/top_b.png"
        pause 0.15
        pause 0.15
        pause 0.15
        xoffset -10
        pause 0.15
        xoffset 0
    contains:
        "{{assets}}/curtains/top_a.png"
        pause 0.15
        pause 0.15
        pause 0.15
        xoffset 10
        pause 0.15
        xoffset 0

# The side curtains opening. This is a big one.
# All the commands between `pause` statements essentially define frames.
# There is no tweening or interpolation here, for style reasons.

# This is written oddly. Can you figure out why?
transform bfs_curtains_side_open:
    contains:
        "{{assets}}/curtains/backside.png"

    contains:
        alpha 1.0

        "{{assets}}/curtains/side4.png"
        xoffset 0
        pause 0.15

        "{{assets}}/curtains/side4.png"
        xoffset -10
        pause 0.15

        "{{assets}}/curtains/side3.png"
        xoffset 0
        pause 0.15

        "{{assets}}/curtains/side2b.png"
        xoffset 0
        pause 0.15

        "{{assets}}/curtains/side2b.png"
        xoffset -180
        alpha 1.0
        pause 0.15

        alpha 0.0
        pause 0.15

# The full animation for opening the curtains.
# Includes the top and two sides
image bfs_curtains open:
    # alpha 1.0 
    contains:
        # The right side is mirrored
        xzoom -1.0
        bfs_curtains_side_open
    contains:
        "{{assets}}/curtains/side4.png"
        # The left side is one frame slower than the right
        pause 0.15
        bfs_curtains_side_open
    contains:
        bfs_curtains_top_shuffle
    # Since it's just a dissolve we don't need this:
    # on hide:
    #     linear .5 alpha 0.0

# Static, opened curtains.
image bfs_curtains opened:
    contains:
        "{{assets}}/curtains/backside.png"
        xzoom -1.0
    contains:
        "{{assets}}/curtains/backside.png"
    contains:
        bfs_curtains_top

# Same as `bfs_curtains open`, but closes them.
image bfs_curtains close:
    contains:
        xzoom -1.0
        bfs_curtains_side_close
    contains:
        "{{assets}}/curtains/backside.png"
        pause 0.15
        bfs_curtains_side_close
    contains:
        bfs_curtains_top_shuffle

# Static, closed curtains
image bfs_curtains closed:
    contains:
        "{{assets}}/curtains/side4.png"
        xzoom -1.0
    contains:
        "{{assets}}/curtains/side4.png"
    contains:
        bfs_curtains_top
    
###

# This is placed oddly. Can you figure out why?
transform bfs_curtains_side_close:
    contains:
        "{{assets}}/curtains/backside.png"

    contains:
        pause 0.15
        alpha 0.0

        pause 0.15
        alpha 1.0
        xoffset -180
        "{{assets}}/curtains/side2b.png"

        pause 0.15
        xoffset 0
        "{{assets}}/curtains/side2b.png"

        pause 0.15
        xoffset 0
        "{{assets}}/curtains/side3.png"

        pause 0.15
        xoffset -10
        "{{assets}}/curtains/side4.png"

        pause 0.15
        xoffset 0
        "{{assets}}/curtains/side4.png"

        alpha 1.0