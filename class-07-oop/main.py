# Abstraction
class User:
    def __init__(self, name, cpf):
        self.name = name
        self.__cpf = cpf

    def get_cpf(self):
        return self.__cpf

    def info(self):
        return(self.name, self.__cpf)
    
user = User("Odilon", "111.222.333-44")
    
print(user.name)
print(user.info())

# inheritance


class Admin(User):
    def __init__(self, name, cpf):
        super().__init__(name, cpf)
        self.__status = "admin"

    def set_status(self, status):
        self.__status = status
        
    def get_status(self):
        return self.__status
    
    def info(self):
        return (self.name, self.get_cpf(), self.__status)
        

admin = Admin("Enrique", "000.000.000-00")

print(admin.name)
print(admin.get_status())
admin.set_status("gold")
print(admin.get_status())

