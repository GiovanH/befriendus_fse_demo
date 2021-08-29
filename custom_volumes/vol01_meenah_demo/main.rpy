init offset = 3

# Most names (if not in quotes) can use a very pretty ! instead of the ugly manual __p__ replacement.
image !bg throne room = Image("{{assets}}/bg_throne_room.png")
image !bg throne room blur = im.Blur("{{assets}}/bg_throne_room.png", 1.5)
image bfs_bg pink moon = Image("{{assets}}/bg_pink_moon.png")
image !bg pink moon b = Image("{{assets}}/bg_pink_moon_b.png")
image !bg meenah block = Image("{{assets}}/bg_meenah_block.png")

# Explicitly expose the shore background so maplehoof can get it
# Removing the ! removes the namespacing, so it's global
image bfs_bg beforan shore = Image("{{assets}}/bg_beforan_shore.png")

image bfs_drone = Image("{{assets}}/drone.png")
image !empress portrait = Image("{{assets}}/empress_portrait.png")
image bfs_blood border candy red = Image("{{assets}}/blood_border_candyred.png")

# Define other graphics, end cards
image !endcard_bad1 = "{{assets}}/meenah_endcard_badend1.png"
image !endcard_bad2 = "{{assets}}/meenah_endcard_badend2.png"
image !endcard_good = "{{assets}}/meenah_endcard_goodend.png"

transform !pounce:
    ypos 730
    easeout 0.1 ypos 754
    easeout 0.1 ypos 730
    easeout .15 zoom 2 ypos 400 alpha 0.0

#Default zoom is 1
transform bfs_zoom(z=1.5, time=0.5):
    easein time zoom z

transform bfs_dashhere(x,time=0.2):
    easein time xpos x

transform !slowfade(a=0.0,b=1.0,time=0.5):
    alpha a
    linear time alpha b

transform !stab:
    easein 0.07 xoffset 48 yoffset -5
    pause(0.05)
    linear 0.1 xoffset -32 yoffset 0
    easein 0.2 xoffset 0

transform !dronedeath:
    ease 0.05 xoffset 15 yoffset 3
    ease 0.07 xoffset -12 yoffset 6
    ease 0.09 xoffset 9 yoffset 9
    ease 0.11 xoffset -6 yoffset 12
    ease 0.13 xoffset 3 yoffset 15
    ease 0.15 xoffset 0 yoffset 18
    pause(0.2)
    linear 0.2 yoffset 720

transform bfs_running:
    yoffset 0
    easein 0.1 yoffset 2
    easeout 0.1 yoffset 0
    repeat

# Start of route
label __package_entrypoint___vol01_meenah:    # Start at black screen
    # Set the scene, fade in from black
    scene bfs_bg beforan shore with Dissolve(1.5)

    hide blackcover with dissolve

    "You wake up on the beach."

    "You're pretty sure this is a beach, anyway. Far be it from you to determine what things are on this ass-backwards planet. Maybe they call these things \"sea body borders\" or some inane horseshit like that."

    "You let out a disgusting wet cough because you apparently decided to take a nap in the ocean for some reason?? Beats you, you're just trying to ignore the feeling of wet clothes sticking to your skin."

    "Ugh, this probably means you have sand everywhere too. Even the awful places. You feel the purple waves tickle your feet as you gaze at the alien sky above you."

    "..."

    "Wait a minute. Isn't the ocean meant to be like, a super dangerous place? You recall pretty much every troll you've ever talked to telling you that this is a HORRENDOUS place to be if you're not—"

    #[SPRITE: Meenah sprite slides up from bottom.]
    show !meenah grin shine with easeinbottom #Dissolve(1.0) #!easeup(1730,0.4,730)
    #pause(1.0)

    play music "{{assets}}/music/Chumming the Bassline.ogg" loop
    "A sea dweller. A sea dweller with huge shark teeth and gold adornments from horn to toe and pointy fins flared out as if nature itself was saying, \"hey numbnuts, steer clear.\""

    "You know, like this friendly-looking individual obviously is, stepping up from the depths like a hungry sea monster. Thank god you're right by a pool of water so you can clean up whatever garments you're soiling right now."

    show !meenah grin with Dissolve(0.5)
    !meenah "{pun=whale whale whale}well well well{/pun}" (show_hashtags="#{pun=whale}well{/pun} x3 combo")

    !meenah snarky trident "look who finally decided to come back from snoozeland"

    "Does she want an answer? You can TOTALLY answer, provided she doesn't give you the pointy end of that twofold fork she's got there."

    "It looks very nice by the way. Really, uh, brings out her complexion."

    show !meenah grin shine at bouncing

    "The laugh you get in response is very shrill and piercing, which you hope isn't a theme she has intentions of continuing. You're good without piercings, thanks."

    show !meenah snarky at nod

    !meenah "{pun=dam}damn{/pun} lil freak guess i cant bring {pun=myshellf}myself{/pun} to {pun=krill}kill{/pun} such {pun=a fintense}an intense{/pun} bootlicker" (show_hashtags="#{pun=naut}not{/pun} yet {pun=anywaves}anyways{/pun}")

    !meenah squint talk "that dont answer my q that imma need you to a {pun=reel}real{/pun} quick tho" (show_hashtags="#qs #as")

    show !meenah threaten at bounce(-12, 0.2, 0)

    !meenah "how in the FUCK did your ass wind up appearifyin in the middle of the ocean with no fins and no fake pointy ass wizard hat"

    show !meenah at bounce(12, 0.0, 2)

    "You know she means business because she's nudging you with her pointy business stick."

    "As waterlogged as you are, you still realize a threat when you see one."

    "Slowly, you start to rise to your feet as you ponder..."

    "How... how IN the fuck did your ass wind up appearifying in the middle of the ocean?"

    "Your memories are VERY unclear right now (big fucking surprise, given your track record), but right now you're chalking that up to recovering from drowning as opposed to, like... plot bullshit."

    "Your best bet is plot bullshit and you really wish you had a less ridiculous-sounding answer for her."

    label __p__meenahChoiceOne:
        menu:
            extend ""

            "Go into excruciating detail.":
                jump __p__meenahBadEndOne

            "Be vague and wishy-washy.":
                jump __p__meenahContinueOne

