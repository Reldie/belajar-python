#test
"""
print("Ridho")

umur = int(input("Masukkan umur anda: "))

if umur > 18:
    print("anda sudah dewasa")
elif umur >= 15:
    print("anda sudah remaja")
else:
    print("anda masih anak-anak")


for i in range(10):
    print(i+1, end= " ")

for i in range(1, 101):
    if i % 3 == 0:
        print(i)

for i in range(1, 101):
    if i % 2 == 0:
        print(i, "adalah angka genap")
    else:
        print(i, "adalah angka ganjil")

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")    
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
"""

#PR variabel pakai input, tipe datanya sebuah angka memakai input
"""
nilai = int(input("Masukkan angka: "))
if nilai >= 0 and nilai <=50:
    print("Nilai anda adalah E")
elif nilai >= 51 and nilai <=60:
    print("Nilai anda adalah D")
elif nilai >= 61 and nilai <=70:
    print("Nilai anda adalah C")
elif nilai >= 71 and nilai <=80:
    print("Nilai anda adalah B")
elif nilai >= 81 and nilai <=100:
    print("Nilai anda adalah A")
else:
    print("Masukkan angka yang valid!")
"""

#{} dict (key : value)
"""
siswa = {
    "nama" : "Ridho",
    "umur" : 15,
    "alamat" : "Bangka",
    "email": "ridho@gmail.com"
}
print(siswa)
print(siswa["nama"])
siswa["nama"] = "Iwan"
print(siswa["nama"])

print("======SETELAH PERUBAHAN======")

siswa["hobby"] = "memancing"
print(siswa)

del siswa["hobby"]
print(siswa)

students = {
    "001": {"nama" : "Ridho", "email": "ridho@gmail.com"},
    "002": {"nama" : "Iwan", "email": "Iwan@gmail.com"}
}
print(students["001"]["nama"])
"""

students = [
  {
    "nama": "Andi Saputra",
    "umur": 17,
    "kelas": "12 IPA 1",
    "nilai": {
      "Matematika": 85,
      "Bahasa Indonesia": 90,
      "Fisika": 78
    }
  },
  {
    "nama": "Siti Nurhaliza",
    "umur": 16,
    "kelas": "11 IPS 2",
    "nilai": {
      "Ekonomi": 88,
      "Sejarah": 92,
      "Bahasa Indonesia": 89
    }
  },
  {
    "nama": "Budi Santoso",
    "umur": 17,
    "kelas": "12 IPA 2",
    "nilai": {
      "Biologi": 80,
      "Kimia": 75,
      "Bahasa Inggris": 82
    }
  },
  {
    "nama": "Rina Marlina",
    "umur": 15,
    "kelas": "10 IPA 1",
    "nilai": {
      "Matematika": 95,
      "Bahasa Indonesia": 93,
      "Fisika": 90
    }
  }
]

"""
print(students[0]["nilai"])
print(students)
for i in students:
    print(i["nilai"])
    if([0] ):
        print(["nama"])
"""
"""     
for student in students:
    if student["umur"] >= 17:
        print(f"{student["nama"]} sudah bisa mendapatkan ktp")
    else: 
        print(f"{student["nama"]} belum bisa mendapatkan ktp")
"""
"""
for student in students:
    print(f"Nama : {student["nama"]}")
    nilai_siswa = student["nilai"]
    for mapel, nilai in nilai_siswa.items():
        print(f"{mapel} : {nilai}")
    rata_rata = sum(nilai_siswa.values())/len(nilai_siswa)
    print(f"Nilai rata-rata : {rata_rata:.2f}\n")
"""

