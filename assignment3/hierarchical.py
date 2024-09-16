
#hirarchical inheritence

class office:
    def profession(self):
        print("I work for Infosys")

class shreeram(office):
    def web_dev(self):
        print("I am a full stack dev")

class keerthi(office):
    def da(self):
            print("I am a data analyst")

dev = shreeram()
dev.profession()
dev.web_dev()

data_an = keerthi()
data_an.profession()
data_an.da()
