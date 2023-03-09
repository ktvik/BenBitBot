input.onButtonPressed(Button.A, function on_button_pressed_a() {
    if (kjør) {
        GrønnTilRød()
    } else {
        RødTilGrønn()
    }
    
    radio.sendNumber(kjør)
})
function GrønnTilRød() {
    
    pins.analogWritePin(AnalogPin.P0, 0)
    pins.analogWritePin(AnalogPin.P1, 1023)
    pins.analogWritePin(AnalogPin.P2, 0)
    basic.pause(1000)
    pins.analogWritePin(AnalogPin.P0, 1023)
    pins.analogWritePin(AnalogPin.P1, 0)
    pins.analogWritePin(AnalogPin.P2, 0)
    kjør = 0
}

function RødTilGrønn() {
    
    pins.analogWritePin(AnalogPin.P0, 1023)
    pins.analogWritePin(AnalogPin.P1, 1023)
    pins.analogWritePin(AnalogPin.P2, 0)
    basic.pause(1000)
    pins.analogWritePin(AnalogPin.P0, 0)
    pins.analogWritePin(AnalogPin.P1, 0)
    pins.analogWritePin(AnalogPin.P2, 1023)
    kjør = 1
}

let kjør = 0
pins.analogWritePin(AnalogPin.P0, 1023)
basic.forever(function on_forever() {
    
})
