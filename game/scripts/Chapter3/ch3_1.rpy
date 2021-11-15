label ch3_1:

    "1 year later…"

    "Early in the morning, you meet with Merlin."

    menu:

        mc "Merlin, I _____ I’ll go to Elysium."

        "think":
        $renpy.fix_rollback()
        $ scores += 10

        "thought":
        $renpy.fix_rollback()
        
        "am thinking":
        $renpy.fix_rollback()

    ml "The Mansion of Dragons mentioned in the documentary you found?"

    Mc "Yes. I have been here in Olympus for a year, and I know that my power is different from everyone else's. I want ______(answers, conclusion, explanation) to who I am and if possible… I might find my parents there."

    "Suddenly, Darrick breaks the door and shouts."

    dr "I’m coming with you!"

    Dr "Darrick! How many times do I have to tell you? Knock on the door first before you come in!" 

    menu:

        "Merlin yells _____ Darrick."

        "towards":
        $renpy.fix_rollback()
        $ scores += 10

        "with":
        $renpy.fix_rollback()
        
        "over":
        $renpy.fix_rollback()

    dr "Haha, I’m sorry, I’ll watch out next time."

    Dr "MC, I’m going with you. You can’t leave me behind, and I’m your best partner!"

    mc"Alright, alright, I will never stop you from following me… Hmm, we need to prepare before leaving. So, we are leaving tomorrow."

    dr "Yes, Sir!"

    "The next day"

    "At the entrance of Olympus…"

    menu:

        ml "Be careful on your _____."

        "journy":
        $renpy.fix_rollback()
       
        "jorney":
        $renpy.fix_rollback()
        
        "journey":
        $renpy.fix_rollback()
        $ scores += 10

    mc "Take care, Sir."

    dr "Take care, old man."

    "Walk away while waving hand"
    
    dr "Bye~."
    
    "On the way to Elysium"

    menu:

        dr "MC, are we gonna rest? It’s almost night, I’m so tired and hungry"
        
        "Saying while looking up at the sky."

        "Continue the journey":
            jump ch3_continue_journey


        "Stop to rest":
            jump ch3_rest

    label ch3_continue_journey:
        mc "It’s still early. We still have some time before it gets dark. Let’s walk a little more."

        dr "Alright…"

        jump ch3_darrick_cont

    label ch3_rest:
        mc "Ok then, let’s find a place to have a rest, and we will continue our journey tomorrow. Sounds good for you?"

        dr "Yes!!! Finally I get to rest for such a long walk."

        jump ch3_darrick_cont

    label ch3_darrick_cont:

        "Suddenly, you stopped."

        dr "What’s the matter?"

        mc "I think we’ve got company..." 
        
        "Saying while firing a blast towards nearby grass."

        menu:

            dr "Hey, leave some for me. Fighting demons is the only way to _____ my boredom." 

            "stop":
            $renpy.fix_rollback()
        
            "clear":
            $renpy.fix_rollback()
            $ scores += 10
            
            "solve":
            $renpy.fix_rollback()

        "Both of you are preparing to fight."

        "Demons run away…"

        dr "...Ahh, that’s it? Hey, demons! Come back!" 
        
        "Ran to chase the demons, but he stops."

        mc "Darrick?"

        dr "Woah, Mc, there’s a boy here, still breathing!"

        mc "Is he hurt or something?"

        dr "Nope. He looks fine but just unconscious."

        mc "Okay, we rest here today and find out who he is tomorrow."