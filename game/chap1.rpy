define f = Character("Fern")
define fu = Character("Furu")
define ry = Character("Rylo")
define m = Character("Melyssa")

label chap1:
    "My eyes creak open, but I do not see a thing. My body still feels heavy from sleep, but I can tell what time of day it is from the sound of--"

    "SCREEEECHH!"

    "A flock of sand hawks swoop over the camp, most likely waking others up as well. I rub my eyes and blindly swat out to open the tent flap." 

    ##[Sweep transition to the savanna setting]

    "A wave of soothing heat and lightly dusty wind greets me. Early in the morning the heat isn't so bad… mornings and nights are my favourite time of day for this reason."

    "Far on the horizon the gigantuous head of Solephica rests against the mountain, the slowly brightening sun glinting off the metal and right into my eyeballs." 

    fu "Rise and shine, trooper."

    "A green light stirs in my chest as Furu awakes, materializing in front of me."

    menu:
        "Amused":
            jump amused

        "Annoyed":
            jump angry   

    label amused:
        m "Oh-! Haha, hey Furu. Didn't reckon you'd be out so soon."
        jump cont

    label angry:
        m "Furu- please give me a warning before you decide to- exist."
        jump cont
            
    
    label cont:

        "I rub the goosebumps from my arms, which are unusual to see in the heat. Whenever he does this without me being ready, it quite literally feels like my heart is being yanked out of my chest."

        "Furu chuckles, small specks of cinders flittering from his nostrils." 

        fu "'Ey, its a good wake up call."

        "I raise my arm so he can perch on it."

        fu "Nice day today, huh?"

        m "Hmhm. Let's hope it stays that way."

        "My attention is redirected to Solephica. Furu follows my gaze and grins a bit."

        fu "Still focused on that old thing, eh?"

        "An ancient reminder of a war fought and lost long long ago. Gaping holes in the place of the eyes stare lifelessly to the sky, and the detached torso is scattered nearby. The legs are barely visible anymore… Rylo told me that they had used the metal to build the cities and towns nearby."

        "Because in the Metal Wastes, anything goes. Or so they say."

        m "Well of course, its a major tactical point and a landmark. It's also the last checkpoint we need before closing in toward the city."

        fu "I dunno, it kinda creeps me out sometimes. It's a lil hard to believe that these things were once… yknow, a l i v e."

        "Furu shakes his scales and stretches his wings. “Anywho, I dont like thinkin too much. That's your job. Which way today, Mel?"

        # [jump 1- North, moving to the east.]

        # [jump 2- south, moving to the west.]

        # With a flap of his wings and a silent communion, Furu takes off to start our daily patrol over the savannas. I watch my familiar disappear into the distance then turn around, immediately walking right into a bright and cheery blur of orange.

        #fern appears very close to the screen

        m "Wagghh!!" with hpunch

        f "Morning Melyssa!"


    