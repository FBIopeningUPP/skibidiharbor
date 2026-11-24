label chapter_01:

    scene black

    "SKIBIDI HARBOR"
    "June 67, 2067"
    "67:67 am"

    "sigma hotel - room 404"

    "blood hits the hotel window"

    "3d printer clicks"

    unknown "still working lawl"

    jay "who are u dawg"

    unknown "u burned me, dont u remember, dude?"

    menu:
        "ask whotf are u":
            $ suspicion += 1
            jump question

        "remain silent":
            $ sanity -= 10
            jump silent

label question:

    jay "what the hell u yapping about"

    unknown "u figure it out for sure"

    jump room_intro

label silent:

    "you say nothing"

    unknown "still the same coward"

    jump room_intro

label room_intro:

    "the light flickers"

    "for a moment, all black"

    "when light come back, stranger gone"

    "a body lies beside the bed"

    "you approach it"

    jay "what the actual flying fuck(i use arch btw)"

    "the dead man looks like u wtf"

    "suddenly, the phone rangs"    

label room_investigation:

    "what will u investiage??"

    menu:
        "examine the body":
            jump examine_body
        
        "check the telephone":
            jump check_phone

        "look through the window":
            jump check_window

        "view evidence":
            call screen evidence_viewer
            jump room_investigation
        
        "inspect hidden compartment" if body_examined and not cassette_found:
            jump hidden_compartment

        "play LOOP6767 cassette" if cassette_found and not cassette_played:
            jump play_cassette

        "play LOOP6767 cassette" if cassette_found and not cassette_played:
            jump play_cassette

        "leave the room":
            jump room_exit

label examine_body:

    if not body_examined:

        "you kneel beside the body"

        "its face is identical to yours"

        "a number has been carved in his rist"

        $ evidence.append("SUBJECT 67 ID")
        $ body_examined = True

        "evidence collected: SUBJECT 67 ID"

    else:

        "body already done"

    jump room_investigation

label check_phone:

    "you pick the telephone"

    unknown "room 404. u have sixty seconds"

    jay "sixty seconds until what"

    unknown "until they remeber u"

    "the call disconnects"

    jump room_investigation

label check_window:

    "you approach the window"

    "neon advertisement illuminte the streets"

    "a massive billboard displays your face"

    "WANTED: SUBJECT 67"

    jay "damn me cooked"

    jump room_investigation

label room_exit:

    if not cassette_played:
        "missing something important"
        jump room_investigation

    "you approach the door"

    "someone outside"

    unknown "jay, open the door pls"

    menu:
        "open the door":
            jump open_door
        
        "escape through the window":
            jump window_escape
        
        "hide inside the room":
            jump hide_room

label open_door:

    "you slowly open the door"

    "a woman in a black coat stands out"

    unknown "we need to talk"

    $ escape_route = "door"

    "you slowly open the door"

    unknown "we need to talk"

    jump chapter_one_end

label window_escape:

    $ escape_route = "window"

    "you force the window open"

    "cold rain hits your face"

    "four floors below, the city is waiting"

    jay "this better not be my last sigma moment"

    jump chapter_one_end

label hide_room:

    $ escape_route = "hide"

    "you switch off the lights"

    "footsteps approach"

    unknown "you cant hide from urself"

    jump chapter_one_end

label hidden_compartment:

    "you find a hidden comartpment beneath the bed"

    "inside is a cassate marked LOOP6767"

    $ cassette_found = True
    $ evidence.append("LOOP 67")

    jump room_investigation

label play_cassette:

    "you insert LOOP6767 into the cassette player"

    "static fills the room"

    unknown "test subject 67. memory reset successful"

    jay "what the fuck"

    "a familiar voice interrupts the recording"

    jay "if ur hearing this, dont trust the woman outside"

    "the cassette stops"

    $ cassette_played = True

    jump room_investigation

label chapter_one_end:

    if escape_route == "door":
        "the woman smiles"
        "she knows something about you"

    elif escape_route == "window":
        "you land on a fire escape"
        "a black car follows you"

    elif escape_route == "hide":
        "the door slowly opens"
    
    "CHAPTER 1 COMPLETE"

    return