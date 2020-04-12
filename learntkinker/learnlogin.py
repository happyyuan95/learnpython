import tkinter as tk
import pickle
import tkinter.messagebox

window = tk.Tk()
window.title("欢迎登录")
window.geometry("520x520")

#放置图片，使用画布
canvas = tk.Canvas(window, height=400, width=800)
image_file = tk.PhotoImage(file="2.gif")
image = canvas.create_image(50,0,anchor="nw", image=image_file)
canvas.pack(side="top")

#添加label
tk.Label(window, text="username:").place(x=60, y=380)
tk.Label(window, text="password:").place(x=60, y=420)

#添加输入框entry
var_usrname = tk.StringVar()
var_usrname.set("hahha@qq.com")  #设置默认值
var_pwd = tk.StringVar()
entry_usrname = tk.Entry(window, textvariable=var_usrname)
entry_psw = tk.Entry(window, textvariable=var_pwd, show="*")
entry_usrname.place(x=140, y=380)
entry_psw.place(x=140, y=420)

#添加处理函数
def usr_login():
    #获取输入值
    usrname = var_usrname.get()
    pwd = var_pwd.get()
    try:
        with open("usrinfo.txt", "rb") as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open("usrinfo.txt", "ab") as usr_file:
            usrs_info = {"admin":"admin"}
            pickle.dump(usrs_info, usr_file)

    #判断信息
    if usrname in usrs_info:
        if pwd == usrs_info[usrname]:
            tk.messagebox.showinfo("welcome", "how are you, %s ?" % usrname)
        else:
            tk.messagebox.showwarning("error", "password wrong,try again")
    else:
        is_sign_up = tk.messagebox.askyesno("welcome", "do you want to sign up today?")
        if is_sign_up:
            usr_signup()


def usr_signup():
    #创建一个window
    window_signup = tk.Toplevel(window)
    window_signup.geometry("300x300")
    window_signup.title("sign up")

    tk.Label(window_signup, text="usrname:").place(x=10,y=10)
    tk.Label(window_signup, text="password:").place(x=10, y=50)
    tk.Label(window_signup, text="confirm:").place(x=10, y=90)
    # 添加输入框entry
    var_usrname = tk.StringVar()
    var_usrname.set(" ")  # 设置默认值
    var_pwd = tk.StringVar()
    var_confirmpwd = tk.StringVar()
    entry_usrname = tk.Entry(window_signup, textvariable=var_usrname)
    entry_psw = tk.Entry(window_signup, textvariable=var_pwd, show="*")
    confirm_psw = tk.Entry(window_signup, textvariable=var_confirmpwd, show="*")
    entry_usrname.place(x=80, y=10)
    entry_psw.place(x=80, y=50)
    confirm_psw.place(x=80, y=90)

    def signto():
        name = entry_usrname.get()
        pwd = entry_psw.get()
        confirm = confirm_psw.get()

        with open("usrinfo.txt", "rb") as usr_file:
            usrs_info = pickle.load(usr_file)
        if pwd != confirm:
            tk.messagebox.showwarning("warning", "password and confirm pwd is not equal")
        elif name in usrs_info:
            tk.messagebox.showwarning("warnning", "the usr has already signed up")
        else:
            usrs_info[name] = pwd
            with open("usrinfo.txt", "ab") as usr_file:
                pickle.dump(usrs_info, usr_file)
            tk.messagebox.showinfo("welcom", "you have signed up successful")
            window_signup.destroy()

    btn_confirmsignup = tk.Button(window_signup, text="signup", command=signto)
    btn_confirmsignup.place(x=100, y=120)


#添加btn
btn_login = tk.Button(window, text="login", command=usr_login)
btn_login.place(x=80, y=450)
btn_signup = tk.Button(window, text="signup", command=usr_signup)
btn_signup.place(x=170, y=450)

window.mainloop()