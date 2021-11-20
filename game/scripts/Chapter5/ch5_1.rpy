label ch5_1:

    scene plaza

    "You reach a wide, open plaza in Savanna Forest."

    "The plaza looks ancient and abandoned, but it emits a powerful and mysterious aura."

    show darrick at left
    show edgar at right
    with dissolve

    dr "This has to be the place! There's nothing else in this forest."

    ed "It feels like the right place. It looks like something happened here a long time ago."

    menu:
        mc "I feel it too. I think we can _____ around a bit. We might be able to find what the people in my visions were talking about."

        "look":
            $renpy.fix_rollback()
            $ scores += 10
        "looking":
            $renpy.fix_rollback()
        "looks":
            $renpy.fix_rollback()

    show darrick surprised
    show edgar hurt

    ed "Argh!"

    "Edgar holds his head in pain."

    dr  "What's wrong, Edgar?"

    "You approach him cautiously to get a closer look."

    menu:
        mc "Is your head _____ ?" 

        "hurt":
            $renpy.fix_rollback()
        "hurting":
            $renpy.fix_rollback()
            $ scores += 10
        "pain":
            $renpy.fix_rollback()
    
    show edgar

    ed "I... I'm feeling a little bit dizzy. So you guys go on without me. I'll catch up later."

    dr "MC, I'll stay here with Edgar. You can explore the plaza first."

    mc "Are you sure?"

    show darrick grin

    dr "Yup, we'll catch up with you."

    hide darrick
    hide edgar
    with dissolve
    scene plaza inside

    "You walk into the plaza alone, drawn by how beautiful the structure is or used to be."

    mc "This place must have held many people before it was abandoned.."

    mc "The teardrop must be here somewhere.."

    menu:
        "As you walk _____ into the plaza, you feel warm air coming from the centre."

        "inner":
            $renpy.fix_rollback()
        "slower":
            $renpy.fix_rollback()
        "deeper":
            $renpy.fix_rollback()
            $ scores += 10

    mc "That's weird. It feels like there's a fire nearby."

    mc "It could be the teardrop! I better follow it."

    "As you walk closer to the centre, the air gets warmer and warmer."

    mc "There's nothing -"

    show crystal at center with dissolve:
        ypos 0.6
        delay 0.5

    "Suddenly, right before your eyes, a shiny teardrop materialises in front of you."

    "The warmth of the air feels cosy and familiar. You reach out your hand and grab the teardrop."

    mc "This is it.."

    hide crystal with fade 
    with shakescreen_long

    mc "Argh!"

    "You fall to the ground as soon as your hand wraps around the teardrop. Your head starts hurting."

    mc "My head.. it hurts so much... What's going on?"

    "As quickly as it comes, the pain leaves, and you feel something change within you."

    show darrick worried
    with moveinright

    dr "MC! Are you alright? I saw you fall.."

    mc "No, I mean, yes I did fall, but I... I'm alright... I feel amazing!"

    mc "I found the teardrop, and when I touched it, I felt something changed in me. I feel.. warmer now."

    show darrick surprised

    dr "What's that on your neck?"

    menu:
        "You look at your _____, and sure enough, there is a dark tattoo on your neck."

        "refection":
            $renpy.fix_rollback()
        "reflection":
            $renpy.fix_rollback()
            $ scores += 10
        "refektion":
            $renpy.fix_rollback()

    mc "It's exactly like the one from my vision... "

    mc "Darrick, could I perhaps be a..?"

    ed "You!"

    show darrick surprised at left with move
    show edgar angry tattoo at right with moveinright
    with shakescreen_long

    "The ground shakes violently. You and Darrick turn to look at Edgar, who starts charging at you angrily."

    show darrick angry

    dr "Hey Edgar! Calm down!"

    show magic black at attack_left
    pause(0.1)
    show darrick angry at moveout_left
    with shakescreen_long
    hide darrick

    "Edgar throws his hand towards Darrick, and a black wave knocks Darrick to the ground."

    mc "Darrick!"

    show edgar angry tattoo at center
    with ease
    show magic black at rotation_slow
    with dissolve

    "You try to run to Darrick, but Edgar extends his hand towards you instead, a black ball of fire already forming."

    "Quickly, you extend your hand towards him, and a bright red ball of fire strikes Edgar."

    show magic red full at attack_center
    with shakescreen_long
    hide magic
    show edgar hurt tattoo

    mc "Wait- What? How did I do that?"

    ed "You killed my people! I'll make you pay!"

    mc "Edgar, stop! What's going on with you?"

    show edgar angry tattoo

    ed "You.. Don't you get it now? The teardrops, the fire, the tattoo.."

    ed "You're the child of the last two dragons. The dragons who defeated me ten years ago.."

    mc "Defeated you? Edgar... What do you mean? You were only a child ten years ago. How could dragons have fought with you?"

    ed "I am no child, MC, and neither are you. Coming to this place restored my memories. This was where the fight happened.. The fight between the dragons and me." 

    ed "I am Edgar, the Demon King of the Underworld. I was reborn after your parents banished me from this world ten years ago."

    ed "And you... You are their only child, the last dragon... So you have to pay for what they have done."

    show magic black full at rotation_slow
    with dissolve

    "Edgar summons black flames onto his hands, preparing to strike you."
    
    $scores = 200
    
    if scores < 200:
        jump ending_bad
    if (scores >= 200 and scores < 300):
        jump ending_good
    if scores >= 300:
        jump ending_best 

