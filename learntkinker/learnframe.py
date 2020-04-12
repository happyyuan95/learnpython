import tkinter as tk

window = tk.Tk()
window.title("学习frame框架")
window.geometry("300x300")

#在主window上
label = tk.Label(window, bg="yellow", height=2, width=20, text="on the window")
label.pack()

#添加主frame
frame = tk.Frame(window)
frame.pack()

#添加左右两个frame
frame_left = tk.Frame(frame)
frame_right = tk.Frame(frame)
frame_left.pack(side="left")  #side指定左右位置
frame_right.pack(side="right")

#在左右两个frame上添加label
tk.Label(frame_left, text="on the left1").pack()
tk.Label(frame_left, text="on the left2").pack()

tk.Label(frame_right, text="on the right1").pack()
tk.Label(frame_right, text="on the right2").pack()

window.mainloop()