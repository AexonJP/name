def load():
    import pickle
    return pickle.load(open("schedule.dat1", "rb") )

def press():
    return input("\nPress Enter to continue...")

def save(data):
    import pickle
    return   pickle.dump(data, open("schedule.dat1", "wb") )

def clear():
    import os
    return os.system("cls")

def salah():
    print("Format yang anda masukkan salah\n")

def bulan(yes):
    from datetime import date
    waktu = date.today()
    bulan = int(waktu.strftime(yes))
    if bulan == 1:
        bulan = "Januari"
    elif bulan == 2:
        bulan = "Februari"
    elif bulan == 3:
        bulan = "Maret"
    elif bulan == 4:
        bulan = "April"
    elif bulan == 5:
        bulan = "Mei"
    elif bulan == 6:
        bulan = "Juni"
    elif bulan == 7:
        bulan = "Juli"
    elif bulan == 8:
        bulan = "Agustus"
    elif bulan == 9:
        bulan = "September"
    elif bulan == 10:
        bulan = "Oktober"
    elif bulan == 11:
            bulan = "November"
    elif bulan == 12:
        bulan = "Desember"
    return bulan
     
def hari():
    from datetime import date
    waktu = date.today()
    hari = waktu.strftime("%A")    
    tanggal1 = waktu.strftime(f"%d {bulan('%m')} %Y")
    tanggal = waktu.strftime("%y%m%d")
    if hari == "Monday":
        hari = "Senin"
    elif hari == "Tuesday" :
        hari = "Selasa"
    elif hari == "Wednesday":
        hari = "Rabu"
    elif hari == "Thursday":
        hari = "kamis"
    elif hari == "Friday":
        hari = "Jum'at"
    elif hari == "Saturday":
        hari = "Sabtu"
    elif hari == "Sunday":
        hari = "Minggu"
    print (f"Tanggal {tanggal1}\nHari {hari}")
    return str(tanggal)

def tanggal():
    tanggal = {
    'Tahun Baru 2021 Masehi':'01 Januari',
    'Tahun Baru Imlek':'12 Februari',
    'Hari Suci Nyepi Tahun Baru Saka':'14 Maret',
    'Wafat Isa Al Masih':'02 April',
    'Hari Buruh Internasional':'01 Mei',
    'Kenaikan Isa Al Masih':'13 Mei',
    'Hari Raya Waisak':'26 Mei',
    'Hari Lahir Pancasila':'01 Juni',
    'Hari Kemerdekaan Republik Indonesia':'17 Agustus',
    'Hari Raya Natal':'25 Desember'}
    return tanggal

def garis():
    garis = ("=======================================")
    return garis

def menu():
    print (garis())
    print (f"1. Melihat jadwal ke depannya.\n2. Menambahkan jadwal baru.\n3. Menghapus Jadwal yang sudah ada.\n4. Daftar tanggal merah (Tetap).\n5. Mengubah jadwal yang sudah ada")
    print (garis())
    masukan = input ("Ingin membuka nomor : ")
    return masukan

def tahun():
    from datetime import date
    waktu = date.today()
    hari = waktu.strftime("%Y")
    return hari

def check(masukan):
    if masukan == "done":
        return "done"
    try:
        masukan = int(masukan)
        if masukan > 0 :
            return masukan
        else:
            return 0
    except :
        return 0

def loading(times):
    import time
    return time.sleep(times)

def data_jadwal():
    data = {
    "jadwal":[],
    "kode":[]}
    return data

def daftar_menu(jadwal, kode):
    for i in range(len(jadwal)):
                    loading(0.3)
                    print (f"{i+1}. {jadwal[i]} ({kode[i]})\n")
    

def mulai():
    merah = tanggal()
    data = data_jadwal()
    try :
        data =load()
    except :
        pass
    while(True): 
        hari()
        kode = check(menu())
        if kode == 1:
            clear()
            print (garis())
            print ("Berikut adalah jadwal yang ada :\n")
            if len(data["jadwal"]) > 0:
                daftar_menu(data['jadwal'], data['kode'])
                loading(0.5)
                press()
                clear()
            else :
                print ("Masih belum ada jadwal terbaru\n\n")
            
        elif kode == 2:
            clear()
            print (garis())
            print ("Berikut adalah jadwal yang ada :\n")
            if len(data["jadwal"]) > 0:
                daftar_menu(data['jadwal'], data['kode'])
            else :
                print ("Masih belum ada jadwal terbaru\n\n")
            qer = input ("Judul dari jadwal yang akan di tambah : ")
            wer = input ("Masukkan tanggal (day/month/year or 00/00/0000) : ")
            data['jadwal'].append (qer)
            data['kode'].append (wer)
            loading(0.3)
            print("\nJadwal berhasil di tambahkan")
            loading(0.3)
            press()
            clear()

            
        elif kode == 3:
            clear()
            print (garis())
            print ("Berikut adalah jadwal yang ada :\n")
            if len(data["jadwal"]) > 0:
                daftar_menu(data['jadwal'], data['kode'])
            else :
                print ("Masih belum ada jadwal terbaru\n\n")
            hapus = input ("Nomor dari jadwal yang ingin di hapus : ")
            hapus = check(hapus)
            if hapus > 0 :
                try:
                    del data['jadwal'][hapus-1]
                    del data['kode'][hapus-1]
                    loading(0.5)
                    print ("\nJadwal berhasil di hapus")
                except:
                    loading(0.5)
                    print("\nPenghapusan jadwal gagal")
            else:
                loading(0.5)
                print("\nPenghapusan jadwal gagal")
            loading(0.3)
            press()
            clear()
        elif kode == 4:
            clear()
            print(garis())
            print ("Berikut adalah jadwal yang ada :\n")
            cobas1 = []
            for cobas in merah:
                cobas1.append (f"{cobas} ({merah[cobas]} {tahun()})")
            for i in range(len(cobas1)):
                loading(0.1)
                print (f"{i+1}. {cobas1[i]}")
            print ()
            press()
            clear()
        elif kode == 5 :
            if len(data["jadwal"]) > 0:
              daftar_menu(data['jadwal'], data['kode'])
            else :
                print ("Masih belum ada jadwal terbaru\n\n")
            hapus = input("Masukkan nomor jadwal yang ingin di ubah : ")
            hapus = check(hapus)
            if hapus > 0:
                try:
                    data['jadwal'][hapus-1] = input("Masukkan judul baru jadwal : ")
                    data['kode'][hapus-1] = input("Masukkan tanggal (day/month/year or 00/00/0000) : ")
                    loading(0.5)
                    print ("\nJadwal berhasil di ubah")
                except:
                    loading(0.5)
                    print("\nPengubahan jadwal gagal")
            else:
                loading(0.5)
                print("\nPengubahan jadwal gagal")
            press()
            clear()
        elif kode == "done":
            break
        else:
            salah()
            press()
            clear()
        save(data)
    clear()

mulai()