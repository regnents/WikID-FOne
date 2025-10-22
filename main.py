import time
import creator_template
import updater_db_balapan
import updater_db_klasemen


def wrong_input():
    print("Maaf, perintah yang Anda masukkan salah. Silahkan coba lagi.")
    time.sleep(1.5)

if __name__ == "__main__":
    print("Selamat datang ke dalam WikID-FOne!")
    isDone = False
    while not isDone:
        print("Daftar perintah:")
        print("1. Pembaruan basis data")
        print("2. Pembuatan templat")
        print("0. Keluar")
        opsi = input("Masukkan kode perintah yang ingin Anda lakukan: ")
        if opsi == "0":
            print("Mengakhiri program...")
            time.sleep(1.5)
            print("Sampai jumpa!")
            isDone = True
        elif opsi == "1":
            print("Anda hendak memperbarui basis data Anda")
            print("Pembaruan basis data yang dapat dilakukan:")
            print("1. Pembaruan keseluruhan klasemen")
            print("2. Pembaruan hasil keseluruhan suatu Grand Prix")
            print("0. Batal")
            opsi_update = input("Masukkan opsi pembaruan yang ingin Anda lakukan: ")
            if opsi_update == "0":
                print("Membatalkan perintah.")
                print("Kembali ke menu utama...")
                time.sleep(1.5)
            elif opsi_update == "1":
                updater_db_klasemen.update_all()
            elif opsi_update == "2":
                updater_db_balapan.update_all()
            else:
                wrong_input()
        elif opsi == "2":
            print("Anda hendak membuat templat berdasarkan data yang tersimpan di dalam basis data")
            print("Templat yang dapat dibuat:")
            print("1. Templat F1 Drivers Standing")
            print("2. Templat F1R2025")
            print("0. Batal")
            opsi_templat = input("Masukkan kode templat yang ingin dibuat:")
            if opsi_templat == "0":
                print("Membatalkan perintah.")
                print("Kembali ke menu utama...")
                time.sleep(1.5)
            elif opsi_templat == "1":
                creator_template.creator_f1_drivers_standing()
            elif opsi_templat == "2":
                creator_template.creator_f1r2025()
            else:
                wrong_input()
        else:
            wrong_input()

            