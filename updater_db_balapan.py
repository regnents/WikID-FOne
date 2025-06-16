from additional_func import db_activator, db_closer, soup_creator, url_fixer

QUERY_INSERT_HASIL_BALAPAN = "INSERT INTO hasil_balapan(kode_pembalap, kode_balapan, posisi, dnf) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE posisi=%s;"
QUERY_UPDATE_POSISI_POLE = (
    "UPDATE hasil_balapan SET pole=TRUE WHERE kode_pembalap=%s AND kode_balapan=%s;"
)
QUERY_UPDATE_FL = (
    "UPDATE hasil_balapan SET fl=TRUE WHERE kode_pembalap=%s AND kode_balapan=%s;"
)
QUERY_UPDATE_SPRINT = "UPDATE hasil_balapan SET posisi_sprint=%s WHERE kode_pembalap=%s AND kode_balapan=%s;"


def update_all():
    kode_balapan = input("Masukkan kode Grand Prix:")
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
        isDNF = False
        if list_td[0].find("p").text == "NC":
            finish_pos = "Ret"
            isDNF = True
        elif list_td[0].find("p").text == "DQ":
            finish_pos = "DSQ"
        elif list_td[0].find("p").text.isnumeric():
            if len(list_td[0].find("p").text) == 1:
                finish_pos = "0" + list_td[0].find("p").text
            else:
                finish_pos = list_td[0].find("p").text
            if list_td[5].find("p").text == "DNF":
                isDNF = True
        else:
            finish_pos = list_td[0].find("p").text
        kode_pembalap = list_td[2].find("span", class_="tablet:hidden").text
        val = (kode_pembalap, kode_balapan, finish_pos, isDNF, finish_pos)

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
    kode_pembalap = (
        tbody.find_all("tr")[0]
        .find_all("td")[2]
        .find("span", class_="tablet:hidden")
        .text
    )
    update_pole_kode_pembalap(kode_balapan, kode_pembalap)


def update_fl_kode_pembalap(kode_balapan, kode_pembalap):
    mydb = db_activator()
    mycursor = mydb.cursor()
    mycursor.execute(QUERY_UPDATE_FL, (kode_pembalap, kode_balapan))
    mydb.commit()
    db_closer(mycursor, mydb)


def update_fl_link(kode_balapan, url_fl):
    tbody = soup_creator(url_fl).find("tbody")
    kode_pembalap = (
        tbody.find_all("tr")[0]
        .find_all("td")[2]
        .find("span", class_="tablet:hidden")
        .text
    )
    update_fl_kode_pembalap(kode_balapan, kode_pembalap)


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
