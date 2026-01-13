from additional_func import db_activator, db_closer, f1r_coltit_color, f1_race_position

RACE_AMOUNT = 24
QUERY_SELECT_HASIL_BALAPAN_TERURUT = """
SELECT balapan.urutan, hasil_balapan.posisi, hasil_balapan.posisi_sprint, hasil_balapan.pole, hasil_balapan.fl, hasil_balapan.dnf
FROM balapan LEFT JOIN hasil_balapan 
ON balapan.kode = hasil_balapan.kode_balapan
AND balapan.musim = hasil_balapan.musim 
WHERE hasil_balapan.kode_pembalap = %s
AND balapan.musim = %s
ORDER BY balapan.urutan;
"""
QUERY_SELECT_BALAPAN_TERURUT = """
SELECT * FROM balapan
WHERE musim = %s
ORDER BY urutan;
"""
QUERY_SELECT_KLASEMEN_TERURUT_POSISI = """
SELECT pembalap.kode, pembalap.nama, pembalap.judul, pembalap.nation, klasemen.poin 
FROM pembalap JOIN klasemen 
ON pembalap.kode=klasemen.kode_pembalap 
WHERE klasemen.musim = %s
ORDER BY klasemen.posisi_klasemen
;
"""
QUERY_SELECT_KLASEMEN_TERURUT_KODE_PEMBALAP = """SELECT * FROM klasemen 
WHERE musim = %s
ORDER BY kode_pembalap;
"""
QUERY_SELECT_HASIL_BALAPAN_SPESIFIK_PEMBALAP_BALAPAN = """
SELECT  posisi, posisi_sprint, pole, fl, dnf
FROM hasil_balapan
WHERE kode_pembalap = %s 
AND kode_balapan = %s 
AND musim = %s;
"""


def creator_f1_drivers_standing():
    musim = input("Masukkan musim yang ingin dibuat: ")
    mydb = db_activator()
    mycursor = mydb.cursor()

    mycursor.execute(QUERY_SELECT_BALAPAN_TERURUT, (musim,))
    list_balapan = mycursor.fetchall()

    text = "<!-- Tolong jangan perbarui templat ini menggunakan {{F1R" + musim + "}} karena dapat menyebabkan artikel [[Formula Satu musim " + musim + ']] melewati batas transklusi artikel dan merusak artikel tersebut -->\n<div style="overflow-x: auto; margin: 1em 0">\n{|\n|\n{|class="wikitable" style="font-size:80%; text-align:center"\n'
    # PENAMBAHAN HEADER ATAS
    text_header = "!{{Abbr|Pos|Posisi}}\n!Pembalap\n"
    for balapan in list_balapan:
        text_header = (
            text_header
            + "![["
            + balapan[2]
            + "|"
            + balapan[0]
            + "]]<br>{{flagicon|"
            + balapan[3]
            + "}}\n"
        )
    text = text + text_header
    text += '!style="position:sticky; right: 0; background-clip: padding-box;"|[[Daftar sistem poin Kejuaraan Dunia Formula Satu|Poin]]\n|-\n'
    # PEMBUATAN ISI TABEL TEMPLAT
    mycursor.execute(QUERY_SELECT_KLASEMEN_TERURUT_POSISI, (musim,))
    list_pembalap = mycursor.fetchall()
    for i in range(len(list_pembalap)):
        text_driver = "! " + str(i + 1) + "\n"
        text_driver = (
            text_driver
            + "| style='text-align:left'|{{flagicon|"
            + list_pembalap[i][3]
            + "}} "
        )
        if list_pembalap[i][2]:
            text_driver = (
                text_driver
                + "[["
                + list_pembalap[i][2]
                + "|"
                + list_pembalap[i][1]
                + "]]\n"
            )
        else:
            text_driver = text_driver + "[[" + list_pembalap[i][1] + "]]\n"
        mycursor.execute(QUERY_SELECT_HASIL_BALAPAN_TERURUT, (list_pembalap[i][0],musim))
        list_hasil_balapan = mycursor.fetchall()
        j = 0
        k = 0
        while j < RACE_AMOUNT:
            text_driver = text_driver + "| "
            if (list_hasil_balapan) and k < len(list_hasil_balapan):
                if j + 1 == list_hasil_balapan[k][0]:
                    pos = list_hasil_balapan[k][1]
                    # REMOVE THE PRECEDING 0 IN BELOW 10 POSITION
                    if pos.isnumeric():
                        pos = str(int(pos))
                    # ADDING THE COLOR OF THE BACKGROUND
                    if pos == "DSQ":
                        text_driver = (
                            text_driver
                            + "style='background-color:#000000; color:white' |"
                        )
                    else:
                        text_driver = text_driver + "bgcolor="
                        text_driver += f1r_coltit_color(pos)
                    if (pos.isnumeric()) and (list_hasil_balapan[k][5]):
                        pos += "\u2020"
                    # CHANGE POS INTO USING F1 RACE POSITION TEMPLATE WHEN NECESSARY
                    if (
                        (list_hasil_balapan[k][2])
                        or (list_hasil_balapan[k][3])
                        or (list_hasil_balapan[k][4])
                    ):
                        pos = f1_race_position(
                            pos,
                            s=list_hasil_balapan[k][2],
                            p=list_hasil_balapan[k][3],
                            f=list_hasil_balapan[k][4],
                        )
                    # ADD INTO THE MAIN text_driver STRING
                    text_driver = text_driver + pos + "\n"
                    k += 1
                else:
                    text_driver = text_driver + "bgcolor= |\n"
            else:
                text_driver = text_driver + "bgcolor= |\n"
            j += 1
        text_driver = (
            text_driver
            + "! style='position:sticky; right: 0; background-clip: padding-box; color: var(--color-base,#202122);'|"
            + str(list_pembalap[i][4])
            + "\n"
        )
        text_driver = text_driver + "|-\n"
        text = text + text_driver
    db_closer(mycursor, mydb)
    # PENAMBAHAN HEADER BAWAH
    text = text + text_header
    text = text + "![[Daftar sistem poin Kejuaraan Dunia Formula Satu|Poin]]\n|-\n"
    # PENAMBAHAN TEKS PELENGKAP
    text_end = """!colspan=27|Sumber:<ref>{{cite web|url= |title= |date= |access-date= |language=en|publisher=Federasi Automobil Internasional}}</ref>
|}
|valign=top|
{{F1 driver results legend 8}}
|}
</div>
'''Catatan:''' 
* {{dagger}}&nbsp;– Pembalap gagal untuk menyelesaikan balapan, tetapi diklasifikasi telah menyelesaikan balapan karena telah menempuh lebih dari 90% jarak tempuh pemenang balapan.<noinclude>
{{pp-template}}
{{reflist}}
[[Kategori:Templat Formula Satu]]</noinclude>
<noinclude>"""
    text = text + text_end
    text = text.replace("Sao", "São")
    # PENYIMPANAN KE DOKUMEN
    with open("drivers_standing.txt", "w", encoding="utf-8") as f:
        f.write(text)
    db_closer(mycursor, mydb)


