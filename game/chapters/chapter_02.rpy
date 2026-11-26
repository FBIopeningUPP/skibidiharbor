
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

    "STOP TRUSTING YOUR MEMORIES."

    jay "who keeps texting me dawg"

    "a second message arrives"

    "FIND YUNA. BEFORE SHE FINDS YOU."

    jump meet_yuna


label meet_yuna:

    "a woman approaches from the shadows"

    yuna "jay finnaly"

    jay "whotf are u"

    yuna "your girlfriend, dumbass"

    jay "i dont even remember having one single af"

    yuna "thats because they erased ur ssd"

    menu:

        "trust yuna (girls named yuna holy hell)":

            $ yuna_trust += 1

            jump yuna_trusted

        "question yuna":

            $ yuna_trust -= 1

            jump yuna_questioned


label yuna_trusted:

    yuna "good we dont have much time"

    "she hands you a photograph"

    "it shows you and yuna standing outside sigma hotel"

    jump yuna_scene_end


label yuna_questioned:

    jay "prove you're my girlfriend"

    yuna "you always say that"

    "she shows you a photograph"

    "it shows you and yuna standing outside sigma hotel"

    jump yuna_scene_end


label yuna_scene_end:

    "the photograph is dated june 67, 2067"

    "on the back, someone has written"

    "SHE IS NOT YUNA FAAK"

    jay "nah this lore is getting crazy"

    jump yuna_secret


label yuna_secret:

    "yuna looks around nervously"

    if yuna_trust > 0:

        yuna "jay i need to tell u something"

        jay "what now dawg"

        yuna "we've met 67 times before"

        yuna "and every single time you die"

        jay "so im basically playing hardcore minecraft"

    else:

        yuna "we need to leave right now"

        jay "why are u avoiding my questions"

        yuna "because some answers get people killed"

        jay "bro thinks shes in a netflix original"

    "suddenly a black car stops nearby"

    "three armed agents step outside"

    unknown "SUBJECT 67 DO NOT MOVE"

    jump agent_encounter


label agent_encounter:

    menu:

        "run with yuna":

            jump escape_agents

        "surrender to agents":

            jump surrender_agents


label escape_agents:

    $ agent_choice = "escape"
    $ agent_reputation -= 1

    "yuna grabs your hand"

    "you both run into the neon lit streets"

    jay "bro why is everyone after me"

    "behind you, the agents begin chasing"

    unknown "DO NOT LET SUBJECT 67 ESCAPE"

    yuna "keep running"

    "you disappear into an underground subway entrance"

    jump chapter_02_end


label surrender_agents:

    $ agent_choice = "surrender"
    $ agent_reputation += 1

    "you raise your hands"

    jay "alright alright chill"

    "one of the agents approaches"

    unknown "welcome back subject 67"

    jay "back? bro i dont even know u"

    "the agent injects something into your neck"

    "your vision begins fading"

    "everything goes black"

    jump chapter_02_end


label chapter_02_end:

    scene black

    "END OF CHAPTER 2"

    "TO BE CONTINUED..."

    jump chapter_03