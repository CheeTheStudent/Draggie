# We can divide each chapter into a few sections based on each scene.
#This scene will be the MC's dream and finding out about MC's grandma.

label ch1_1:

  scene burning_village

  menu:

    "10 years ago, a demon king was _____ into the world."

    "birth":

      $ renpy.fix_rollback() # This is to prevent users changing answers
      
      "This is the wrong answer. Choosing wrong answers will deduct your scores." (what_color="#cc8888")

      "Your scores won't be deducted now, but it will the next time!" (what_color="#cc8888")

    "born": 

      $ renpy.fix_rollback()
      $ scores += 10
      "That's right! Keep answering the questions correctly to add scores." (what_color="#8c8")

  "Remember your scores will determine the ending." (what_color="#8c8")

  "So think twice before answering! Now, on with the story!" (what_color="#8c8")

  "The Demon King was a cruel and evil being who showed no mercy."

  "He burned villages and cities down to ashes, and killed thousands of people."

  "At that time, the last two remaining dragons stepped up to fight against the Demon King to save the world from slaughter."

  "The battle finally ended when the dragons and the Demon King mysteriously disappeared."
   
  menu:
    "Now, this is all that people recall from the _____ ."

    "incident":
      $ renpy.fix_rollback()
      $ scores += 10
    
    "accident":
      $ renpy.fix_rollback()

  scene black
  with Pause(1)

  "You find yourself facing two blurry unfamiliar figures in the fog."

  scene misty_parents
  with dissolve

  "They are casting some sort of spell on you."

  menu:
    "The things they are _____ are hard to make out except for a few words."

    "said":
      $renpy.fix_rollback()

    "saying":
      $renpy.fix_rollback()
      $ scores += 10

    "says":
      $renpy.fix_rollback()

  "Mysterious Voice" "{i}Beware of the black flame...{/i}"

  "Suddenly, you wake up and realize it was all a dream."

  scene bedroom

  mc "{i}Gosh, that was a weird dream!{/i}"

  menu:

    "It’s broad daylight and the sun is _____ through the windows of your room."

    "shining":
      $renpy.fix_rollback()
      $ scores += 10
    "sparkling":
      $renpy.fix_rollback()
    "sprinkling":
      $renpy.fix_rollback()

  mc "{i}What a lovely day, I guess I better start getting dressed for breakfast with grandma.{/i}"

  scene kitchen

  "You make your way downstairs towards the dining area to have breakfast but notice the empty table."

  mc "{i}That’s odd… I wonder where grandma is...{/i}"

  "You have been living with grandma for as long as you can remember."

  "She is usually awake before sunrise and she prepares breakfast for you."

  "You go around the house, looking for your grandma."

  menu:
    mc "Grandma, where _____ you?"

    "is":
      $renpy.fix_rollback()
    "are":
      $renpy.fix_rollback()
      $ scores += 10
    "was":
      $renpy.fix_rollback()

  "You look for grandma all over the house and eventually find her lying still on the bed."

  mc "Grandma, are you okay… do you need help?"

  menu:

    "Grandma chooses to ignore the question and instead, gestures for you to come closer."

    "Go closer":

      jump ch1_care_for_grandma

    "Ignore her":

      jump ch1_ignore_grandma

  label ch1_care_for_grandma:

    "You go closer to grandma."

    mc "How can I help you grandma?"

    mc "{i}What happened to grandma today?{/i}"

    "You walk towards grandma's bed."

    jump ch1_grandma_cont

  label ch1_ignore_grandma:

    mc "Later, grandma. I’m going to prepare breakfast now. You can stay in bed."

    "You turn to walk away."

    "Suddenly, grandma starts coughing badly."

    mc "{i}Something is wrong with grandma…{/i}"

    "You rush close to grandma's bed."

    mc "Grandma, are you okay?"

    jump ch1_grandma_cont

  label ch1_grandma_cont:

    menu:
      "Grandma finally _____ the silence and starts speaking to you."

      "broken":
        $renpy.fix_rollback()
      "breaks":
        $renpy.fix_rollback()
        $ scores += 10
      "breaking":
        $renpy.fix_rollback()

