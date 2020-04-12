import tkinter as tk

window = tk.Tk()
window.title("学习menubar")
window.geometry("300x300")

label = tk.Label(window, bg="yellow", height=2, width=20, text="empty")
label.pack()

menubar = tk.Menu(window)  #在窗口上创建个菜单栏
count = 0
def do_job():
    global count
    label.config(text="do - %s" % str(count))
    count+=1

#tearoff是否可以分开
filemenu = tk.Menu(menubar, tearoff=0)
#在menubar上添加filemenu
menubar.add_cascade(label="file", menu=filemenu)  #在menu上添加子菜单
filemenu.add_command(label="new", command=do_job) #在子菜单下添加选项
filemenu.add_command(label="open", command=do_job)
filemenu.add_command(label="close", command=do_job)
filemenu.add_separator()  #添加分割线
filemenu.add_command(label="exit", command=window.quit)

editmenu = tk.Menu(menubar, tearoff=0)
#在menubar上添加filemenu
menubar.add_cascade(label="edit", menu=editmenu)
editmenu.add_command(label="copy", command=do_job)
editmenu.add_command(label="paste", command=do_job)
editmenu.add_command(label="cut", command=do_job)


submenu = tk.Menu(filemenu, tearoff=0)
filemenu.add_cascade(label="import", menu=submenu)
submenu.add_command(label="sub1", command=do_job)

window.config(menu=menubar)  #设置menu，将menu添加到窗口上

window.mainloop()