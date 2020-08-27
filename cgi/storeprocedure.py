
#!"C:\Python38\python.exe"
import cgi, cgitb, os, mysql.connector,json
from mysql.connector import Error

print ("Content-type: text/html\n\n")
cnx =  mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='sakila')
cursor=cnx.cursor()
args = ("ACADEMY DINOSAUR", 2006, 6)
cursor.callproc('busqueda', args)
for result in cursor.stored_results():
    print(result.fetchall())
cursor.close()
cnx.close()

def object_decoder(obj):
    if '__type__' in obj and obj['__type__'] == 'Categoria':
        return Categoria(obj['id'], obj['name'])
    return obj

class Categoria(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name