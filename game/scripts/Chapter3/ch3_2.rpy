label ch3_2:

    play sound "audio/TheNextDay.mp3"
    call scene_transition_title('The next day...')

    scene rest forest

    show edgar 
    b "Argh..."

    show edgar at left
    with move
    show darrick at right with dissolve

    menu:

        dr "Oh, you’re _____ ! Do you want some bread?"

        "awoke":
            $renpy.fix_rollback()
            jump ch3_boy_no_answer
        
        "awaken":
            $renpy.fix_rollback()
            jump ch3_boy_no_answer
            
        "awake":
            $renpy.fix_rollback()
            $ scores += 10
            jump ch3_boy_answer

    label ch3_boy_answer:

        b "...yes, please."

        "The boy takes the bread and stares at both of you."

        jump ch3_boy_cont

    label ch3_boy_no_answer:

        b "..."

        "The boy doesn’t answer and stares at both of you."

        jump ch3_boy_cont
    
    label ch3_boy_cont:

        dr ".... [mc], is there something on my face?"

        mc "Huh? No. Why do you ask?"

        show darrick angry
        dr "He’s staring at me, don’t you see?"

        mc "Not just you. He’s staring at me too."

        show darrick
        dr "Oh, is that right? ...Oh, oh, okay."

        "..."

        dr "...Are we done staring at each other?"

        b "Who are you?"

        mc "Don’t you think it’s better to introduce yourself first?"

        dr "Yes, that’s right, I agree."

        b "..."

        "After some time, the boy starts introducing himself."

        b "I only remember my name is Edgar. I can't recall anything else."

        dr "I'm Darrick, and [he]'s [mc]. So, why were you here, unconscious on the ground?"

        mc "He already said he doesn't remember anything."

        dr "Ya, I heard that."

        mc "Then, why are you asking again?"
        
        show darrick worried
        dr "I… just… Okay, fine."

        show darrick

        ed "Well, what are you two doing out here?"

        dr "We are heading to Elysium. Do you want to follow us?"

        ed "..."

        mc "It’s dangerous out here alone. We can protect you until your memory recovers."

        "Edgar nods quietly."

        hide edgar
        hide darrick
        with dissolve

        scene mansion
        with dissolve

        "You and your friends continue your journey and reach Elysium, the mansion of Dragons."

        menu:

            mc "Wow, this is beyond my _____ ."

            "imaginations":
                $renpy.fix_rollback()
            
            "expectations":
                $renpy.fix_rollback()
                $ scores += 10 

            "apprehension":
                $renpy.fix_rollback()

        show darrick grin 
        dr "Yeah, it’s insane! I’m claiming this house. Let’s just live here from now on!"

        show darrick at left
        with move
        show edgar at right with dissolve
        ed "...[mc], I think we should just leave him here..."

        show darrick grin
        dr "Hey! You made a joke! You’re one of us now!"

        mc "Welcome to the gang."

        menu:
            "Darrick runs into the mansion _____ you and Edgar follow behind closely."

            "while":
                $renpy.fix_rollback()
                $ scores += 10 

            "although":
                $renpy.fix_rollback()

            "but":
                $renpy.fix_rollback()

        scene inside mansion
        with dissolve

        menu:
            "Prank Darrick.":
                jump ch3_prank_darrick

            "Ask Darrick to slow down.":
                jump ch3_warn_darrick

        label ch3_prank_darrick:

            mc "Watch out, there's someone behind you!"

            show darrick surprised
            dr "Oh my god, where!!??"

            ed "Above you!"
    
            "Darrick looks up and trips on the uneven ground."

            show darrick worried at left
            with move
            dr "Ouch! That hurt!"

            show edgar smile at right
            with dissolve

            "You and Edgar laugh, watching Darrick pout on the ground."

            "Darrick gets up and storms away, pretending to be mad."

            jump ch3_darrick_cont2

        label ch3_warn_darrick:

            mc "Watch out!"

            "Darrick stops in his tracks and looks down at the uneven ground."

            show darrick surprised
            dr "Phew, thanks for the heads up!"

            mc "You're welcome."

            jump ch3_darrick_cont2

        label ch3_darrick_cont2:

            show darrick
            ed "Let’s move on, shall we?"

            menu:
                "You and your friends continue exploring the mansion further and eventually find a _____ of stairs leading to an underground basement."

                "flock":
                    $renpy.fix_rollback()
                
                "fleet":
                    $renpy.fix_rollback()

                "flight":
                    $renpy.fix_rollback()
                    $ scores += 10 

            scene stairs
            with dissolve

            show darrick worried at left
            show edgar at right
            with dissolve
            dr "It’s so scary down here… Hold me."

            "You and Edgar ignore Darrick and continue walking down the stairs."

            show darrick
            dr "Hey! Wait for me!"

            hide darrick
            hide edgar
            "In front of you, you notice a bright, red light coming from the end of the stairs."

            scene red light
            with dissolve

            mc "Guys, something is in front."

            scene far blur crystal
            with dissolve

            menu:

                "You and your friends walk closer to the red light and notice that it is being _____ from a floating crystal-like object."

                "amitted":
                    $renpy.fix_rollback()
                
                "emitted":
                    $renpy.fix_rollback()
                    $ scores += 10

                "admitted":
                    $renpy.fix_rollback()

            show darrick surprised at left
            with dissolve
            dr "Woah, what do you think that is?"
            
            mc "I have no idea. Let’s take a closer look."
            hide darrick
            with dissolve

            scene blur crystal
            with eyes_awake
            scene blur crystal
            with eyes_asleep
            
            "You approach the crystal, your vision blurring due to the bright reflection it emits."

            "You reach your hand out and look towards Darrick for reassurance."

            show darrick at left
            with dissolve
            mc "Should I?"

            "Darrick nods his head in agreement, and without a second thought, you wrap your fingers around the crystal."