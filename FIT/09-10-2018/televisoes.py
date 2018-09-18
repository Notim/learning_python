class Televisao:

    def __init__(self, arg1, arg2):
        self.ligada = False
        self.canal = 1
        self.__cmin = arg1
        self.__cmax = arg2

        print("Television v0.1\nfunctions:\n(o) turn on/off\n(a) down channel\n(d) up channel\nany number change direct to channel\nenjoy!!")

    def get_cmin(self):
        return self.__cmin

    def get_cmax(self):
        return self.__cmax

    def changeCh(self, opt):
        try:
            opt = int(opt)
            if self.ligada:
                self.canal = opt
                self.verifRange()
                print(self.canal)
            else:
                print("Zzz..")

        except ValueError:
            if self.ligada:
                print("Press a number")
            else:
                print("Zzz..")


    def Ch(self, opt):
        if self.ligada:
            self.verifRange()

            if opt == "u":
                self.canal -= 1
                print("<", self.canal)
            elif opt == "d":
                self.canal += 1
                print(">", self.canal)
        else:
            print("Zzz..")

    def off(self):
        if self.ligada:
            self.ligada = False
            print("Shutdown system..")
        else:
            self.ligada = True
            print("Wellcome!...")

    def verifRange(self):

        if self.canal < self.__cmin:
            self.canal = self.__cmax

        elif self.canal > self.__cmax:
            self.canal = self.__cmin
