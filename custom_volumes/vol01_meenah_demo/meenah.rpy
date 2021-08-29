init offset = 2

init python:
    # H -> )(
    # E -> -E
    QuirkStore["meenah"] = [("H", ")("), ("E", "-E")]

### CHARACTER DEFINITIONS ###
#############################
define !meenah = HtagChar("MEENAH", quirklist=["meenah"], kind=bfs_kind, image="__p__meenah", show_blood="fuchsia",)

### CHARACTER SPRITES ##
########################
image !meenah idle = Image("{{assets}}/characterp/meenah/idle.png", yanchor=820)
image !meenah idle trident = Image("{{assets}}/characterp/meenah/idle_trident.png", yanchor=820)
image !meenah idle trident talk = Composite(
    (1400, 1000),
    (0, 0), Crop((0, 0, 1400, 319), "__p__meenah idle trident"),
    (0, 319), Crop((0, 319, 637, 387), "__p__meenah idle trident"),
    (637, 319), "{{assets}}/characterp/meenah/idle_trident_talk 637,319.png",
    (714, 319), Crop((714, 319, 1400, 387), "__p__meenah idle trident"),
    (0, 387), Crop((0, 387, 1400, 1000), "__p__meenah idle trident"), yanchor=820
)
image !meenah idle talk = Composite(
    (1400, 1000),
    (0, 0), Crop((0, 0, 1400, 319), "__p__meenah idle"),
    (0, 319), Crop((0, 319, 637, 387), "__p__meenah idle"),
    (637, 319), "{{assets}}/characterp/meenah/idle_talk 637,319.png",
    (714, 319), Crop((714, 319, 1400, 387), "__p__meenah idle"),
    (0, 387), Crop((0, 387, 1400, 1000), "__p__meenah idle"), yanchor=820
)
image !meenah content = Composite(
    (1400, 1000),
    (0, 0), Crop((0, 0, 1400, 104), "__p__meenah idle"),
    (0, 104), Crop((0, 104, 433, 1000), "__p__meenah idle"),
    (433, 104), "{{assets}}/characterp/meenah/content 433,104.png",
    (911, 104), Crop((911, 104, 1400, 1000), "__p__meenah idle"),
    (0, 1000), Crop((0, 1000, 1400, 1000), "__p__meenah idle"), yanchor=820
)
image !meenah content trident = Image("{{assets}}/characterp/meenah/content_trident.png", yanchor=820)
image !meenah ecstatic = Composite(
    (1400, 1000),
    (0, 0), Crop((0, 0, 1400, 105), "__p__meenah idle"),
    (0, 105), Crop((0, 105, 321, 1000), "__p__meenah idle"),
    (321, 105), "{{assets}}/characterp/meenah/ecstatic 321,105.png",
    (1037, 105), Crop((1037, 105, 1400, 1000), "__p__meenah idle"),
    (0, 1000), Crop((0, 1000, 1400, 1000), "__p__meenah idle"), yanchor=820
)
image !meenah eyeroll = Composite(
    (1400, 1000),
    (0, 0), Crop((0, 0, 1400, 125), "__p__meenah idle"),
    (0, 125), Crop((0, 125, 433, 1000), "__p__meenah idle"),
    (433, 125), "{{assets}}/characterp/meenah/eyeroll 433,125.png",
    (903, 125), Crop((903, 125, 1400, 1000), "__p__meenah idle"),
    (0, 1000), Crop((0, 1000, 1400, 1000), "__p__meenah idle"), yanchor=820
)
image !meenah eyeroll annoyed = Composite(
    (1400, 1000),
    (0, 0), Crop((0, 0, 1400, 229), "__p__meenah eyeroll"),
    (0, 229), Crop((0, 229, 595, 297), "__p__meenah eyeroll"),
    (595, 229), "{{assets}}/characterp/meenah/eyeroll_annoyed 595,229.png",
    (757, 229), Crop((757, 229, 1400, 297), "__p__meenah eyeroll"),
    (0, 297), Crop((0, 297, 1400, 1000), "__p__meenah eyeroll"), yanchor=820
)
image !meenah eyeroll annoyed trident = Image("{{assets}}/characterp/meenah/eyeroll_annoyed_trident.png", yanchor=820)
image !meenah grin = Composite(
    (1400, 1000),
    (0, 0), Crop((0, 0, 1400, 105), "__p__meenah idle"),
    (0, 105), Crop((0, 105, 368, 1000), "__p__meenah idle"),
    (368, 105), "{{assets}}/characterp/meenah/grin 368,105.png",
    (969, 105), Crop((969, 105, 1400, 1000), "__p__meenah idle"),
    (0, 1000), Crop((0, 1000, 1400, 1000), "__p__meenah idle"), yanchor=820
)
image !meenah grin shine = Composite(
    (1400, 1000),
    (0, 0), Crop((0, 0, 1400, 361), "__p__meenah grin"),
    (0, 361), Crop((0, 361, 579, 434), "__p__meenah grin"),
    (579, 361), "{{assets}}/characterp/meenah/grin_shine 579,361.png",
    (768, 361), Crop((768, 361, 1400, 434), "__p__meenah grin"),
    (0, 434), Crop((0, 434, 1400, 1000), "__p__meenah grin"), yanchor=820
)
image !meenah grumpy = Composite(
    (1400, 1000),
    (0, 0), Crop((0, 0, 1400, 105), "__p__meenah idle"),
    (0, 105), Crop((0, 105, 373, 1000), "__p__meenah idle"),
    (373, 105), "{{assets}}/characterp/meenah/grumpy 373,105.png",
    (917, 105), Crop((917, 105, 1400, 1000), "__p__meenah idle"),
    (0, 1000), Crop((0, 1000, 1400, 1000), "__p__meenah idle"), yanchor=820
)
image !meenah grumpy puff = Composite(
    (1400, 1000),
    (0, 0), Crop((0, 0, 1400, 230), "__p__meenah grumpy"),
    (0, 230), Crop((0, 230, 662, 410), "__p__meenah grumpy"),
    (662, 230), "{{assets}}/characterp/meenah/grumpy_puff 662,230.png",
    (813, 230), Crop((813, 230, 1400, 410), "__p__meenah grumpy"),
    (0, 410), Crop((0, 410, 1400, 1000), "__p__meenah grumpy"), yanchor=820
)
image !meenah observe = Composite(
    (1400, 1000),
    (0, 0), Crop((0, 0, 1400, 73), "__p__meenah idle"),
    (0, 73), Crop((0, 73, 433, 874), "__p__meenah idle"),
    (433, 73), "{{assets}}/characterp/meenah/observe 433,73.png",
    (965, 73), Crop((965, 73, 1400, 874), "__p__meenah idle"),
    (0, 874), Crop((0, 874, 1400, 1000), "__p__meenah idle"), yanchor=820
)
image !meenah observe trident = Image("{{assets}}/characterp/meenah/observe_trident.png", yanchor=820)
image !meenah pissed = Composite(
    (1400, 1000),
    (0, 0), Crop((0, 0, 1400, 105), "__p__meenah idle"),
    (0, 105), Crop((0, 105, 378, 1000), "__p__meenah idle"),
    (378, 105), "{{assets}}/characterp/meenah/pissed 378,105.png",
    (974, 105), Crop((974, 105, 1400, 1000), "__p__meenah idle"),
    (0, 1000), Crop((0, 1000, 1400, 1000), "__p__meenah idle"), yanchor=820
)
image !meenah shrug = Composite(
    (1400, 1000),
    (0, 0), Crop((0, 0, 1400, 105), "__p__meenah idle"),
    (0, 105), Crop((0, 105, 373, 1000), "__p__meenah idle"),
    (373, 105), "{{assets}}/characterp/meenah/shrug 373,105.png",
    (917, 105), Crop((917, 105, 1400, 1000), "__p__meenah idle"),
    (0, 1000), Crop((0, 1000, 1400, 1000), "__p__meenah idle"), yanchor=820
)
image !meenah shrug puff = Composite(
    (1400, 1000),
    (0, 0), Crop((0, 0, 1400, 286), "__p__meenah shrug"),
    (0, 286), Crop((0, 286, 661, 409), "__p__meenah shrug"),
    (661, 286), "{{assets}}/characterp/meenah/shrug_puff 661,286.png",
    (793, 286), Crop((793, 286, 1400, 409), "__p__meenah shrug"),
    (0, 409), Crop((0, 409, 1400, 1000), "__p__meenah shrug"), yanchor=820
)
image !meenah snarky = Composite(
    (1400, 1000),
    (0, 0), Crop((0, 0, 1400, 73), "__p__meenah idle"),
    (0, 73), Crop((0, 73, 433, 1000), "__p__meenah idle"),
    (433, 73), "{{assets}}/characterp/meenah/snarky 433,73.png",
    (966, 73), Crop((966, 73, 1400, 1000), "__p__meenah idle"),
    (0, 1000), Crop((0, 1000, 1400, 1000), "__p__meenah idle"), yanchor=820
)
image !meenah snarky trident = Image("{{assets}}/characterp/meenah/snarky_trident.png", yanchor=820)
image !meenah squint = Composite(
    (1400, 1000),
    (0, 0), Crop((0, 0, 1400, 232), "__p__meenah idle"),
    (0, 232), Crop((0, 232, 437, 1000), "__p__meenah idle"),
    (437, 232), "{{assets}}/characterp/meenah/squint 437,232.png",
    (910, 232), Crop((910, 232, 1400, 1000), "__p__meenah idle"),
    (0, 1000), Crop((0, 1000, 1400, 1000), "__p__meenah idle"), yanchor=820
)
image !meenah squint trident = Image("{{assets}}/characterp/meenah/squint_trident.png", yanchor=820)
image !meenah squint trident talk = Composite(
    (1400, 1000),
    (0, 0), Crop((0, 0, 1400, 319), "__p__meenah squint trident"),
    (0, 319), Crop((0, 319, 637, 387), "__p__meenah squint trident"),
    (637, 319), "{{assets}}/characterp/meenah/squint_trident_talk 637,319.png",
    (714, 319), Crop((714, 319, 1400, 387), "__p__meenah squint trident"),
    (0, 387), Crop((0, 387, 1400, 1000), "__p__meenah squint trident"), yanchor=820
)
image !meenah squint talk = Composite(
    (1400, 1000),
    (0, 0), Crop((0, 0, 1400, 319), "__p__meenah squint"),
    (0, 319), Crop((0, 319, 637, 387), "__p__meenah squint"),
    (637, 319), "{{assets}}/characterp/meenah/squint_talk 637,319.png",
    (714, 319), Crop((714, 319, 1400, 387), "__p__meenah squint"),
    (0, 387), Crop((0, 387, 1400, 1000), "__p__meenah squint"), yanchor=820
)
image !meenah threaten = Composite(
    (1400, 1000),
    (0, 0), Crop((0, 0, 1400, 105), "__p__meenah idle"),
    (0, 105), Crop((0, 105, 350, 1000), "__p__meenah idle"),
    (350, 105), "{{assets}}/characterp/meenah/threaten 350,105.png",
    (1111, 105), Crop((1111, 105, 1400, 1000), "__p__meenah idle"),
    (0, 1000), Crop((0, 1000, 1400, 1000), "__p__meenah idle"), yanchor=820
)
