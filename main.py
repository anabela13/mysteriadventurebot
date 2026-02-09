import time
import random

class MysteryGame:
    def __init__(self):
        self.detective_name = ""
        self.current_hour = 1
        self.current_minute = 0
        self.pelaku = None  # "Satpam" atau "Sekretaris"
        self.bukti = []
        self.lokasi_diperiksa = set()
        self.case_solved = False
        self.final_guess = None
        
    def add_time(self, minutes):
        """Tambah waktu permainan"""
        self.current_minute += minutes
        if self.current_minute >= 60:
            self.current_hour += 1
            self.current_minute -= 60
        return self.current_hour < 3  # Batas maksimal jam 03:00
    
    def get_time_str(self):
        """Format waktu dalam string"""
        return f"{self.current_hour:02d}:{self.current_minute:02d}"

def intro():
    """Sequence pembukaan game"""
    print("\n" + "="*70)
    print("        *** THE MYSTERY ADVENTURE BOT ***")
    print("          A Case of Missing Blue Star Diamond")
    print("="*70)
    
    print("\n🌧️  LATAR BELAKANG KASUS:\n")
    print("Jam 01:00 pagi, di tengah hujan badai...")
    print("")
    print("Tuan Abraham menemukan brankas pribadinya TERBUKA.")
    print("Berlian 'BLUE STAR' senilai miliaran rupiah... HILANG!")
    print("")
    print("Tidak ada jendela yang pecah.")
    print("Tidak ada pintu yang dirusak.")
    print("Satu-satunya petunjuk: Sebuah cangkir kopi HANGAT di atas meja brankas.")
    print("")
    print("Hanya ada 2 orang di rumah selain Tuan Abraham:")
    print("  1. SATPAM (Budi) - Memiliki akses ke semua ruangan")
    print("  2. SEKRETARIS (Sandi) - Punya kode brankas")
    print("")
    print("Kedua mereka punya motif dan akses. Tapi hanya SATU yang berbohong.")
    print("")
    print("Waktu: Polisi akan tiba dalam 2 JAM!")
    print("")
    
    nama = input("👤 Siapa nama Anda, Detektif? ").strip()
    if not nama:
        nama = "Detective X"
    
    print(f"\n✓ Selamat datang, {nama}!")
    print(f"⏰ Waktu dimulai: 01:00 pagi")
    print(f"📍 Lokasi: Rumah Tuan Abraham\n")
    
    return nama

def setup_game():
    """Setup game baru"""
    game = MysteryGame()
    game.detective_name = intro()
    game.pelaku = random.choice(["Satpam", "Sekretaris"])
    
    print("="*70)
    print("Sistem investigasi siap. Mulai pencarian bukti!\n")
    
    return game

def show_menu(game):
    """Tampilkan menu utama"""
    waktu_tersisa = 120 - ((game.current_hour - 1) * 60 + game.current_minute)
    
    print(f"\n⏰ Waktu: {game.get_time_str()} | ⏳ Tersisa: {waktu_tersisa} menit")
    print(f"📋 Bukti terkumpul: {len(game.bukti)}")
    print("-"*70)
    
    print("\n📍 PILIH LOKASI YANG AKAN DIPERIKSA:\n")
    print("1. 🛡️  POS SATPAM - Cari barang di meja (Putar bingkai foto)")
    print("2. 💼 RUANG KERJA - Periksa komputer (Lihat log digital)")
    print("3. 🍳 DAPUR - Gunakan senter UV (Cari jejak kopi/kaki)")
    print("4. 📋 LIHAT BUKTI - Tampilkan semua bukti yang dikumpulkan")
    print("5. 🎯 TUDUH PELAKU - Lakukan akusasi final")
    print("6. ❌ HENTIKAN PERMAINAN\n")
    
    pilihan = input("Pilihan Anda (1-6): ").strip()
    return pilihan

