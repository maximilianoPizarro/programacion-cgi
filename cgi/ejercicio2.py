#!"C:\Python38\python.exe"
import cgi, cgitb, os, mysql.connector
                                  
class Main():   
    def __init__(self):                                 
        try:            
            print ("Content-type: text/html\n")
            if os.environ['REQUEST_METHOD'] == "GET": 
                self.buscarPelicula()
            if os.environ['REQUEST_METHOD'] == "POST": 
                self.setCategorias()
            if os.environ['REQUEST_METHOD'] == "PUT":           
                self.altaActor()     
        except:
            print("Server Internal Error : request method not allowed");
    def conectar(self):
        try:
            return mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='sakila')
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
    def setCategorias(self):
        cnx=self.conectar()
        cursor = cnx.cursor()
        cursor.callproc('categorias', args=())
        for result in cursor.stored_results():
            resultados=result.fetchall()
            for row in resultados:
                print ("<option value='%d'>%s</option>"%(row[0],row[1]))
        cursor.close()
        cnx.close()
    def buscarPelicula(self):
        print ("<html>");
        print ("<head>");
        print ("<meta name='author' content='Maximiliano Pizarro'>");
        print("<style>table, th, td { border: 1px solid black; border-collapse: collapse;}th, td { padding: 15px; text-align: left;}#t01 { width: 100%; background-color: #f1f1c1;}</style>")
        form = cgi.FieldStorage() 
        cnx=self.conectar()
        cursor = cnx.cursor()
        args = (form.getvalue('titulo'),form.getvalue('anio'),form.getvalue('categoria'))
        cursor.callproc('busqueda', args)
        print ("<table style='width:100%'>");
        print ("<tr><th>ID</th><th>TÍTULO</th><th>AÑO</th><th>ELENCO</th></tr>");
        for result in cursor.stored_results():
            resultados=result.fetchall()
            for row in resultados:
                print( "<tr><td><b>%20s</b></td> <td>%s</td><td>%s</td><td>%s %s</td></tr>" %(row[0],row[1],row[2],row[3],row[4]))
        print("</table>");
        cursor.close()
        cnx.close()
        print("<body>");        
        print("</body>");
        print("</html>"); 
    def altaActor(self):
        print ("<html>");
        print ("<head>");
        print ("<meta name='author' content='Maximiliano Pizarro'>");
        print("<style>table, th, td { border: 1px solid black; border-collapse: collapse;}th, td { padding: 15px; text-align: left;}#t01 { width: 100%; background-color: #f1f1c1;}</style>")
        form = cgi.FieldStorage() 
        print(form["titulo"].value)
        print("<body>");        
        print("</body>");
        print("</html>"); 
if __name__ == "__main__":
    Main()