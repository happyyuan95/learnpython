import tkinter as tk

window = tk.Tk()
window.title("学习checkbtn")
window.geometry("300x300")

label = tk.Label(window, bg="yellow", height=2, width=20, text="empty")
label.pack()
def print_selection():
    if (var1.get()==0) &(var2.get()==0):
        label.config(text="i don't like them")
    elif (var1.get()==0) & (var2.get()==1):
        label.config(text="i like zhoushen")
    elif (var1.get()==1) & (var2.get()==0):
        label.config(text="i like lijian")
    else:
        label.config(text="i like lijian and zhoushen")

var1 = tk.IntVar()
var2 = tk.IntVar()
#选中时var1赋值为onvalue，不选中赋值为offvalue
checkbtn1 = tk.Checkbutton(window, text="lijian", variable=var1, onvalue=1, offvalue=0,
                           command=print_selection)
checkbtn2 = tk.Checkbutton(window, text="zhoushen", variable=var2, onvalue=1, offvalue=0,
                           command=print_selection)
checkbtn1.pack()
checkbtn2.pack()

window.mainloop()