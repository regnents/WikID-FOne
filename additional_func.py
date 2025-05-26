import mysql.connector
import os
import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from dotenv import load_dotenv

load_dotenv()
DB_HOST = os.getenv('host')
DB_USER = os.getenv('user')
DB_PASS = os.getenv('password')
DB_NAME = os.getenv('database')

def db_activator():
    mydb = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME
    )
    return mydb

def db_closer(cursor, db):
    cursor.close()
    db.close()

def soup_creator(link: str):
    req = Request(
        link,
        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0; RSP/rafaelseanputra@gmail.com"
        },
    )
    with urlopen(req) as page:
        soup = BeautifulSoup(page.read(), "html.parser")
    return soup

def url_fixer(url, option):
    new_url = re.sub("race-result|fastest-laps|starting-grid|sprint-results","", url)
    if option == 1:
        return (new_url + "race-result")
    elif option == 2:
        return (new_url + "sprint-results")
    elif option == 3:
        return (new_url + "starting-grid")
    elif option == 4:
        return (new_url + "fastest-laps")
    else:
        return new_url

def f1r_coltit_color(pos: str):
    if pos.isnumeric():
        temp = int(pos)
        if temp == 1:
            return "FFFFBF|"
        elif temp == 2:
            return "DFDFDF|"
        elif temp == 3:
            return "FFDF9F|"
        elif temp > 3 and temp <= 10:
            return "DFFFDF|"
        elif temp > 10:
            return "CFCFFF|"
    elif pos == "NC":
        return "CFCFFF|"
    elif pos == "Ret":
        return "EFCFFF|"
    elif pos == "DNQ":
        return "FFCFCF|"
    elif pos == "DSQ":
        return "000|FFF|"
    else:
        return "FFFFFF|"

def f1_race_position(pos, s= None, p = None, f = None):
    if s or p or f:
        text = "{{F1 race position|" + pos
        if s:
            text += ("|s|" + str(int(s)))
        if p:
            text += "|p"
        if f:
            text += "|f"
        text += "}}"
        return text
    else:
        return pos 
