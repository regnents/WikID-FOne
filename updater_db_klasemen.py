from additional_func import db_activator, db_closer, soup_creator

STANDING_LINK = "https://www.formula1.com/en/results/2025/drivers"
QUERY_UPDATE_KLASEMEN = "INSERT INTO klasemen(posisi_klasemen, poin, kode_pembalap) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE posisi_klasemen=%s, poin=%s"


def update_all():
    mydb = db_activator()
    mycursor = mydb.cursor()
    tbody = soup_creator(STANDING_LINK).find("tbody")
    for tr in tbody.find_all("tr"):
        list_td = tr.find_all("td")
        posisi = list_td[0].find("p").text
        if len(posisi) == 1:
            posisi = "0" + posisi
        kode_pembalap = list_td[1].find("span", class_="md:hidden").text
        poin = int(list_td[4].find("p").text)
        val = (posisi, poin, kode_pembalap,  posisi, poin)
        mycursor.execute(QUERY_UPDATE_KLASEMEN, val)
        mydb.commit()
    db_closer(mycursor, mydb)


def update_one():
    mydb = db_activator()
    mycursor = mydb.cursor()
    tbody = soup_creator().find("tbody")
    kode_pembalap = input("Masukkan kode pembalap yang ingin datanya diperbarui: ")

    for tr in tbody.find_all("tr"):
        list_td = tr.find_all("td")
        isFound = False
        if not isFound and (
            list_td[1].find("span", class_="md:hidden").text == kode_pembalap
        ):
            posisi = list_td[0].find("p").text
            if len(posisi) == 1:
                posisi = "0" + posisi
            poin = int(list_td[4].find("p").text)
            mycursor.execute(QUERY_UPDATE_KLASEMEN, (posisi, poin, kode_pembalap, posisi, poin))
            mydb.commit()
            if mycursor.rowcount == 0:
                print(
                    "WARNING, "
                    + kode_pembalap
                    + " IS NOT DETECTED IN THE klasemen TABLE, PLEASE UPDATE THE klasemen AND pembalap TABLES FIRST."
                )
            isFound = True
    db_closer(mycursor, mydb)