label ending_bad:

    mc "Wait!!"

    mc "Why are you doing this, Edgar?"

    mc "You can't punish me for something that happened years ago while I was only a child."

    ed "You are the last dragon, and all dragons should vanish from this world."
    
    mc  "People say you caused chaos and mayhem, so the dragons had to risk their lives to stop you. It was their job!"

    ed "All you believe is what people say, huh? Do you even know why I did all those things?"

    mc "I.. I am sure there's no good reason for killing thousands of innocent people. You should be thankful you have a second chance to live after what you did."

    ed "You know nothing, MC. This world is corrupted, and I am the only one who can fix it."

    mc "And how are you going to do that?"

    ed "By killing as many people as I have to. All who listen to my commands will be spared. It will be a peaceful world with a good leader."

    mc "That's crazy, Edgar. Lives are not for us to take."

    ed "I think I can decide that for myself, MC."

    show edgar tattoo
    hide magic with dissolve

    ed "However, I shall spare your life. You and Darrick have been.. good to me. I may be cruel, but I know when to be grateful."

    ed "This time, I'll let you two go. But if I ever see you again, MC, don't expect me to be so kind."

    hide edgar tattoo with dissolve

    "Edgar turns his back on you and disappears before you can respond."

    show darrick worried at center
    with moveinleft

    dr "Are you alright, [mc]?"

    mc "I'm fine... Are you okay? He pushed you quite hard just now."

    show darrick grin

    dr "It was just a scratch. So don't worry about it!"

    show darrick surprised

    dr "I'm shocked, though... I didn't know we were travelling with the Demon King all this time!"

    dr "And you're a Dragon! That's insane!"

    show darrick worried

    dr "But.. What are we going to do about Edgar? I mean, the Demon King... Is he planning to conquer the world?"

    mc "I don't know, Darrick. The best we can do now is prepare for the worst. If he is as dangerous as they say, I don't know if we can stop him."

    mc "I wish I did a better job at convincing Edgar to stay. He was such an innocent guy, and I'm sure there's good in him.."

    mc "I just didn't know how to reach it."

    dr "Well, we can't do anything about it now."

    dr "Let's head back to the city to tell Merlin about it, alright? He'll fix this."

    "You sigh and follow Darrick back to the city."

    scene black
    with dissolve

    mc "I don't think this is something we can fix."




