#이 함수 안에 기능을 구현하시오
#기능구현 클래스를 따로 만들고 그 객체를 생성하여 실행하는 코드를 넣으면 ok
from car import car_member

class service:
    def __init__(self):
        self.dao = car_member.CarMemberDao()

    def join(self, app):
        self.dao.insert(car_member.CarMember(id=app.id_e.get(),
                                             pwd=app.pwd_e.get(),
                                             name=app.name_e.get(),
                                             tel=app.tel_e.get(),
                                             car_num=app.car_e.get()))
        mem = self.dao.select(app.id_e.get())
        mem.print_member()

    def login(self, app):
        mem = self.dao.select(app.id_e.get())
        if mem!= None:
            if mem.pwd == app.pwd_e.get():
                car_member.CarMember.log_id = mem.id


    def my_info(self, app):
        if car_member.CarMember.log_id !=None:
            mem = self.dao.select(car_member.CarMember.log_id)
            app.id_e.insert(0, mem.id)
            app.pwd_e.insert(0, mem.pwd)
            app.name_e.insert(0, mem.name)
            app.tel_e.insert(0, mem.tel)
            app.car_e.insert(0, mem.car_num)
        else:
            print("please login first")

    def update(self, app):
        pass

    def logout(self, app):
        car_member.CarMember.log_id = None
        app.title["text"] = "log in id:"

    def deleteId(self, app):
        if car_member.CarMember.log_id != None:
            self.dao.delete(car_member.CarMember.log_id)
            self.logout(app)
        else:
            print("please login first")