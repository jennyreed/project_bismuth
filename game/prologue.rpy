# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ry = Character("????")
define ro = Character("?????")

# The game starts here.

label prologue:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black 

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "{b}{i}CRASH!{/i}{/b}" with hpunch

    show castle1

    with fade

    "Panicked feet flee down the long stone hallway as ragged breaths mix with loud crashes of thunder."
    
    "The young man grips his eye socket with one bloodied hand and his ribs with the other, practically having to hold in what remained of his right eye."

    ro "REE HEE HEE HEE HEE HEE!!"

    "A maddened howl of laughter bounces down the hall, causing the fleeing figure to growl and clutch his torn eye socket tighter."

    ry "Gods damn you...."

    "His insult is answered by sharp metal vines erupting from the walls and floor, gaining him little to no solace and forcing him to run once more."

    ro "YOU CAN RUN, BUT YOU--"

    "SMASH" with hpunch

    ro "--CAN'T--"

    "{b}{i}CRASH!{/i}{/b}" with vpunch

    ##Rylo darts around a corner holding the hilt of a blade, only for a grinning face to appear next to him.

    ##whispering sound effect

    ""

    ""

    ro "{cps=0}hide.{/cps}"

    "He screams and is thrown back hard on the concrete slabs."

    ro "Come now my dear, you didn't think I'd let you go so easily? You and I are not finished."

    ry "Ro, listen-"

    ro "YOU DO NOT CALL ME BY THAT NAME!"

    ro "SHE IS DEAD!" 
    
    ro "I." 
    
    ro "KILLED." 
    
    ro "HER."

    "She pants for a bit, taking a deep breath before returning to her quietly deadly composure."

    ro "Haah… haah.. After all this… I can't believe you would just try to leave me… you... You...  traitorous BASTARD!"

    ry "Just--! Shut UP for once and LISTEN TO M-!"

    "SLAP!" with hpunch

    ry "...!"

    "She stretched her fingers slightly, as if slapping him had brought more pain to her than the one in a crumpled heap on the floor."

    ro "You. Do not understand. I have.. Done so much for this family." 
    
    ro "For us."

    ro "You said. You {cps=8}PROMISED.{/cps} We'd be together."

    "Her eyes turned black."

    ro "Or does the promise of a sibling mean nothing to you?"

    ry "Shut up..."

    ry "shutupshutupshutupSHUTUP!"

    "FWOOM"

    "His hands burning with unquenchable flame, he grabs the mad woman's face briefly, before shoving her away into the ground."

    "Without turning back to check on her he fled, the only confirmation that his tyrannical sister was still alive being the howls of pain and fury following him into the night..."


    hide castle1
    
    with dissolve

    # This ends the game.

    return
