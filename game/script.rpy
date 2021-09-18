# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene forest

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show demon_king

    mc "You've created a new Ren'Py game."

    mc "Once you add a story, pictures, and music, you can release it to the world!"

    s "Let's go to chapter 1!"

    # "call" directs users to the label, like "ch1_1" and when it's done,
    # user comes back here. If you use "jump", user will not return to
    # this file anymore.
    
    call ch1_1

    call ch1_2

    call ch2_1

    # This ends the game.

    return
