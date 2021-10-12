class product:
    def __init__(self,id,name,quantity,required_quantity):
        self.__id = id
        self.__name = name
        self.__quantity = quantity
        self.__required_quantity = required_quantity

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_quantity(self):
        return self.__quantity

    def get_required_quantity(self):
        return self.__required_quantity

    def set_id(self,id):
        self.__id = id

    def set_name(self,name):
        self.__name = name

    def set_quantity(self,quantity):
        self.__quantity = quantity

    def set_required_quantity(self,required_quantity):
        self.__required_quantity = required_quantity