def periksa_pos_satpam(game):
    """Periksa Pos Satpam - temukan barang di meja"""
    if "Pos Satpam" in game.lokasi_diperiksa:
        print("\n🛡️  Sudah diperiksa sebelumnya. Tidak ada temuan baru.")
        return True
    
    if not game.add_time(30):
        print("\n⏰ WAKTU HABIS! Polisi tiba!")
        return False
    
    game.lokasi_diperiksa.add("Pos Satpam")
    
    print("\n🛡️  POS SATPAM:\n")
    print("Ruangan kecil dengan meja, kursi, dan papan log kehadiran.")
    print("Anda mulai memeriksa meja satpam...\n")
    
    print("✓ Temuan: Catatan tangan di atas meja:")
    print("  'Bikin kopi hangat jam 23:45 untuk Tuan Abraham'")
    print("")
    
    game.bukti.append({
        "nama": "Catatan Kopi Satpam",
        "deskripsi": "Catatan: 'Bikin kopi jam 23:45'",
        "lokasi": "Pos Satpam"
    })
    
    print("✓ Temuan: Bingkai foto di atas meja")
    print("  [Anda memutar bingkai foto...]")
    time.sleep(1)
    print("  Di belakang bingkai, ada kertas kecil terselip!")
    print("  Tertulis: 'Alibi Satpam - Ronde jam 23:30'")
    print("")
    
    game.bukti.append({
        "nama": "Alibi Ronde Satpam",
        "deskripsi": "Kertas: 'Alibi - Ronde jam 23:30'",
        "lokasi": "Pos Satpam (di belakang bingkai)"
    })
    
    print("✓ Temuan: Catatan lain yang tercium aneh:")
    print("  'Tidak ada koneksi internet sejak jam 22:30'")
    print("")
    
    game.bukti.append({
        "nama": "Catatan Internet Mati",
        "deskripsi": "Catatan: 'Internet mati sejak jam 22:30'",
        "lokasi": "Pos Satpam"
    })
    
    return True

def periksa_ruang_kerja(game):
    """Periksa Ruang Kerja - lihat log digital di komputer"""
    if "Ruang Kerja" in game.lokasi_diperiksa:
        print("\n💼 Sudah diperiksa sebelumnya. Tidak ada temuan baru.")
        return True
    
    if not game.add_time(30):
        print("\n⏰ WAKTU HABIS! Polisi tiba!")
        return False
    
    game.lokasi_diperiksa.add("Ruang Kerja")
    
    print("\n💼 RUANG KERJA:\n")
    print("Meja rapi dengan komputer desktop.")
    print("Anda membuka file log sistem komputer...\n")
    
    print("📊 LOG LISTRIK (Power Management):")
    print("  - Jam 22:00 - 23:10: NORMAL")
    print("  - Jam 23:10 - 23:25: ⚠️  LONJAKAN DAYA MESIN KOPI")
    print("  - Jam 23:25 - 23:45: NORMAL")
    print("  - Jam 23:45 - 00:10: NORMAL\n")
    
    game.bukti.append({
        "nama": "Log Listrik Mesin Kopi",
        "deskripsi": "⚠️  MESIN KOPI MENYALA JAM 23:10-23:25 (bukan 23:45!)",
        "lokasi": "Komputer - Ruang Kerja"
    })
    
    print("📡 LOG WI-FI (Koneksi Internet):")
    print("  - Jam 22:30 - 00:00: ⚠️  INTERNET MATI TOTAL")
    print("  - Jam 00:00 - 01:00: INTERNET KEMBALI NORMAL\n")
    
    game.bukti.append({
        "nama": "Log Internet Mati",
        "deskripsi": "⚠️  INTERNET MATI JAM 22:30-00:00",
        "lokasi": "Komputer - Ruang Kerja"
    })
    
    print("🚪 LOG AKSES PINTU (Security Log):")
    print("  - Jam 23:00 - Satpam: Buka pintu dengan kartu akses")
    print("  - Jam 23:45 - Satpam: Buka pintu brankas")
    print("  - Jam 00:15 - Sekretaris: Buka pintu kamar dengan ID")
    print("")
    
    game.bukti.append({
        "nama": "Log Akses Brankas",
        "deskripsi": "Batasan akses brankas: Jam 23:45 oleh Satpam",
        "lokasi": "Komputer - Ruang Kerja"
    })
    
    return True

