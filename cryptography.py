import string
abjad = string.printable

def enkrip(pesan):
    global abjad

    key = int(input('masukkan key   : '))
    cipher = ' ' #menampilkan cipher
    for i in pesan :
        if i in abjad :
            k = abjad.find(i) #menentukan variasi
            k = (k + key) %100
            cipher = cipher + abjad[k]
        else:
            cipher = cipher + i
    return cipher

def dekrip(cipher):
    global abjad 
    key = int(input('masukkan key   : '))
    pesan = ' ' #menampilkan pesan dekripsi
    for i in cipher :
        if i in abjad:
            k = abjad.find(i)
            k = (k - key)%100
            pesan = pesan+abjad[k]
        else:
            pesan = pesan + i
    return pesan

if __name__ == '__main__' :
    print('-----20.240.0152 Awan Widiatma-----')

option = int(input('1. Enkripsi\n2. Dekripsi\n Pilih Option     :'))
if option == 1:
    pesan = input('Masukkan Pesan (Plaintext)   :')
    print(enkrip(pesan))
elif option == 2:
    cipher = input('Masukkan Pesan (Ciphertext)   :')
    print(dekrip(cipher))
else:
    print('Masukkan option 1 atau 2')
