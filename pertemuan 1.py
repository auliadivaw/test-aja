class PersegiPanjang184220019  : 

    def __init__(self,p,l):
        self.panjang = p
        self.lebar = l

    def ubahPanjang (self,p):
        self.panjang = p

    def ubahLebar (self,l):
        self.lebar = l

    def hitungLuas(self):
        return self.panjang * self.lebar

    def hitungKeliling(self):
        return 2 * (self.panjang + self.lebar)

    def cetakLuas(self):
        print('Luas persegi panjang = %.2f' % self.hitungLuas())

    def cetakkeliling(self):
        print('Keliling persegi panjang=% .2f' % self.hitungKeliling())    
        
obj1 = PersegiPanjang184220019(10,3)
obj1.cetakLuas()
print(obj1)