def periksa_dapur(game):
    """Periksa Dapur - gunakan senter UV"""
    if "Dapur" in game.lokasi_diperiksa:
        print("\n🍳 Sudah diperiksa sebelumnya. Tidak ada temuan baru.")
        return True
    
    if not game.add_time(30):
        print("\n⏰ WAKTU HABIS! Polisi tiba!")
        return False
    
    game.lokasi_diperiksa.add("Dapur")
    
    print("\n🍳 DAPUR:\n")
    print("Ruangan dapur yang bersih. Ada mesin kopi di meja.")
    print("Anda menggunakan senter UV untuk mencari bukti tersembunyi...\n")
    
    print("🔦 Hasil pemeriksaan Senter UV:\n")
    
    print("✓ Temuan: JEJAK KAKI di lantai dapur")
    print("  - Jejak dari brankas ke dapur (25 meter)")
    print("  - Ukuran sepatu: 41 (sesuai Satpam)")
    print("  - Jejak SEGAR, kemungkinan hari ini\n")
    
    game.bukti.append({
        "nama": "Jejak Kaki Brankas-Dapur",
        "deskripsi": "Jejak kaki ukuran 41 dari brankas ke dapur (segar, hari ini)",
        "lokasi": "Dapur - Lantai"
    })
    
    print("✓ Temuan: TETESAN KOPI di lantai dekat brankas")
    print("  - Tetesan masih basah dan lengket")
    print("  - Aroma kopi masih tercium segar\n")
    
    game.bukti.append({
        "nama": "Tetesan Kopi Segar",
        "deskripsi": "Tetesan kopi segar dan lengket di lantai brankas",
        "lokasi": "Dapur - Lantai Brankas"
    })
    
    print("✓ Temuan: CANGKIR KOPI di wastafel dapur")
    print("  - Cangkir masih hangat (baru digunakan)")
    print("  - Di dasar cangkir ada sisa lipstik merah\n")
    
    game.bukti.append({
        "nama": "Cangkir Kopi + Lipstik",
        "deskripsi": "Cangkir hangat dengan jejak lipstik merah (milik Sekretaris?)",
        "lokasi": "Dapur - Wastafel"
    })
    
    return True

def lihat_bukti(game):
    """Tampilkan semua bukti yang dikumpulkan"""
    if not game.bukti:
        print("\n❌ Belum ada bukti yang dikumpulkan!")
        print("   Silakan kunjungi lokasi untuk mengumpulkan bukti.\n")
        return
    
    print("\n" + "="*70)
    print("                    📋 BUKTI TERKUMPUL")
    print("="*70)
    print(f"Total bukti: {len(game.bukti)}\n")
    
    for idx, bukti in enumerate(game.bukti, 1):
        print(f"\n{idx}. 🔍 {bukti['nama']}")
        print(f"   📝 Deskripsi: {bukti['deskripsi']}")
        print(f"   📍 Lokasi: {bukti['lokasi']}")
    
    print("\n" + "="*70 + "\n")

def tuduh_pelaku(game):
    """Akusasi final - tuduh pelaku"""
    if len(game.bukti) < 2:
        print("\n⚠️  Belum cukup bukti untuk akusasi!")
        print(f"   Bukti terkumpul: {len(game.bukti)}/2 (minimum)")
        return
    
    print("\n" + "="*70)
    print("                    🎯 AKUSASI FINAL 🎯")
    print("="*70 + "\n")
    
    print("Sekarang saatnya untuk menuduh pelaku!\n")
    print("Siapa yang menurut Anda adalah pencuri berlian Blue Star?\n")
    print("1. 🛡️  SATPAM (Budi)")
    print("2. 💼 SEKRETARIS (Sandi)")
    print("3. ❌ BATALKAN AKUSASI\n")
    
    pilihan = input("Pilihan Anda (1-3): ").strip()
    
    if pilihan not in ["1", "2"]:
        print("\n❌ Akusasi dibatalkan.\n")
        return
    
    tersangka = "Satpam" if pilihan == "1" else "Sekretaris"
    
    print(f"\n🎤 Anda menuduh: {tersangka}\n")
    print("Sekarang, pilih ALASAN akusasi Anda:\n")
    print("1. ⏰ JAM MESIN KOPI tidak cocok dengan alibi")
    print("2. 📡 INTERNET MATI saat pencurian terjadi")
    print("3. 👣 JEJAK KAKI membongkar alibi")
    print("4. ❌ BATALKAN\n")
    
    alasan = input("Pilihan Anda (1-4): ").strip()
    
    if alasan not in ["1", "2", "3"]:
        print("\n❌ Akusasi dibatalkan.\n")
        return
    
    # Tentukan hasil akusasi
    alasan_text = {
        "1": "Jam Mesin Kopi",
        "2": "Internet Mati",
        "3": "Jejak Kaki"
    }
    
    game.final_guess = {
        "tersangka": tersangka,
        "alasan": alasan_text[alasan],
        "alasan_code": alasan
    }
    
    cek_akusasi(game)

