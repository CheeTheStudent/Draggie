style chapter_title_style is text:
  font "MedievalSharp-Regular.ttf"
  color "ffd92e"
  size 100

image chapter_title = ParameterizedText(style="chapter_title_style")

label chapter_splash_screen(chap):

  scene black
  with dissolve
  with Pause(1)

  show chapter_title "Chapter [chap]" at truecenter
  with dissolve
  with Pause(2)

  scene black with dissolve
  with Pause(2)

  return