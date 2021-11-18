label ch4_1:

    "The moment you make contact with the crystal, all hell breaks loose. There is a strong vibration that causes both you and Darrick to stumble and fall."

    mc "Darrick, you alright?"

    dr "I’m good, but did you feel that? What was that?"

    "You feel the rocks crumbling down in the underground basement."

    mc "Darrick, I don’t feel so good..."

    dr "....." 

    mc "I’m losing consciousness.."

    "As soon as you get a hold of the teardrop crystal, you immediately faint from the strong force of the crystal."

    "You feel your eyes close slowly as Darrick lays unmoving in front of you."

    "~ dreaming"

    "You open your eyes and things are blurry. You soon regain your vision but realize what you see is an unfamiliar atmosphere."

    "You realize you’re in a dream from someone else’s point of view but you can’t seem to make out who it is."

    "You then see a person walking past you and into a room."

    mc "{i}I wonder who that is.{/i}"

    "‘You’ get up from the bed and follow the person in front into the room."

    "You are able to observe what was going to happen as if it was from your own memories. However, your vision is not clear enough to see anything clearly."

    "‘You’ enter the room behind the mysterious person and close the door. You roughly see that the person is a man."

    "Taking a closer look, you spot a dragon tattoo on the man’s neck. The person and ‘You’ engage in a conversation and start _________ over your son’s safety."

    menu:
        "Taking a closer look, you spot a dragon tattoo on the man’s neck. The person and ‘You’ engage in a conversation and start _________ over your son’s safety."

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

    you  "What are we going to do about our son?"

    man "Shhh, lower your voice. He might hear us."

    you "Have you come up with a plan? I’m worried about him."

    man "I have it worked out. He will be safe."

    "The conversation went on for a couple of minutes. There was a debate between both parties over what to do with the boy in question."

    "He and ‘You’ eventually come to a conclusion to leave the boy at a house where he would be safe."

    jump ch4_branch1_cont

label ch4_branch1_neg:

    "You know they are there, and you try to pay close attention to what is going on, but you can’t  seem to hear anything as the voices start cutting out and the blurry vision reappears."

    "For a moment it seems like you were almost losing the visions and you try everything to regain it."

    you "What are we going to do about our son?"

    man "Shhh, lower your voice. He might hear us."

    you "Have you come up with a plan? I’m worried about him."

    man "I have it worked out. We will...” *voice disappears*"

    "The man’s voice starts cutting off and you can’t hear him anymore. But by reading his lips and their body language, you can tell they have decided to leave the boy at a house where he would be safe."

    jump ch4_branch1_cont

label ch4_branch1_cont:

    "The man mentions that the demon king has been a threat towards them, and that he might make a move to attack their family, and even worse, he might harm the boy."

    "He informs ‘You’ to take this opportunity to bring the boy to a house he and ‘You’ went to before to seek shelter as the man tries to lure the demon king into a place called the Savanna forest."

    you "I am pretty sure the old lady wouldn’t mind taking care of him."

    man "Well, then we better hurry before it’s too late."

    you "I’ll get his bags ready to go, and… please be careful out there.."

    man "Alright,I will. See you at Savanna Forest. Be ready for the worst.."

    "‘You’ rush to drop the boy off at an old lady’s house."

    mc "{i}Grandma ??! Who is this baby? What’s going on{/i}?"

    "Your vision cuts off and when it recovers, ‘You’ have come to the mansion’s underground basement."

    mc "{i}This is Elysium!{/i}"

    you "Son, this is what mother can do for you. I love you, always..."

    "The woman cries and as her tears drop onto her hand, she uses her power to crystallize it and makes it float in the air."

    mc "It’s the red power! It’s the same as mine! What is the relationship between this woman and I? And also… grandma."

    "After that, the woman rushes to Savanna Forest to meet the man. You want to keep following the story but your sight goes dark."

    "You are eventually awakened by Darrick calling out your name, and you notice it was, in fact, a dream."

    mc "Woah, that was odd.."
    
    "Darrick sits you upright and checks to make sure you are okay."

    dr "How are you feeling there? Had a good dream?"

    mc "You know what, let’s leave this place now before anything weirder happens."

    "You, Darrick, and Edgar all decide to leave Elysium mansion after retrieving the teardrop crystal."

    dr "Did anything happen? Are we in a hurry? Where do we head off to now?"

    ed "I was wondering the same."

    menu:
        "Tell them about your dream":

            jump ch4_branch2_pos

        "Don’t tell them all about your dream":

            jump ch4_branch2_neg

label  ch4_branch2_pos:

    dr "A man, a woman, a child and your grandma? Argh, I’m confused!"

    ed "You just said Savanna Forest, right?"

    mc "Yes, I think we can get all the answers at Savanna Forest. Let’s go!"

    jump ch4_branch2_cont

label  ch4_branch2_neg:

    mc "I think it's best for our safety, and we need to head to another place. It’s called Savanna Forest."

    dr "Sure thing, let's go."

    ed "Okay"

    jump ch4_branch2_cont

label ch4_branch2_cont:

    "On the journey back, Darrick tries to figure out the location of Savanna Forest."

    dr "Was there any clue in your dream that will help get us there?"

    mc "The dream seems foggy to me now, maybe once I see a spot, I might remember."

    dr "Sure thing."

    "The next goal is to make it to Savanna Forest and find the meaning behind the dream."

    "Darrick suggests going to Merlin, the guild master, once again for help on finding the location."

    "Upon your return to the guild, Merlin greets you with an old scroll in his hand. He passes the scroll to Darrick and tells him that the location of Savanna Forest can be found on this map."

    dr "Did you hear that? *whispers*"

    ed "Shhh..."

    mc "Yes I can, he gave us an old map. *Whispers*"

    ml "You know I can hear you right?"

    "You and Darrick both start to giggle"

    ed "*Sighs*"

    "You and Darrick are overjoyed. With the map in hand, you are one step closer to finally uncovering the missing piece of the story."

    "The guild master, however, didn’t seem to be too happy about it. He informs both of you that Savanna Forest can be a dangerous place to step foot in and that you have to keep your guard up at all times."

    ml "Both of you need to pay attention and stay strong out there. It is a wild place. Always pay attention to your surroundings."

    dr "Do you think we are ready? Because I think we can take on anyone that crosses us! HAHA!"

    ml "It seems like you made a new friend."

    ml "glances at Edgar with a curious look on his face."

    ed "Hi, I’m Edgar. Nice to meet you."

    ml "My name is Merlin. It’s good seeing new faces around here lately."

    ml "Well, take care on your next journey, boys."

    "With the help of the Merlin’s map, the three of you make your way to Savanna Forest."

    "After a long and gruelling journey, you, Darrick, and Edgar find yourselves at the entrance of a large plaza."