#latihan kalau nilainya lebih dari 85 lulus kalau kurang dari 85 gak lulus
"""
for student in students:
    total_nilai = sum(student["nilai"].values())
    print (f"Total nilai {student["nama"]} adalah {total_nilai}")
    nilai_rata_rata = total_nilai / len(student["nilai"])
    print(f"Total nilai {student['nama']} adalah {total_nilai}, dengan rata-rata {nilai_rata_rata:.2f}")
    if nilai_rata_rata >= 85:
        print(f"{student['nama']} lulus dengan nilai rata-rata {nilai_rata_rata:.2f}")
    else:
        print(f"{student['nama']} tidak lulus dengan nilai rata-rata {nilai_rata_rata:.2f}")
"""
#[] list 
"""
nilai = [100, 90, 80, 79, 92]
print(nilai)
print(nilai[2])
print(str(nilai[2])[1])
print(nilai*2)
for i in nilai:
    if(i % 2 == 1):
        print(f"{i} adalah bilangan ganjil" )


buah = ["pisang", "jambu", "mangga", "durian"]
print(buah)
print(buah[3])

buah.append("kelengkeng")
print(buah)

buah.remove("jambu")
print(buah)
"""

#() tuple
"""
"""

#input
"""
nama = input("masukkan nama anda:")
alamat = input("masukkan alamat anda:")
umur = int(input("masukkan umur anda:"))

print("nama anda adalah" + nama)
print("alamat anda adalah" + alamat)

if umur >= 18:
    print("anda seharusnya memiliki ktp")
else:
    print("anda seharusnya belum memiliki ktp")

print(f"nama anda adalah {nama}")
print(f"alamat anda adalah {alamat}")
print(f"umur anda adalah {umur}")

print("nama anda adalah {}".format(nama))
print("alamat anda adalah {}".format(alamat))
print("umur anda adalah {}".format(umur))
"""

#function
"""
def greet (nama):
    nama = input("masukkan nama anda:")
    print("hello world", nama)

greet("") #memanggil fungsi greet
""" 

"""
numbers1 = [23,45,66,76,98,100,34,56,78,90]
numbers2 = [44,55,66,77,88,99,100,101]
numbers3 = [12,34,56,78,90,123,456,789]

def check_even_odd(numbers):
    for  number in numbers:
        if number % 2 == 0:
            print(f"{number} adalah bilangan genap")
        else: 
            print(f"{number} adalah bilangan ganjil")

check_even_odd(numbers1)
check_even_odd(numbers2)
check_even_odd(numbers3)
"""

#pr bikin function simulasi login, parameter username, kalau saat dipanggil usernamenya sama maka berhasil login kalau tidak maka tidak berhasil login
"""
def simulasi_login(username):
    user = input("Masukkan username: ")
    if user == username:
        print(f"Login akun dengan username {username} berhasil! ")
    else:
        print("Login gagal! Username tidak sama.")

simulasi_login("ridho")
"""

#nama = input("Masukkan nama anda: ")
"""
def ubah_vocal_ke_angka(angka):
    hasil = "" 

    for huruf in angka:
        if huruf == "e":
            hasil += "3"
        elif huruf == "a":
            hasil += "4"
        elif huruf == "i":
            hasil += "1"            
        elif huruf == "u":
            hasil += "2"
        elif huruf == "o":
            hasil += "0"        
        else:
            hasil += huruf
    print(hasil)
    return hasil

ubah_vocal_ke_angka("tikus")
"""

"""
def naik_satu_tingkat(letters):
    
    result = ""
    for letter in letters:
        if letter not in ["a", "e", "i", "o", "u", "3", "4", "1", "2", "0"]:   
            kode = ord(letter)
            if letter >= "a" and letter <= "z":
                if letter == "z":
                    kode_baru = ord("a")
                else:
                    kode_baru = kode + 1
            else: 
                result += letter
        else: 
            result += letter
    return result

def final(nama):
    langkah1 = ubah_vocal_ke_angka(nama)
    langkah2 = naik_satu_tingkat(langkah1)

print(final("Setiawan"))
"""

#pr ubah huruf besar jadi angka 
"""
def ubah_huruf_besar_ke_angka(teks):
    hasil = ""

    for huruf in teks:
        if huruf == "A":
            hasil += "1"
        elif huruf == "B":
            hasil += "2"
        elif huruf == "C":
            hasil += "3"
        elif huruf == "D":
            hasil += "4"
        else:
            hasil += huruf
    print(hasil)

ubah_huruf_besar_ke_angka("ayAm")
"""