label __p__meenahBadEndOne:

    show !meenah squint trident

    "{i}So,{/i} you tell the sea dweller with renewed vigor, {i}let me tell you about a homesick traveler crash-landing on an alien planet.{/i}"
    
    show !meenah idle trident

    "She already looks incredibly done with whatever bullshit you're about to subject her to, but it's okay, you assure her. This story involves, um. Explosions! Action!"

    "Teen drama and heartbreak? Is that something she'd be into?"

    show !meenah snarky trident at nod

    !meenah "id be into yo lusus" (show_hashtags="#{pun=SHELL}EL{/pun} #EM #AY #OH")

    "Joke's on her, you don't HAVE a lusus."

    show !meenah idle trident

    "You expect her to feel overwhelmingly guilty for poking fun at your orphan status but she doesn't bat an eye. What, no apologies or comments about how sad that is?"

    "Fine, alright, you get it. You've got a story to tell anyhow."

    "To cover up the awkwardness of the situation, your mouth starts to run like it's a god damned waterfall with everything your little mind can dredge up."

    "Not necessarily all in chronological order, but let's be real, you won't understand the whole clown armpit thing without first diving into your thirst for someone who turned out to be a drug dealer??"

    show !meenah squint trident

    "Or, wait. Was that part in your head? God damn it, even WITH your memories intact you can't make heads or tails of that party at Ardata's. You were way too trashed and/or soothed by a pretty guy."

    "You start to recite the entirety of Chixie's rap battle, but proceed to forget half of her second verse and struggle to fill in the blanks with the most vulgar-sounding verbs possible."

    show !meenah eyeroll annoyed trident

    "She looks like she's about to fall asleep. Not really, but she definitely looks like she's pretending to really fall asleep. Shit, you're losing her."

    "Uh, did you mention the time you got abductnapped? Some asshole swiped you up and dumped you right on the green moon—"

    show !meenah eyeroll annoyed at nod(-12, 0.0, 0.3)

    !meenah "fuuuuuck {pun=ocray}okay{/pun} im gonna stop you right there"

    !meenah shrug "lbr there was a 0\% chance of me givin literally a single shit {pun=aboat}about{/pun} {pun=whatebber}whatever{/pun} youre sayin with those seed flaps a yours" (show_hashtags="#lbr stands for lets be {pun=reel}real{/pun} ftr")

    !meenah squint talk "but if you think ima sit here and listen to a whole new windfang chew me out with make believe bs you cray" (show_hashtags="#cray chumps #chump like chum #heh")

    show !meenah threaten at nod(6, 0.0, 0.08)

    !meenah "do us both a favor and fuck off" (show_hashtags="#mostly me tho")

    "What? {i}Make believe?{/i} This is all real as shit, you assure her. Do you think you could make up an underground sewer flood on the hunt for hot dogs??"

    "Okay maybe that sounds somewhat unrealistic now that you say it out loud, but—"

    !meenah squint trident talk "maybe you still got some water clogged in your hearin shells"

    show !meenah grin shine at nod

    !meenah "GET ON YOUR STRUTPODS"

    show !meenah pissed at nod(12,0.0,0.12,0.0,2)

    #S)(OUTPOL---E
    !meenah "AND {pun=CLAMSCRAY}AMSCRAY{/pun} {pun=REEFORE}BEFORE{/pun} I FORK YA" (show_hashtags="#{quirked=S)(OUTPOL---E}SHOUTPOLE{/quirked} TIMES {pun=FINFINITY}INFINITY{/pun} COMBO")

    "It's about now that you're remembering her teeth are razor sharp. It helps that she's baring them at you. It jogs your memory a little."

    show !meenah threaten at height(715)
    with ease

    "Her raised trident, on the other hand, kicks your jogged memory to a sprint for the high hills."

    "With a split second to react, you think of safety. None of this salty-smelling dangerscape, none of this oppressed dystopian alien society, and most CERTAINLY no raggedy death princesses."

    show !meenah at !pounce
    pause(0.2)

    #[SCENE: zap to white, then to black]
    scene black
    with Fade(.25, 0.25, .25, color="#FFFFFF")
    show bfs_blood border candy red at !slowfade(0.0,1.0,10)

    "Well, there's good news and bad news."

    "The good news is that you seem to not be by the beach anymore, if the lack of shoreside ambience is anything to go by."

    "The bad news is that you zapped away a split second after her trident landed right in your gut."

    "In your last moments, you don't hear her angry, accusatory glubs. You don't hear her demanding you return her trident to her. You just hear the blood in your ears."

    "You also feel it, all around you. It's kind of really fucking gross."

    show bfs_blood border candy red at !slowfade(1.0,0.0,5)
    "Thankfully dead people don't care so much about things like cleanliness. You proceed to stop caring so much."

    call fseToastEnding pass ("__p__endcard_bad1", "__p__meenah_bad_end_1", False)
    return

