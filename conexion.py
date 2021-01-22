import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="admin",
    db="python"
)

cursor =conn.cursor()

sqlUpdate = "update usuarios set nombre='PRUEBA' where rut = 'de'"
sqlInsert = "insert into usuarios values (%s,%s,%s,%s,%s,%s)"
sqlDel = "delete from usuarios where rut = %s"
#cursor.execute(sqlInsert)
#conn.commit()
#conn.close()

def agregar(datosUs):
    #print("Se agrega un usuario nuevo:")
    cursor.execute(sqlInsert,datosUs)
    
    conn.commit()
    conn.close()
print("Usuario agregado OK")

def actualiza(rut):
    cursor.execute(sqlUpdate)
    conn.commit()
    conn.close()
print("Usuario actualizado")    

def eliminar(rut):
    #print("Se eliminara el usuario")
    cursor.execute(sqlDel,rut)
    conn.commit()
    conn.close()
print("usuarios eliminados")

print = ("Selecciona una opcion: ")
op= int(input("1.- Agregar un usuario, 2.-Actualizar usuario 3.- Elminar usuario : "))

if op == 1:
    nombre = input("Ingresa el nombre: ")
    apepat = input("Ingresa apellido paterno: ")
    apemat = input("Ingresa apellido materno: ")
    rut = input("Ingresa el rut: ")
    edad = int(input("Ingresa edad: "))
    sede = input("Ingresa la sede donde pertence: ")
    datosUs = (nombre,apepat,apemat,rut,edad,sede)
    agregar(datosUs)
elif op == 2:
    rut = input("Ingresa el rut a actualizar: ")
    actualiza(rut)
else:
    rut = input("Ingresa el rut a eliminar: ")
    eliminar(rut)    




