def on_button_pressed_a():
    if kjør:
        GrønnTilRød()
    else:
        RødTilGrønn()
    radio.send_number(kjør)
input.on_button_pressed(Button.A, on_button_pressed_a)

def GrønnTilRød():
    global kjør
    pins.analog_write_pin(AnalogPin.P0, 0)
    pins.analog_write_pin(AnalogPin.P1, 1023)
    pins.analog_write_pin(AnalogPin.P2, 0)
    basic.pause(1000)
    pins.analog_write_pin(AnalogPin.P0, 1023)
    pins.analog_write_pin(AnalogPin.P1, 0)
    pins.analog_write_pin(AnalogPin.P2, 0)
    kjør = 0
def RødTilGrønn():
    global kjør
    pins.analog_write_pin(AnalogPin.P0, 1023)
    pins.analog_write_pin(AnalogPin.P1, 1023)
    pins.analog_write_pin(AnalogPin.P2, 0)
    basic.pause(1000)
    pins.analog_write_pin(AnalogPin.P0, 0)
    pins.analog_write_pin(AnalogPin.P1, 0)
    pins.analog_write_pin(AnalogPin.P2, 1023)
    kjør = 1
kjør = 0
pins.analog_write_pin(AnalogPin.P0, 1023)

def on_forever():
    pass
basic.forever(on_forever)