label __p__meenahContinueOne:

    "Okay, okay. Be cool, this is obviously one cool customer over here. You can't scare her away by acting like a total doofus."

    "If there were a lamp post nearby, you would be crossing your arms and leaning against it all cool-like and casually, like you don't give an {i}F{/i} about what your parents have to say about your life choices."

    show !meenah squint trident

    "Instead you just shrug and tell her that you can teleport. Yeah, whatever. No big deal. There's more fish in the sea where that came from. You're pretty sure that's what that saying means."

    "Shit you're actually not sure if saying fish things around her is like, offensive to her."

    "You're about to drop your total \"too cool for school\" attitude and apologize, but she cuts you off before you can."

    show !meenah grumpy puff at nod

    #W---EAKN---ESS
    !meenah "uuuugh why you gotta use fish puns they be my \n{quirked=W---EAKN---ESS}WEAKNESS{/quirked}" (show_hashtags="#dont stop tho")

    !meenah idle talk "alright you dont seem like a tidal shore to be around so lemme give you the rundown"

    show !meenah idle
    "Tidal what now?"

    !meenah squint talk "total chore" (show_hashtags="#cmon keep up")

    !meenah observe "speakin of {pun=shores}chores{/pun}"

    !meenah snarky "i need you to do {pun=somefin}something{/pun} for me"

    "You've got a sneaking suspicion that this favor she's about to ask for is a little more mandatory than you would generally prefer. Quite frankly you arrived just to make friends and—"

    !meenah content "you after chums huh"

    show !meenah content trident at nod

    !meenah "tell you what how {pun=aboat}about{/pun} i scrape your back chitin and you scrape mine"

    menu:
        extend ""
        
        "Sure!":
            pass

        "Um!":
            pass

    "Well actually that sounds like{w=0.4}{nw}"

    show !meenah snarky trident at nod

    !meenah "glad to hear it knew i could count on you"

    !meenah observe trident "so heres what the moves finna be" (show_hashtags="#{pun=finstructions}instructions{/pun} #{pun=rudderections}directions{/pun} #{pun=surfvival}survival{/pun} guide")

    !meenah content trident "you use your lil zappy bs to help a grl escape tf {pun=troutta}outta{/pun} here and ill uh"

    !meenah squint trident talk "be ya pal" (show_hashtags="#{pun=frondship}friendship{/pun} #i guess?? #{pun=frondships}friendships{/pun} free aint it")

    "Nothing's really stopping you from zapping straight out of here to avoid getting forked down the road, you're realizing. As much as friends are great, self-preservation is starting to grow on you."

    "But you're starting to remember something. The feeling of wanting to get away from this hellscape of a planet."

    "Someone you deeply cared about wanted you to take her with you if you ever found a way out."

    "You couldn't, back then. You didn't have this... feeling of incredible importance to the plot. Whatever the actual hell that means in any sense whatsoever?"

    "But you have the power to help someone out now."

    "Alright, you tell her. For the power of friendship, you will do whatever it takes to help her. She seems pleased and something in you melts from her approval."

    !meenah content "so hows this work exactly"

    !meenah "can you just like"

    !meenah squint talk "go anywhere if you think aboat it??" (show_hashtags="#do you click your heels and believe in lepreprawns or what")

    !meenah observe "do you {pun=gotter}gotta{/pun} have been there or do you just like..." (show_hashtags="#man lepreprawns sounds supes awkward actually")

    !meenah "already {pun=minnow}know{/pun} how to get there somehow" (show_hashtags="#{pun=OH HOLD UP #lepreconches #3B)}lepreconches??? #38/ #just leprechauns{/pun}")

    "That's pretty much how it works, yeah. You're kind of overpowered like that. You're still being chill about this so you throw another shrug in there. Yeah. Whatever. Did you mention yeah?"

    show !meenah grin at nod(12,0.0,0.12,0.2,1)

    !meenah grin "oh thats {pun=pearlfect}perfect{/pun}" (show_hashtags="#F YEAH {pun=beaches}bitches{/pun}")

    show !meenah snarky

    !meenah "first {pun=oarder}order{/pun} of business: my palace" (show_hashtags="#and make it {pun=SNAPPERY}SNAPPY{/pun}")

    "You give her a salute and hold your hand out for her to grab onto."

    show !meenah idle at nod(8,0.7,1.0)

    "She doesn't get what you're going for for a second and gives you an incredibly half-hearted high five."

    "There is literally nothing more unpleasant than a soft caressing high five from a recently resurfaced fish murderer."

    "Her hand's still super wet from just having resurfaced. You're staring at each other awkwardly. You feel like crumpling up like a soda can as it slowly dawns on her."

    !meenah squint "..."

    !meenah squint talk "oh"

    show !meenah squint

    "You grab her hand and refrain from judging her for her faux pas, mostly because the look she gives you tells you laughing means getting stabbed three times over."

    "When you open your eyes again, you're expecting to see the inside of some kind of Star Wars death fortress. You know, torture chamber escape pods, pillars of fire, statues of the empress..."

    #[SCENE: ZAP to throne room BG.]
    show !meenah observe
    show !bg throne room behind !meenah
    with Fade(.25, 0.25, .25, color="#FFFFFF")

    "...but you arrive in an incredibly cushy-looking throne room filled with bright colors and portraits of a smiling fish lady."

    show !meenah grin at nod
    "You're obviously in the right place because she's got her hands on her hips like this is business as usual, despite the abstract form of transport."

    "Geez, is it just you or does this place look a lot cozier than you would've expected from the person in charge of society around here?"

    "What was her name again... Her Impressionable Compensation? Her Impervious Compression? Something like that."

    "IMPERIOUS CONDESCENSION. There we go. You know your shit after all, you proudly proclaim with your hands on your hips."

    !meenah eyeroll "glubbin fuck you dont got no idea how to clam up do you" (show_hashtags="#jackin that empress {pun=tidal}title{/pun} though")

    !meenah observe trident "for {pun=reel}real{/pun} tho if you think this be any {pun=soart}sort{/pun} of out-of-character {pun=expierience}experience{/pun} then you definitely aint from {pun=aflound}around{/pun} here" (show_hashtags="#as if the lack of horns didnt give it away #like {pun=incredibubbly}incredibly{/pun} worthless candy")

    "You could say something to that effect, yes."

    !meenah content trident "alright im off to start packing" (show_hashtags="#and also finish packing #fin-ish being a pun")

    !meenah "wasnt expectin a ride so soon so i got some loose nets to tie up" (show_hashtags="#guess the shuttlefish stays unjacked #for now")

    !meenah idle trident talk "keep watch for me here and {pun=lemminnow}lemme know{/pun} if you hear anybody come this {pun=wave}way{/pun}"

    "Wait. You're being left on guard duty?? But you're tiny and unarmed, doesn't she think that this is kind of a terrible idea???"

    show !meenah threaten at twitch
    "You start to go down the laundry list of reasons why it probably isn't a good idea to put you in a position of looking out but her pointing three sharp prongs at you shuts you up pretty quickly."

    #[SPRITE: Meenah slides out to the right.]
    hide !meenah with easeoutright
    
    "Before you can build up enough dumb and foolish courage to refute her, she's disappearing down one of the five hallways this place connects to. It's like spaghetti down here."

    stop music fadeout 0.7
    queue music "custom_assets_bfs_shared/music/Interlude.ogg" loop

    "Oh yeah. Down here. You found a giant glass wall that shows you just how \"down here\" you are: you're Under God Damned Motherglubbing Water."

    "There's something that looks like a cross between an anglerfish and a whale shark that's swimming closer and you have a funny feeling it isn't looking for friendship."

    #[SCENE: Screenshake.]
    show !bg throne room with hpunch

    "Despite its best efforts, it's no match for the glass, but it sure as hell tried to turn you into some kind of foreign alien dessert and you're really starting to feel unsafe. Just a little."

    "You would love to maybe not be standing in the throne room all by yourself."

    "Then again, disobeying the orders of Alternia's heiress might not exactly be safe either. Looks like you've got another choice to make, buster."

    menu:
        extend ""
        
        "Follow her to her block.":
            jump __p__meenahContinueTwo

        "Stay put and keep an eye out.":
            jump __p__meenahBadEndTwo

