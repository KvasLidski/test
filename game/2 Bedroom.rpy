
label prebedroom:
    $ morning = 0
    play music rest fadein 3.0
label bedroom:
    scene bg bedroomnight
    show mc:
        xpos 850
    show pinkbody 0:
        xpos 850
    show mcpiercings blank:
        xpos 850
    show mccatears blank:
        xpos 850
    show mco:
        xpos 850
    show mch:
        xpos 850
    show pinkhair 0:
        xpos 850
    call clothes from _call_clothes
    show mce happy:
        xpos 850
    with d
    label variableevents:
        label pregnancy:
            if pregnancyterm >= 10 and pregnancyshowing == 0:
                $ pregnancies += 1
                $ pregnancyshowing = 1
                $ pregnancyterm += 1
                $ condomon =  0
                if pregnancyintro == 0:
                    $ pregnancyintro = 1
                    show mce neutral with d
                    "Oh sheesh... There's no doubt about it... I'm definitely pregnant, I can already feel my belly bloating."
                    "(Whoops! You're pregnant, but it's not permanent! Check the Hospital for more information.)"
                    "(This affects a lot of things. Find out and have fun!)"
                else:
                    show mce neutral with d
                    "Welp, pregnant again!"
            if pregnancyterm == 3:
                "Uhmm... Hmm... That's strange, my period hasn't come through."
        if personality == 1 and sd > 50:
            $ personalityname = "An 'Innocent' Girl"
        if personality == 1 and sd > 75 and shame < 30:
            "(Innocent Girl) I started University as an innocent girl, but..."
            show mce sad with d
            "Right now... Right now... I can't even relate to that person."
            "Just who am I now?"
            "So desperate for money."
            "Regularly lustful with a strong desire for sex."
            "I'm not innocent at all anymore..."
            show mce horny with d
            "And the fact I enjoy my transformation terrifies me."
            play sound success
            "(Your personality has changed from 'An Innocent Girl' to 'Corrupted Innocence'!)"
            "(You now gain +10%% Sexual Desire, and +10%% Shame)"
            $ personality = 6
            $ sdmult = 1.1
            $ shamemult = 1.1
            $ personalityname = "Corrupted Innocence"
        if personality == 4 and shame == 0:
            "(Overly Confident) Sigh... I've powered through my troubles with my confidence alone..."
            "But I have to say, it does feel like I've given up my sense of shame in that pursuit."
            "Even if I am being too hardy. I think I'll just get through this if I push through my doubts."
            "I'll have to discover myself in new ways, and perhaps exploring myself sexually will help me deal with that."
            "(Your personality has changed from 'Overly Confident' to 'Sexually Confident'!)"
            "(You now gain +20%% Sexual Desire.)"
            $ sdmult = 1.2
            $ personality = 7
            $ personalityname = "Sexually Confident"
        call potencollegemissed from _call_potencollegemissed
    $ dsd = int(sd)
    $ dshame = int(shame)+1
    label postbedroom:
        pass
    call screen bedroom
    with d

label inventory:
    hide bedroom screen border
    "Is there something I want to use?"
    menu inventorymenu:
        "[condoms] Condom(s)" if condoms > 0:
            "Not a lot I can do with these on my own."
            jump inventorymenu
        "[aphrodisiac] Aphrodisiac" if aphrodisiac > 0:
            if aphrodisiacdrank == 1:
                "I'm already extremely sensitive! There's no way I'm having two!"
                jump inventorymenu
            "*Gulp*... If I drink this, I'll become incredibly sensitive and aroused."
            menu:
                "Drink! (+20 Sexual Desire, -10 Shame, until morning)":
                    $ aphrodisiac -= 1
                    $ aphrodisiacdrank = 1
                    $ sd += 20
                    $ shame -= 10
                    "Haahhh... I feel hotter already."
                    if qlightweight == 1:
                        $ sd += 20
                        $ shame -= 10
                        "And it's hitting me even harder because I'm a complete lightweight. (2x Effect!)"
                        play sound success
                        "(+40 Sexual Desire, -20 Shame)"
                    else:
                        play sound success
                        "(+20 Sexual Desire, -10 Shame)"
                    jump inventorymenu
                "No way!":
                    jump inventorymenu
        "[fertilityplus] Fertility+ Tablets" if fertilityplus > 0:
            "*Gulp*... If I take this, I'll become incredibly fertile..."
            menu:
                "Let's do it! (+99%% fertility chance until morning)":
                    $ fertile = 1
                    $ fertilityplus -= 1
                    $ pregchan = 0
                    "Haahhh... I can't believe I'm doing this..."
                    jump inventorymenu
                "No way!":
                    jump inventorymenu
        "Pepper Spray" if pepperspray == 1:
            "This protects me against perverts outside. Should I keep it on my person?"
            menu:
                "Pepper Spray On":
                    $ peppersprayon = 1
                "Pepper Spray Off":
                    $ peppersprayon = 0
            jump inventorymenu
        "The Pill" if pill == 1:
            if onpill == 1:
                "I am currently on the pill."
                menu:
                    "Stop taking the pill.":
                        $ onpill = 0
                        "Hm... I should probably save these for later, right? Right..."
                        jump inventorymenu
                    "Keep on keeping on!":
                        jump inventorymenu
            else:
                "I am currently off the pill."
                menu:
                    "Take the pill.":
                        $ onpill = 1
                        "Too risky to stay off it, let's start taking them again."
                        jump inventorymenu
                    "Keep on keeping on!":
                        jump inventorymenu
        "Vibrator" if vibrator == 1:
            "I'll use this from the bed when I'm ready to masturbate."
            jump inventorymenu
        "Dildo" if dildo == 1:
            "I'll use this from the bed when I'm ready to masturbate."
            jump inventorymenu
        "Close":
            if morning == 1:
                jump bedroommorning
            else:
                jump bedroom
