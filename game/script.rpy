# The game starts here.

label start:

    # Prompts user to key in name

    python:
        player_name = renpy.input("Enter your name.", length=32)
        player_name = player_name.strip()

        if not player_name:
            player_name = "Ren"

    menu:

        "Select your gender."

        "Female": 
            $ he = "she"
            $ his = "her"
            $ him = "her"
            $ himself = "herself"
            $ He = "She"
            $ His = "Her"
            $ boy = "girl"
            $ Boy = "Girl"

        "Male":
            pass


    # "call" directs users to the label, like "ch1_1" and when it's done,
    # user comes back here. If you use "jump", user will not return to
    # this file anymore.
    
    call chapter_splash_screen(1)
    show screen gameStats
    call ch1_1
    call ch1_2

    call chapter_splash_screen(2)
    show screen gameStats
    call ch2_1

    # This ends the game.

    return
