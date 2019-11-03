from django.core.management.base import BaseCommand
import requests
import sqlite3
from bs4 import BeautifulSoup
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        page = requests.get('https://www.tecmundo.com.br/');
        soap = BeautifulSoup(page.text, 'html.parser')
        container = soap.find_all(class_='tec--list__item')
        self.create_table()
        connection = sqlite3.Connection('db.sqlite3')
        cursor = connection.cursor()
        #cursor.execute('drop table notices')
        lista = []
        # pega os titulos transforma em tuplas e adiciona a lista
        for item in container:
            h3 = item.find('h3')
            if h3 is not None:
                lista.append((item.find('h3').text,))

        #print(cursor.execute('SELECT * FROM notices').fetchall())

        #self.insert_data(lista)
        print(cursor.execute("SELECT * FROM notices").fetchall())

    def create_table(self):

        connection = sqlite3.Connection('db.sqlite3')
        cursor = connection.cursor()

        exist_table = cursor.execute('''SELECT * FROM sqlite_master WHERE type='table';''')

        # se não existir tabela a tabela notices é  criada
        if exist_table.fetchone() is None:
            cursor.execute('''CREATE TABLE notices (title text)''')
            cursor.close()
            connection.close()


    def insert_data(self, data):
        connection = sqlite3.Connection('db.sqlite3')
        cursor = connection.cursor()
        print(data)
        #print(tuple('a'))
        cursor.executemany('INSERT INTO notices VALUES (?)', data)
        #cursor.execute(f'''INSERT INTO notices(title) VALUES ('{data}')''')
        #print(cursor.execute('SELECT * FROM notices').fetchone())
        cursor.close()
        connection.commit()
        connection.close()



