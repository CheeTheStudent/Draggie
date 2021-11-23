label ch3_1:

    play sound "audio/1yearLater.mp3"
    
    call scene_transition_title('1 year later...')
    
    scene merlin_office
    show merlin at left:
        ypos 1.1
        
    "Early in the morning, you meet with Merlin."

    menu:

        mc "Merlin, I _____ I’ll go to Elysium."

        "think": 
            $renpy.fix_rollback()
            $ scores += 10

        "thought":
            $renpy.fix_rollback()
        
        "thinks":
            $renpy.fix_rollback()

    ml "The Mansion of Dragons mentioned in the books you've read?"

    mc "Yes. I have been here in Olympus for a year... I know that my powers are different from everyone else's."

    menu:
        mc "I want ______ to who I am and if possible… I want to find my parents."

        "answers":
            $renpy.fix_rollback()
            $ scores += 10
        "conclusion":
            $renpy.fix_rollback()
        "explanation":
            $renpy.fix_rollback()

    play sound "audio/DoorOpen.mp3"

    hide merlin
    
    show darrick at right
    with moveinright

    "Suddenly, Darrick breaks open the door and shouts."

    dr "I’m coming with you!"

    show merlin angry at left:
        ypos 1.1

    ml "Darrick! How many times do I have to tell you? Knock before you come in!" 

    menu:

        "Merlin yells _____ Darrick."

        "at":
            $renpy.fix_rollback()
            $ scores += 10

        "with":
            $renpy.fix_rollback()
        
        "over":
            $renpy.fix_rollback()

    show darrick grin
    dr "Haha, I’m sorry, I’ll watch out next time."

    show merlin

    show darrick
    dr "[mc], I’m going with you. You can’t leave me behind, and I’m your best partner!"

    mc"Alright, alright, I will never leave you behind... We are leaving tomorrow so let's make some preparations first."

    show darrick grin
    dr "Yes, Sir!"

    play sound "audio/TheNextDay.mp3"
    call scene_transition_title('The next day...')

    scene olympus_entrance

    "At the entrance of Olympus…"

    show merlin at left:
        ypos 1.1
    show darrick at right
    menu:
        ml "Be careful on your _____. Look out for each other."

        "journy":
            $renpy.fix_rollback()
       
        "jorney":
            $renpy.fix_rollback()
        
        "journey":
            $renpy.fix_rollback()
            $ scores += 10

    mc "We will, and you take care too, Master."

    dr "Yeah, take care, old man."

    "You and Darrick walk away while waving goodbye to Merlin."
    
    dr "Goodbye!"
    
    call scene_transition_title('On the way to Elysium...')

    scene forest2

    show darrick worried
    dr "[mc], are we gonna rest? It’s almost night, I’m so tired and hungry."

    menu:
        "You look at the sky."

        "Continue the journey":
            jump ch3_continue_journey
        "Stop to rest":
            jump ch3_rest

    label ch3_continue_journey:
        mc "It’s still early. We still have some time before it gets dark. Let’s walk a little more."

        dr "Alright…"

        jump ch3_darrick_cont

    label ch3_rest:
        mc "Ok then, let’s find a place to have a rest, and we will continue our journey tomorrow. Sounds good to you?"

        show darrick
        dr "Yes!!! Finally, I get to rest after such a long walk."

        jump ch3_darrick_cont

    label ch3_darrick_cont:

        "Suddenly, you stop in your tracks."

        show darrick surprised
        dr "What’s the matter?"

        mc "I think we’ve got company..." 
        
        "You fire a blast towards nearby grass."

        show darrick
        menu:
            
            dr "Hey, leave some for me. Fighting demons is the only way to _____ my boredom." 

            "stop":
                $renpy.fix_rollback()
        
            "cure":
                $renpy.fix_rollback()
                $ scores += 10
            
            "solve":
                $renpy.fix_rollback()

        "Both of you prepare to fight."

        "The demons run away."

        dr "...Ahh, that’s it? Hey, demons! Come back!" 
        
        "Darrick runs to chase the demons, but suddenly stops."

        mc "Darrick?"

        scene rest forest

        show darrick surprised
        dr "Woah, [mc], there’s a boy here on the ground... He's still breathing!"

        mc "Is he hurt?"

        show darrick
        dr "Nope. He looks fine, just unconscious."

        mc "Okay, let's rest here today and find out who he is tomorrow."