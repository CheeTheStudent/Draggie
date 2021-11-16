label ch3_2:

    "The next day"

    b: "Argh..."

    menu:

        dr "Oh, you’re _____ !"

        "awoke":
        $renpy.fix_rollback()
        
        "awaken":
        $renpy.fix_rollback()
            
        "awake":
        $renpy.fix_rollback()
        $ scores += 10

    "Do you want some bread?"

    menu:

        "The boy answer.":

            jump ch3_boy_answer

        "The boy does not answer.":

            jump ch3_boy_no_answer

    label ch3_boy_answer:

        b: "...yes, please."

        "The boy gets the bread and stares at both of you."

        jump ch3_boy_cont

    label ch3_boy_no_answer:

        b: "..."

        "The boy doesn’t answer and stares at both of you."

        jump ch3_boy_cont
    
    jump ch3_boy_cont:

        dr ".... [mc], am I looking weird?"

        mc "Huh? No. Why did you ask?"

        dr "He’s staring at me, don’t you see?"

        mc "Not just you. He’s staring at me too."

        dr "Oh ya? ...oh, oh, okay."

        dr "...Are we done staring at each other?"

        b "Who are you?"

        mc "Don’t you think it’s better to tell yours before asking for others?"

        dr "Yes, that’s right, I agree."

        b "..."

        "After some time, the boy started introducing himself."

        b "I only remember that my name is Edgar. I don’t remember anything else."

        dr "I am Darrick, and he is [mc]. So, why are you here unconsciously?"

        mc "He already said he doesn't remember anything."

        dr "Ya, I heard that."

        mc "Then, why are you asking again?"

        dr "I… just… Okay, fine."

        "Edgar smiles."

        ed "Well, what are you doing out here?"

        dr "We are heading to Elysium. Do you want to follow us?"

        ed "..."

        You "It’s dangerous out here alone. We can protect you until your memory recovers."

        "Edgar nods quietly."

        "So you and your friends continue your journey and reach the mansion of Dragons in Elysium."

        menu:

            mc "Wow, this is something beyond my _____ ."

            "imaginations":
            $renpy.fix_rollback()
            
            "expectations":
            $renpy.fix_rollback()
            $ scores += 10 

            "apprehension":
            $renpy.fix_rollback()

        dr "Yeah, it’s insane! I’m claiming this house. Let’s just live here from now on!" (grin)

        ed "...[mc], I think we can leave him here."

        dr "Hey! You made a joke! You’re one of us now!"

        mc "Welcome to the gang."

        menu:

            "Darrick runs into the mansion _____ you and Edgar follow behind closely.

            "while":
            $renpy.fix_rollback()
            $ scores += 10 

            "although":
            $renpy.fix_rollback()

            "but":
            $renpy.fix_rollback()

        menu:

            "Prank Darrick.":
                jump ch3_prank_darrick

            "Ask Darrick to slow down."
                jump ch3_warn_darrick

        label ch3_prank_darrick:
            mc "Watch out, someone is behind you!"

            dr "Oh my god, where!!??"

            ed "Above you!"
    
            "Darrick looks up and trips on the uneven ground."

            dr "Ouch! That hurts!"

            "You and Edgar laugh, watching Darrick pout on the ground." (Edgar smile)

            "Darrick gets up and storms away, pretending to be mad."

            jump ch3_darrick_cont2

        label ch3_warn_darrick:

            mc "Watch out!"

            "Darrick stops in his tracks and looks down at the uneven ground."

            dr "Phew, thanks for the heads up!"

            mc "You are welcome."

            jump ch3_darrick_cont2

        label ch3_darrick_cont2:

            ed "Let’s move on, shall we?"

            menu:

                "You and your friends continue exploring the mansion further and eventually find a _____ of stairs leading to an underground basement.

                "flock":
                $renpy.fix_rollback()
                
                "fleet":
                $renpy.fix_rollback()

                "flight":
                $renpy.fix_rollback()
                $ scores += 10 

            dr "It’s so scary down here… Hold me."

            "You and Edgar ignore Darrick and continue walking down the stairs."

            dr "Hey! Wait for me!"

            "In front of you, you notice a bright, red light coming from the end of the stairs."

            mc "Guys, something is in front."

            menu:

                "You and your friends walk closer to the red light and notice that it is being _____ from a floating crystal-like object.

                "amitted":
                $renpy.fix_rollback()
                
                "emitted":
                $renpy.fix_rollback()
                $ scores += 10

                "admitted":
                $renpy.fix_rollback()

            dr "Woah, what do you think that is?"

            mc "I have no idea. Let’s take a closer look."

            "You approach the crystal, your vision blurring due to the bright reflection it emits."

            "You reach your hand out and look towards Darrick for reassurance."

            mc "Should I?

            "Darrick nods his head in agreement, and without a second thought, you wrap your fingers around the crystal."