import mysql.connector
con = mysql.connector.connect(host ="localhost", username = "root", password = "ayush22001", database = "school")
if con.is_connected:
    print("sucessfully connected")

cursr = con.cursor()
print("sucessfully curser created") 

# cursr.execute("create database abc;")
# print("created sucessfully")


cursr.execute("insert  into info values(3,'akash','akash@gmail.com','Palampur','985525414'); ")
con.commit()
print("data save sucessfully in data base:::")