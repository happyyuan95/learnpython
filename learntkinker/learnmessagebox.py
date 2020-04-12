import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title("学习frame框架")
window.geometry("300x300")

def clickit():
    #tk.messagebox.showinfo(title="hi", message="xixiixi")
    #tk.messagebox.showwarning(title="hi", message="warningwarning")
    #tk.messagebox.showerror(title="hi", message="error")
    #print(tk.messagebox.askquestion(title="hi", message="ask you"))  #return yes or no
    #print(tk.messagebox.askyesnocancel(title="hi", message="ask you"))  # return true false none
    #print(tk.messagebox.askyesno(title="hi", message="ask you"))  # return true false
    print(tk.messagebox.askretrycancel(title="hi", message="ask you")) #return true false 重试
btn = tk.Button(window, text="click", command=clickit)

btn.pack()
window.mainloop()