import cx_Oracle

class CarMember:
    def __init__(self, id = None, pwd=None, name = None, tel = None, car_num=None):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.tel = tel
        self.car_num = car_num

    def print_member(self):
        print(self.id, '/', self.pwd, '/', self.name, '/', self.tel, '/', self.car_num)

class CarMemberDao:

    def select(self, id):
        conn = cx_Oracle.connect("hr", "hr", "localhost:1521/xe", encoding='utf-8')

        cursor = conn.cursor()

        sql = "select * from car_member where id=:1"

        d= (id, )

        cursor.excute(sql,d)

        mem = cursor.fetchone()

        conn.close()

        if mem is not None:
            return CarMember(mem[0],mem[1],mem[2],mem[3],mem[4])


    def insert(self, mem):
        conn = cx_Oracle.connect("hr", "hr", "localhost:1521/xe", encoding='utf-8')

        cursor = conn.cursor()

        sql = 'insert into test values(seq_test.nextval, :1, :2, :3, :4, :5)'

        d = (mem.id, mem.pwd, mem.name, mem.car_num, mem.tel)

        cursor.execute(sql, d)

        conn.commit()  # 자바와 달리 자동 커밋이 안되므로 쓰기동작 후 커밋 필수

        conn.close()

    def update(self, mem):
        conn = cx_Oracle.connect("hr", "hr", "localhost:1521/xe", encoding='utf-8')

        cursor = conn.cursor()

        sql = 'update test set car_num=:1, phonenum=:2 where id=:3'

        d = (mem.car_num, mem.tel, mem.id)

        cursor.execute(sql, d)

        conn.commit()

        conn.close()

    def delete(self, id):
        conn = cx_Oracle.connect("hr", "hr", "localhost:1521/xe", encoding='utf-8')

        cursor = conn.cursor()

        sql = 'delete from car_member where id=:1'

        d = (id,)

        cursor.execute(sql, d)

        conn.commit()

        conn.close()