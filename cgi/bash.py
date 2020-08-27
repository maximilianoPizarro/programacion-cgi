#!C:\Program Files\mysql-shell-8.0.21-windows-x86-64bit\bin\mysqlsh --file
print ("Content-type: text/html\n\n");
print ("<html>");
print ("<head>");
print ("<meta name='author' content='Maximiliano Pizarro'>");
print ("<link href='/xampp/xampp.css' rel='stylesheet' type='text/css'>");
print ("</head>");
print ("<body>&nbsp;<p><h1>GCI con Python");
session = shell.open_session('mysql://root:root@127.0.0.1/sakila?compression=required', 'root')
session.get_session()
print(session)
print("</h1>");
print  ("CGI con Python esta listo ...</body></html>");


