# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene forest
    
    show screen gameStats

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show demon_king

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

        "Male":
            pass


    # "call" directs users to the label, like "ch1_1" and when it's done,
    # user comes back here. If you use "jump", user will not return to
    # this file anymore.
    
    call ch1_1

    call ch1_2

    call ch2_1

    # This ends the game.

    return
