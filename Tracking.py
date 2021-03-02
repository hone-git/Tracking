from PIL import ImageGrab
import time
import os
from os.path import expanduser
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog

def capture(event):
    span = int(entry_span.get())
    split = int(entry_split.get())
    lap_imagine = span/split
    global captures
    captures = []

    for i in range(split):
        start = time.time()
        captures.append(ImageGrab.grab())
        lap_real = time.time() - start
        if lap_imagine > lap_real:
            time.sleep(lap_imagine - lap_real)
        else:
            print("split:{} is too many\n1cycle:{}sec".format(split, lap_real))


def save(event):
    iDir = os.path.abspath(os.path.dirname(__file__))
    iDirPath = tkinter.filedialog.askdirectory(initialdir=iDir)
    dir = iDirPath + "/{}".format(entry_dir.get())
    try:
        os.chdir(dir)
    except FileNotFoundError:
        os.mkdir(dir)
        os.chdir(dir)
    for i, c in enumerate(captures):
        c.save("scene{}.png".format(i))


if __name__ == '__main__':
    caputures = []

    root = tk.Tk()
    root.title("Caputo")
    root.geometry("200x322")

    button_cap = tk.Button(root, text="Capture Scene")
    button_cap.pack(fill=tk.BOTH, expand=1)
    button_cap.bind('<1>', capture)

    entry_span = tk.Entry(root)
    entry_span.pack(fill=tk.BOTH, expand=1)
    entry_span.insert(0, "Capturing Second")

    entry_split = tk.Entry(root)
    entry_split.pack(fill=tk.BOTH, expand=1)
    entry_split.insert(0, "Capturing Leaves")

    button_save = tk.Button(root, text="Save Captures")
    button_save.pack(fill=tk.BOTH, expand=1)
    button_save.bind('<1>', save)

    entry_dir = tk.Entry(root)
    entry_dir.pack(fill=tk.BOTH, expand=1)
    entry_dir.insert(0, "Saving Folder Name")

    root.mainloop()
