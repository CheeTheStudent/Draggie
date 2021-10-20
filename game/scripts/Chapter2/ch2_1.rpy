label ch2_1:

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

    "You realize that your body reeks from skipping out on showers during your walk to Olympus."

    mc "{i}*Sigh* I can’t continue my journey like this.{/i}"

    menu:
        mc "{i}I should find a place to _____ up and rest for the night.{/i}"

        "freshen":
            $renpy.fix_rollback()
            $ scores += 10
        "brighten":
            $renpy.fix_rollback()

    "You walk around the unfamiliar town looking for a place to stay."

    "Suddenly, you feel a pat on your back."

    sg "Hey!"

    menu:
        "You turn around and spot a stranger standing behind you, grinning.":

            jump ch2_be_polite_to_stranger

        "You turn around and see a scary-faced mask close to your face.":

            jump ch2_be_hostile_towards_stranger

    label  ch2_be_polite_to_stranger:

        menu:
            "Stunned, you then _____ the stranger, “How can I help you?”"

            "ask":
                $renpy.fix_rollback()
                $ scores += 10
            "asked":
                $renpy.fix_rollback()
            

        sg "Hehe, this way, follow me. I’ll lead you. *still grinning*"

        mc "Thank you, sir. I think I’m good."

        sg "I know an inn, where you can take a rest for the day. I can tell that you must be exhausted."

        menu:
            "Knowing that you will never find a place out _____ on your own, you decide to take up the offer before the stranger leaves."
        
            "there":
                $renpy.fix_rollback()
            "where":
                $renpy.fix_rollback()
            "here":
                $renpy.fix_rollback()
                $ scores += 10

        mc "{i}I am hungry too… and I definitely need a shower badly.{/i}*you think to yourself.*"

        mc "Can I follow you to the inn?"

        sg "Of course, let’s go. I’ll lead the way and you try to keep up, alright?"

        menu:
            "You _____ in agreement."

            "nod":
                $renpy.fix_rollback()
                $ scores += 10
            "nodded":
                $renpy.fix_rollback()
            "nods":
                $renpy.fix_rollback()

        jump ch2_polite_cont

    label  ch2_be_hostile_towards_stranger:

        menu:
            "You are frightened _____ compelled to hit the stranger."

            "not":
                $renpy.fix_rollback()
            "and":
                $renpy.fix_rollback()
                $ scores += 10
            "or":
                $renpy.fix_rollback()

        "“Woah!” The stranger steps back."

        sg  "Hey, hey, take it easy! I’m just joking!"

        "You stop your action and look at the stranger with an alert."

        "The stranger takes off the mask."

        menu:
            sg  "Relax. I’m here to help you. You probably need to go to an inn to tidy up yourself, right? I can lead you ______."

            "where":
                $renpy.fix_rollback()
            "here":
                $renpy.fix_rollback()
            "there":
                $renpy.fix_rollback()
                $ scores += 10

        "You are still on guard against him."

        sg "*Sigh* Alright, I’ll lead you to the inn. You follow behind me, okay?"

        menu:
            "You _____ in agreement."

            "nod":
                $renpy.fix_rollback()
                $ scores += 10
            "nodded":
                $renpy.fix_rollback()
            "nods":
                $renpy.fix_rollback()

        "You follow behind the stranger and walk into the crowd."

        jump ch2_hostile_cont

    label ch2_polite_cont:
        
        menu:
            "On the way to the inn, you take a short break to quench your thirst. When you _____ up, the stranger is gone from your sight."

            "look":
                $renpy.fix_rollback()
                $ scores += 10
            "looked":
                $renpy.fix_rollback()
            "looking":
                $renpy.fix_rollback()

        mc "{i} Hey... Are you there?{/i}"

        "You wonder if you were abandoned by the stranger in the middle of the way."

        mc "{i} He would never do that, he seemed like a nice person{/i} you think to yourself."

        "After circling the area, you find a hint of *Colour of Stranger’s hair* at the back of a rock."

        menu:
            "The stranger quietly creeps up _____ and scares you from the back."

            "further":
                $renpy.fix_rollback()
            "closer":
                $renpy.fix_rollback()
                $ scores += 10

        mc "You really got me there, I almost fell for it!"

        "You both share a good laugh."

        sg "I am pretty sure, you are a smart and brave boy."

        mc "Why do you think so?"

        sg "It’s just an initial feeling."

        jump ch2_both_cont

    label ch2_hostile_cont:

        "On your way following the stranger’s path, You get lost along the way."

        mc "Hey…. Are you there?"

        menu:
            "No one ______ and you are disappointed."

            "replied":
                $renpy.fix_rollback()
            "reply":
                $renpy.fix_rollback()
            "replies":
                $renpy.fix_rollback()
                $ scores += 10

        mc "* Sigh * {i}Where is he? Maybe I’ll just walk down this road and find the inn on my own.{/i}"

        "When you decide to find the inn on your own, the stranger creeps up behind you and scares you all of a sudden."

        sg "You fell for it didn’t you? Hahahahah"

        "You make a poker face and stare at the stranger."

        "The stranger is embarrassed by your stares."

        sg "Alright, I’m sorry, I’ll stop making fun of you. I’ll lead you to the inn now."

        mc "Are you serious now?"

        sg "Yeah! I’m serious. Believe me."

        "You smile, believe him and follow him."

        sg "Oh yeah, let’s go!"

        "Looking at your smile, the stranger becomes lively again."

        jump ch2_both_cont

    label ch2_both_cont:

        "On the way to the inn, the stranger introduces himself as Darrick to you. He also questions your appearance."

        menu:
            "Looking all embarrassed, you mention your encounter with the demon on _____ way to Olympus to Darrick."

            "my":
                $renpy.fix_rollback()
            "our":
                $renpy.fix_rollback()
            "your":
                $renpy.fix_rollback()
                $ scores += 10

        "You also explain that you have no clue how you defeated the demon with the force field."

        menu:
            "As you two approach the inn, Darrick urges you to take a shower while he _____ at the cafeteria."

            "waits":
                $renpy.fix_rollback()
                $ scores += 10
            "wait":
                $renpy.fix_rollback()
            "waited":
                $renpy.fix_rollback()

        "Darrick also helps you out with the payment for the inn and tells you not to not worry about it."

        "After a nice warm bath, you make your way to the cafeteria to find Darrick."

        "You then continue the conversation from where it was left off earlier."

        menu:
            "After you describe the demon that you _____ in the forest, Derrick explains to you that the demon you fought was a goblin."

            "incanted":
                $renpy.fix_rollback()
            "encountered":
                $renpy.fix_rollback()
                $ scores += 10

        "Darrick then raises his hand and produces a force field around it similar to what you experienced."

        "You are in awe at the sight of the force field that Darrick had produced."

        "However, you notice the force field you encountered had a red tint to it as compared to the blue tint of Derrick’s force field."

        menu:
            "You _____ that thought up to Darrick."

            "brought":
                $renpy.fix_rollback()
            "bring":
                $renpy.fix_rollback()
                $ scores += 10
            "bought":
                $renpy.fix_rollback()

        "Darrick seemed to be unfamiliar with that occurrence but he suggests that he should introduce you to the Guild Master."

        menu:
            "By doing so he hopes that the Guild Master will have an answer to _____ doubts."

            "their":
                $renpy.fix_rollback()
            "your":
                $renpy.fix_rollback()
                $ scores += 10
            "our":
                $renpy.fix_rollback()

    menu:

        "You nod in agreement to Darrick’s statement. You become excited and say, “I would love to meet the Guild Master”.":

            jump nod_in_agreement

        "Feeling doubtful, you ask Darrick, “How can the Guild Master help me?”":

            jump feeling_doubtful

    label nod_in_agreement:

        "“When will we leave to meet the Master?” you ask in excitement. “Do we leave now?” you add."

        menu:
            dr "We will leave tomorrow, you can rest today. You _____ be exhausted after that long journey."

            "should":
                $renpy.fix_rollback()
            "will":
                $renpy.fix_rollback()
            "must":
                $renpy.fix_rollback()
                $ scores += 10

        mc "What is for dinner?"

        dr "Porridge, you like it?"

        menu:
            "You are suddenly _____ by a rush of memories as your grandma used to make you porridge every day and it's your favourite meal anyday anytime."

            "overwhelmed":
                $renpy.fix_rollback()
                $ scores += 10
            "underwhelmed":
                $renpy.fix_rollback()

        "“Of course, I love porridge!” you said in excitement. “My grandma used to make this for me everyday,” you add."

        dr "That’s great, although it may not be as delicious as your grandma’s porridge but I hope it keeps you full for now."

        menu:
            mc "Don't worry, it's delicious. It tastes just like my grandma’s porridge."

        "Both you and Darrick eat the porridge for dinner and hit the hay, a well deserved rest after a long day."

        jump ch2_2_cont

    label feeling_doubtful:

        menu:
            dr  "You should not doubt the Guild Master _____, you should meet him for yourself and see."

            "himself":
                $renpy.fix_rollback()
                $ scores += 10
            "itself":
                $renpy.fix_rollback()
            "themself":
                $renpy.fix_rollback()

        mc  "Alright then, I will not doubt the Master’s help. Do we leave now?"

        "You are eager to see if this Guild Master can actually help you solve your doubts."

        dr "Now I see that you're excited to meet the Guild Master, we shall leave tomorrow as its already late and we shall hit the sack soon after dinner."

        jump ch2_2_cont

    label ch2_2_cont:

        "The following day, you and Darrick head towards the guild to meet the Guild Master."

        "Darrick introduces the Guild Master, Merlin, to you."

        menu:
            "Darrick then proceeds to _____ the red force field power you experienced to Merlin."

            "inscribe":
                $renpy.fix_rollback()
            "describe":
                $renpy.fix_rollback()
                $ scores += 10

        "Merlin is taken aback listening to this. He then informs you and Darrick that the red force field power you experienced belongs to the family of dragons."

        "However, he explained that there have been no signs of dragon life that exist in the world today. The last two dragons reported alive had disappeared after their clash with the demon king 10 years ago."

        menu:
            "The three of them are now curious to know how you _____ the power of the dragon family."

            "posess":
                $renpy.fix_rollback()
            "possess":
                $renpy.fix_rollback()
                $ scores += 10
            "posses":
                $renpy.fix_rollback()

        "Merlin’s first theory is that you are a child of the dragons."

    menu:

        "Upon hearing this, you freeze and remain silent. You stutter, “How..What?”":

            jump ch2_positive_reaction

        "Stunned, you say, “Me? A child of dragons? No way.”":

            jump ch2_negative_reaction

    label ch2_positive_reaction:

        menu:
            ml  "It _____ be a shock to you now but you will eventually see that you are gifted."

            "shall":
                $renpy.fix_rollback()
            "would":
                $renpy.fix_rollback()
            "may":
                $renpy.fix_rollback()
                $ scores += 10

        "Merlin immediately notices the silence in the room as soon as he speaks."

        ml "Well, you may find out something if you could find the documentary about dragons."

        "He then quickly changes the topic of their conversation."

        jump ch2_3_cont

    label ch2_negative_reaction:

        "Everyone in the room remains quiet while you make a joke out of what Merlin said."

        menu:
            ml "It’s up to you to believe me or not but that is the truth. You should start taking precautions and explore the guild. Also, you _____ find a documentary about dragons if you want."

            "shall":
                $renpy.fix_rollback()
            "would":
                $renpy.fix_rollback()
            "may":
                $renpy.fix_rollback()
                $ scores += 10

        jump ch2_3_cont

    label ch2_3_cont:

        "Merlin then suggests that you are to be given some time to explore the guild and get comfortable with your surroundings."

        menu:
            "Derrick takes this opportunity to guide you _____ the guild. He knew that you wanted to learn more about this world but you lacked the knowledge and needed time to understand new things."

            "about":
                $renpy.fix_rollback()
            "around":
                $renpy.fix_rollback()
                $ scores += 10
            "over":
                $renpy.fix_rollback()

        "He brings you to the library of the guild and advises you to get used to reading books to help expand your knowledge of the world."

        menu:
            "Darrick soon invites you to become his partner and help him with _____ to help you gain more real life experience."

            "quests":
                $renpy.fix_rollback()
                $ scores += 10
            "missions":
                $renpy.fix_rollback()
                $ scores += 10

        "You agree with the suggestion there and then since you really need to understand the world and learn to cast spells."

        "On top of that, you will also be able to gain some fighting experience and learn to manage financial matters."

        menu:
            "You end up staying in Olympus to gain knowledge of the world, learn to cast spells and _____ missions with Darrick."

            "complete":
                $renpy.fix_rollback()
                $ scores += 10
            "do":
                $renpy.fix_rollback()
                $ scores += 10
            "finish":
                $renpy.fix_rollback()
                $ scores += 10