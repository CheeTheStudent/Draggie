label ch4_1:
    
    scene black 
    scene clear crystal with dissolve

    "The moment you make contact with the crystal, a strong vibration causes both you and Darrick to stumble and fall."
    
    show clear crystal with shakescreen_long
    mc "Darrick, you alright?"
 
    dr "I’m good, but did you feel that? What was that?"
   
    show shuteye
    with shakescreen_long
    
    play sound "audio/RocksCrumbling.mp3"
    "You feel the rocks crumbling down in the underground basement."
    stop sound

    mc "Darrick, I don’t feel so good..."

    dr "....." 

    show eye
    with dissolve

    mc "I’m losing consciousness.."

    "As soon as you get a hold of the teardrop crystal, you immediately faint from the strong force of the crystal."
    play sound "audio/PowerForce.mp3"

    show eye close with dissolve

    "You feel your eyes close slowly as Darrick lays unmoving in front of you."
    stop sound
    "You enter a dream."

    show basement blur with dissolve

    "You open your eyes and things are blurry."
    
    menu:
        "You soon ______ your vision but realize what you see is an unfamiliar atmosphere."

        "regain":
            $renpy.fix_rollback()
            $ scores += 10
        "redeem":
            $renpy.fix_rollback()
        "retake":
            $renpy.fix_rollback()
  
    show basement clear with dissolve
   
    "You realize you’re in a dream from a woman's point of view but you can’t make out who it is."

    show father with dissolve

    menu:
        "You see a man in front of you with a glowing ______ on his neck."

        "tatoo":
            $renpy.fix_rollback()
        "tatto":
            $renpy.fix_rollback()
        "tattoo":
            $renpy.fix_rollback()
            $ scores += 10

    mc "{i}I wonder who that is.{/i}"

    "You are able to predict what was going to happen as if it was from your own memories. However, your vision is not clear enough to see anything clearly."

    menu:
        "The woman and the man engage in a conversation and start ________ over their [son]’s safety."

        "deliberating":
            $renpy.fix_rollback()
            $ scores += 10
            jump ch4_branch1_pos
        "deliberate":
            $renpy.fix_rollback()
            jump ch4_branch1_neg
        "deliberated":
            $renpy.fix_rollback()
            jump ch4_branch1_neg
    
label ch4_branch1_pos:

    woman  "What are we going to do about our [son]?"

    man "Shhh, lower your voice. [He] might hear us."

    woman "Have you come up with a plan? I’m worried about [him]."

    man "I have it worked out. [He] will be safe."

    "The conversation went on for a couple of minutes. There was a debate between both of them over what to do with the [boy] in question."

    "The both of them eventually come to a conclusion to leave the [boy] at a house where [he] would be safe."

    jump ch4_branch1_cont

label ch4_branch1_neg:

    "You know they are there and you try to pay close attention to what is going on..."
    
    "...but you can’t hear anything as the voices start cutting off and the blurry vision reappears."

    "For a moment, you almost lose the visions but you try hard to regain it."

    woman "What are we going to do about our [son]?"

    man "Shhh, lower your voice. [He] might hear us."
    
    woman "Have you come up with a plan? I’m worried about [him]."

    man "I have it worked out. We will -"

    "The man’s voice cuts off and you can’t hear him anymore. But by reading his lips and their body language, you can tell they have decided to leave the [boy] at a house where [he] would be safe."

    jump ch4_branch1_cont

label ch4_branch1_cont:

    "The man mentions that the Demon King has been a threat towards them, and that he might make a move to attack their family, and even worse, he might harm the [boy]."

    menu:
        "He informs the woman to take this ________ to bring the [boy] to a house they went to before to seek shelter as the man tries to lure the Demon King into a place called the Savanna forest."

        "oppotunity":
            $renpy.fix_rollback()
        "opportunity":
            $renpy.fix_rollback()
            $ scores += 10
        "opportunitee":
            $renpy.fix_rollback()

    woman "I am pretty sure the old lady wouldn’t mind taking care of [him]."

    man "Well, then we better hurry before it’s too late."

    woman "I’ll get [his] bags ready to go, and... please be careful out there.."

    man "Alright, I will. See you at Savanna Forest. And..."
    
    man "Be ready for the worst..."

    hide father with dissolve
    hide basement with dissolve
    scene black with dissolve
    show grandma house with dissolve
    play sound "audio/GrandmaHouse.mp3"

    "The woman rushes to drop the boy off at an old lady’s house."

    mc "{i}Grandma's house? What’s going on{/i}?!"

    stop sound
    hide grandma house with dissolve
    scene black 
    "Your vision cuts off and when it recovers, the woman has come to the mansion’s underground basement."
    scene black
    show stairs with dissolve
    
    mc "{i}This is Elysium!{/i}"

    woman "[Son], this is what mother can do for you. I love you, always..."

    show magic red at rotation_slow
    with dissolve
    show crystal at center with dissolve:
        ypos 0.6
        delay 0.5

    "The woman cries and as her tears drop onto her hand, she uses her power to crystallize it and makes it float in the air."
    
    mc "{i}It’s the red power! It’s the same as mine! What exactly is the relationship between this woman and I? And also... grandma...{/i}"
    
    hide magic
    hide crystal
    hide stairs with dissolve
    "After that, the woman rushes to Savanna Forest to meet the man. You want to keep following the story but your sight goes dark."
    
    show inside mansion with dissolve
    show darrick worried at left 
    with dissolve
    
    menu:
        "You are _______ by Darrick calling out your name, and you are pulled out from your dream."

        "awakened":
            $renpy.fix_rollback()
            $ scores += 10
        "awakening":
            $renpy.fix_rollback()
        "awakens":
            $renpy.fix_rollback()

    mc "That was odd.."
    
    "Darrick sits you upright and checks to make sure you are okay."
    
    show darrick
    dr "How are you feeling there? Had a good dream?"

    mc "You know what, let’s leave this place now before anything weirder happens."

    hide darrick with dissolve
    "You, Darrick, and Edgar all decide to leave Elysium mansion after retrieving the teardrop crystal."

    show darrick surprised with dissolve
    dr "Did anything happen? Are we in a hurry? Where do we head off to now?"

    show darrick surprised at left with move
    show edgar at right 
    with move
    ed "I was wondering the same."

    menu:
        "Tell them about your dream":

            jump ch4_branch2_pos

        "Don’t tell them all about your dream":

            jump ch4_branch2_neg

