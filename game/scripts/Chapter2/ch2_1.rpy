label ch2_1:

    scene olympus

    play sound "audio/BusyTown.mp3" volume 0.25
    "You breathe a sigh of relief as soon as you set foot in the town of Olympus."

    menu:
        "The town is bustling with people, some even _____ you curious looks as they walk by."
    
        "gave":
            $renpy.fix_rollback()
        "giving":
            $renpy.fix_rollback()
            $ scores += 10
        "given":
            $renpy.fix_rollback()

    stop sound 

    "You realise that your body reeks from skipping out on showers during your walk to Olympus."
    
    play sound "audio/McSigh.mp3"
    mc "{i}*Sigh*...{/i}" 
    
    mc "{i}I can’t continue my journey like this.{/i}"
    menu:
        mc "{i}I should find a place to _____ up and rest for the night.{/i}"

        "freshen":
            $renpy.fix_rollback()
            $ scores += 10
        "brighten":
            $renpy.fix_rollback()

    "You walk around the unfamiliar town looking for a place to stay."

    play sound "audio/PatBack.mp3"
    "Suddenly, you feel a pat on your back."

    sg "Hey!"

    menu:
        "Turn back":

            jump ch2_be_polite_to_stranger

        "Ignore the voice":

            jump ch2_be_hostile_towards_stranger

label  ch2_be_polite_to_stranger:

    show darrick
    with dissolve

    "You turn back and spot a stranger standing behind you, grinning."
    
    "You are taken aback."

    jump ch2_both_cont

label  ch2_be_hostile_towards_stranger:

    "You are too tired to respond to the voice." 
    
    "Because you ignored them, the person moves in front of you, blocking your way."

    show darrick
    with moveinright

    sg "Hey! I’m talking to you."

    jump ch2_both_cont

label ch2_both_cont:

    mc "How can I help you?"

    show darrick grin

    sg "Hehe, this way, follow me. I’ll lead you."

    mc "Thank you but I think I’m good."
    
    show darrick

    sg "I know an inn where you can take a rest for the day. I can tell that you’re exhausted."

    menu:
        "Knowing that you will never find a place out _____ on your own, you decide to take up the offer before the stranger leaves."
    
        "there":
            $renpy.fix_rollback()
        "where":
            $renpy.fix_rollback()
        "here":
            $renpy.fix_rollback()
            $ scores += 10

    mc "{i}Well, I am hungry… and I need a shower badly too.{/i}"

    mc "Can I follow you to the inn?"

    show darrick grin

    sg "Of course, let’s go. I’ll lead the way, and you try to keep up, alright?"

    menu:
        "You _____ in agreement."

        "nod":
            $renpy.fix_rollback()
            $ scores += 10
        "nodded":
            $renpy.fix_rollback()
        "nods":
            $renpy.fix_rollback()
    
    hide darrick
    with moveoutleft

    menu:
        "On the way to the inn, you take a short break to quench your thirst. When you _____ up, the stranger is gone from your sight." 

        "look":
            $renpy.fix_rollback()
            $ scores += 10
        "looking":
            $renpy.fix_rollback()
        "looked":
            $renpy.fix_rollback()

    mc "{i} Hey... Where did he go?{/i}"

    "You wonder if the stranger abandoned you halfway."

    mc "{i} He would never do that, he seemed like such a nice person.{/i}"
    
    "After circling the area, you find a hint of brown behind a rock."

    menu:
        "The stranger quietly creeps up _____ and scares you from the back."

        "further":
            $renpy.fix_rollback()
        "closer":
            $renpy.fix_rollback()
            $ scores += 10

    show darrick grin
    with shakescreen_long

    mc "Ah! You scared me!"

    "You both share a good laugh."
    
    show darrick

    sg "You seem like a smart and brave [boy]."
    
    mc "Why do you think so?"
    
    show darrick grin

    sg "It’s just a feeling."

    "On the way to the inn, the stranger introduces himself as Darrick. He also questions your appearance."

    menu:
        "Looking embarrassed, you recount _____ fight with the demon in the forest to Darrick."

        "my":
            $renpy.fix_rollback()
        "our":
            $renpy.fix_rollback()
        "your":
            $renpy.fix_rollback()
            $ scores += 10

    show darrick surprised

    mc "Darrick, one thing strikes me as odd though... I have no clue how I defeated the demon with the force field."

    dr "Hmmm, tell me more about that later."

    hide darrick
    with dissolve
    scene inn
    with dissolve

    "You two approach the inn."

    show darrick
    with dissolve

    menu:
        dr "I suggest you take a shower. After that, I'll be _____ for you at the dining hall."

        "waits":
            $renpy.fix_rollback()
        "waiting":
            $renpy.fix_rollback()
            $ scores += 10
        "waited":
            $renpy.fix_rollback()

    "Darrick helps you out with the payment for the accomodation."
    
    dr "Don't worry about it, it's on me."

    "After a nice warm bath, you make your way to the dining hall to find Darrick."

    "You then continue the conversation from where you left off earlier."

    menu:
        "You describe the demon that you _____ in the forest."

        "incanted":
            $renpy.fix_rollback()
        "encountered":
            $renpy.fix_rollback()
            $ scores += 10

    show darrick surprised

    dr "Oh my, that demon you fought was a goblin!"

    show darrick
    show magic blue at rotation_slow
    with dissolve

    "Darrick raises his hand and produces a force field around it, similar to what you experienced."

    "You are in awe at the sight of the force field that Darrick produced."

    "However, you notice the force field you encountered was red compared to Darrick’s blue force field."
    
    menu:
        "You _____ that thought up to Darrick."

        "brought":
            $renpy.fix_rollback()
        "bring":
            $renpy.fix_rollback()
            $ scores += 10
        "bought":
            $renpy.fix_rollback()

    hide magic blue
    with dissolve

    dr "Well, to be honest with you, I am quite unfamiliar with that, but I can introduce you to the Guild Master. He is all-knowing!"
    
    menu:
        "By doing so, he hopes that the Guild Master will have an answer to _____ doubts."

        "their":
            $renpy.fix_rollback()
        "your":
            $renpy.fix_rollback()
            $ scores += 10
        "our":
            $renpy.fix_rollback()

    menu:
        
        "Excited":

            jump nod_in_agreement
        
        "Doubtful":

            jump feeling_doubtful

