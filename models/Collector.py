from utilities import StringBuilder

def Collector(Entity):

    def __init__(self):
        super.__init__()
        self.__name = ""
        self.__album = Album()
        self.__count_packages = 0
        self.__not_stickeds = list()
        self.__money = 0.0
    
    def __str__(self):
        sb = StringBuilder()
        sb.append("{")
        sb.append(f"\n\tId: {self.id}")
        sb.append(f"\n\tNome: {self.__name}")
        sb.append(f"\n\tMoney: {self.__money}")
        sb.append(f"\n\tCount_packages: {self.__name}")
        sb.Append(f"\n\tNot stickeds: {self.__not_stickeds}")
        sb.append(f"\n\tAlbum: {self.__album}")
        return sb
