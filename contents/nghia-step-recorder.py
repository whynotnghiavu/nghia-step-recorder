import os
# pip install pyautogui
import tkinter as tk
import datetime
# pip install pyautogui
import pyautogui
# pip install pynput
from pynput.keyboard import Key, Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener


class RecorderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Recorder")

        self.record_button = tk.Button(self.master, text="RECORD", command=self.start_recording)
        self.record_button.pack(pady=20)

        self.stop_button = tk.Button(self.master, text="STOP", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack(pady=20)

        self.is_recording = False

        # Lắng nghe sự kiện từ bàn phím
        self.keyboard_listener = KeyboardListener(on_press=self.on_press)

        # Lắng nghe sự kiện từ chuột
        self.mouse_listener = MouseListener(on_click=self.on_click)

    def start_recording(self):
        self.is_recording = True
        self.record_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        # Bắt đầu lắng nghe từ bàn phím và chuột
        self.keyboard_listener.start()
        self.mouse_listener.start()

    def stop_recording(self):
        self.is_recording = False
        self.record_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

        # Dừng lắng nghe từ bàn phím và chuột
        self.keyboard_listener.stop()
        self.mouse_listener.stop()

        exit()

    def on_press(self, key):
        if self.is_recording:
            print(f"🚀 {key}")
            self.capture_screen()

            if key == Key.esc:
                self.stop_recording()
                return False

    def on_click(self, x, y, button, pressed):
        if self.is_recording:
            if pressed:
                print(f"🖱️ Click at ({x}, {y}) with {button}")
                self.capture_screen()

    def capture_screen(self):
        # Chụp màn hình và lưu lại
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S%f")
        screenshot = pyautogui.screenshot()

        filename = f"{timestamp}.png"
        filename = os.path.join(folder_output, filename)
        screenshot.save(filename)
        print(f"Đã chụp màn hình và lưu thành công vào '{filename}'")


if __name__ == "__main__":

    Downloads = os.path.expanduser("~/Downloads")

    folder_output = os.path.join(Downloads, "NghiaStepRecorder")
    if not os.path.exists(folder_output):
        os.mkdir(folder_output)

    _Delete = os.path.join(folder_output, "_Delete")
    if not os.path.exists(_Delete):
        os.mkdir(_Delete)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S%f")
    folder_output = os.path.join(folder_output, f"{timestamp}")
    if not os.path.exists(folder_output):
        os.mkdir(folder_output)

    root = tk.Tk()
    app = RecorderApp(root)
    root.mainloop()