def creator_f1r():
    musim = input("Masukkan musim yang ingin dibuat: ")
    mydb = db_activator()
    mycursor = mydb.cursor()

    text = "{{safesubst:<noinclude />#switch: {{{1|}}}\n | UPTO = "
    mycursor.execute(QUERY_SELECT_KLASEMEN_TERURUT_KODE_PEMBALAP, (musim,))
    list_pembalap = mycursor.fetchall()

    mycursor.execute(QUERY_SELECT_BALAPAN_TERURUT, (musim,))
    list_balapan = mycursor.fetchall()

    for pembalap in list_pembalap:
        text_driver = (
            "\n\n\n | " + pembalap[0] + " = {{safesubst:<noinclude />#switch: {{{2|}}}\n"
        )
        for balapan in list_balapan:
            mycursor.execute(
                QUERY_SELECT_HASIL_BALAPAN_SPESIFIK_PEMBALAP_BALAPAN,
                (pembalap[0], balapan[0], musim),
            )
            hasil_balapan = mycursor.fetchone()

            # CREATE THE COLTIT FOR BACKGROUND COLOR
            text_coltit = "{{Coltit|"
            if hasil_balapan:
                text_coltit = text_coltit + f1r_coltit_color(hasil_balapan[0])
            text_coltit = text_coltit + "x=}}"

            text_driver = text_driver + " | " + balapan[0] + " = " + text_coltit
            if hasil_balapan:
                pos = hasil_balapan[0] if not hasil_balapan[0].isnumeric() else str(int(hasil_balapan[0]))
                if pos.isnumeric() and hasil_balapan[4]:
                    pos += "\u2020"
                text_driver = text_driver + " " + f1_race_position(pos, s=hasil_balapan[1], p=hasil_balapan[2], f=hasil_balapan[3])
            text_driver = text_driver + "\n"
            text_driver = text_driver + " | " + balapan[0] + "2 = " + text_coltit

            # CREATE THE GRAND PRIX URL FOR DSQ CONDITION
            text_url_gp = ""
            if hasil_balapan and hasil_balapan[0] == "DSQ":
                text_url_gp += (
                    "{{colored link|white|" + balapan[2] + "|" + balapan[0] + "}}"
                )
            else:
                text_url_gp += "[[" + balapan[2] + "|" + balapan[0] + "]]"

            text_driver = text_driver + " " + text_url_gp + "<br />{{small|"
            if hasil_balapan:
                pos = hasil_balapan[0] if not hasil_balapan[0].isnumeric() else str(int(hasil_balapan[0]))
                if pos.isnumeric() and hasil_balapan[4]:
                    pos += "\u2020"
                text_driver += f1_race_position(pos, s=hasil_balapan[1])
            else:
                text_driver += " "
            text_driver = text_driver + "}}\n"
        text_driver += "\n"
        text_driver = text_driver + " | points = " + str(pembalap[1]) + "\n"
        text_driver = (
            text_driver + " | WDC = {{Coltit|x=}} "
        )
        if (pembalap[2]):
            text_driver  += str(int(pembalap[2]))
        text_driver += "\n"
        text_driver = (
            text_driver
            + " | points2 = {{Coltit|x=}} "
            + str(pembalap[1])
            + "\n}}"
        )
        text += text_driver
    text += "\n\n}}<noinclude>\n{{Documentation}}</noinclude>"
    text = text.replace("Sao", "São")
    with open("f1r"+musim+".txt", "w", encoding="utf-8") as f:
        f.write(text)
    db_closer(mycursor, mydb)