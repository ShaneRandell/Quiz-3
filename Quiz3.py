from gpiozero import LED, Button
from guizero import App, Text, TextBox, PushButton
from threading import Thread
from time import sleep

red = LED(22)
yellow = LED(27)
green = LED(17)
walk = LED(3)
button = Button(4, pull_up=True)


def update():
    while True:
        Text1.value = red.value
        Text2.value = yellow.value
        Text3.value = green.value
        Text4.value = walk.value


def button_reader_thread():
    while True:

        if button.is_pressed:

            print("button pressed")
            green.off()
            Text1.value = "Green light Off"
            sleep(.2)
            yellow.on()
            Text2.value = "Yellow light On"
            sleep(3)
            yellow.off()
            Text2.value = "Yellow light Off"
            red.on()
            Text3.value = "Red light On"
            walk.on()
            Text4.value = "Walk Now"
            sleep(5)
            red.off()
            Text3.value = "Red light Off"
            walk.off()
            Text4.value = "Don't Walk"

        else:

            green.on()
            Text1.value = "Greenlight On"
            Text2.value = "Yellow Light Off"
            Text3.value = "Red Light Off"
            Text4.value = "Don't Walk"
            sleep(1)


if __name__ == '__main__':

    app = App("Traffic Light ", height=600, width=400, layout="grid")

    Text1 = TextBox(app, width=100, grid=[1, 0], command=update)
    Text2 = TextBox(app, width=100, grid=[1, 1], command=update)
    Text3 = TextBox(app, width=100, grid=[1, 2], command=update)
    Text4 = TextBox(app, width=100, grid=[1, 3], command=update)

    thread = Thread(target=button_reader_thread)
    thread.start()
    app.display()
