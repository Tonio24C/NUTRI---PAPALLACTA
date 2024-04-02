import mysql.connector

def insertar_datos(nombre, correo, telefono, asunto, mensaje):
    try:
        conexion = mysql.connector.connect(user='root', password='root', 
                                           host='localhost',
                                           database='Nutrillacta',
                                           port='3306')
        cursor = conexion.cursor()
        sql_insert_query = "INSERT INTO tabla (nombre, correo, telefono, asunto, mensaje) VALUES (%s, %s, %s, %s, %s)"
        datos = (nombre, correo, telefono, asunto, mensaje)
        cursor.execute(sql_insert_query, datos)
        conexion.commit()
        print("Datos insertados correctamente")
    except mysql.connector.Error as error:
        print("Error al insertar datos: {}".format(error))
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada")
