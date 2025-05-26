from additional_func import db_activator, db_closer, soup_creator, url_fixer

QUERY_INSERT_HASIL_BALAPAN = "INSERT INTO hasil_balapan(kode_pembalap, kode_balapan, posisi) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE posisi=%s;"
QUERY_UPDATE_POSISI_POLE = (
    "UPDATE hasil_balapan SET pole=TRUE WHERE kode_pembalap=%s AND kode_balapan=%s;"
)
QUERY_UPDATE_FL = (
    "UPDATE hasil_balapan SET fl=TRUE WHERE kode_pembalap=%s AND kode_balapan=%s;"
)
QUERY_UPDATE_SPRINT = "UPDATE hasil_balapan SET posisi_sprint=%s WHERE kode_pembalap=%s AND kode_balapan=%s;"


def update_all(kode_balapan):
    link_balapan = input("Masukkan url balapan: ")
    update_hasil(kode_balapan, link_balapan)
    isSprint = input("Apakah balapan sprint? (Y/N) ")
    if isSprint == "Y":
        update_sprint(kode_balapan, url_fixer(link_balapan, 2))
    update_pole_link(kode_balapan, url_fixer(link_balapan, 3))
    update_fl_link(kode_balapan, url_fixer(link_balapan, 4))


def update_hasil(kode_balapan, url_balapan):
    tbody = soup_creator(url_balapan).find("tbody")
    mydb = db_activator()
    mycursor = mydb.cursor()
    for tr in tbody.find_all("tr"):
        list_td = tr.find_all("td")
        finish_pos = ""
        if list_td[0].find("p").text == "NC":
            finish_pos = "Ret"
        elif list_td[0].find("p").text == "DQ":
            finish_pos = "DSQ"
        elif len(list_td[0].find("p").text) == 1:
            finish_pos = "0" + list_td[0].find("p").text
        else:
            finish_pos = list_td[0].find("p").text
        kode_pembalap = list_td[2].find("span", class_="tablet:hidden").text
        val = (kode_pembalap, kode_balapan, finish_pos, finish_pos)

        mycursor.execute(QUERY_INSERT_HASIL_BALAPAN, val)
        mydb.commit()
    db_closer(mycursor, mydb)


def update_pole_kode_pembalap(kode_balapan, kode_pembalap):
    mydb = db_activator()
    mycursor = mydb.cursor()
    mycursor.execute(QUERY_UPDATE_POSISI_POLE, (kode_pembalap, kode_balapan))
    mydb.commit()
    db_closer(mycursor, mydb)


def update_pole_link(kode_balapan, url_grid_awal):
    tbody = soup_creator(url_grid_awal).find("tbody")
    mydb = db_activator()
    mycursor = mydb.cursor()
    kode_pembalap = (
        tbody.find_all("tr")[0]
        .find_all("td")[2]
        .find("span", class_="tablet:hidden")
        .text
    )
    mycursor.execute(QUERY_UPDATE_POSISI_POLE, (kode_pembalap, kode_balapan))
    mydb.commit()
    db_closer(mycursor, mydb)


def update_pole(kode_balapan):
    print("Anda hendak memperbarui peraih pole pada " + kode_balapan)
    print(" Terdapat dua opsi cara memperbarui data:")
    print("1. Pembaruan menggunakan kode pembalap")
    print("2. Pembaruan menggunakan URL grid awal situs web F1")
    print("0. Keluar (Kembali ke opsi sebelumnya)")
    isPoleDone = False
    isCancelled = False
    while not isPoleDone:
        opsi = input("Pilihan opsi: ")
        if opsi == "1":
            kode_pembalap = input(
                "Masukkan kode pembalap yang meraih posisi pole pada GP "
                + kode_balapan
                + ": "
            )
            update_pole_kode_pembalap(kode_balapan, kode_pembalap)
            isPoleDone = True
        elif opsi == "2":
            link_pole = input("Masukkan URL grid awal: ")
            update_pole_link(kode_balapan, link_pole)
            isPoleDone = True
        elif opsi == "0":
            isPoleDone = True
            isCancelled = True
        else:
            print("Input salah, silahkan coba lagi")
    return isCancelled


