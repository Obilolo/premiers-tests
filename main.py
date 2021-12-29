def on_sound_loud():
    basic.pause(200)
    pins.servo_write_pin(AnalogPin.P1, 0)
    pins.servo_write_pin(AnalogPin.P2, 0)
    basic.pause(1000)
    pins.servo_write_pin(AnalogPin.P1, 90)
    pins.servo_write_pin(AnalogPin.P2, 90)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_button_pressed_a():
    basic.pause(500)
    pins.servo_write_pin(AnalogPin.P1, 180)
    pins.servo_write_pin(AnalogPin.P2, 0)
    basic.pause(2000)
    pins.servo_write_pin(AnalogPin.P1, 90)
    pins.servo_write_pin(AnalogPin.P2, 90)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    pins.servo_write_pin(AnalogPin.P1, 90)
    pins.servo_write_pin(AnalogPin.P2, 90)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.pause(500)
    pins.servo_write_pin(AnalogPin.P1, 0)
    pins.servo_write_pin(AnalogPin.P2, 180)
    basic.pause(2000)
    pins.servo_write_pin(AnalogPin.P1, 90)
    pins.servo_write_pin(AnalogPin.P2, 90)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    basic.pause(500)
    pins.servo_write_pin(AnalogPin.P1, 180)
    pins.servo_write_pin(AnalogPin.P2, 180)
    basic.pause(1000)
    pins.servo_write_pin(AnalogPin.P1, 90)
    pins.servo_write_pin(AnalogPin.P2, 90)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

input.set_sound_threshold(SoundThreshold.LOUD, 230)
pins.servo_write_pin(AnalogPin.P1, 90)
pins.servo_write_pin(AnalogPin.P2, 90)