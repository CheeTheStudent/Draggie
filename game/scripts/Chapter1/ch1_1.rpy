# We can divide each chapter into a few sections based on each scene.
#This scene will be the MC's dream and finding out about MC's grandma.

label ch1_1:

  menu:

    "10 years ago when [mc] was 3 years old, a demon king was ___________ into the world."

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
   
  "Now, this is all that people recall from the _____ (incident, accident)."

  "[mc] finds [himself] facing two blurry unfamiliar figures in the fog."

  "They are casting some sort of spell on [him]."

  "The things they are _____ (said, saying, says) are hard to make out except for a few words."

  "Mysterious Voice" "{i}Beware of the black flame...{/i}"

  "Suddenly, [mc] wakes up and realizes it was all a dream."

  mc "{i}Gosh, that was a weird dream!{/i}"

  "It’s broad daylight and the sun is _____ (shining, sparkling, sprinkling) through the windows of [mc]’s room."

  mc "{i}What a lovely day, I guess I better start getting dressed for breakfast with grandma.{/i}"

  "[mc] makes [his] way downstairs towards the dining area to have breakfast but notices the empty table."

  mc "{i}That’s odd… I wonder where grandma is...{/i}"

  "[mc] has been living with [his] grandma for as long as [he] can remember."

  "She is usually awake before sunrise and she prepares breakfast for [mc]."

  "[mc] goes around the house, looking for [his] grandma."

  mc "Grandma, where _____ (is, are, was) you?"

  "[He] looks for grandma all over the house and eventually finds her lying still on the bed."

  mc "Grandma, are you okay… do you need help?"

  menu:

    "Grandma chooses to ignore the question and instead, gestures for [mc] to come closer."

    "Go closer":

      jump ch1_care_for_grandma

    "Ignore her":

      jump ch1_ignore_grandma

  label ch1_care_for_grandma:

    "[He] goes closer to grandma."

    mc "How can I help you grandma?"

    mc "{i}What happened to grandma today?{/i}"

    "[mc] walks towards grandma's bed."

    jump ch1_grandma_cont

  label ch1_ignore_grandma:

    mc "Later, grandma. I’m going to prepare breakfast now. You can stay in bed."

    "[He] turns to walk away."

    "Suddenly, grandma starts coughing badly."

    mc "{i}Something is wrong with grandma…{/i}"

    "[mc] rushes close to grandma's bed."

    mc "Grandma, are you okay?"

    jump ch1_grandma_cont

  label ch1_grandma_cont:

    "Grandma finally _____ (broken, breaks, breaking) the silence and starts speaking to [him]."

