init offset = 3

screen __p__tagsay:
    textbutton what:
        id "what"
        xalign 0.5
        yalign 0.0
        ypos 40
        xpadding 10
        ypadding 10
        xmargin 5
        ymargin 5
        xsize None
        text_font "courbd.ttf"
        text_size 40
        text_color "#000000"
        text_text_align 0.5
        text_layout "subtitle"

define !TheTagMan = Character("The Tag Man", screen="__p__tagsay")

image !bg mainmenu = "gui/main_menu.png"

image __p__greenscreen = Solid(hemospectrum("#E8E2EF"))
image __p__greenscreen menutop = Solid(hemospectrum("#281049"))
image __p__greenscreen shade kankri = Solid("#F004")
image __p__greenscreen shade meulin = Solid("#416600AA")
image __p__greenscreen shade latula = Solid("#008282AA")

image __p__greenscreen kankri = Solid(hemospectrum("candyred"))
image __p__greenscreen meulin = Solid(hemospectrum("olive"))
image __p__greenscreen rufioh = Solid(hemospectrum("bronze"))
image __p__greenscreen latula = Solid(hemospectrum("teal"))
image __p__greenscreen damara = Solid(hemospectrum("burgundy"))



label __p__trailerRoot:  # jump bfs_shared_trailerRoot
    $ quick_menu = True

    menu:
        "Meenah openeyes":

            scene bfs_bg beforan shore 
            show blackcover
            show vol01_meenah_meenah grin shine behind blackcover # with easeinbottom

            hide blackcover with openeyes

            $ renpy.pause()

            vol01_meenah_meenah snarky trident "look who finally decided to come back from snoozeland"

        "Tags":
            # Eight beats
            scene __p__greenscreen
            $ quick_menu = False

            !TheTagMan "{hemocolor=fuchsia}#if two trolls were on the moon and one krilled the otter w a 2x3dent #would that be fucked up oar what{/color}{fast}{p=0.14}{nw}"
            extend "#i bought myself a toblerone and wished that i could make this game{fast}{p=0.14}{nw}"
            extend "{hemocolor=gold}#the world is gonna roll you #don't say i never told you{/color}{fast}{p=0.14}{nw}"
            extend "#no friend in sight #(f1x th4t){fast}{p=0.14}{nw}"
            extend "{hemocolor=cerulean}#the game's alright #but the book was better{/color}{fast}{p=0.14}{nw}"
            extend "#it's the friend of the world as we know it{fast}{p=0.14}{nw}"
            extend "{hemocolor=jade}#betty friedan's {i}the jadeblood mystique{/i}{/color}{fast}{p=0.14}{nw}"
            extend "{hemocolor=maplepink}#why do they call it a horse-off when you horse on ride the race #horse off trophy win the race{/color}{fast}{p=0.14}{nw}"
            extend "{p}"

        "Kankri":

            scene vol05_kankri_bg livingroom
            show vol05_kankri_kankri talk crossed

            vol05_kankri_kankri """
Now, there’s some rich subtext going on here. 
This could be a great opening to put your budding interspecies social analysis tools to good use, but feel free to tap out at any time; 

again, this is a safe educational space, you have a designated Beforan affairs liaison to fall back on at any time.
"""
            $ renpy.pause()

        "Meulin":

            scene vol06_meulin_bg meulinbedroom
            show vol06_meulin_meulin idle

            vol06_meulin_meulin "moggers"
            $ renpy.pause()

        "Outro":

            $ quick_menu = False

            scene __p__greenscreen
            scene __p__greenscreen menutop
            show !bg mainmenu:
                align (0.5, 0.9)
                zoom 1.4
                pause 1.0
                parallel:
                    ease 3.0 zoom 1.0
                parallel:
                    easein 4.0 yalign 0.0 ypos 0.6

            $ renpy.pause()

        "Preview":

            $ quick_menu = False

            scene __p__greenscreen
            scene __p__greenscreen menutop with None

            show vol08_latula_latula sil:
                default
                pos (0.15, 1.0) # Not sure why side_left isn't working here? concerning.
            with easeinbottom
            $ renpy.pause(0.1)
            show vol09_damara_damara sil:
                default
                pos (0.85, 1.0)
            with easeinbottom
            $ renpy.pause(0.1)
            show vol07_rufioh_rufioh sil:
                default
                pos (0.54, 1.0)
            with easeinbottom

            $ renpy.pause()

        "Meulinbg":

            scene vol06_meulin_bg meulinbedroom 

            $ renpy.pause()
            show vol06_meulin_meulin sil at default:
                pos (0.7, 2.0)
                easein 0.5 ypos 1.0 
            $ renpy.pause()

        "Slowpreview":

            $ quick_menu = False

            scene __p__greenscreen

            $ sp_trans_scene = Dissolve(0.5)
            $ sp_trans_char = easeinbottom

            scene __p__greenscreen kankri 
            scene vol05_kankri_bg livingroom
            show __p__greenscreen shade kankri
            with None

            # $ renpy.pause(1.0)
            $ renpy.pause(2.4-0.5) # block - sp_trans_char

            show vol05_kankri_kankri sil at default:
                pos (0.3, 1.0)
            with sp_trans_char

            $ renpy.pause(2.4-0.5) # block - sp_trans_scene

            scene vol06_meulin_bg meulinbedroom 
            show __p__greenscreen shade meulin
            with sp_trans_scene
            $ renpy.pause(2.4-0.5)
            
            # Hack here to make sure the bg animation is perfectly smooth: no with
            show vol06_meulin_meulin sil at default:
                pos (0.7, 2.0)
                easein 0.5 ypos 1.0 
            $ renpy.pause(2.4)

            # scene __p__greenscreen latula
            scene vol02_mituna_bg skatepark
            show __p__greenscreen shade latula
            with sp_trans_scene
            $ renpy.pause(2.4-0.5)

            show vol08_latula_latula sil at default:
                pos (0.15, 1.0)
            with sp_trans_char

            $ renpy.pause(2.4-0.5-0.5)

            scene __p__greenscreen damara with sp_trans_scene
            show vol09_damara_damara sil at default:
                pos (0.85, 1.0)
            with sp_trans_char

            $ renpy.pause(2.4-0.5-0.5)

            scene __p__greenscreen rufioh with sp_trans_scene
            show vol07_rufioh_rufioh sil at default:
                pos (0.54, 1.0)
            with sp_trans_char

            $ renpy.pause()

        "NOT IMPLEMENTED":
            vol01_meenah_meenah snarky trident "Yo! You're a ??? too, right?"

        "Shortcuts":
            menu:
                "int02 int2Continue":
                    scene bfs_bg pink moon
                    show vol01_meenah_meenah observe
                    jump vol04b_int2Continue
                "vol04 porrim privilege":
                    scene vol04_porrim_bg den interior
                    show vol04_porrim_porrim smile
                    jump vol04_porrim_porrimConvFour

jump __p__trailerRoot