label __p__meenahBadEndTwo:

    "Murderplanet fauna be damned, you're not going to get the heiress on your good side flying in the face of everything she wants. Besides, you can't help but want to be a nosy asshole and explore the place."

    "You're basically in the prime position to learn more about this empress you keep hearing so much about. You're honestly surprised you haven't seen her in person yet, given what you know about her hating aliens."

    "Wait. Was that the heiress? You might be thinking of the heiress hating aliens."

    "Speaking of heiresses, is this the Trizza Tethis you've been hearing so much about??? She hasn't told you her name yet but you're connecting the dots here."

    "Shit! You may be befriending the next generation of tyranny and villainy and the reason Alternia is so shitty!"

    "...You guess you've made worse friends???"

    "Taking a deep breath, you decide to do some browsing around the throne room. There's room for plenty of exposition here."

    "You mean exploration.{w} Did you mean exploration?"

    "You decide to start with the giant fuck-off portrait of the empress, who without question has more hair than several small towns combined."

    #[SCENE: Feferi empress shot]
    show !empress portrait with Dissolve(1.0)
    show !bg throne room blur with Dissolve(1.0)

    "\")(er Impassioned Conservation, Feferi Peixes, Empress DCXII.\""

    "Huh. That's not a very familiar name to you."

    "There's no biographical article or anything, but using the power of imagination, you take one look at her angelic smile and fill in the blanks yourself."

    "{i}This must be one smart cookie,{/i} you remark in a shitty noir voice, {i}using that smile to deceive an entire empire. Pearly whites really make the skeletons in her closet blend in.{/i}"

    "Okay your narration is even more insufferable now. You are not feeling particularly hard-boiled tonight."

    "The point is, there's no way SHE could be responsible for such an oppressive and brutally dystopian society, right?"

    "Where are the acid-spitting appendages? Where is the throne made of bones and fire?? You have not seen ONE doomsday device yet and you are feeling so ripped off."

    hide !empress portrait
    show !bg throne room
    with Dissolve(1.0)

    "You keep walking down the hall and interpreting the various decorative displays like you're in a museum{w}... of underwater death."

    "You see )(IC cuddling a giant spaceship, wearing an incredibly poofy and colorful ballgown, holding a freshly baked cake..."

    "Oh, here's something juicy. She's sitting a tiny finned grub with pigtails on her lap. It looks freshly hatched."

    "It's been vandalized with a fuchsia marker to make the grub look more... how do you say this."

    "There are sharp teeth and angry eyebrows messily scrawled over the grub to make it look like a way more terrible person."

    "You wonder how that heiress feels about this. If that grub is her, she must be pissed. Off-the-walls livid. Flames on the sides of her face and everything."

    "You consider telling her about this flagrant abuse of royal property but you don't exactly feel like being the messenger for someone with a seeming love for stabbing things.{w} Or people.{w} Or you."

    "By the time you make your way down the museum-esque hallway reading up about the Squiddlian Peace Treaty you've had it up to here with history lessons. You've also been standing around for a good long while reading Boring Bullshit."

    "You haven't read a single word about anything remotely violent and after all your time spent toughing it out on Alternia the lack of bloodshed is threatening to bore you. Yikes."

    "You elect to take a seat on the throne since it's really the only place to sit down in this room. You don't think anybody will mind. You've got quite the renowned ass in some parts."

    "..."

    "Okay, maybe YOU mind, because this throne has a super uncomfortable lump in it."

    "You can't see anything out of the ordinary? You pat the throne down and you definitely feel that lump in one very particular spot. Is there... something hidden under the cushion???"

    $ fse_achtoast("__p__journal_obtained")
    $ achievement.grant("bfs_journal_obtained")

    "There's a little flap in the cushion you dig your hand into, and once you loot around in the fluff and foam, you manage to pull a whole ass black leather book out. What the fuck???"

    "It's got a big pointy {hemocolor=cerulean}M{/hemocolor} on it. The M probably stands for Massive because this thing's as thick as two dictionaries getting a little too close and personal to describe in a PG context."

    "You have every intention of sitting the fuck down and reading through this whole thing right here. You make yourself comfy on the throne, wiggle your ass right in, and..."

    "{size=-8}\"INTRUDER ALERT.\"{/size}"

    "Wait a minute. You didn't make that sound."

    "\"INTRUDER ALERT.\""

    "Okay you {i}definitely{/i} didn't make that sound. You don't even know of any intruders other than..."

