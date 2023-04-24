import serial, time


class arduino():
    conexion = ""
    
    def __init__(self, conexion):
        self.conexion = serial.Serial(conexion,9600, timeout=1)

    def moverServo(self, color):
        # print('hola')
        (self.conexion).write("3:{}".format(color).encode('ascii'))
        print("\nEl servomotor se movio al color {}\n".format(color))
        time.sleep(2)
        
        
    def consultar_servo(self):
        (self.conexion).write("2".encode('ascii'))
        time.sleep(2)
        color = self.puerto()
        return color
            
    def puerto(self):
        # (self.conexion).write(str(self.conexion).encode())
        linea = (self.conexion).readline()
        return linea.decode('utf-8').strip()
    
    def cambiar_modo(self, modo):
        # print('hola')
        (self.conexion).write("1:{}".format(modo).encode('ascii'))
        # print("\nEl servomotor se movio al color {}\n".format(color))
        time.sleep(2)
        
    def cerrar(self):
        self.conexion.close()
        print("Se cerro la conexion con arduino")
    
        
        

