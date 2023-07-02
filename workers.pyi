from person import person
class workers(person):

    def __init__(self, name, id, tel, address, salary):
        person.__init__(self, name, id, tel, address)
        self.salary = salary



