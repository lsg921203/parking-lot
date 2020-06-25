import tkinter as tk
import car.main_ui as win
import car.make_widgets as mkw
import car.car_member as car
def main():
    img_path = 'img/c2.jpg'
    root = tk.Tk()
    app = win.AppWindow(root, '800x600+100+100', img_path)
    dao = car.CarMemberDao()
    mkw.make(app, dao)
    app.mainloop()

main()