radio.onReceivedNumber(function (receivedNumber) {
    KartoffelnHaben = 1
    basic.showLeds(`
        . # # # .
        # # # # #
        # # # # #
        # # # # #
        . # # # .
        `)
})
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    while (VFunkgruppe == OFunkgruppe) {
        VFunkgruppe = randint(1, 4)
    }
    if (VFunkgruppe != OFunkgruppe && KartoffelnHaben == 1) {
        radio.setGroup(VFunkgruppe)
        radio.sendNumber(0)
        KartoffelnHaben = 0
    }
    radio.setGroup(OFunkgruppe)
    VFunkgruppe = OFunkgruppe
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(OFunkgruppe)
    basic.clearScreen()
})
let KartoffelnHaben = 0
let VFunkgruppe = 0
let OFunkgruppe = 0
// Original Funkgruppe, jeder Spieler bekommt ihre eigene Funkgruppe für sich
OFunkgruppe = 4
// Der Micro:Bit Funkgruppe wird gesetzt auf Original Funkgruppe
radio.setGroup(OFunkgruppe)
VFunkgruppe = randint(1, 4)
KartoffelnHaben = 0
