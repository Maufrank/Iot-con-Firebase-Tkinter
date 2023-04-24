from datetime import datetime
import mysql.connector


class basedatos():
    conexion = ""
    
    def __init__(self):
    # conexion = mysql.connector.connect(host="localhost", user="root", passwd="", database="prueba")
        # self.conexion = mysql.connector.connect(host="localhost", user="root", passwd="", database="prueba")
        self.conexion = mysql.connector.connect(host="localhost", user="root", passwd="", database="raiot")

    def insertar_registro(self,rojo, verde, azul, color):
        hoy = datetime.now()
        fecha = hoy.date()
        hoy = datetime.now()
        hora = hoy.strftime("%H-%M-%S")
        instruccion = '''INSERT INTO registros (rojo, verde, azul, color, fecha, hora) VALUES ({}, {}, {}, "{}", "{}", "{}");
        '''.format(rojo, verde, azul, color, fecha, hora)
        consulta = self.conexion.cursor()
        consulta.execute(instruccion)
        n = consulta.rowcount
        self.conexion.commit()
        consulta.close()
        return n

    # def consultar(self):
    #     instruccion = "SELECT * FROM registros"
    #     consulta = self.conexion.cursor()
    #     consulta.execute(instruccion)
    #     resultado = ""
    #     resultado = "idRe\trojo\tverde\tazul\tcolor\tfecha\t\thora\n"
    #     print("idRe\trojo\tverde\tazul\tcolor\tfecha\t\thora\n")
    #     for (idRegistro, rojo, verde, azul, color, fecha, hora) in consulta:
    #         resultado += "\n{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(idRegistro, rojo, verde, azul, color, fecha, hora)
    #     consulta.close()
    #     return resultado
    
    # def consultar(self):
    #     instruccion = "SELECT * FROM registros ORDER BY idRegistro DESC LIMIT 10;"
    #     consulta = self.conexion.cursor()
    #     consulta.execute(instruccion)
    #     # resultado = ""
    #     resultado = "idRe\tcolor\tfecha\t\thora\n"
    #     # print("idRe\trojo\tverde\tazul\tcolor\tfecha\t\thora\n")
    #     for (idRegistro, rojo, verde, azul, color, fecha, hora) in consulta:
    #         resultado += "{}\t{}\t{}\t{}\n".format(idRegistro, color, fecha, hora)
    #     consulta.close()
    #     return resultado
    
    def filtro(self, color):
        instruccion = f"SELECT * FROM registros ORDER BY idRegistro DESC LIMIT 10 where color = {color};"
        consulta = self.conexion.cursor()
        consulta.execute(instruccion)
        # resultado = ""
        resultado = "idRe\tcolor\tfecha\t\thora\n"
        # print("idRe\trojo\tverde\tazul\tcolor\tfecha\t\thora\n")
        for (idRegistro, rojo, verde, azul, color, fecha, hora) in consulta:
            resultado += "{}\t{}\t{}\t{}\n".format(idRegistro, color, fecha, hora)
        consulta.close()
        return resultado
    
    def cerrar_conexion(self):
        self.conexion.close()
        print("Conexion con la bd terminada")

    def consultar(self):
        instruccion = "SELECT * FROM registros ORDER BY idRegistro ASC;"
        consulta = self.conexion.cursor()
        consulta.execute(instruccion)
        resultado = []
        # resultado = "idRe\tcolor\tfecha\t\thora\n"
        # print("idRe\trojo\tverde\tazul\tcolor\tfecha\t\thora\n")
        datos = consulta
        for (idRegistro, rojo, verde, azul, color, fecha, hora) in consulta:
            resultado.append([idRegistro, color, fecha, hora])
        consulta.close()
        return resultado