from pynput import keyboard
import threading
import time

class KeyPresser:
    def __init__(self):
        self.pressing = False
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        self.thread_z = threading.Thread(target=self.press_z)
        self.thread_a = threading.Thread(target=self.press_a)
        self.thread_z.start()
        self.thread_a.start()

    def on_press(self, key):
        if key == keyboard.Key.space:
            self.pressing = not self.pressing

    def press_z(self):
        controller = keyboard.Controller()
        while True:
            if self.pressing:
                controller.press('z')
                time.sleep(0.1)
                controller.release('z')
            time.sleep(0.1)

    def press_a(self):
        controller = keyboard.Controller()
        while True:
            if self.pressing:
                controller.press('a')
                time.sleep(0.1)
                controller.release('a')
            time.sleep(10)  # Espera 10 segundos antes de pressionar 'a' novamente

if __name__ == "__main__":
    KeyPresser()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
