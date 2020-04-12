import tkinter as tk

window = tk.Tk()
window.title("learn scale - 拖动条")
window.geometry("300x300")

#width和height指定的为字符高度
lable = tk.Label(window, bg="yellow", width=20, height=2, text="0")
lable.pack()

def print_selection(v):
    lable.config(text="you selected %s" % v)

#lable指定名称，from_和to_指定范围，orient指定方向，length指定长度单位为像素，
#showvalue显示数值，tickinterval单位长度，resolution保留小数
scale = tk.Scale(window, label="try me", from_=5, to_=10, orient=tk.HORIZONTAL,
                 length=200, showvalue=0, tickinterval=1, resolution=0.01, command=print_selection)
scale.pack()

window.mainloop()