label __p__drones:
    "Hm! This presents a problem."

    show !bg throne room with hpunch
    show bfs_drone with easeinbottom
    show bfs_drone as bfs_drone2 at xpos(-400) behind bfs_drone with easeinleft 
    show bfs_drone as bfs_drone3 at xpos(400) behind bfs_drone,bfs_drone2 with easeinright

    "Before you can continue boggling vacantly, a swarm of three bulky looking drones bust open the giant ornate doors at the end of the hallway. That gets your adrenaline pumping somewhat! Fuck!"

    "In a panic, you tuck and roll behind the nearest cover, which in your case happens to be a fish-shaped shrub."

    show blackcover with moveinbottom

    "Cowered like a coward, you screw your eyes shut and wait for a big metallic hand to grab you by the scruff of your hoodie and send you back to the title screen."

    "..."

    "...You hear the mechanical whirring getting closer."

    "....."

    ".........."

    hide bfs_drone
    hide bfs_drone2 
    hide bfs_drone3
    #with easeoutright

    "The drones pass you without a second thought."

    hide blackcover with moveoutbottom

    "Holy shit, your shrub-hiding game is on POINT, no cardboard box necessary. Suck it, Metal Gear."

    "You guess you just convinced the big bad machines to forget that there was an"

    "{size=-8}\"MEENAH PEIXES, YOU ARE FORBIDDEN FROM LEAVING PAST YOUR CURFEW.\"{/size}"

    "Wait, you don't have a curfew. Also your name isn't Meenah."

    "By the time you put two and two together and realize that your new friend isn't named Trizza Tethis (thank god), you hear a bunch of cursing and screaming and like three different levels of ruckuses."

    !meenah "{size=-8}I SWEAR TO {pun=COD}GOD{/pun} YOU ARE DEAD FORKED MEAT{/size}" (show_hashtags="{size=-3}#DO YOU HEAR ME???????{/size}")

    !meenah "{size=-8}IM GONNA FUCKIN {pun=KRILL}KILL{/pun} YOU SO HARD YOUR DESCENDANTS WILL BE HATCHED WITH TINY LITTLE FORK HOLES IN THEIR {pun=CRABDOMENS}ABDOMENS{/pun} TO GO WITH THEIR *BLIND GLUBBIN PEEP BULBS* YOU {pun=LOUSEA}LOUSY{/pun} GOOD FOR {pun=NOFIN}NOTHING{/pun} LOOKOUT{/size}"

    "You really hope she isn't talking about you."
    
    show bfs_drone at xpos(-300) behind !meenah
    show !meenah pissed
    show !meenah at bobbing
    show bfs_drone as bfs_drone2 at xpos(300) behind !meenah, bfs_drone
    with easeinright

    "Peeking over the aquatic-themed foliage, you catch two of those hulking machines dragging a thrashing and screaming Meenah out. Oh, god, what have you done!?"

    "You can't imagine what horrible fate awaits her, but you know that you're not going to let it happen on your watch! Even if her moral compass is questionable at best!"

    #[SCENE: ZAP.]
    show !bg throne room with Fade(.25, 0.25, .25, color="#FFFFFF")

    "Taking exactly zero seconds to think your plan through, you ZAP right in front of the drones to block their path. HEY, you say, LET MY FRIEND GOH SHIT"

    #[SCENE: Screenshake, eyes close.]
    show !bg throne room with hpunch
    show blackcover with closeeyes

    "Without skipping a beat, one of the drones extends a mechanical arm and bonks you on the head, instantly knocking you unconscious."

    "Thankfully, being unconscious means you don't hear the rest of the extraordinarily unpleasant speech Meenah gives you."

    "Something about various methods she's threatening to fillet you with and some choice remarks about your brain size?"

    #[SCENE: Eyes open, everything's blurry.]
    hide bfs_drone
    hide bfs_drone2
    hide !meenah

    hide blackcover with openeyes

    show bfs_drone with easeinbottom

    "When you finally come to, you think you can make out one of those drones in front of you. It's hard to say, since you may or may not have a concussion right now?"

    "You have no idea how concussions really work and your brain hurts just thinking about it."

    "Or maybe it was just the drubbing it gave you earlier."

    "While you try to rub the sleep out of your eyes, you find that your hands are tied behind your back. No, wait, your whole body is trapped in some kind of person-sized net."

    show bfs_drone at bfs_zoom(1.1, 0.5)

    "What the hell! you say. The drone leans in a little closer and you hear some kind of high-pitched whirring sound. Is it scanning you? You think it's scanning you."

    "\"ALL ALIENS TO BE SENT TO THE FUNGEON UNTIL TRIAL. DO NOT RESIST. RESISTANCE IS SILLY.\""

    show bfs_drone at bfs_zoom(1, 0.5)

    "You must not be hearing the drone right. Fungeon? Like. Fun dungeon? That's totally what it is, isn't it."

    "Ugh, you hate plays on words."

    menu:

        extend ""

        "ZAP out of here.":
            pass

    "You close your eyes and think the homeliest thoughts you can, hoping for your wicked new wizard powers to kick in and get you out of here, but there's nothing doing."

    menu:

        extend ""

        "Um. ZAP out of here?":
            pass

    "You try again. No dice."

    "Okay maybe you DO have a concussion. Now you're starting to get worried about this fungeon, because despite half the name being fun, half the name is also dungeon."

    show bfs_drone at nod

    "The drone seems to have had enough of you wriggling on the floor like you're trapped in a sleeping bag and really need to pee, and hoists you up before flying you down to the end of the hall."

    "You're set on what feels suspiciously like a trap door, before..."

    show !bg throne room at hpunch
    pause(0.2)

    scene black
    with PushMove(0.2, "pushup")

    "Like the world's poshest dunk tank, you're deposited into a giant body of water and quickly realize that this fungeon might not have been designed for non-water breathers like you."

    call fseToastEnding pass ("__p__endcard_bad2", "__p__meenah_bad_end_2", False)
    return

