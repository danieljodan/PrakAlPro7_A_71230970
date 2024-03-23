# Program Anagram
def cekAnagram (masukan1, masukan2):
    kata1 = masukan1.lower()
    kata1Urut = sorted (kata1)
    kata2 = masukan2.lower()
    kata2Urut = sorted (kata2)
    if kata1Urut == kata2Urut:
        print(f"{kata1} dan {kata2} adalah anagram.")
    else:
        print("Bukan Anagram")
        
kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")
cekAnagram (kata1,kata2)

