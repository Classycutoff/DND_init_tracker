#!/usr/bin/python

import tkinter as tk

window = tk.Tk()

window.title('DND Initiative tracker')
window.configure(width=500, height=300)
window.configure(bg='lightgray')


# This positions the window to the middle of the screen
winWidth = window.winfo_reqwidth()
winwHeight = window.winfo_reqheight()
posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
window.geometry("+{}+{}".format(posRight, posDown))

## Start your code here





window.mainloop()