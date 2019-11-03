from django.core.management.base import BaseCommand
import requests
import sqlite3
from bs4 import BeautifulSoup
import json


class Command(BaseCommand):
    def handle(self, *args, **options):

        page = requests.get('https://www.tecmundo.com.br/')

        if page.status_code == 200:
            # faz uma requisição get para pegar toda a página
            soap = BeautifulSoup(page.text, 'html.parser')

            # faz uma busca no conteúdo da página buscando classes css nomeadas por tec--list__item
            container = soap.find_all(class_='tec--list__item')

            self.create_table()

            lista = []

            # pega os titulos transforma em tuplas e adiciona a lista
            for item in container:
                h3 = item.find('h3')
                if h3 is not None:

                    lista.append((item.find('h3').text,))

            self.insert_data(lista)

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

        cursor.executemany('INSERT INTO notices VALUES (?)', data)

        cursor.close()
        connection.commit()
        connection.close()



