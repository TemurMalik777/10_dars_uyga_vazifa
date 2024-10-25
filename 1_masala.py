class Shaxs:
    def __init__(self, ism, familiya, age):
        self.ism = ism
        self.familiya = familiya
        self.age = age

    def get_info(self):
        return f"Shaxs: {self.ism} {self.familiya}, Yoshi: {self.age}"    


class Talaba(Shaxs):
    def __init__(self, ism, familiya, age):
        super().__init__(ism, familiya, age)
        self.fanlar = []

    def fanga_yozil(self, fan):
        if isinstance(fan, Fan):
            self.fanlar.append(fan.nomi)
        else:
            print("Fan kiritilishi kerak!!!")

    def remove_fan(self, fan):
        if fan.nomi in self.fanlar:
            self.fanlar.remove(fan.nomi)
        else:
            print("Bu talaba bu fanga yozilmagan")

    def get_info(self):
        return f"Talaba: {self.ism} {self.familiya}, Yoshi: {self.age}, Fanlari: {', '.join(self.fanlar) if self.fanlar else 'Yoq'}"


class Fan:
    def __init__(self, nomi, kreditlar):
        self.nomi = nomi
        self.kreditlar = kreditlar


matematika = Fan("Matematika", 4)
fizika = Fan("Fizika", 3)
informatika = Fan("Informatika", 5)

n = int(input("Talabalar sonni kiriting: "))

talabalar = []

for i in range(n):
    ism = input(f"{i+1}-talabaning ismi: ")
    familiya = input(f"{i+1}-talabaning familiyasi: ")
    age = int(input(f"{i+1}-talabaning yoshi: "))

    talaba = Talaba(ism, familiya, age)

    print("Qaysi fanga yozilmoqchi? (1: Matematika, 2: Fizika, 3: Informatika)")
    fanlar_soni = int(input("Nechta fanga yozilmoqchisiz? "))

    for j in range(fanlar_soni):
        fan_tanlov = int(input(f"{j+1}-fan raqamini kiriting: "))
        if fan_tanlov == 1:
            talaba.fanga_yozil(matematika)
        elif fan_tanlov == 2:
            talaba.fanga_yozil(fizika)
        elif fan_tanlov == 3:
            talaba.fanga_yozil(informatika)

    talabalar.append(talaba)

for talaba in talabalar:
    print(talaba.get_info())


class Professor(Shaxs):
    def __init__(self, ism, familiya, age, unvoni):
        super().__init__(ism, familiya, age)
        self.fani = unvoni

    def get_info(self):
        return f"{super().get_info()}, Fani: {self.fani}"


class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, age, email):
        super().__init__(ism, familiya, age)
        self.email = email

#Foydalanuchi voris classidan voris olish
class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, age, email, parol):
        super().__init__(ism, familiya, age, email)
        self.__parol = parol

    def get_info(self):
        return f"Admin: {self.ism} {self.familiya}, Yoshi: {self.age}, Email: {self.email}, Password: {self.__parol}"

    def ban_user(self):
        print("Foydalanuvchi bloklandi")

class Sotuvchi(Shaxs):
    def __init__(self, ism, familiya, age, dokon_nomi):
        super().__init__(ism, familiya, age)
        self.dokon_nomi = dokon_nomi

    def get_info(self):
        return f"{super().get_info()}, Do'kon Nomi: {self.dokon_nomi}"


class Mijoz(Shaxs):
    def __init__(self, ism, familiya, age, xarid_soni):
        super().__init__(ism, familiya, age)
        self.xarid_soni = xarid_soni

    def get_info(self):
        return f"{super().get_info()}, Xarid Soni: {self.xarid_soni}"


professor = Professor("Zokir", "Aliyev", 45, "Professor")
foydalanuvchi = Foydalanuvchi("Zuhra", "Karimova", 30, "zuhra@mail.com")
sotuvchi = Sotuvchi("Jasur", "Ergashev", 35, "Jasur Do'koni")
mijoz = Mijoz("Dilmurod", "Rasulov", 28, 5)
admin = Admin("Hasan", "Berdiyev", 30, "malikovtimur2000@gmail.com", "HasAn45")

admin.ban_user()
print(professor.get_info())
print(foydalanuvchi.get_info())
print(sotuvchi.get_info())
print(mijoz.get_info())
print(admin.get_info())
