data = "ini adalah string"
print(data)
print(type(data))

# 1. Cara membuat string
'''

1. Dengan menggunakan single quote '...'
2. Dengan menggunakan double quote "..."

'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('''Halo, apa kabar?''')
print('''Halo, apa kabar?''')
print("ini adalah hari jum'at")


# 2. Menggunakan tanda \
# Membuat tanda ' menjadi string
print('Mari shalat jum\'at')
print('g\'day, isn\'t it?')

# Backlash
print("C:\\user\\Ucup")

# Tab
print("ucup\t\totong, semakin jauhan")

# Backspace
print("ucup\botong, jadi deketan")

# Newline
print("baris pertama.\nbaris kedua.") # LF -> line feed -> unix, macos, linux
print("baris pertama.\nbaris kedua.") # CR -> carriage return -> commodore, acorn, lisp
print("baris pertama\r\nbaris kedua.") # CRLF -> line feed carriage return -> dipakai oleh windows


# 3. String literal atau RAW
# Hati-hati
print('C:\new folder') # Akan salah pathnya

# Menggunakan raw string
print(r'C:\new folder')

# Multiline literal string
print("""
Nama : Ucup
Kelas : 3 SD
""")

# Multiline literal string dan RAW
print(r"""
Nama : Ucup
Kelas : 3 SD\new normal
Website : www.ucup.com/newID
""")