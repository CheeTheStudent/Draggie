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
            $ son = "daughter"
            $ Son = "Daughter"

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

    call chapter_splash_screen(3)
    show screen gameStats
    call ch3_1
    call ch3_2

    call chapter_splash_screen(4)
    show screen gameStats
    call ch4_1
    
    call chapter_splash_screen(5)
    show screen gameStats
    call ch5_1
  
    call scene_transition_title('The End')

    # This ends the game.

    return
