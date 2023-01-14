# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ry = Character("????")
define ro = Character("?????")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black 

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "{b}{i}CRASH!{/i}{/b}"

    "Panicked feet flee down the long stone hallway as ragged breaths mix with loud crashes of thunder."
    
    "The young man grips his eye socket with one bloodied hand and his ribs with the other, practically having to hold in what remained of his right eye."

    ro "REE HEE HEE HEE HEE HEE!!"

    "A maddened howl of laughter bounces down the hall, causing the fleeing figure to growl and clutch his torn eye socket tighter."

    ry "Gods damn you...."

    "His insult is answered by sharp metal vines erupting from the walls and floor, gaining him little to no solace and forcing him to run once more."
 
    with dissolve

    # This ends the game.

    return
