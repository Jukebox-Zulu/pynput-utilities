from pynput.mouse import Button, Controller as MController
from pynput.keyboard import Key, Controller as KBController
from time import sleep

Keyboard = KBController()
Mouse = MController()

keys = {
    'space': Key.space,
    'enter': Key.enter,
    'ret': Key.enter,
    'shift': Key.shift,
    'ctrl': Key.ctrl,
    'alt': Key.alt,
    'tab': Key.tab,
    'pause': Key.pause,
    'insert': Key.insert,
    'pagedown': Key.page_down,
    'pageup': Key.page_up,
    'end': Key.end,
    'home': Key.home,
    'down': Key.down,
    'up': Key.up,
    'left': Key.left,
    'right': Key.right,
    'f1': Key.f1,
    'f2': Key.f2,
    'f3': Key.f3,
    'f4': Key.f4,
    'f5': Key.f5,
    'f6': Key.f6,
    'f7': Key.f7,
    'f8': Key.f8,
    'f9': Key.f9,
    'f10': Key.f10,
    'f11': Key.f11,
    'f12': Key.f12
}

buttons = {
    'left': Button.left,
    'right': Button.right,
    'middle': Button.middle
}


def key(string, loops=1, enter=False, interval=0.1):
    for i in range(loops):
        if isinstance(string, list):
            for item in string:
                if isinstance(item, tuple):
                    key(item[0], loops=item[1], enter=enter, interval=interval)
                else:
                    key(item, enter=enter, interval=interval)
        else:
            key_obj = keys.get(string)
            if key_obj:
                Keyboard.press(key_obj)
                Keyboard.release(key_obj)
            elif len(string) == 1 and string.islower():
                Keyboard.press(string)
            else:
                Keyboard.type(string)
            if enter:
                Keyboard.press(Key.enter)
        sleep(interval)


class held(object):
    def __init__(self, button):
        self.button = keys.get(button)

    def __enter__(self):
        Keyboard.press(self.button)

    def __exit__(self, *args):
        Keyboard.release(self.button)


def click(x=Mouse.position[0], y=Mouse.position[1], clicks=1, interval=0.1, button='left'):
    button = buttons.get(button)
    Mouse.position = (x, y)
    for i in range(clicks):
        Mouse.click(button)
        sleep(interval)


def drag(start=Mouse.position, end=Mouse.position, duration=0.1, button='left'):
    button = buttons.get(button)
    Mouse.position = start
    Mouse.press(button)
    sleep(duration/2)
    Mouse.position = end
    sleep(duration/2)
    Mouse.release(button)


def mouse_move(x, y):
    Mouse.position = (x, y)
