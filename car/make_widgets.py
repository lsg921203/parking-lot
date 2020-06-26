import tkinter as tk
import cv2
from functools import partial
from car import car_member
from car import service

serv = service.service()

def remove_ent(app):
    app.id_e.delete(0, 'end')
    app.pwd_e.delete(0, 'end')
    app.name_e.delete(0, 'end')
    app.tel_e.delete(0, 'end')
    app.car_e.delete(0, 'end')



def btn1_clicked(app, event):
    if car_member.CarMember.log_id == None:
        serv.join(app)
    remove_ent(app)


def btn2_clicked(app, event):
    if car_member.CarMember.log_id == None:
        serv.login(app)
        if car_member.CarMember.log_id == None:
            print("아이디 혹은 비밀번호가 틀렸습니다.")
        else:
            app.title["text"] = "log in id: " + car_member.CarMember.log_id
    else:
        print("이미 로그인")
        return




    remove_ent(app)


def btn3_clicked(app, event):
    remove_ent(app)
    serv.my_info(app)

def btn4_clicked(app, event):
    print(event)
    img = cv2.imread('img/b.jpg')
    app.change_img(img)

def btn5_clicked(app, event):
    serv.logout(app)


def btn6_clicked(app, event):
    remove_ent()
    serv.deleteId(app)


def btn7_clicked(app, event):
    remove_ent(app)

def make(app, service=None):
    app.title = tk.Label(app.sub_fr, text='회원정보', font=60)
    app.id_t = tk.Label(app.sub_fr, text='id:', font=60)
    app.id_e = tk.Entry(app.sub_fr, width=60)
    app.pwd_t = tk.Label(app.sub_fr, text='pwd:', font=60)
    app.pwd_e = tk.Entry(app.sub_fr, width=60)
    app.name_t = tk.Label(app.sub_fr, text='name:', font=60)
    app.name_e = tk.Entry(app.sub_fr, width=60)
    app.tel_t = tk.Label(app.sub_fr, text='tel:', font=60)
    app.tel_e = tk.Entry(app.sub_fr, width=60)
    app.car_t = tk.Label(app.sub_fr, text='car number:', font=60)
    app.car_e = tk.Entry(app.sub_fr, width=60)

    app.title = tk.Label(app.sub_fr, text='log in id: ', font=60)

    app.btn1 = tk.Button(app.sub_fr, width=10, font=60, text='join')
    app.btn2 = tk.Button(app.sub_fr, width=10, font=60, text='login')
    app.btn3 = tk.Button(app.sub_fr, width=10, font=60, text='내정보')
    app.btn4 = tk.Button(app.sub_fr, width=10, font=60, text='수정')
    app.btn5 = tk.Button(app.sub_fr, width=10, font=60, text='logout')
    app.btn6 = tk.Button(app.sub_fr, width=10, font=60, text='탈퇴')
    app.btn7 = tk.Button(app.sub_fr, width=10, font=60, text='clear')

    app.title.grid(row=0, column=0, columnspan=3)
    app.id_t.grid(row=1, column=0)
    app.id_e.grid(row=1, column=1, columnspan=2)
    app.pwd_t.grid(row=2, column=0)
    app.pwd_e.grid(row=2, column=1, columnspan=2)
    app.name_t.grid(row=3, column=0)
    app.name_e.grid(row=3, column=1, columnspan=2)
    app.tel_t.grid(row=4, column=0)
    app.tel_e.grid(row=4, column=1, columnspan=2)
    app.car_t.grid(row=5, column=0)
    app.car_e.grid(row=5, column=1, columnspan=2)


    app.btn1.grid(row=6, column=0)
    app.btn2.grid(row=6, column=1)
    app.btn3.grid(row=6, column=2)
    app.btn4.grid(row=7, column=0)
    app.btn5.grid(row=7, column=1)
    app.btn6.grid(row=7, column=2)
    app.title.grid(row=8, column=0)
    app.btn7.grid(row=8, column=2)
    #app.btn1['command'] = btn1_clicked
    #app.btn2['command'] = btn2_clicked
    #app.btn3['command'] = btn3_clicked
    #app.btn4['command'] = btn4_clicked
    #app.btn5['command'] = btn5_clicked
    #app.btn6['command'] = btn6_clicked

    app.btn1.bind('<Button-1>',partial(btn1_clicked, app))
    app.btn2.bind('<Button-1>', partial(btn2_clicked, app))
    app.btn3.bind('<Button-1>', partial(btn3_clicked, app))
    app.btn4.bind('<Button-1>', partial(btn4_clicked, app))
    app.btn5.bind('<Button-1>', partial(btn5_clicked, app))
    app.btn6.bind('<Button-1>', partial(btn6_clicked, app))
    app.btn7.bind('<Button-1>', partial(btn7_clicked, app))
    '''
    #app.btn1['command'] = btn1_clicked
    app.btn1.bind('<Button-1>', partial(btn1_clicked, app))
    app.btn2['command'] = btn2_clicked
    app.btn3['command'] = btn3_clicked
    '''