label nod_in_agreement:

    "Excitedly, you nod in agreement."
    
    mc "I would love to meet the Guild Master!"

    mc "When will we leave to meet the Master? Do we leave now?"

    menu:
        dr "We will leave tomorrow. You can rest today. You _____ be exhausted after that long journey."

        "should":
            $renpy.fix_rollback()
        "will":
            $renpy.fix_rollback()
        "must":
            $renpy.fix_rollback()
            $ scores += 10

    mc "Very well. What's for dinner?"

    dr "Porridge, is that okay?"

    menu:
        "Suddenly, you are_____ with a rush of memories as your grandma used to make your porridge every day, and it was your absolute favourite meal."

        "overwhelmed":
            $renpy.fix_rollback()
            $ scores += 10
        "underwhelmed":
            $renpy.fix_rollback()

    mc "Of course, I love porridge! My grandma used to make this for me everyday."

    dr "That’s great. Although it may not be as delicious as your grandma’s porridge, I hope it keeps you full for now."

    mc "Don't worry, it's delicious. It tastes just like grandma’s."

    "Both you and Darrick have a filling dinner."

    jump ch2_2_cont

label feeling_doubtful:

    mc "I don’t know.. Can he really help me?"

    menu:
        dr "Don’t doubt the Guild Master, you should meet him for  _____ then you will see."

        "yourself":
            $renpy.fix_rollback()
            $ scores += 10
        "itself":
            $renpy.fix_rollback()
        "themself":
            $renpy.fix_rollback()

    mc  "Alright then, I won't. Do we leave now?"

    menu:
        "You are ______ to see if this Guild Master can actually help you solve your doubts."

        "eager":
            $renpy.fix_rollback()
            $ scores += 10
        "eagle":
            $renpy.fix_rollback()
        "eagar":
            $renpy.fix_rollback()

    dr "Now I see that you're excited to meet the Guild Master."
    
    dr "We shall leave tomorrow as it's already late. Let’s get some rest after dinner."

    jump ch2_2_cont