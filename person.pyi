class person:

    def __init__(self, name, id, tel, address):
        self.name = name
        self.id = id
        self.tel = tel
        self.address = address

    def set_tel(self, tel):
        self.tel = tel

    def set_address(self, address):
        self.address = address