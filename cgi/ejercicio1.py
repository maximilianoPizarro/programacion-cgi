#!"C:\Python38\python.exe"
import cgi, cgitb, os 
print ("Content-type: text/html\n\n");
print ("<html>");
print ("<head>");
print ("<meta name='author' content='Maximiliano Pizarro'>");
print("<style>table, th, td { border: 1px solid black; border-collapse: collapse;}th, td { padding: 15px; text-align: left;}#t01 { width: 100%; background-color: #f1f1c1;}</style>")
print("<body>");
try:
    form = cgi.FieldStorage() 
    print ("<table style='width:100%'>");
    print ("<tr><th>Variable</th><th>Valor</th></tr>");
    for param in form.keys():
        print( "<tr><td><b>%20s</b></td> <td>%s</td></tr>" % (param, os.environ[param]))
    print("</table>");
except:
    print("Server Internal Error");
print("</body>");
print("</html>");   