label __p__meenahContinueTwo:

    "You come to the conclusion that being eaten alive by a giant sea creature is much less desirable than putting your foot down and offering a hand with packing."

    "With your shoulders puffed out, you march down the hallway you saw her head down and ignore the loud CLUNK of teeth hitting the window again."

    "You find the door you think you saw her enter, and you know you've got the right place when you hear rustling on the other side."

    #[SCENE: Wipe to Meenah's block.]
    scene !bg meenah block
    show !meenah observe 
    show !meenah at bobbing
    with wipeleft
    stop music fadeout 0.7
    queue music "{{assets}}/music/Chumming the Bassline.ogg" loop

    "After knocking to respect her privacy, you assert your dominance over the narrative by entering anyway."

    "This doesn't exactly make your finned friend feel like she's won the lottery, if the look she gives you is any indication. (It probably is.) She stops shoving the belongings of her whirlwind-struck hive into a suitcase to glare at you."

    show !meenah pissed at nod

    !meenah "man what in the glubbin FUCK did i just say" (show_hashtags="#p sure i used non fish words too")

    !meenah squint talk "dyou got someone on your tail or what"

    show !meenah squint

    "No, no, nothing like that. She's good to keep packing! You just wanted to keep her company, and also maybe help her out."

    "She seems like someone who would appreciate some free labor so you do your best to sweeten the deal with that very logic."

    show !meenah eyeroll at bounce(12, 0.0, 2)

    "She stares at you long and hard, but ultimately decides that kicking you out isn't worth it. She cocks her head to a big golden suitcase lying open and half-stuffed with trinkets in the middle of the room."

    !meenah idle talk "alright fine ive {pun=haddock}had it{/pun} up to here with doin this {pun=bullship}bullshit{/pun} {pun=myshellf}myself{/pun} {pun=anywaves}anyways{/pun}" (show_hashtags="#just dont fuck this up aight #aight")

    !meenah "shove {pun=anyfin}anythin{/pun} {pun=valbelugable}valuable{/pun} lookin in cuz im takin as much of this block with me as i can" (show_hashtags="#is \"{pun=valbelugable}valuable{/pun}\" too {pun=crabstract}abstract{/pun} #if it bling throw it in")

    show !meenah idle

    "Ever an obedient suitcase packer, you start rifling through the absolute mess of her bedroom floor and try to cram it into the already-stuffed suitcase."

    "The tridents are unfortunately like three times longer than the suitcase is wide so you defeatedly let them just roll off and clatter onto the floor."

    "You settle for a few baking apparatuses (apparati?) instead. Whisks, spatulas, you see something that looks like a remote control but with legs?"

    "Speaking of \"taking with her,\" though, that does raise a question: where is she taking all this junk to, exactly?"

    "You don't say the word junk but you say the rest of the words and replace the word junk with like, priceless treasure or something."

    !meenah idle talk "kind of a long story but fuck me i got my fins glubbed off plannin this shit out in the first place" (show_hashtags="#thanks for {pun=nofin}nothin{/pun} windfang")

    !meenah squint talk "so lemme {pun=skipper}skip{/pun} past all the boring {pun=carp}crap{/pun}"

    !meenah idle talk "im meenah peixes right"

    !meenah shrug "fated to challenge my ancestor for the throne and become the boss ass {pun=beach}bitch{/pun} future queen im meant to be" (show_hashtags="#air quotes")

    !meenah shrug puff "finally hand her blubbery ass to her after being the lamest and most glubbin {i}{pun=rowverbearing}overbearing{/pun}{/i} guardian a punk gal could ask for" (show_hashtags="#which i DIDNT ask for just ftr")

    show !meenah eyeroll at breathe
    !meenah "but maaaannnn" (show_hashtags="#le glubbin SIGH if ever there was one")

    !meenah squint talk "that {pun=reprawnsibility}responsibility{/pun} sounds like nothin but bad news from where im sittin and trust me im sittin pretty" (show_hashtags="#alt pun: responswimbility")

    !meenah snarky "so im running away" (show_hashtags="#{pun=clamscrayin}amscrayin{/pun} BITCH")

    "Oh! Wow! You guess you should have seen that coming because she did mention escaping. When you're a brutal fish princess, there's really only one form of escaping other than going to prison."

    "{i}Is she sure about this?{/i} you muse to yourself while examining a bundle of old shitty rope looped into a lasso. Being the ruler seems like it's a pretty sweet deal to you."

    "You're not sure if this rope is all that important, actually, so you just dump it on the floor at your feet."

    !meenah grumpy "i mean ruling sounds dope in THEORY"

    !meenah shrug "but being in charge only rules if the peeps youre {pun=bassing}bossing{/pun} around are worth commanding" (show_hashtags="#which they aint")

    !meenah shrug puff "besides"

    !meenah idle talk "tha best part of bein in charge is having the freedom to do {pun=waterever}whatever{/pun} you want w {pun=zeroe}zero{/pun} {pun=reefercussions}repercussions{/pun}"

    !meenah content "which is what im doing aint it"

    "This all comes off as incredibly immature to you, so you guess that Meenah of all people stepping out of the running for ruling this place isn't actually the worst thing in the world?"

    !meenah snarky "ok so MAYBE the best part is tellin {pun=otter}other{/pun} peeps what to do but close second" (show_hashtags="#{pun=gillver}silver{/pun} medal and all that")

    show !meenah ecstatic at nod(8,0.0,0.08)

    !meenah "maybe i could fly some suckas up to {pun=oarder}order{/pun} around"

    "You are suddenly feeling much better about helping her drop out of the royal running, here."

    "You pick up a hefty metal sphere and inspect it curiously. You ask her where she's running to while you try to determine what the hell this thing is."

    !meenah snarky "the moon"

    "excuse you but what"

    "In your stunned disbelief, your butterfingers lose grip of the orb and Meenah flips out when she notices."

    show !meenah pissed at nod

    !meenah "HEY CAREFUL WITH THAT-!"

    show !meenah at xpos(640)
    show !meenah shrug puff at bfs_dashhere(300)

    "She visibly flinches when it clunks against the ground, but nothing seems to happen."

    "Well, that's a lie, you feel a throbbing pain on your foot from the area of impact. You're hopping on the spot in pure fucking agony, actually."

    show !meenah grumpy puff at sigh

    "Once she notices the fact that the damage is minimal, she deflates at a pace you've never seen before."

    show !meenah threaten at xpos(640) with ease

    !meenah "careful with that shit {pun=DAM}DAMN{/pun}"

    show !meenah at nod

    "In a huff, she swipes the ball from the floor and stashes it... somewhere? You didn't quite see where while you're nursing your injury."

    !meenah pissed "do you WANNA blow us up or what"

    "Why the hell does she just have a bomb in her block??"

    !meenah idle talk "last resort"

    !meenah squint talk "might come in handy for the whole escape thing" (show_hashtags="#where was i")

    show !meenah squint

    "Right, escaping. She said she was going to... the moon?"

    !meenah idle talk "yeah the moon" (show_hashtags="#aint no thang")

    !meenah snarky "pink glowing ball in the sky"

    !meenah observe "that not a word where you come from or....." (show_hashtags="#alien terminology #i guess?? #{pun=whaliens}aliens{/pun} be whack")

    "No, no, you know what the moon is. The problem isn't a lack of knowledge."

    !meenah squint talk "then whats w/ you bein all bugeyed and shit"

    !meenah pissed "you think im dumb enough to run from the {pun=fintergalactic}intergalactic{/pun} throne by just moving down a subgrub???"

    !meenah grumpy puff "scratch that you think id stay on this dumb fuckin hellrock if i COULD?????" (show_hashtags="#you {pun=shore}sure{/pun} aint the think pans of this {pun=operocean}operation{/pun} dats fo {pun=shore}sure{/pun}")

    !meenah shrug "id ditch this joint for a seashell"

    "Fair point. This planet kind of sucks."

    "You're just... not sure if your powers are on an interplanetary level? Okay so maybe the problem IS a lack of knowledge, but only technically."

    !meenah squint talk "yo whats the big glubbin deal you cant know for {pun=shore}sure{/pun} if you dont try right"

    !meenah idle talk "if youre just gonna roll over and take it then i guess youll fit right in on this {pun=laccodaisy}lackadaisy{/pun} grubby planet lol" (show_hashtags="#important note: not {pun=laughfin}laughin{/pun} out loud #important = port pun fyi")

    show !meenah idle

    "Geez, if she thinks THIS planet is cushy and comfy, she must be the toughest customer in this whole damn store of a planet."

    "Looking at her, you don't exactly doubt this. You've seen murderclowns bathed in blood before, too!"

    !meenah idle talk "look im not gonna bother keeping you around if you aint in ship shape so you gotta work this out"

    !meenah eyeroll annoyed "can you or can you {pun=naut}not{/pun} zap to the moon"

    !meenah "cmon youve got to the count of five" (show_hashtags="#1 2 3 4 #chop chop")

    "Give you a second, geez! Where's the fire?? Can't a protagonist try to figure their powers out in peace?"

    show !meenah squint

    "Meenah's expression goes from being annoyed with you to being mildly alarmed. Her fins do a little fluttering motion you're trying to interpret on top of trying to figure out where the fire is."