jump bedroom

label outside:
    if qintrovert == 1:
        $ alonemult = 1
    scene bg door with dissolve
    jump worldmap
jump bedroom
label bed:
    scene bg bedsex
    if mrslime == 1:
        show mrslime:
            xpos 50
    if morning == 1:
        "A nap, or something else?"
    else:
        "An early night, or maybe something else?"
    menu bedmenu:
        "Mr Slime" if mrslime == 1:
            menu:
                "Double Penetration":
                    mc "Let's have some fun, Mr. Slime!"
                    play sound2 foreplay2
                    scene tentaclesdpsexb
                    show tentaclesdpsexbedroom
                    if tan == 1:
                        show tentaclesdpsexbtan
                    if pregnancyshowing == 1:
                        show tentaclesdpsexbp
                        if tan == 1:
                            show tentaclesdpsexbtanp
                    if hair == 1:
                        show tentaclesdpsexh black
                    if hair == 2:
                        show tentaclesdpsexh blonde
                    if piercingson == 1:
                        show tentaclesdpsexpiercings
                    show tentaclesdpsex 1
                    show tentaclesdpsexbedroomclip
                    with d
                    mc "Mmphh, I'm all yours."
                    jump doubletentaclessex
                "Standing Sex":
                    mc "Let's have some fun, Mr. Slime!"
                    play sound2 foreplay2
                    scene tentaclesstandingsexb
                    show tentaclesstandingsexbedroom
                    if tan == 1:
                        show tentaclesstandingsexbtan
                    if pregnancyshowing == 1:
                        show tentaclesstandingsex1p
                        show tentaclesstandingsexbp
                        if tan == 1:
                            show tentaclesstandingsexbtanp
                    if hair == 1:
                        show tentaclesstandingsexh black
                    if hair == 2:
                        show tentaclesstandingsexh blonde
                    if piercingson == 1:
                        show tentaclesstandingsexpiercings
                    show tentaclesstandingsex 1
                    show tentaclesstandingsexbedroomclip
                    show mrslime:
                        xpos 50
                    with d
                    mc "Mmphh, I'm all yours."
                    jump standingtentaclessex
                "Back":
                    jump bedmenu
        "Masturbate":
            menu bedmm:
                "Use Fingers":
                    scene bg black with d
                    play music action fadein 3.0
                    "I shimmy my clothes off and lay down comfortably on bed."
                    scene masturbationb
                    if tan == 1:
                        show masturbationbtan
                        if pregnancyshowing == 1:
                            show masturbationbtanp
                    if hair == 1:
                        show masturbationh black
                    if hair == 2:
                        show masturbationh blonde
                    if piercingson == 1:
                        show masturbationpiercings
                    show masturbation 1a
                    if pregnancyshowing == 1:
                        show masturbatione pregnant
                    with d
                    "My hands roam down the warm skin of my body, one finding itself carassing my breast and the other between my legs."
                    play ambience sex fadein 3.0
                    $ rand3 = renpy.random.randint(1,2)
                    if rand3 == 1:
                        "My pussy is already a little wet as I readily rub my clit."
                    else:
                        "My hands roam down to my thighs and begin to gently rub my clit."
                    $ rand3 = renpy.random.randint(1,2)
                    if rand3 == 1:
                        "Meanwhile, my nipples rapidly stiffen as I tease and squeeze my chest."
                    else:
                        "Occasionally I bring my right hand to my breasts, teasing and squeezing my sensitive nipples."

                    "What should I think about?"
                    menu:
                        "My crush...":
                            "I gasp as I sink two fingers deep into my pussy, all at the thought of having my crush's cock slide deep inside."
                        "A stranger...":
                            "I rub my clit faster as the thrill and excitement of being taken by someone I don't know fills my thoughts."
                        "Something... inhuman?":
                            "I stifle moans as I imagine something inhuman and lustful ravaging me from behind."
                            "Sliding two fingers in, I imagine it taking me with its unique tool."
                        "Watch porn." if xtube == 1:
                            "With my knowledge of xTube, I stick on a few videos until I find a hot one."
                        "Browse hentai!":
                            "Why think? I sift through some erotic art until I find something that really gets me going."
                        "Girls...":
                            "Haahh... I'm horny for girls today, soft and curvy... I rub my clit at the thought of having a cute girl between my thighs."
                    "I speed up, causing lewd wet noises which only turn me on more."
                    $ rand3 = renpy.random.randint(1,2)
                    if rand3 == 1:
                        "Pleasure surges and shivers throughout my body as my inevitable orgasm slowly builds."
                    else:
                        "The pleasure really builds, and I'm so sensitive that I can feel it throughout my entire body. Without really thinking, my hand speeds up as I push for the release of my orgasm."
                    show masturbation 1b with d
                    "Losing my mind to the pure primal instinct of the moment, I rub my pussy with reckless abandon as I push for the finish."
                    play sound cum
                    show masturbation 1b with cum
                    play sound cum
                    show masturbation 1b with cum
                    "Swelling in my mind and body, pure euphoria overwhelms me as I indulge in a potent orgasm."
                    play sound cum
                    show masturbation 1b with cum
                    play sound cum
                    show masturbation 1b with cum
                    "I enjoy the high to its fullest until it finally fades and I'm left panting and slightly sweaty on my bed."
                    stop ambience fadeout 3.0
                    scene bg black with dissolve
                "Use Vibe (Vibe Required)":
                    if vibrator == 0:
                        "I don't have one of those."
                        jump bedmm
                    "The vibrator definitely gives me stronger orgasms than I can achieve with just my fingers. I can't wait!"
                    play sound equip
                    show masturbation2b
                    if tan == 1:
                        show masturbation2btan
                        if pregnancyshowing == 1:
                            show masturbation2btanp
                    if hair == 1:
                        show masturbation2h black
                    if hair == 2:
                        show masturbation2h blonde
                    if piercingson == 1:
                        show masturbation2piercings
                    show masturbation2e 1
                    show masturbation2 vibe
                    if pregnancyshowing == 1:
                        show masturbation2p
                    with d
                    "I waste no time getting comfortable in bed, my hands brushing over my supple skin as I get into the mood."
                    "My pussy is already a little wet as I insert the vibe, placing the control device next to my butt."
                    play ambience sex fadein 3.0
                    "Hmm, let's try the first level first..."
                    show masturbation2e 2 with d
                    "Woah! This feels good already!"
                    "Ooohhh, it's like a constant pleasureful tingle. Mmmphhh..."
                    "Without even realizing it, I lose myself in the moment and the pleasure."
                    show masturbation2e 1 with d
                    "It's a good warmup, but I'll need to turn it up to start really feeling it."
                    "I rotate the pink vibe to level 2 and the difference is immediately noticable!"
                    show masturbation2e 2 with d
                    "Pleasure surges and shivers throughout my body as the vibrator moves like crazy!"
                    "It's not just a flatline of pleasure either, I can feel my body gradually grow more sensitive."
                    mc "Aahhh, aahhhh..."
                    "I have to hold my moans back slightly, lest I not disturb my neighbours and embarass myself."
                    show masturbation2e 1 with d
                    "I bite my lip as I make the decision to go all out on the highest level. I'm gonna come like crazy!"
                    show masturbation2 vibe with vpunch
                    "*Click*... *BZZZZZZZZZZT!*"
                    show masturbation2e 2
                    show masturbation2 vibe with vpunch
                    "Phew! It's vibrating so hard and fast that it almost feels like my entire pelvis is shaking!"
                    show masturbation2 vibe with vpunch
                    "The pleasure is overwhelming and an inevitable orgasm builds faster than I could possibly anticipate."
                    show masturbation2 vibe with vpunch
                    "Losing my mind to the pure primal instinct of the moment, I rub my pussy recklessly as I push for the finish."
                    play sound cum
                    show masturbation2 vibe with cum
                    play sound cum
                    show masturbation2 vibe with cum
                    "Swelling in my mind and body, pure euphoria overwhelms me as I indulge in a potent orgasm."
                    play sound cum
                    show masturbation2 vibe with cum
                    play sound cum
                    show masturbation2 vibe with cum
                    "I enjoy the high to its fullest until it finally fades and I'm left panting and slightly sweaty on my bed."
                    stop ambience fadeout 2.0
                    show masturbation2e 1
                    hide masturbation2 vibe
                    with d
                    "I have to quickly fumble to turn the vibrator off before it drives me completely insane with pleasure."
                    scene bg bed
                    with d
                    "Haaahhh... I merely lay in bed for a while in a euphoric daze as I catch my breath."
                    scene bg bed
                "Use Dildo (Dildo Required)":
                    if dildo == 0:
                        "I don't have one of those."
                        jump bedmm
                    scene bg black with d
                    play music action fadein 3.0
                    "I shimmy my clothes off and lay down comfortably on bed."
                    play sound equip
                    show masturbation2b
                    if tan == 1:
                        show masturbation2btan
                        if pregnancyshowing == 1:
                            show masturbation2btanp
                    if hair == 1:
                        show masturbation2h black
                    if hair == 2:
                        show masturbation2h blonde
                    if piercingson == 1:
                        show masturbation2piercings
                    show masturbation2e 1
                    show masturbation2 dildo
                    if tan == 1:
                        show masturbation2 dildotan
                    if pregnancyshowing == 1:
                        show masturbation2p
                    with d
                    $ rand3 = renpy.random.randint(1,2)
                    if rand3 == 1:
                        "My pussy is already a little wet as I readily tease it with the tip of the dildo. Gradually, I ease it in inch by inch."
                    else:
                        "I coo as I press the cool tip of the dildo against my vaginal opening and press it deeper inside."
                    play ambience sex fadein 3.0
                    if rand3 == 1:
                        "Ohhh, it's tiiight... But that's good, I like it when there's a bit of resistance."
                    else:
                        "Mmmphh, it fills me up so much, and feels so, so good!"
                    "What should I think about?"
                    menu:
                        "My crush...":
                            "I gasp as I sink the dildo deeper into my pussy, all at the thought of having my crush's cock slide deep inside."
                        "A stranger...":
                            "I rub my clit faster as the thrill and excitement of being taken by someone I don't know fills my thoughts."
                        "Something... inhuman?":
                            "I stifle moans as I imagine something inhuman and lustful ravaging me from behind."
                            "Sliding the dildo in, I imagine it taking me with its unique tool."
                        "Watch porn." if xtube == 1:
                            "With my knowledge of xTube, I stick on a few videos until I find a hot one."
                        "Browse hentai!":
                            "Why think? I sift through some erotic art until I find something that really gets me going."
                        "Girls...":
                            "Haahh... I'm horny for girls today, soft and curvy... I thrust the dildo at the thought of having a cute girl between my thighs."
                    "I speed up, causing lewd wet noises which only turn me on more."
                    if rand3 == 1:
                        "The thick dildo really fills me up, grinding against each and every sensitive nerve ending along my pussy."
                    else:
                        "It's so big it even manages to create a pleasurable sensation against my clit! It's not long until I see the early signs of my orgasm rising from deep within."
                    "Pleasure surges and shivers throughout my body as my inevitable orgasm slowly builds."
                    show masturbation2e 2 with d
                    $ rand3 = renpy.random.randint(1,2)
                    if rand3 == 1:
                        "Losing my mind to the pure primal instinct of the moment, I pound my pussy with reckless abandon as I push for the finish."
                    else:
                        "With more lust than thought, I close my eyes tightly as I push for my orgasm."
                    play sound cum
                    show masturbation2e 2 with cum
                    play sound cum
                    show masturbation2e 2 with cum
                    "My mind goes blank as a powerful orgasm takes over. I keep slamming the dildo into my pussy to push the high as far as it can go."
                    play sound cum
                    show masturbation2e 2 with cum
                    play sound cum
                    show masturbation2e 2 with cum
                    "*Thwap, thwap, thwap!* Recklessly I fuck myself throughout my entire orgasm, the pleasure is euphoric."
                    "I enjoy my climax to its fullest until it finally fades and I'm left panting and slightly sweaty on my bed."
                    stop ambience fadeout 3.0
                    scene bg black with dissolve
                "Back":
                    jump bedmenu
            "I get up and slip my pyjamas back on."
            play sound success
            $ masturbations += 1
            $ sdgain = 1
            call sdgain from _call_sdgain_13
            "(+[fsd] Sexual Desire!)"
            stop music fadeout 3.0
            if morning == 1:
                jump postworktrans
            "Afterwards, I get under the covers and soon drift off to sleep."
            jump morning
        "Nap" if morning == 1:
            stop music fadeout 3.0
            if mrslime == 1:
                "I crawl into bed with Mr. Slime and soon drift off to sleep."
            else:
                "I get into bed and soon drift off to sleep."
            jump postworktrans
        "Sleep" if morning == 0:
            stop music fadeout 3.0
            "I get into bed and soon drift off to sleep."
            jump morning
        "Cheats":
            if dtc == 0:
                "Are you sure you want to use cheats? It may ruin your experience and result in inconsistencies."
                "It's recommended to play through the game normally at least once."
                menu:
                    "Cheats for life!":
                        $ dtc = 1
                        jump cheatsmenu
                    "You're right, I'll go play normally.":
                        jump bedmenu
            else:
                menu cheatsmenu:
                    "Change My Name":
                        python:
                            mc = renpy.input("Name your character.")
                            mc = mc.strip()
                            if not mc:
                                mc = "Taco"
                        jump cheatsmenu
                    "Extra $$$":
                        menu cheatsmoneymenu:
                            "Money: $[money]"
                            "+$50":
                                play sound success
                                $ money += 50
                                jump cheatsmoneymenu
                            "+$500":
                                play sound success
                                $ money += 500
                                jump cheatsmoneymenu
                            "+$5000":
                                play sound success
                                $ money += 5000
                                jump cheatsmoneymenu
                            "Back":
                                jump cheatsmenu
                    "Alter Stats":
                        menu cheatsstatsmenu:
                            "Smarts: [smarts], Sexual Desire: [sd], Shame: [shame]"
                            "+2 Smarts":
                                play sound success
                                $ smarts += 2
                                jump cheatsstatsmenu
                            "-2 Smarts":
                                play sound success
                                $ smarts -= 2
                                jump cheatsstatsmenu
                            "+2 Sexual Desire":
                                play sound success
                                $ sd += 2
                                jump cheatsstatsmenu
                            "-2 Sexual Desire":
                                play sound success
                                $ sd -= 2
                                jump cheatsstatsmenu
                            "-2 Shame":
                                play sound success
                                $ shame -= 2
                                jump cheatsstatsmenu
                            "+2 Shame":
                                play sound success
                                $ shame += 2
                                jump cheatsstatsmenu
                            "Max Stats":
                                play sound success
                                $ shame -= 100
                                $ sd += 200
                                $ smarts += 100
                                jump cheatsstatsmenu
                            "Reset Stats":
                                play sound success
                                $ shame = 100
                                $ sd = 0
                                $ smarts = 0
                                jump cheatsstatsmenu
                            "Back":
                                $ dsd = int(sd)
                                $ dshame = int(shame)+1
                                $ dsmarts = int(smarts)
                                jump cheatsmenu
                    "Art Gallery":
                        jump cheatgallery
                    "Become Pregnant" if pregnant == 0:
                        "You step into an alternative timeline where you're pregnant."
                        $ pregnancy = 1
                        $ pregnant = 1
                        $ pregnancyshowing = 1
                        $ pregnancyterm = 10
                        $ pregnancies += 1
                        jump cheatsmenu
                    "Remove Pregnancy" if pregnant == 1:
                        "You step into an alternative timeline where you're not pregnant."
                        $ pregnancy = 0
                        $ pregnant = 0
                        $ pregnancyshowing = 0
                        $ pregnancyterm = 0
                        $ pregnancies -= 1
                        jump cheatsmenu
                    "Natural Pregnancy Speed":
                        menu:
                            "1x Speed (280 Days)":
                                $ pregnancyspeed = 1
                            "2x Speed (140 Days)":
                                $ pregnancyspeed = 2
                            "4x Speed (70 Days)":
                                $ pregnancyspeed = 4
                            "6x Speed (35 Days)":
                                $ pregnancyspeed = 6
                            "Back":
                                jump cheatsmenu
                    "Advanced Cheats":
                        menu cheatsmm:
                            "Change Day":
                                menu:
                                    "Mon":
                                        play sound success
                                        $ event = 1
                                        jump cheatsmm
                                    "Tue":
                                        play sound success
                                        $ event = 2
                                        jump cheatsmm
                                    "Wed":
                                        play sound success
                                        $ event = 3
                                        jump cheatsmm
                                    "Thur":
                                        play sound success
                                        $ event = 4
                                        jump cheatsmm
                                    "Fri":
                                        play sound success
                                        $ event = 5
                                        jump cheatsmm
                                    "Sat":
                                        play sound success
                                        $ event = 6
                                        jump cheatsmm
                                    "Sun":
                                        play sound success
                                        $ event = 7
                                        jump cheatsmm
                                    "Back":
                                        jump cheatsmm
                            "Change Personality":
                                menu:
                                    "1- Innocent Girl":
                                        play sound success
                                        $ sdmult = 0.8
                                        $ shamemult = 0.8
                                        $ smartsmult = 1.2
                                        $ folmult = 1.2
                                        $ moneymult = 1.2
                                        $ personality = 1
                                        $ personalityname = "An Innocent Girl"
                                        "Note, this personality will change to 'Corrupted Innocence' if your stats are too lewd."
                                        jump cheatsmm
                                    "2 - Always Horny":
                                        play sound success
                                        $ sdmult = 1.2
                                        $ personality = 2
                                        $ personalityname = "Always Horny"
                                        jump cheatsmm
                                    "3 - A Smooth Operator":
                                        play sound success
                                        $ money += 50
                                        $ shame -= 5
                                        $ shamemult = 1.1
                                        $ moneymult = 1.2
                                        $ personality = 3
                                        $ personalityname = "A Smooth Operator"
                                        jump cheatsmm
                                    "4 - Overly Confident":
                                        play sound success
                                        $ shame -= 10
                                        $ shamemult = 1.2
                                        $ personality = 4
                                        $ personalityname = "Overly Confident"
                                        "Note, this personality will change to 'Sexually Confident' if your shame hits 0."
                                        jump cheatsmm
                                    "5 - Thrill Junkie":
                                        play sound success
                                        $ sd += 5
                                        $ shame -= 5
                                        $ sdmult = 1.10
                                        $ shamemult = 1.10
                                        $ smartsmult = 0.9
                                        $ personality = 5
                                        $ personalityname = "Thrill Junkie"
                                        jump cheatsmm
                                    "6 - (Secret) Corrupted Innocence":
                                        play sound success
                                        $ personality = 6
                                        $ sdmult = 1.2
                                        $ shamemult = 1.1
                                        $ personalityname = "Corrupted Innocence"
                                        jump cheatsmm
                                    "7 - (Secret) Sexually Confident":
                                        play sound success
                                        $ sdmult = 1.2
                                        $ personality = 7
                                        $ personalityname = "Sexually Confident"
                                        jump cheatsmm
                                    "Reset Personality (Good idea to do this before changing)":
                                        play sound success
                                        $ sdmult = 1
                                        $ smartmult = 1
                                        $ shamemult = 1
                                        $ moneymult = 1
                                        $ folmult = 1
                                        $ personality = 0
                                        $ personalityname = "Flesh Automatron"
                                        "Personality severed. You are a flesh automatron animated by neurotransmitters."
                                        jump cheatsmm
                                    "Back":
                                        jump cheatsmm
                            "Add/Remove Quirks":
                                menu cqmm:
                                    "Stat related quirks that don't affect gameplay aren't included here."
                                    "Selfie Star":
                                        menu:
                                            "Add":
                                                play sound success
                                                $ folmult = 1.1
                                                $ qselfiestar = 1
                                            "Remove":
                                                play sound success2
                                                $ folmult = 1
                                                $ qselfiestar = 0
                                            "Back":
                                                jump cqmm
                                    "Rich Parents":
                                        menu:
                                            "Add":
                                                play sound success
                                                $ qrichkid = 1
                                            "Remove":
                                                play sound success2
                                                $ qrichkid = 0
                                            "Back":
                                                jump cqmm
                                    "Anal Queen":
                                        menu:
                                            "Add":
                                                play sound success
                                                $ qanalqueen = 1
                                            "Remove":
                                                play sound success2
                                                $ qanalqueen = 0
                                            "Back":
                                                jump cqmm

                                    "Heavy Sleeper":
                                        menu:
                                            "Add":
                                                play sound success
                                                $ qheavysleeper = 1
                                            "Remove":
                                                play sound success2
                                                $ qheavysleeper = 0
                                            "Back":
                                                jump cqmm

                                    "Lightweight":
                                        menu:
                                            "Add":
                                                play sound success
                                                $ qlightweight = 1
                                            "Remove":
                                                play sound success2
                                                $ qlightweight = 0
                                            "Back":
                                                jump cqmm

                                    "Introvert":
                                        menu:
                                            "Add":
                                                play sound success
                                                $ qintrovert = 1
                                                $ alonemult = 1.1
                                            "Remove":
                                                play sound success2
                                                $ qintrovert = 0
                                                $ alonemult = 1
                                            "Back":
                                                jump cqmm

                                    "Secretly Depraved":
                                        menu:
                                            "Add":
                                                play sound success
                                                $ qsecretlydepraved = 1
                                            "Remove":
                                                play sound success2
                                                $ qsecretlydepraved = 0
                                            "Back":
                                                jump cqmm

                                    "Back":
                                        jump cheatsmm
                                jump cqmm
                            "Add All Items" if allitems == 0:
                                play sound success
                                $ cami = 1
                                $ bs = 1
                                $ dildo = 1
                                $ vibrator = 1
                                $ cgl = 1
                                $ swimsuit = 1
                                $ plug = 1
                                $ allitems = 1
                                "Done!"
                                jump cheatsmm
                            "Unlock All Areas" if allareas == 0:
                                play sound success
                                $ dungeonunlocked = 1
                                $ massageparlourunlocked = 1
                                $ clubunlocked = 1
                                $ maledormsunlocked = 1
                                $ studiounlocked = 1
                                $ bankunlocked = 1
                                $ parkunlocked = 1
                                $ stripclubunlocked = 1
                                $ allareas = 1
                                "Done!"
                                if pregnant == 0:
                                    "Hospital is still only available if you're pregnant."
                                jump cheatsmm
                            "Unlock All Endings" if endingoverride == 0 or endingsunlocked == 0:
                                play sound success
                                $ endingoverride = 1
                                $ endingsunlocked = 1
                                jump cheatsmm
                            "Change Names":
                                menu:
                                    "[mc]":
                                        python:
                                            mc = renpy.input("Name your character.")
                                            mc = mc.strip()
                                            if not mc:
                                                mc = "Taco"
                                    "[susu]":
                                        python:
                                            susu = renpy.input("Name your character.")
                                            susu = susu.strip()
                                            if not susu:
                                                susu = "Susu"
                                    "[yomo]":
                                        python:
                                            yomo = renpy.input("Name your character.")
                                            yomo = yomo.strip()
                                            if not yomo:
                                                yomo = "Yomo"
                                    "[tina]":
                                        python:
                                            tina = renpy.input("Name your character.")
                                            tina = tina.strip()
                                            if not tina:
                                                tina = "Tina"
                                    "[yoko]":
                                        python:
                                            yoko = renpy.input("Name your character.")
                                            yoko = yoko.strip()
                                            if not yoko:
                                                yoko = "Yoko"
                                    "[crush]":
                                        python:
                                            crush = renpy.input("Name your Crush. Leave blank for the default name 'Crush'.")
                                            crush = crush.strip()
                                            if not crush:
                                                crush = "Crush"
                                    "Back":
                                        jump cheatsmm
                                play sound success
                                jump cheatsmm
                            "+2 Crush Affection" if ca < 8:
                                play sound success
                                $ ca += 2
                                jump cheatsmm
                            "Back":
                                jump cheatsmenu
                    "Back":
                        jump bedmenu
        "Back":
            if morning == 1:
                jump bedroommorning
            else:
                jump bedroom
    jump morning

