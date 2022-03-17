import os
import sys

class User:
    def __init__(self, user_info_file = "user.txt"):
        self.name = None
        self.login = None
        self.password = None
        self.password_t = None
        self.age = None
        self.kasbi = None
        self.user_info_file = user_info_file
        self.all_users = []
        self.welcome()

    def welcome(self):
        reg_log = input(''' 
        Quydagilardan birini tanlang:
        [1] Register
        [2] Login
        [3] Exit program''')

        while reg_log.strip() not in ["1", "2", "3"]:
            os.system("cls")
            print("Noto'g'ri tanlov!")
            reg_log = input(''' 
                    Ilti keraklisini tanlang:
                    [1] Register
                    [2] Login
                    [3] Exit program
                    --->:
                    ''')
        if reg_log == "1":
            self.register()
        elif reg_log == "2":
            self.log_in()
        else:
            sys.exit()

    def register(self):
        self.name = input("Your name: ").strip().capitalize()
        while not self.name.isalpha():
            print("Ism soralyapti sandan!!!")
            self.name = input("Your name: ").strip().capitalize()
        self.age = input("Your age: ").strip()
        while not self.age.isdigit():
            print("Yoshini kirgiz ahmoq :): ")
            self.age = input("Your age: ").strip()
        self.kasbi = input("Kasbingiz: ").strip().capitalize()
        while not self.kasbi.isalpha():
            print("Kasbingizni odamchasiga yoz: ")
            self.kasbi = input("Kasbingiz: ").strip().capitalize()
        self.login = input("You login: ").strip()
        with open(self.user_info_file) as file:
            for user_row in file.read().split():
                log = {
                    user_row.split(',')[0].split(':')[0]: user_row.split(',')[0].split(':')[1],
                }
                for self.login in log:
                    self.login = input("You login: ").strip()
        while not self.login.isalnum():
            os.system("cls")
            print("Please chose alphanumeric characters: ")
            self.login = input("You login: ").strip()
        self.password = input("You Password: ")
        while not self.password or len(self.password) < 6:
            print("Parol kamida 6 ta belgidan iborat bo'lishi kerak! "
                  "yana bir bor urinib ko'ring: ")
            self.password = input("You Password: ")
        self.password_t = input("Passwordni tasdiqlang: ")
        while self.password_t != self.password:
            print("Password tasdiqlanmadi. Qayta urinib ko'ring: ")
            self.password_t = input("Passwordni tasdiqlang: ")

        with open(self.user_info_file, 'a') as file:
            file.write(f"login:{self.login},password:{self.password},name:{self.name},age:{self.age},kasbi:{self.kasbi}\n")
        self.self_none()
        print("Ro'yxatdan o'tdingiz! ")
        self.log_out()

    def log_in(self):
        self.self_none()
        if self.login is not None and self.password is not None:
            print("You are already logged in!")
        else:
            if self.file_empty():
                print("You are not registered!")
                self.welcome()
            else:
                # User login teryabdi
                os.system("cls")
                self.login = input("You login: ").strip()
                while not self.login.isalnum():
                    os.system("cls")
                    print("Please chose alphanumeric characters: ")
                    self.login = input("You login: ").strip()
                # User password teryabdi
                self.password = input("You Password: ")
                while not self.password or len(self.password) < 6:
                    os.system("cls")
                    print("Parol kamida 6 ta belgidan iborat bo'lishi kerak! "
                          "yana bir bor urinib ko'ring: ")
                    self.password = input("You Password: ")
                self.get_all_user_in_db()

                if self.user_exists():
                    print("Siz tizimga muvaffaqiyatli kirdingiz! ")
                    self.self_none()
                    self.log_in_wel()

                else:
                    print("Bu foydalanuvchi mavjud emas! ")
                    self.log_pass()

    def log_pass(self):
        log_pass_x = input('''
            [1] Parol_Loginni qayta kiritish
            [2] Ro'yxatdan o'tish
            [3] Tizimdan chiqish
        ''')
        while log_pass_x.strip() not in ["1", "2", "3"]:
            print("Noto'g'ri tanlov!")
            log_pass_x = input('''
                        [1] Login_Parol qayta kiritish
                        [2] Ro'yxatdan o'tish
                        [3] Tizimdan chiqish
                    ''')
            if log_pass_x == "1":
                self.log_in()
            elif log_pass_x == "2":
                self.register()
            else:
                sys.exit()

    def log_in_wel(self):
        self.self_none()
        reg_log_in = input(''' 
                [1] change password
                [2] Log out
                [3] Exit program
                --->:
                ''')
        while reg_log_in.strip() not in ["1", "2", "3"]:
            os.system("cls")
            print("Noto'g'ri tanlov!")
            reg_log_in = input(''' 
                           [1] change password
                           [2] Log out
                           [3] Exit program
                           --->:
                           ''')
        if reg_log_in == "1":
            print("ERROR 404")
            self.log_in_wel()
        elif reg_log_in == "2":
            self.log_out()
        else:
            sys.exit()

    def log_out(self):
        self.welcome()

    def change_password(self):
        pass

    def delete_account(self):
        pass

    def file_empty(self):
        with open(self.user_info_file) as file:
            text = file.read()
        return text == ""

    def get_all_user_in_db(self):
        with open(self.user_info_file) as file:
            for user_row in file.read().split():
                user_dict = {
                    user_row.split(',')[0].split(':')[0]: user_row.split(',')[0].split(':')[1],
                    user_row.split(',')[1].split(':')[0]: user_row.split(',')[1].split(':')[1]
                }
                self.all_users.append(user_dict)

    def user_exists(self):
        for row in self.all_users:
            if self.login == row["login"] and self.password == row["password"]:
                return True
        return False

    def self_none(self):
        self.name = None
        self.login = None
        self.password = None
        self.password_t = None
        self.age = None
        self.kasbi = None




person = User()
person.log_in()
