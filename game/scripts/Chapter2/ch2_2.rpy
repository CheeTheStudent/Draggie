label ch2_2_cont:

    scene black
    with dissolve
    pause(1)
    scene guild
    with dissolve
    show darrick
    with dissolve

    "The following day, you and Darrick head towards the guild to meet the Guild Master."

    dr "This is Merlin, the Guild Master I was telling you about."

    show darrick at left
    with move
    show merlin at right with dissolve:
        ypos 1.1

    menu:
        "Darrick then proceeds to _____ the red force field you conjured to Merlin."

        "inscribe":
            $renpy.fix_rollback()
        "describe":
            $renpy.fix_rollback()
            $ scores += 10

    "Merlin is taken aback after listening to this."

    ml "The red force field you summoned belongs to the family of dragons."

    ml "However, there have been no signs of dragon life existing in the world today. The last two dragons reported alive disappeared after their clash with the Demon King ten years ago."

    menu:
        "The two of them are now curious to know how you _____ the power of the dragon family."

        "posess":
            $renpy.fix_rollback()
        "possess":
            $renpy.fix_rollback()
            $ scores += 10
        "posses":
            $renpy.fix_rollback()

    ml "My first theory is that you are perhaps a child of the dragons."

    show darrick surprised

    menu:

        "Upon hearing this, you freeze and remain silent."
        
        "How..Wh-what?":
            jump ch2_positive_reaction

        "Me? A child of dragons? You’ve got to be kidding me!":
            jump ch2_negative_reaction

    label ch2_positive_reaction:

    menu:
        ml "I understand it _____ come as a shock to you, but this is just a theory."

        "shall":
            $renpy.fix_rollback()
        "would":
            $renpy.fix_rollback()
        "may":
            $renpy.fix_rollback()
            $ scores += 10

    ml "There are many other reasons one might inherit dragon powers."
    
    "Merlin immediately notices the silence in the room as soon as he speaks."
    
    ml "Well, you might find something of interest by reading some books about dragons."
    
    "He then quickly changes the topic of their conversation."

    show darrick

    jump ch2_3_cont

    label ch2_negative_reaction:

    show darrick

    "Everyone in the room remains quiet as you dismiss what Merlin said carelessly."

    ml "It’s up to you to believe me or not, but it is still just a theory. You should start taking precautions and explore the guild."

    menu:
        ml "Also, you _____ look into dragons if you want."

        "shall":
            $renpy.fix_rollback()
        "would":
            $renpy.fix_rollback()
        "may":
            $renpy.fix_rollback()
            $ scores += 10

    jump ch2_3_cont

    label ch2_3_cont:

    "Merlin suggests that you take some time to explore the guild and get comfortable with your surroundings."

    menu:
        "Darrick takes this opportunity to guide you _____ the guild. He knows that you want to learn more about this world, but you lack the knowledge and need time to adjust."

        "about":
            $renpy.fix_rollback()
        "around":
            $renpy.fix_rollback()
            $ scores += 10
        "over":
            $renpy.fix_rollback()

    show darrick grin

    dr "Hey, I'll show you the guild library. You should get used to reading books to help expand your knowledge of the world."

    scene library
    with dissolve
    show darrick
    with dissolve

    menu:
        "Darrick invites you to become his partner and help him out with _____ to help you gain more experiences."

        "quests":
            $renpy.fix_rollback()
            $ scores += 10
        "missions":
            $renpy.fix_rollback()
            $ scores += 10

    "You agree with his suggestion and become determined to understand the world and learn magic."

    show darrick grin

    menu:
        "You end up staying in Olympus to gain more knowledge, learn to cast spells, and _____ missions with Darrick."

        "complete":
            $renpy.fix_rollback()
            $ scores += 10
        "doing":
            $renpy.fix_rollback()
        "finish":
            $renpy.fix_rollback()