label __p__dronesbreakin:

    !meenah squint talk "shit"

    !meenah pissed "shit shit SHIT"

    show !bg meenah block with hpunch
    show !meenah at bfs_dashhere(900, 0.3)
    show bfs_drone at xpos(-300) with easeinleft
    show bfs_drone2 at xpos(-550) behind bfs_drone with easeinleft

    "The source of her panic makes itself pretty apparent when the door to her respiteblock is busted down by a giant buff robot drone, tailed by two others for backup."

    "The drones start spouting something about an alien kidnapping the heiress before Meenah yoinks one of the tridents you'd dumped on the suitcase and completely severs the first drone's head."

    show !meenah threaten at flipped
    show !meenah at !stab
    pause(0.17)
    show bfs_drone at !dronedeath
    pause(1.1)
    hide bfs_drone
    pause(0.2)

    show !meenah at nod(-8)
    !meenah "guess the cakes done" (show_hashtags="#stuck a fork in #bon appetit bitch")

    hide !meenah grin with easeoutleft
    "Its speech slows to a slurred, glitchy crawl as its metallic body drops dead. In a heartbeat, the suitcase vanishes into a pink card-looking thing and she makes a run for it."

    "Before you can accuse her of leaving you behind, you notice that she's got a tail of her own. Of rope, namely. You look down just in time to see your foot in the rope loop before you're forcefully dragged behind her."

    "Springboarding off of the first drone corpse, she slides under the other two like a baseball star (subsequently dragging your face along the floor in the process) before sprinting off."

    "Your helpless body is colliding with all sorts of decorative furniture on your way out."

    #[SCENE: Hallway.]
    scene !bg throne room at bfs_running with wiperight

    "Holy shit, how strong IS this girl?? She's like, thirteen years old and she's hauling you behind her like she's flying a kite."

    "You feel a sharp tug on your leg as she drags you closer to her, which you're thankful for because the drones are hot on your trail, and more are starting to emerge from various side entrances."

    show !meenah grin
    show !meenah at bfs_running
    with easeinbottom #at driving with easeinbottom

    "Soon enough you manage to roll and stumble onto your feet, but you're still having a hard time keeping up with her running speed. She's really going for it, it's like you're running after the bus you just missed."

    "Except, you know, with incredibly deadly stakes."

    !meenah "HEY HORNLESS"

    "She doesn't bother looking behind her, but your panicked response lets her know that you're present and accounted for."

    !meenah grin shine "READY TO FIND OUT HOW POWERFUL YOU {pun=REELY}REALLY{/pun} ARE" (show_hashtags="#IT SINK OR SWIM HERE")

    "That's an awfully ominous statement, but when you realise what she's holding, your choices are clear."

    "She's holding the bomb from earlier, except the little glass light on the side is blinking which obviously means an explosion is impending unless you do something and you do it fast."

    #[SCENE: Eyes close.]
    show blackcover with closeeyes

    "You're freaked out as all fuck, but you've got no choice. You close your eyes and try to figure out how your powers work."

    "GO MOON."

    "Uh. ZAP. UP-UP-AND-AWAY-ZAP."

    "SHAZAM? GO. GO. GO, MOON, GO."

    "Please. You don't want to die."

    "You can't die."

    hide blackcover with openeyes

