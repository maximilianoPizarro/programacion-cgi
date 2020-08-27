#!"C:\Python38\python.exe"
import cgitb,subprocess,os
cgitb.enable()



#subprocess.call(cmd, shell=True))
#cmd="mysqlsh c --mysql  mysql://root:root@127.0.0.1/sakila"
cmd="show databases; | mysqlsh --sql --uri  root:root@127.0.0.1/sakila"
cmd1="git --version"
cmd2="python --version"

def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    os.system("echo show databases; | mysqlsh --sql --uri  root:root@127.0.0.1/sakila")
    return proc_stdout



print ("Content-type: text/html\n\n");
print ("<html>");
print ("<head>");
print ("<meta name='author' content='Maximiliano Pizarro'>");
print ("</head>");
print ("<body>&nbsp;<p><h1>");
#os.system("mysqlsh c --mysql  mysql://root:root@127.0.0.1/sakila")

#os.system("echo show databases; | mysqlsh --sql --uri  root:root@127.0.0.1/sakila")
#os.system("\quit")
print (subprocess_cmd(cmd));
print("<br>");
#print (subprocess_cmd(cmd1));
print("<br>");
#print (subprocess_cmd(cmd2));
print("<br>");
print("</h1>");
print  ("CGI con Python esta listo ...</body></html>");