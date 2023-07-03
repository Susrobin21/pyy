class partyanimal :
    x = 0
    def innit(self):
        print('i am constructed')
    def party(self):
        self.x = self.x+1
        print("so far",self.x)
    def dele(self):
        print('i am destructed',self.x)
an = partyanimal()
an.party()
an.party()
an = 45
print('an contains',an)