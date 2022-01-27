def on_received_number(receivedNumber):
    global KartoffelnHaben
    KartoffelnHaben = 1
    if receivedNumber == 0:
        basic.show_leds("""
            . # # # .
                        # # # # #
                        # # # # #
                        # # # # #
                        . # # # .
        """)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global VFunkgruppe, KartoffelnHaben
    basic.clear_screen()
    while VFunkgruppe == OFunkgruppe:
        VFunkgruppe = randint(1, 5)
    if VFunkgruppe != OFunkgruppe and KartoffelnHaben == 1:
        radio.set_group(VFunkgruppe)
        radio.send_number(0)
    radio.set_group(OFunkgruppe)
    KartoffelnHaben = 0
    VFunkgruppe = randint(1, 5)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(OFunkgruppe)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

KartoffelnHaben = 0
VFunkgruppe = 0
OFunkgruppe = 0
# Original Funkgruppe, jeder Spieler bekommt ihre eigene Funkgruppe für sich
OFunkgruppe = 1
# Der Micro:Bit Funkgruppe wird gesetzt auf Original Funkgruppe
radio.set_group(OFunkgruppe)
VFunkgruppe = randint(1, 5)
KartoffelnHaben = 1
basic.show_leds("""
    . # # # .
        # # # # #
        # # # # #
        # # # # #
        . # # # .
""")