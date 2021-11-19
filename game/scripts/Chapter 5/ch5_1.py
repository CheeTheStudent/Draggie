label ch5_1:

    "You reach a wide, open plaza in Savanna Forest."

    "The plaza looks ancient and abandoned, but it emits a powerful and mysterious aura."

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
    
    ed "I... I'm feeling a little bit dizzy. So you guys go on without me. I'll catch up later."

    dr "MC, I'll stay here with Edgar. You can explore the plaza first."

    mc "Are you sure?"

    "Darrick grins. (Action)"

    dr "Yup, we'll catch up with you."

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

    "Suddenly, right before your eyes, a shiny teardrop materialises in front of you."

    "The warmth of the air feels cosy and familiar. You reach out your hand and grab the teardrop."

    mc "This is it.."

    mc "Argh!"

    "You fall to the ground as soon as your hand wraps around the teardrop. Your head starts hurting."

    mc "My head.. it hurts so much... What's going on?"

    "As quickly as it comes, the pain leaves, and you feel something change within you."

    dr "MC! Are you alright? I saw you fall.."

    mc "No, I mean, yes I did fall, but I... I'm alright... I feel amazing!"

    mc "I found the teardrop, and when I touched it, I felt something changed in me. I feel.. warmer now."

    "Darrick looks at you in shock."

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

    "The ground shakes violently. You and Darrick turn to look at Edgar, who starts charging at you angrily."

    dr "Hey Edgar! Calm down!"

    "Edgar throws his hand towards Darrick, and a black wave knocks Darrick to the ground."

    mc "Darrick!"

    "You try to run to Darrick, but Edgar extends his hand towards you instead, a black ball of fire already forming."

    "Quickly, you extend your hand towards him, and a bright red ball of fire strikes Edgar."

    mc "Wait- What? How did I do that?"

    ed "You killed my people! I'll make you pay!"

    mc "Edgar, stop! What's going on with you?"

    ed "You.. Don't you get it now? The teardrops, the fire, the tattoo.."

    ed "You're the child of the last two dragons. The dragons who defeated me ten years ago.."

    mc "Defeated you? Edgar... What do you mean? You were only a child ten years ago. How could dragons have fought with you?"

    ed "I am no child, MC, and neither are you. Coming to this place restored my memories. This was where the fight happened.. The fight between the dragons and me." 

    ed "I am Edgar, the Demon King of the Underworld. I was reborn after your parents banished me from this world ten years ago."

    ed  "And you... You are their only child, the last dragon... So you have to pay for what they have done."

    "Edgar summons black flames onto his hands, preparing to strike you. "

    # Ending 1 - Bad

    mc "Wait!!"

    mc "Why are you doing this, Edgar?"

    mc "You can't punish me for something that happened years ago while I was only a child."

    ed "You are the last dragon, and all dragons should vanish from this world."
    
    mc  "People say you caused chaos and mayhem, so the dragons had to risk their lives to stop you. It was their job!"

    ed "All you believe is what people say, huh? Do you even know why I did all those things?"

    mc "I.. I am sure there's no good reason for killing thousands of innocent people. You should be thankful you have a second chance to live after what you did."

    ed "You know nothing, MC. This world is corrupted, and I am the only one who can fix it."

    MC "And how are you going to do that?"

    ed "By killing as many people as I have to. All who listen to my commands will be spared. It will be a peaceful world with a good leader."

    mc "That's crazy, Edgar. Lives are not for us to take."

    ed "I think I can decide that for myself, MC."

    ed "However, I shall spare your life. You and Darrick have been.. good to me. I may be cruel, but I know when to be grateful."

    ed "This time, I'll let you two go. But if I ever see you again, MC, don't expect me to be so kind."

    "Edgar turns his back on you and disappears before you can respond."

    dr "Are you alright, MC?"

    mc "I'm fine... Are you okay? He pushed you quite hard just now."

    dr "It was just a scratch. So don't worry about it!"

    dr "I'm shocked, though... I didn't know we were travelling with the Demon King all this time!"

    dr "And you're a Dragon! That's insane!"

    dr "But.. What are we going to do about Edgar? I mean, the Demon King... Is he planning to conquer the world?"

    mc "I don't know, Darrick. The best we can do now is prepare for the worst. If he is as dangerous as they say, I don't know if we can stop him."

    mc "I wish I did a better job at convincing Edgar to stay. He was such an innocent guy, and I'm sure there's good in him.. :

    mc "I just didn't know how to reach it."

    dr "Well, we can't do anything about it now."

    dr "Let's head back to the city to tell Merlin about it, alright? He'll fix this."

    "You sigh and follow Darrick back to the city."

    mc "I don't think this is something we can fix."

    # Ending 2 - Good

    mc "Wait!!"

    mc "It doesn’t have to end like this!”

    ed "You left me no choice, child."

    ed "This world is ruined, and all the people who dwell here are destroying it."

    ed "I must cleanse the world and build it anew!"

    "Edgar hurls the ball of black flame in his hand at you, and it barely misses your ear."

    mc "Edgar, please! Just hear me out!"

    "You nimbly dodge every fireball that Edgar casts."

    ed "I will hear none of it! They deserve to die anyway."

    "Edgar shoots another blast of black flame, and this time it hits home."

    "The black flame shot by Edgar scorches your thigh. "

    mc "Edgar, just stop! You would do all this to hurt me after all that we have been through?"

    ed "Silence! My decision has been made!"

    "An enormous blast of black flame knocks you back."

    mc "Fine. We can do it your way."

    "You channel all your energy into the teardrop as it amplifies your power. "

    mc "Edgar, we don’t have to do this!"

    "As the teardrop slowly fuses with your flames, you shoot a blast of fire so big at Edgar that you could never imagine you were possessed."

    "Edgar takes the blow and is blasted several meters back."

    "For a moment, Edgar doesn’t move."

    "Hurriedly, you catch up to him and investigate the damage you dealt."

    mc "Edgar, are you alright? I didn’t mean to create that big of a blast."

    ed "I see now why the dragons chose you."

    mc "No matter! What matters right now is that you are still alive!"

    ed "With that much potential, you could rule the world too, you know."

    mc "Nah, that’s too much of a responsibility for me to handle. Just promise me you will never do it again."

    ed "You did beat me, after all."

    mc "Of course I did."

    mc "Promise me, Edgar."

    "Edgar suddenly coughs out a mouthful of blood."

    ed "I.."

    "You come to your senses and realise that because you channelled your power into the teardrop, the last blast you had shot at Edgar was amplified."

    "Edgar’s life had been seeping away from the moment you fired the blast."

    mc "Oh Edgar, I’m so sorry… I didn’t mean-"

    "Edgar takes a drag of the last breath."

    ed "It’s…..okay…."

    "Darrick rushes up to you."

    dr "Hey, now. At least we won’t have to worry about anyone taking over the world anymore."

    "You are suddenly overwhelmed by the power and your actions against Edgar."

    "You brace your tears."

    mc "You are right, Darrick. We have defeated him for the greater good."

    mc "He will never cause chaos ever again."

    "Darrick kneels next to you and embraces you."

    "With your head buried in Darrick’s embrace, the last few moments of your fight with Edgar drift away from your mind."

    "You know that you did the right thing."

    # Ending 3 - Best

    mc "Wait!!"

    mc "I may be the child of the last dragons... But I'm also your friend."

    mc "You might be the Demon King, but I would never hurt you."

    mc "Don’t you think we can sort this out another way? I’m sure the dragons didn’t mean to banish you like that!"

    "Darrick grabs you, expecting Edgar to hurl the ball of black flame that he had conjured in his hands."

    "To your surprise, Edgar pauses and thinks for a moment."

    "You don’t remember the battle, after all."

    ed "Tell me, what do you mean that the dragons ‘didn’t mean to banish me like that?"

    mc "They only did what’s best for humanity then. You had wreaked too much havoc, and it was all the dragons could do to prevent worse from happening."

    mc "Listen to me. You have been given one more chance. Take it and change for the better."

    ed "But why…."

    mc "The dragons saw something in you. They believed that someone could change you."

    ed "And that someone…."

    mc "Is me."

    mc "Listen, Edgar, the fight that took place 10 years ago was 10 years ago! Do you even have any concept of time?"

    ed "Hmmm….. You are right. I am the Demon King after all, and naturally, I don’t have any concept of time."

    "Darrick nods in agreement."

    mc "Yes, exactly. So give me a chance. I can show you how much the world has changed."

    ed "Very well then. I hope you can talk some sense into your people."

    ed "Just know that if anyone ever tries to start the same thing that happened 10 years ago, I will be the first to execute them."

    mc "Trust me. It’s been years since the fight between you and the dragons took place. Things have very much changed."

    "Edgar reluctantly agrees, baring his arms open with a slight bow as if to embrace you."

    ed "Alright then, show me."

    mc "Oh Edgar, you'd be surprised!"

    "You head off with Edgar and Darrick out of the Savanna Forest into the night, knowing that the Demon King had a change of heart, and with the Guild’s eye as well as yours on him, he will never cause trouble in the world again."





