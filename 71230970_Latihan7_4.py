# Program Untuk Mengecek Kata Terpendek dan Terpanjang
def kataPendekPanjang(kalimat):
    kata = kalimat.split()
    terpendek = min(kata, key=len)
    terpanjang = max(kata, key=len)
    print(f"terpendek: {terpendek}")
    print(f"terpanjang: {terpanjang}")

masukan1 = input("Masukkan kalimat: ")
kataPendekPanjang(masukan1)