label __p__landonmoon:

    "You reach forward to grab her hand and, just as you hear the sound of glass smashing from bodily contact, you vanish into thin air."

    #[SCENE: Eyes open to Moon BG.]
    scene bfs_bg pink moon
    with Fade(.25, 0.25, .25, color="#FFFFFF")
    stop music fadeout 0.7
    queue music "custom_assets_bfs_shared/music/Interlude.ogg" loop
    
    show !meenah pissed:
        xpos -800 ypos 300
        linear 0.3 xpos 320 ypos 720 rotate 25
        easein 0.3 xpos 800 ypos 1000 rotate 55
    pause(0.3)
    show bfs_bg pink moon at hpunch
    hide !meenah

    "Your forward momentum ends up sending the both of you skidding along the lunar surface before the two of you slow to a stop in a pile of limbs and post-adrenaline exhaustion."

    #[SPRITE: Meenah slides up.]
    show !meenah squint with easeinbottom

    "When Meenah sits up, there aren't words for how shocked she looks. She's staring at the ground — it's pink and crusty — and slowly, her head tilts up and notices the giant celestial body in the distance."

    "Holy shit. You're..."

    !meenah ecstatic "were on the moon"

    show !meenah at nod

    !meenah "holy SHIT" (show_hashtags="#YO")

    show !meenah at nod(12,0.0,0.1,0.0,2)

    #W---E
    !meenah "{quirked=W---E}WE{/quirked} DID IT" (show_hashtags="#YOOOOO")

    "She raises her fists in the air triumphantly and, despite what you've heard about space, you very much hear the way she screams with joy."

    "She detaches herself from you and stands up straight in a power stance, which you mirror once you get over the way every part of your body aches."

    show !meenah at shudder
    #FR-E-----E
    !meenah "EAT A LOAD A MOBY SHIT IM HOME {quirked=FR-E-----E}FREE{/quirked}" (show_hashtags="#YEEEAAAAHHHH")

    show !meenah grin shine at bobbing
    "In a display of great maturity and wisdom, she flips her home planet off with both hands. You know what? You do too."

    "As much as you've spent a lot of time on Alternia, you're not sad to maybe, you know, not do that anymore."

    "Something nags at you. Shit, you're just realising, this is the first time you've managed to leave Alternia since you crash landed."

    "Something else nags at you and that's a beeping sound nearby, now audible since Meenah's stopped yelling."

    show !meenah pissed at nod
    "You both turn in horror when you notice how frantic the sound is getting."

    "It's your turn to think fast and step up to the challenge, so with reckless abandon, you cradle the bomb in your arms and ZAP halfway across the moon."

    #[SCENE: ZAP. Meenah sprite disappears.]
    hide !meenah
    show !bg pink moon b
    with Fade(.25, 0.25, .25, color="#FFFFFF")

    "You hurl the bomb as far as your skinny arms will allow. You're so quick-thinking that you barely register the fact that you're facing a huge stone temple. Oops."

    #[SCENE: Screenshake.]
    show !bg pink moon b with vpunch
    pause(0.2)
    hide !bg pink moon b
    show bfs_bg pink moon
    with dissolve

    "With a BOOM, the temple is no more. Instantly reduced to rubble. Holy shit, Meenah was going to kill herself if things went south?? With your heart crawling into your throat, you retreat."

    #[SCENE: ZAP.]
    show bfs_bg pink moon
    show !meenah content
    with Fade(.25, 0.25, .25, color="#FFFFFF")

    "Meenah seems surprised to see you return, but she gives you a satisfied smirk when she assesses your alive status."

    !meenah grin "yo zappy"

    show !meenah at nod
    "Meenah pipes up and points at the giant planet in the sky."

    !meenah content "ever seen the blowhole thing at once befoar" (show_hashtags="#{pun=meh #blowhole be kind of a stretch}blowhole like whole #meh{/pun}")

    "No, you tell her, this is the first time you've seen what the place looks like. You think you might've seen a chart once or twice at a friend's place, but this..."

    "This takes your breath away (and not in the outer space way)."

    !meenah "yeah lmao" (show_hashtags="#moons be breathable thank fuck")

    !meenah snarky "thats all of beforus"

    "Hahahah, what?"

    show !meenah content
    "You don't say that out loud, but you do fall dead silent as you try to decipher what she just said. What the hell is Beforus?"

    "This is literally the FIRST time you've heard the term and you have like 40 troll friends now."

    "You mumble a half-hearted wow that Meenah probably takes to be your aforementioned breathlessness as you stand there and... slowly start to question everything."

    "Now that she mentions it, you do find it a little strange how one of the planet's moons seems to be missing. Wasn't there a green one? You're pretty sure there was a green one."

    "Quietly, hesitantly, you ask Meenah if she's happy about leaving Alternia."

    !meenah squint talk "the hell is {pun=altunia}alternia{/pun}" (show_hashtags="#and {pun=moar}more{/pun} importantly why should {pun=anymoby}anybody{/pun} give two shits")

    !meenah "sounds like the fakest load a carp guts i never heard of"

    show !meenah squint

    "Okay! You guess you've got a mystery on your hands! You're going to bottle that mental breakdown to open some other time!!! Right now you're just lucky to be alive."

    "You're gonna zap back at some point and like, try to figure out what the deal is, but for now? You're sitting down and taking in the sight."

    show !meenah content

    "Existential crisis or not, space is beautiful. Nothing can touch you here."

    "No {i}one{/i} can touch you here."

    "You can't help but wonder how Meenah's going to manage all by herself out here, with no civilisation to speak of. You wonder just loud enough for you to know that she heard you."

    !meenah snarky "ill get hooked up to the net {pun=eventunally}eventually{/pun}" (show_hashtags="#net like fish net #38D")

    !meenah grumpy puff "you think im dumb enough to plan my {pun=runawave}runaway{/pun} for HALF A SWEEP w/o {pun=conchsidering}considering{/pun} that" (show_hashtags="#trolls got space travel on {pun=lochdown}lockdown{/pun} #not that theyll find me here")

    !meenah content "interplanet adaptors aint hard to come by when you rich lmao" (show_hashtags="#big {pun=surfprise}surprise{/pun} ya grls f-ing $tacked")

    "What about her friends, though? She's gotta have friends, right? She mentioned Windfang. You think it's a stupid name but friends have stupid names sometimes."

    "Aren't they gonna miss her? Isn't she going to miss {i}them?{/i}"

    "She flatly ignores your question and goes on like you never opened your mouth in the first place."

    !meenah idle talk "either {pun=wave}way{/pun} id still rather die of {pun=boardom}boredom{/pun} and starvation than live having to wear big {pun=poolfy}poofy{/pun} dresses pretending to give a single clammin fuck about being a \"good empress\""

    !meenah shrug "if im kickin it im kickin it with my own pair of boots you dig"

    "This troll really is ride or die, huh?"

    !meenah shrug puff "get shit done or die imo"

    "You guess that explains the bomb."

    !meenah squint talk "what no itll take way more than a dinky little boom to finish me off" (show_hashtags="#cant say the same for {pun=rowbots}robots{/pun} tho")

    !meenah idle talk "but i mean even if i wasnt basically fucking invincible"

    !meenah eyeroll annoyed "id have the gills to do it unlike EVERY GLUBBIN ONE ELSE"

    #)(AT---E
    !meenah pissed "which is why i fucking {quirked=)(AT---E}HATE{/quirked} it on beforus" (show_hashtags="#besnoreus")

    show !meenah threaten at nod

    #DO---ES
    !meenah "{pun=nomoby}nobody{/pun} {quirked=DO---ES}DOES{/quirked} {pun=anyfin}anything{/pun} they all just stand around with their thinkin gourds up their waste chutes hopin someone else will take care of it" (show_hashtags="#why you think we got robo slaves huh")

    !meenah eyeroll annoyed "that or they just aint allowed to do stuff thats \"too dangerous\"" (show_hashtags="#BARF")

    !meenah snarky "but thats enough scalding leaf water off my chest it aint my problem no mo"

    "You nod solemnly and, despite your best efforts to deny it, somewhat awkwardly and complacently. You're just kind of naturally inclined to agree with her at this point."

    "Beforus doesn't sound like Alternia, from what brief and honestly kind of cryptic descriptions you got just now. You can't imagine that planet in front of your eyes being anything close to cuddly or soft."

    "You just assumed Meenah was really really hardcore but you're starting to wonder if something's up."

    "Is this one of those Berenstain/Berenstein situations where you just wake up in some alternate universe? That sounds like a load of hoofbeastshit."

    "You decide that now's maybe time to head back down and investigate."

    show !meenah content at nod

    "When you mention such to Meenah, she gives you a passive shrug, but coughs to grab your attention before you make the metaphysical jump back down."

    !meenah "hey {pun=reel}real{/pun} quick"

    !meenah "just wanted to say"

    show !meenah idle

    "There's a small pause before she picks herself back up, almost like she's not used to speaking so seriously."

    !meenah idle talk "i can dig the cut of your jib"

    !meenah "if youre lookin to study nerd shit i can hook you up w/ someglub who knows a thing or two"

    !meenah content "but lets link up every once in a {pun=whale}while{/pun} you hear"

    !meenah "thats an {pun=oarder}order{/pun}"

    "You give her an affirmative nod and a salute, and she rolls her eyes at you. She's smiling, though. Just a little."

    !meenah squint talk "no but {pun=seariously}seriously{/pun} if you dont i will hunt you down and {pun=krill}kill{/pun} you"

    call fseToastEnding pass ("__p__endcard_good", "__p__meenah_friended", True)
    return
