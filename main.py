class Ember:
    def __init__(self, nem, szul, az, k):
        self.nem = int(nem)
        self.szul = szul
        self.az = int(az)
        self.k = int(k)
        self.ev = int(szul[:2])
        self.ho = int(szul[2:4])
        self.nap = int(szul[4:])

    def __str__(self):
        return f"{self.nem} {self.szul} {self.az} {self.k}"

    def CdvE11(self):
        ch = self.nem * 10 + int(self.szul[0]) * 9 + int(self.szul[1]) * 8 + int(self.szul[2]) * 7 + int(self.szul[3]) * 6 + int(
            self.szul[4]) * 5 + int(self.szul[5]) * 4 + int(str(self.az)[0]) * 3 + int(str(self.az)[1]) * 2 + int(str(self.az)[2])
        ch = ch % 11
        if ch == self.k:
            return True
        else:
            return False


main_list = []


def read():
    with open('vas.txt', 'r', encoding='utf-8') as f:
        for i in f:
            i = i.strip()
            i = i.split('-')
            main_list.append(Ember(i[0], i[1], i[2][:3], i[2][-1]))


def f4():
    for i in main_list:
        if i.CdvE11() == False:
            return f"{i} rossz"


def main():
    print(f"2. feladat: Adatok beolvasása, tárolása{read()}")
    print(f"4. feladat: Ellenőrzés: {f4()}")


main()
