
#!"C:\Python38\python.exe"

import cgi, cgitb
import os, mysql.connector,json
from mysql.connector import Error
from types import SimpleNamespace as Namespace
cgitb.enable()

print ("Content-type: text/html\n\n");
print ("<html>");
print ("<head>");
print ("<meta name='author' content='Maximiliano Pizarro'>");
print ("<link href='/xampp/xampp.css' rel='stylesheet' type='text/css'>");
print ("</head>");
print("<body>");        
 
def Convert(tup, di): 
    di = dict(tup) 
    return di 

cnx =  mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='sakila')
cursor = cnx.cursor()
cursor.execute("select name as categorias from category")
resultados=cursor.fetchmany(size =16)
#dictionary = {} 
#print (json.dumps(Convert(resultados, dictionary)))
print("<label for='categorias'>Categorias:</label>")

for row in resultados:
    x = json.loads(json.dumps(row), object_hook=lambda d: Namespace(**d))    
    print ("<option value='id'>"% x)
    print (x)
    print ("</option>")
print("</select>")    

cursor.close()
cnx.close()    

print("</body>");
print("</html>");   

