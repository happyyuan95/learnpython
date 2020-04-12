import tkinter as tk

window = tk.Tk()
window.title("学习画布canvas")
window.geometry("500x500")

canvas = tk.Canvas(window, bg="blue", height=400, width=500)
img_file = tk.PhotoImage(file="1.gif")
image = canvas.create_image(0, 0, anchor="nw", image=img_file)  #添加图片，anchor指定图片位置，图片只支持gif格式
line = canvas.create_line(50,50,70,70)  #直线x0 y0 x1 y1 为坐标
oval = canvas.create_oval(50,50,70,70, fill="red") #圆圈 fill为颜色
arc = canvas.create_arc(90,90,180,180, start=0, extent=180, fill="green") #扇形,start为起始角度，extend为结束角度
rect = canvas.create_rectangle(200,200,300,300, fill="black") #方形
canvas.pack()

def moveitdown():
    canvas.move(rect, 0, 2)  #rect选定元素，0为控制x坐标不动，2控制y坐标每次按下则+2

btn = tk.Button(window, text="move", command=moveitdown)
btn.pack()
window.mainloop()