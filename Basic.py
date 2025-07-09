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

#{} dict
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

print(students[0]["nilai"])
print(students)
for i in students:
    print(i["nilai"])
    if([0] ):
        print(["nama"])
"""
        

#[] list 
"""
nilai = [100, 90, 80, 79, 92]
print(nilai)
print(nilai[2])
print(nilai[2][1])
print(nilai*2)
for i in nilai:
    if(i % 2 == 1):
        print(i)

buah = ["pisang", "jambu", "mangga", "durian"]
print(buah)
print(buah[3])

buah.append("kelengkeng")
print(buah)

buah.remove("jambu")
print(buah)
"""



#() tuple
