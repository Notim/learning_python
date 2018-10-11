class Professor:

    def __init__(self):
        self.__email = None
        self.__nome = None
        self.__ra = None
        self.__celular = None
        self.__listaDisciplina = []

    def email(self):
        return __email

    def email(self, vaue):
        self.__email = email

    """
    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email
    
    """

    def set_nome(self, arg):
        self.__nome = arg

    def get_nome(self):
        return self.__nome

    def set_ra(self, arg):
        self.__ra = arg

    def get_ra(self):
        return self.__ra

    def set_celular(self, arg):
        self.__celular = arg

    def get_celular(self):
        return self.__celular

    def add_disciplinas(self, arg):
        self.__listaDisciplina.append(arg)

    def get_disciplinas(self):
        return self.__listaDisciplina




