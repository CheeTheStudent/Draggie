style title_style is text:
  size 60

image title = ParameterizedText(style="title_style")

label scene_transition_title(text):

  scene black
  with dissolve
  with Pause(1)

  show title "[text]" at truecenter
  with dissolve
  with Pause(2)

  scene black with dissolve
  with Pause(2)

  return