label  ch4_branch2_pos:

    show darrick worried
    dr "A man, a woman, a child and your grandma? Argh, I’m confused!"
    
    ed "You just said Savanna Forest, right?"
    
    mc "Yes, I think we can get all the answers at Savanna Forest. Let’s go!"

    jump ch4_branch2_cont

label  ch4_branch2_neg:

    mc "I think it's best for our safety, and we need to head to another place. It’s called Savanna Forest."

    show darrick grin
    dr "Sure thing, let's go."

    ed "Okay."

    jump ch4_branch2_cont

label ch4_branch2_cont:

    hide darrick
    hide edgar
    with dissolve

    scene forest2
    show darrick with dissolve

    menu:
        "On the journey back, Darrick tries to _______ the location of Savanna Forest."

        "figure in":
            $renpy.fix_rollback()
        "figure out":
            $renpy.fix_rollback()
            $ scores += 10
        "figure around":
            $renpy.fix_rollback()

    dr "Was there any clue in your dream that will help get us there?"
    show darrick surprised
    mc "The dream seems foggy to me now, maybe once I see a spot, I might remember."

    show darrick grin
    dr "Sure thing."
    
    hide darrick
    "The next goal is to make it to Savanna Forest and find the meaning behind the dream."

    "Darrick suggests going to Merlin once again for help on finding the location."

    scene merlin_office with fade
    show scroll with dissolve

    menu:
        "Upon your return to the guild, Merlin greets you with an old scroll ______ his hand."

        "on":
            $renpy.fix_rollback()
        "in":
            $renpy.fix_rollback()
            $ scores += 10
    
    "He passes the scroll to Darrick and tells him that the location of Savanna Forest can be found on this map."

    hide scroll
    show darrick surprised with dissolve
    dr "{i}Did you hear that?{/i}"
    
    show darrick surprised at left with move
    with dissolve
    show edgar at right with dissolve
    ed "{i}Shhh...{/i}"

    mc "{i}Yes I can, he gave us an old map.{/i}"

    show darrick at center
    show merlin at left:
        ypos 1.1
    with move

    ml "You know I can hear you right?"

    "You and Darrick both start to giggle."

    ed "*Sighs*"

    hide edgar with dissolve
    show darrick at right with move
    
    "You and Darrick are overjoyed. With the map in hand, you are one step closer to finally uncovering the missing piece of the story."

    "Merlin, however, didn’t seem to be too happy about it."
    
    menu:
        "He informs both of you that Savanna Forest can be a dengerous place to venture and that you have to _____________ at all times."

        "take a break":
            $renpy.fix_rollback()
        "keep to yourself":
            $renpy.fix_rollback()
        "keep your guard up":
            $renpy.fix_rollback()
            $ scores += 10

    ml "Both of you need to pay attention and stay strong out there. It is a wild place. Always pay attention to your surroundings."

    show darrick grin at right with dissolve
    dr "Do you think we are ready? Because I think we can take on anyone that crosses us! HAHA!"
    
    ml "It seems like you made a new friend."

    hide darrick with dissolve
    show edgar at right with dissolve

    "Merlin glances at Edgar with a curious look on his face."

    ed "Hi, I’m Edgar. Nice to meet you."

    ml "My name is Merlin. It’s good seeing new faces around here lately."

    ml "Well, take care on your next journey, boys."

    hide merlin
    hide edgar
    with dissolve
    
    "With the help of the Merlin’s map, the three of you make your way to Savanna Forest."

    "After a long and gruelling journey, you, Darrick, and Edgar find yourselves at the entrance of a large plaza."










