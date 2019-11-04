from django.shortcuts import render
import sqlite3
import json

# Create your views here.

def home(request):
    connection = sqlite3.Connection('db.sqlite3')
    cursor = connection.cursor()
    list_news = []

    for item in cursor.execute('SELECT * FROM notices').fetchall():
        list_news.append(item[0])

    return render(request, 'noticias.html', {'list_news': json.dumps(list_news)})
