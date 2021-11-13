label ch1_2:

  gm "[mc]… I’m sorry I kept this from you all these years."

  gm "I never wanted to hurt you… I love you like my own grandchild."

  mc "... Grandma? What’s going on? What do you mean?"

  gm "[mc]… 10 years ago, a woman came to me, asking for help on my doorstep."

  gm "She was carrying an adorable crying baby [boy]... She asked me to take care of [him]. She had urgent matters to attend to."

  gm "That baby [boy] stopped crying the moment I held [him]."

  show grandma smile
  "She smiles at you."

  gm "That baby [boy] was you, [mc]. You are the best grandchild I could ever ask for."

  show grandma neutral
  gm "Your mother left you a letter before she left."

  "She places a folded letter onto the palm of your hand."

  gm "It’s time for you to take care of yourself, [mc]."

  gm "You will face many challenges ahead… so make good friends and you won’t have to face them alone."

  menu:
      gm "I believe you will _____ able to survive just fine without me, my dear [boy]."

      "can":
        $renpy.fix_rollback()
      "be":
        $renpy.fix_rollback()
        $ scores += 10
      "shall":
        $renpy.fix_rollback()

  hide grandma
  with fade
  "Grandma closes her eye and you feels her pulse beating slowly to a stop."

  "Your eyes fill up with tears, trying to process what happened."

  menu:
      "For the first time in a long time, you start _____."

      "balling":
        $renpy.fix_rollback()
      "bawling":
        $renpy.fix_rollback()
        $ scores += 10


  call scene_transition_title('Time passes..')
  

  play sound "audio/WaterFlow.mp3"
  scene home
  with dissolve

  "A couple of weeks have passed since the death of your grandma."

  "You have been sheltered by grandma for the majority of your life."

  "You have now decided to get out of your comfort zone and explore the city to gain new knowledge and experience."

  menu:
      "You live in the mountains. In order to _____ into the city, you need to cross a forest."

      "venture":
        $renpy.fix_rollback()
      "venturing":
        $renpy.fix_rollback()
        $ scores += 10
  
  stop sound
  
  scene forest
  show goblin
  with dissolve

  "The journey to the city was not an easy task. As you approach the final leg of the journey, you encounter a demon that tries to harm you."  
  play sound "audio/GoblinLaugh.mp3"

  mc "{i}How am I going to fight this demon?{/i}"

  mc "{i}I never fought anyone before... And I’m no match for the demon’s speed.{/i}"

  "Suddenly, the demon starts running towards you."
  show goblin fierce
  with shakescreen_long

  scene black
  with eyes_close
  menu:
      "You brace yourself for the _____, holding up your hands and closing your eyes."

      "affect":
        $renpy.fix_rollback()
      "effect":
        $renpy.fix_rollback()
      "impact":
        $renpy.fix_rollback()
        $ scores += 10


  "But the impact never comes."

  scene forest
  show magic red full
  with eyes_open

  "Confused, you open your eyes and find the demon lying on the ground, defeated."

  mc "{i}What is going on, how am I alive?{/i}"

  "You realize a force field is shining brightly around you."

  mc "{i}The force field protected me… Not only that, it even reflected the demon’s attack!{/i}"

  mc "{i}Did… Did I do that?{/i}"

  "You lower your hands and watch the force field disappear."

  hide magic red
  with dissolve

  menu:
      "You slowly come to the _____ that as crazy as it is, you have supernatural powers!"

      "realization":
        $renpy.fix_rollback()
        $ scores += 10
      "realizing":
        $renpy.fix_rollback()
      "reality":
        $renpy.fix_rollback()


  mc "{i}That is awesome!{/i}"

  "With the help of the force field, you manage to defeat the demon and continue your journey to the city."