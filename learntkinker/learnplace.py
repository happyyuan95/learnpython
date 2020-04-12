import tkinter as tk

window = tk.Tk()
window.title("学习放置位置pack grid place")
window.geometry("300x300")

#使用pack中side参数控制方位
# tk.Label(window, text="top").pack(side='top')
# tk.Label(window, text="bottom").pack(side='bottom')
# tk.Label(window, text="right").pack(side='right')
# tk.Label(window, text="left").pack(side='left')

#grid以方格的形式放置
#row column 指定行和列 padx和pady指定每格的面积
# for i in range(4):
#     for j in range(3):
#         tk.Label(window, text=j).grid(row=i, column=j, padx=10, pady=10)

#指定放置在哪个位置哪个点上,anchor用法和convas中的相同
tk.Label(window, text="top").place(x=10, y=20, anchor="nw")
window.mainloop()