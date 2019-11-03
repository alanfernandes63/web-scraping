from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup


class Command(BaseCommand):
    def handle(self, *args, **options):
        page = requests.get('https://www.tecmundo.com.br/');
        soap = BeautifulSoup(page.text, 'html.parser')
        container = soap.find_all(class_='tec--list__item')
        for item in container:
            h3 = item.find('h3')
            if h3 != None:
                print(item.find('h3').text)
