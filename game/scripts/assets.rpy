# Here you can define characters, images, or audios with simple variables!
# These will be used for a;; the definitions in all the chapters.

###########     CHARACTERS      ###########
define mc = Character("[player_name]", who_color="#92fcfb")
define gm = Character("Grandma", who_color="e0ab2f")
define s = Character("Salazar")
define sg = Character("Stranger", who_color="e0ab2f")
define dr = Character("Darrick", who_color="e0ab2f")
define ml = Character("Merlin", who_color="e0ab2f")
define ed = Character("Edgar", who_color="e0ab2f")

###########     BACKGROUNDS     ###########


###########     VARIABLES     ###########
default scores = 0

default he = "he"
default his = "his"
default him = "him"
default himself = "himself"
default He = "He"
default His = "His"
default boy = "boy"
default Boy = "Boy"

###########     ANIMATIONS     ###########
define shakescreen_long = Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.5)

init python:
  def eyewarp(x):
      return x**1.33
  eyes_awake = ImageDissolve("eye.png", 1.0, ramplen=128, reverse=False, time_warp=eyewarp)
  eyes_asleep = ImageDissolve("eye.png", 1.0, ramplen=128, reverse=True, time_warp=eyewarp)

define eyes_open = ImageDissolve("shuteye.png", 1.5, 100)
define eyes_close = ImageDissolve("shuteye.png", 0.3, 100, reverse=True)

transform rotation_slow:
  around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
  subpixel True
  rotate 0
  linear 30.0 rotate 360 #linear to change speed
  repeat