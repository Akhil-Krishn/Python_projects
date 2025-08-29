import tkinter as tk
from tkVideoPlayer import TkinterVideo


root = tk.Tk()
root.geometry('600x600')

videoplayer = TkinterVideo(master=root, scaled=True)
videoplayer.load("focus_logo.mp4")
videoplayer.pack(expand=True, fill="both")

videoplayer.play() # play the video
root.after(3000, lambda: root.destroy())

root.mainloop()