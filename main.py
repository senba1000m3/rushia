def on_pin_pressed_p0():
    basic.show_number(randint(0, 10))
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    while True:
        basic.show_icon(IconNames.HEART)
        led.stop_animation()
        basic.pause(1000)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    while True:
        basic.show_icon(IconNames.SMALL_HEART)
        led.stop_animation()
        basic.pause(1000)
input.on_button_pressed(Button.B, on_button_pressed_b)
