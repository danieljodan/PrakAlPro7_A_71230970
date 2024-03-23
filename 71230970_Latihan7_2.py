# Program Menghitung Frekuensi Kemunculan Kata pada Kalimat
def hitungKata(kalimat, kata):
    kalimatLower = kalimat.lower()
    kataLower = kata.lower()
    kalimatLowerBersih = "".join([i for i in kalimatLower if i.isalpha()])
    frekuensi = kalimatLowerBersih.count(kataLower)
    return frekuensi

kalimat = input("Masukkan kalimat Anda: ")
kata = input("Masukkan kata yang jumlahnya akan dicari: ")
print (f"Kata {kata} ada {hitungKata(kalimat,kata)} buah")


