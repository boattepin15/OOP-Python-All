from abc import ABC, abstractmethod

#UserActions เอาไว้กำหนด ระบบที่จะสามารถใช้ได้ login, logout
#Person กำหนดตัวลักษณะของผู้ใช้งาน
#User ไว้ทำระบบหลักที่ดึงความสามารถของ Class UserActions, Person  สร้างเป็นระบบสมัครสมาชิก
#Amind ทำหน้าที่ดูแลผู้ใช้งานทั่วไป

class UserActions(ABC):
    """ คลาส Abs สำหรับ การทำงานกับผู้ใช้งาน """
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def logout(self):
        pass


class Person:
    def __init__(self, name, email):
        """ กำหนด Attb พื้นฐานของบุคคลทั่วไป"""
        self.name = name
        self.email = email

class User(Person, UserActions):
    """ Class ระบบ login, logout """
    def __init__(self, name, email, username, password):
        super().__init__(name, email)
        self.username = username
        self.__password = password

    def login(self, username, password):
        if username == self.username and password == self.__password:
            print(f"{username} เข้าสู่ระบบเสร็จสิ้น.")

        else:
            print("เข้าสู่ระบบไม่สำเสร็จ")

    def logout(self):
        print(f"{self.username} ออกจากระบบ.")

user = User('Boat', "boat@gmail.com", "boatemail", "boat1234")
user.login("boatemail", "boat1234")
user.logout()













