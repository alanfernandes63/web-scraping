from django.shortcuts import render
import sqlite3

# Create your views here.

def home(request):
    connection = sqlite3.Connection('db.sqlite3')
    cursor = connection.cursor()
    list_notices = []

    for item in cursor.execute('SELECT * FROM notices').fetchall():
        list_notices.append(item[0])

    return render(request, 'noticias.html', {'lista': list_notices})
