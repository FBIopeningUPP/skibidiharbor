label start:

    scene black

    "Skibidi, Harbor"
    "June 67, 2067"
    "67:67 AM."

    "Rain hits the hotel window"

    unknown "you are awake"

    jay "who are u dawg???"

    unknown "u killed dont u remember u dude"

    menu:
        "ask who tf are u"
            $ suspicion += 1
            jump question
        
        "remiain silent noword":
            $ sanity -= 10
            jump silent
    
label question:
    jay "what the hell u yapping about"

    unknown "u figure it out for sure"

    jump chapter_one

label silent:
    
    "you say nothing"

    unknown "still the same coward"

    jump chapter_one

label chapter_one:

    "chapter 1: room 404"

    return