label chapter_02:

    scene black

    "CHAPTER 2: NEON FUNERAL"

    "Skibidi Harbor - 67:67 AM"

    if escape_route == "door":

        "the woman grabs your wrist"

        unknown "you werent supposed to open that door"

        jay "then why tf u knocked"
    
    elif escape_route == "window":

        "you stumble into a dark alley"

        "a black car stops behind you"

        jay "nah bro they got the sigma mobile"
    
    elif escape_route == "hide":

        "someone pulls you out from under the bed"

        unknown "found you, subject 67"

        jay "bro camping is crazy"
    
    jump chapter_02_intro

label chapter_02_intro:

    "a phone starts vibrating"

    "UNKNOWN NUMBER:"

    jay "who keeps texting me dawg"

    "a second message arrives"

    "FIND YUNA. BEFORE SHE FINDS YOU."

    jump meet_yuna

label meet_yuna:

    "a woman approaches from the shows"

    yuna "jay finnaly"

    jay "whotf are u"

    yuna "your girlfriends, dumbass"

    jay "i dont even remember having one single af"

    yuna "thats because they erased ur ssd"

    menu: 
        "trust yuna(girls named yana holly hell)":
            $ yuna_trust += 1
            jump yuna_trusted

        "question yuna":
            $ yuna_trust -= 1
            jump yuna_questioned

label yuna_trusted

    yuna "good we dont have much time"

    "she hands you a photograph"

    "if shows you andd yuna standing outside sigma hotel"

    jump yuna_scene_end

label yuna_questioned:

    jay "prove you're my girlfriends"

    yuna "you always say that."

    "she shows you a photograph"

    "it shows you and yuna standing outside sigma hotel"