label wardrobe:
    hide bedroom screen border
    "Let's see... What to wear?"
    menu wardrobemenu:
        "Nude! (200 Sexual Desire, 0 Shame)":
            if sd < 200 or shame > 0:
                "Not. A. Chance!!!"
                jump wardrobemenu
            $ nude = 1
            $ lewdoutfit = 0
            "Well, it's cozy, technically legal, and extremely arousing to do so!"
            $ clothes = 0
        "Formal Clothes":
            $ lewdoutfit = 0
            $ nude = 0
            "At this time? I guess it'll help me concentrate."
            $ clothes = 1
        "Lewder Formal" if blackmailsex == 1:
            $ lewdoutfit = 0
            $ nude = 0
            "It's formal, it's lewd! Best of both worlds! I can even wear this to college."
            $ clothes = 12
        "Casual Clothes":
            $ lewdoutfit = 0
            $ nude = 0
            "Nothing beats the pure comfort of a tank-top and shorts!"
            $ clothes = 2
        "Fancy Clothes":
            $ lewdoutfit = 0
            $ nude = 0
            "Ah yes, these are the clothes for a 'special event' that's not actually that special, haha."
            $ clothes = 9
        "Hero Costume (<90 Shame)" if herosuit == 1:
            $ lewdoutfit = 0
            $ nude = 0
            "My functional, but slightly too sexy hero suit. I probably shouldn't wear this too much in public until I get my license, but hey, it's not against any rules. I'm sure this'll stop any would-be sexual harassers too."
            if sge == 1:
                menu:
                    "Should I wear the crop top version, or the full suit?"
                    "Crop-Top":
                        $ clothes = 14
                    "Full Suit":
                        $ clothes = 13
            else:
                $ clothes = 13
        "PJs (<80 Shame)":
            if shame > 80:
                "Why would I wear my PJs outside?"
                jump wardrobemenu
            $ lewdoutfit = 0
            $ nude = 0
            "Ahhh... I feel sleepy already."
            $ clothes = 3
        "Lewd Clothes ->":
            menu:
                "Cat Girl Lingerie (75 Sexual Desire, <25 Shame)" if cgl == 1:
                    if sd < 75 or shame > 25:
                        "Hehe, I don't think so."
                        jump wardrobemenu
                    $ lewdoutfit = 1
                    $ nude = 0
                    "It's lewd, but it's also super cute!"
                    $ clothes = 4
                "Bunny Suit (50 Sexual Desire, <50 Shame)" if bs == 1:
                    if sd < 50 or shame > 50:
                        "While not as lewd as other costumes, I'd look pretty stupid wearing this for no reason."
                        jump wardrobemenu
                    $ lewdoutfit = 1
                    $ nude = 0
                    "I never imagined I'd wear one of these."
                    $ clothes = 5
                "Camisole (80 Sexual Desire, <20 Shame)" if cami == 1:
                    if sd < 80 or shame > 20:
                        "This outfit is far too lewd to go outside in."
                        jump wardrobemenu
                    $ lewdoutfit = 1
                    $ nude = 0
                    "The sheer gown adds an element of sexy mystery."
                    $ clothes = 6
                "Underwear (75 Sexual Desire, <25 Shame)":
                    if sd < 75 or shame > 25:
                        "Uhmm, I think underwear alone might be a bit too risque."
                        jump wardrobemenu
                    $ lewdoutfit = 1
                    $ nude = 0
                    "Ahah, I feel cute in this underwear for some reason."
                    $ clothes = 7
                "'Waitress' Clothes (20 Sexual Desire, <80 Shame)" if baroutfit == 1:
                    if sd < 20 or shame > 80:
                        "This outfit isn't so bad for work, but otherwise it's a little too naughty."
                        jump wardrobemenu
                    $ lewdoutfit = 1
                    $ nude = 0
                    "Despite appearances, it's a very comfortable outfit, and rather liberating in a sense."
                    $ clothes = 10
                "Swimsuit (20 Sexual Desire, <80 Shame)" if swimsuit == 1:
                    if sd < 20 or shame > 80:
                        "Ehh, I should only wear this at the beach or pool."
                        jump wardrobemenu
                    $ lewdoutfit = 1
                    $ nude = 0
                    "Wearing my swimsuit on the way to the beach instead of putting it on there? Rather daring, I do say!"
                    $ clothes = 11
                "Dominatrix (80 Sexual Desire, <20 Shame)" if de == 1:
                    if sd < 80 or shame > 20:
                        "Woah! That's way too kinky to wear in public."
                        jump wardrobemenu
                    $ lewdoutfit = 1
                    $ nude = 0
                    "Time to be a bad bitch."
                    $ clothes = 15
                "<- Normal Clothes":
                    jump wardrobemenu
        "Accessories ->":
            menu:
                "Cat Ears" if catears == 1:
                    menu:
                        "Cat Ears do not appear in sex scenes*"
                        "Wear":
                            $ catearson = 1
                        "Remove":
                            $ catearson = 0
                "Piercings" if piercings == 1:
                    menu:
                        "Wear":
                            $ piercingson = 1
                        "Remove":
                            $ piercingson = 0
                "Slime Body" if sge == 1:
                    menu:
                        "Slime Body does not appear in sex scenes*"
                        "Wear":
                            $ slimebody = 1
                        "Remove":
                            $ slimebody = 0
                "Slime Hair" if sge == 1:
                    menu:
                        "Slime Hair does not appear in sex scenes*"
                        "Wear":
                            $ slimehair = 1
                        "Remove":
                            $ slimehair = 0
                "Pink Hair" if ege == 1:
                    menu:
                        "Pink Hair does not appear in sex scenes*"
                        "Wear":
                            $ pinkhair = 1
                        "Remove":
                            $ pinkhair = 0
                "Back":
                    jump wardrobemenu
        "Back":
            pass
    if morning == 1:
        jump bedroommorning
    else:
        jump bedroom
label genericsleep:
    stop music fadeout 3.0
    scene bg black with d
    "I finish up for the evening."
    scene bg bed with d
    "Get into bed and soon drift off to sleep."
    jump morning
