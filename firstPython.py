# nilai_matematika = 90
# nilai_bahasa = 85
# nilai_total = 0

# nilai_total = nilai_matematika + nilai_bahasa
# print(nilai_total)

# umur = int(input("Masukkan umur Anda: "))

# if umur > 18:
#     print("Anda sudah dewasa")
# elif umur >= 15:
#     print("Anda sudah remaja")
# else:
#     print("Anda masih anak-anak")

# saya mencontek dan harus menulis sebanyak 1000 kali
# saya mencontek dan harus menulis sebanyak 1000 kali
# saya mencontek dan harus menulis sebanyak 1000 kali
# saya mencontek dan harus menulis sebanyak 1000 kali
# saya mencontek dan harus menulis sebanyak 1000 kali

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0 :
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# {} dictionary
# [] list

# typedata
# string
# number
# boolean
# undefined
# null
# nama = "john"
# nama = "iwan"
# print(nama)

# for i in range(11):
#     print(i)


# siswa = {
#     "nama" : "iwan",
#     "umur" : 20,
#     "alamat" : "jakarta",
#     "email" : "iwan@mail.com"
# }
# print(siswa)
# # print(siswa["nama"])
# siswa["nama"] = "ridho" #reassign nilai pada dict
# # print(siswa["nama"])

# print(" ======== SETELAH PERUBAHAN ========")

# siswa["hobby"] = "memancing"
# print(siswa)

# del siswa["hobby"]

# print(siswa)

# ============== LIST =============

# print(nilai)
# print(nilai[4])

# buah = ["pisang", "jambu", "mangga", "durian"]
# print(buah)
# buah.append("klengkeng")
# print(buah)

# buah.remove("jambu")
# print(buah)

# nilai = [100, 90, 80, 79, 92,]
# print(nilai)
# for i in nilai:
#     if( i % 2 ==1):
#         print (i )


# students = {
#     "001" : {"nama" : "iwan", "email" : "iwan@mail.com"},
#     "002" : {"nama" : "ridho", "email" : "ridho@mail.com", 
#              "sosmed : {"
#              ""
#              "}"}
# }

# print(students["001"]["nama"])

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

# print(students[0]["nilai"])
# print(students)
for i in students:
    print(i["nilai"])
    # if([0] )
    #     print(["nama"])