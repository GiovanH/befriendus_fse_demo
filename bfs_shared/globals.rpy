init offset = 1

init python:
    def buildBfsTranslations():
        # Generate translation template files for bfs stuff
        renpy.translation.update_translations = True
        stl = renpy.game.script.translator.strings["template"]
        # Tags
        for tag in titletags:
            stl.translate(tag)

        for new_tags in befriendus_achievement_tags.values():
            for tag in new_tags:
                stl.translate(tag)

        stl.write_updated_strings("template")
        return buildTranslations()

    # Grandfather in old ids
    if achievement.has("vol03b_int01_int_01_finished"):
        achievement.grant("vol02b_int_01_finished")


init python:
    if persistent.bfs_puns_enabled is None:
        persistent.bfs_puns_enabled = True

    def texttag_pun(tag, argument, contents):

        pun_text = argument
        has_done = False

        rv = []
        for kind, text in contents:
            if kind == renpy.TEXT_TEXT:
                if has_done:
                    raise Exception("Tag {pun} cannot contain multiple text segments!")
                if persistent.bfs_puns_enabled:
                    rv.append((kind, pun_text))
                else:
                    rv.append((kind, text))
                has_done = True
            else:
                rv.append((kind, text))
        return rv

    config.custom_text_tags["pun"] = texttag_pun