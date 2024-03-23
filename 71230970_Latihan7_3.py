# Program Menghapus Spasi Berlebih
def spasiBerlebih(kalimat):
    kalimatBersih1 = " ".join(kalimat.split())
    return kalimatBersih1

masukan1 = input("Masukkan kalimat:\n")
print("Kalimat dengan spasi normal:\n"+spasiBerlebih(masukan1))