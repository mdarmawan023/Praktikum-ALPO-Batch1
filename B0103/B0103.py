# 1. Buat variabel untuk profil karakter game
nama_hero = "Bruce Wayne - Batman"
level = 50
hp = 999.9
is_alive = True
inventory = ["Batarang", "Grapple Gun", "Smoke Pellet"]
atribut = {"kekuatan": 80, "kelincahan": 65, "kecerdasan": 100}

# 2. Tampilkan seluruh informasi karakter menggunakan print()
print("--- PROFIL AWAL HERO ---")
print("Nama Hero :", nama_hero)
print("Level     :", level)
print("HP        :", hp)
print("Status    :", is_alive)
print("Inventory :", inventory)
print("Atribut   :", atribut)

# 3. Tampilkan tipe data dari masing-masing variabel menggunakan type()
print("\n--- CEK TIPE DATA ---")
print("Tipe nama_hero :", type(nama_hero))
print("Tipe level     :", type(level))
print("Tipe hp        :", type(hp))
print("Tipe is_alive  :", type(is_alive))
print("Tipe inventory :", type(inventory))
print("Tipe atribut   :", type(atribut))

# 4. Kerjakan aksi: Tambah item dan Naik level
# Karakter mendapatkan item baru "Ramuan HP" ke dalam list inventory
inventory.append("Ramuan HP")

# Karakter naik level: konversi level ke float lalu tambahkan 0.5
level = float(level) + 0.5

# 5. Cetak kembali informasi terbaru dari karakter tersebut
print("\n--- PROFIL HERO TERBARU (UPDATE) ---")
print("Nama Hero :", nama_hero)
print("Level Baru:", level)
print("HP        :", hp)
print("Status    :", is_alive)
print("Inventory :", inventory)
print("Atribut   :", atribut)