def update_fl_kode_pembalap(kode_balapan, kode_pembalap):
    mydb = db_activator()
    mycursor = mydb.cursor()
    mycursor.execute(QUERY_UPDATE_FL, (kode_pembalap, kode_balapan))
    mydb.commit()
    db_closer(mycursor, mydb)


def update_fl_link(kode_balapan, url_fl):
    tbody = soup_creator(url_fl).find("tbody")
    mydb = db_activator()
    mycursor = mydb.cursor()
    kode_pembalap = (
        tbody.find_all("tr")[0]
        .find_all("td")[2]
        .find("span", class_="tablet:hidden")
        .text
    )
    mycursor.execute(QUERY_UPDATE_FL, (kode_pembalap, kode_balapan))
    mydb.commit()
    db_closer(mycursor, mydb)


def update_fl(kode_balapan):
    print("Anda hendak memperbarui peraih lap tercepat pada " + kode_balapan)
    print(" Terdapat dua opsi cara memperbarui data:")
    print("1. Pembaruan menggunakan kode pembalap")
    print("2. Pembaruan menggunakan URL hasil lap tercepat situs web F1")
    print("0. Keluar (Kembali ke opsi sebelumnya)")
    isFLDone = False
    isCancelled = False
    while not isFLDone:
        opsi = input("Pilihan opsi: ")
        if opsi == "1":
            kode_pembalap = input(
                "Masukkan kode pembalap yang mencetak lap tercepat pada GP "
                + kode_balapan
                + ": "
            )
            update_fl_kode_pembalap(kode_balapan, kode_pembalap)
            isFLDone = True
        elif opsi == "2":
            fl_link = input("Masukkan URL lap tercepat: ")
            update_fl_link(kode_balapan, fl_link)
            isFLDone = True
        elif opsi == "0":
            isFLDone = True
            isCancelled = True
        else:
            print("Input salah, silahkan coba lagi.")
    return isCancelled


def update_sprint(kode_balapan, url_hasil_sprint):
    tbody = soup_creator(url_hasil_sprint).find("tbody")
    mydb = db_activator()
    mycursor = mydb.cursor()
    list_tr = tbody.find_all("tr")
    i = 0
    while i < 8:  # HANYA MENYIMPAN PEMBALAP YG DAPAT POIN SPRINT (8 TERATAS)
        list_td = list_tr[i].find_all("td")
        sprint_pos = list_td[0].find("p").text
        if len(sprint_pos) == 1:
            sprint_pos = "0" + sprint_pos
        kode_pembalap = list_td[2].find("span", class_="tablet:hidden").text
        val = (sprint_pos, kode_pembalap, kode_balapan)
        mycursor.execute(QUERY_UPDATE_SPRINT, val)
        mydb.commit()
        i += 1
    db_closer(mycursor, mydb)


if __name__ == "__main__":
    kode_balapan = input("Masukkan kode balapan: ")
    isDone = False
    while not isDone:
        print("Anda hendak melakukan pembaruan pada GP " + kode_balapan)
        print("Pembaruan apa yang hendak anda lakukan?")
        print("1. Pembaruan hasil balapan")
        print("2. Pembaruan peraih posisi pole")
        print("3. Pembaruan pencetak lap tercepat")
        print("4. Pembaruan hasil sprint")
        print("5. Pembaruan keseluruhan")
        opsi = input(
            "Silahkan masukkan kode (1, 2, 3) dari pembaruan yang ingin dilakukan: "
        )
        if opsi == "1":
            race_link = input("Masukkan URL hasil balapan: ")
            update_hasil(kode_balapan, race_link)
            isDone = True
        elif opsi == "2":
            temp_result = update_pole(kode_balapan)
            isDone = not temp_result
        elif opsi == "3":
            temp_result = update_fl(kode_balapan)
            isDone = not temp_result
        elif opsi == "4":
            sprint_link = input("Masukkan URL hasil sprint: ")
            update_sprint(kode_balapan, sprint_link)
            isDone = True
        elif opsi == "5":
            update_all(kode_balapan)
            isDone = True
        else:
            print("Input salah, silahkan coba lagi.")
