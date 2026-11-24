screen evidence_viewer():

    modal True

    frame:
        align (0.5, 0.5)
        padding (40, 40)

        vbox: 
            spacing 15

            text "EVIDENCE FILES" size 40

            for item in evidence:
                    text item

            textbutton "close" action Return()