def cek_akusasi(game):
    """Periksa apakah akusasi benar"""
    print("\n" + "="*70)
    
    tersangka = game.final_guess["tersangka"]
    alasan = game.final_guess["alasan"]
    alasan_code = game.final_guess["alasan_code"]
    
    # Logika kemenangan
    is_correct_suspect = (tersangka == game.pelaku)
    
    # Validasi alasan sesuai dengan pelaku yang sebenarnya
    if game.pelaku == "Satpam":
        # Jika Satpam pelaku, bukti yang cocok: Jam Mesin Kopi (alibi bohong: jam 23:45, faktanya 23:10)
        is_correct_reason = (alasan_code == "1")  # Jam Mesin Kopi
    else:
        # Jika Sekretaris pelaku, bukti yang cocok: Internet Mati (saat dia mencuri)
        is_correct_reason = (alasan_code == "2")  # Internet Mati
    
    if is_correct_suspect and is_correct_reason:
        # MENANG!
        print("                    🎉 ANDA MENANG! 🎉")
        print("="*70 + "\n")
        
        print(f"✓ BENAR! Pelaku adalah {tersangka}!\n")
        print(f"✓ Alasan: {alasan}\n")
        
        if tersangka == "Satpam":
            print("PENJELASAN:")
            print("Satpam mengaku membuat kopi jam 23:45,")
            print("tapi LOG LISTRIK mencatat mesin kopi menyala JAM 23:10!")
            print("")
            print("Satpam berbohong. Dia membuat kopi lebih awal di saat")
            print("Tuan Abraham tidur, kemudian membuka brankas dan mencuri!")
            print("")
            print("JEJAK: Jejak kaki ukuran 41 (Satpam) dari brankas ke dapur,")
            print("dan tetesan kopi segar di lantai brankas membuktikan semuanya!")
        
        else:
            print("PENJELASAN:")
            print("Sekretaris mengaku memesan kopi jam 23:00,")
            print("tapi LOG WI-FI mencatat INTERNET MATI JAM 22:30-00:00!")
            print("")
            print("Sekretaris tidak mungkin memesan kopi online saat internet mati.")
            print("Dia berbohong. Alibinya palsu. Dia adalah pencuri!")
            print("")
            print("JEJAK: Cangkir kopi dengan jejak lipstik merah (Sekretaris)")
            print("di wastafel membuktikan dia yang membuat kopi, bukan memesan!")
        
        print("\n🚨 Pelaku ditangkap!")
        print("💎 Berlian Blue Star diselamatkan!\n")
        
        game.case_solved = True
        
    else:
        # KALAH!
        print("                    ❌ ANDA KALAH! ❌")
        print("="*70 + "\n")
        
        print(f"✗ SALAH! Pelaku BUKAN {tersangka}!\n")
        print(f"❌ Alasan Anda ({alasan}) tidak cukup kuat untuk bukti nyata.\n")
        
        print(f"✗ Pelaku sebenarnya adalah: {game.pelaku}\n")
        
        print("PENJELASAN YANG SEHARUSNYA:")
        if game.pelaku == "Satpam":
            print("Satpam adalah pencuri!")
            print("Bukti yang seharusnya Anda gunakan: JAM MESIN KOPI")
            print("(Alibi bohong: jam 23:45, faktanya jam 23:10)")
        else:
            print("Sekretaris adalah pencuri!")
            print("Bukti yang seharusnya Anda gunakan: INTERNET MATI")
            print("(Alibi bohong: pesan kopi online saat internet mati)")
        
        print("\n🚓 Polisi tiba, tapi terlambat...")
        print("Pelaku berhasil melarikan diri dengan berlian Blue Star!")
        print("Kasus ini tetap menjadi MISTERI YANG BELUM TERPECAHKAN!\n")
        
        game.case_solved = True

def main_loop(game):
    """Main game loop"""
    while not game.case_solved:
        # Cek apakah waktu sudah habis
        if game.current_hour >= 3:
            print("\n⏰ WAKTU HABIS! Jam 03:00 pagi!")
            print("🚓 Polisi tiba. Pelaku berhasil melarikan diri!\n")
            break
        
        pilihan = show_menu(game)
        
        if pilihan == "1":
            if not periksa_pos_satpam(game):
                break
        elif pilihan == "2":
            if not periksa_ruang_kerja(game):
                break
        elif pilihan == "3":
            if not periksa_dapur(game):
                break
        elif pilihan == "4":
            lihat_bukti(game)
        elif pilihan == "5":
            tuduh_pelaku(game)
        elif pilihan == "6":
            print("\n❌ Permainan dihentikan.\n")
            break
        else:
            print("\n❌ Pilihan tidak valid!\n")

def game_utama():
    """Entry point - Fungsi utama game"""
    try:
        game = setup_game()
        main_loop(game)
        
        print("="*70)
        print("           TERIMA KASIH TELAH BERMAIN")
        print("          THE MYSTERY ADVENTURE BOT")
        print("="*70)
        print("\nUntuk bermain lagi, jalankan program ini kembali.\n")
    
    except KeyboardInterrupt:
        print("\n\n❌ Permainan dihentikan oleh pengguna.")

if __name__ == "__main__":
    game_utama()