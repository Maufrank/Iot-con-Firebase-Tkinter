from datetime import datetime
import pyrebase

class basedatos():
    datosConexion = {
    "apiKey": "AIzaSyCR8r4Ii4kfENI-AHJsS5xCyaexOBPOmq0",
    "authDomain": "iot-firebase-11286.firebaseapp.com",
    "databaseURL": "https://iot-firebase-11286-default-rtdb.firebaseio.com",
    "projectId": "iot-firebase-11286",
    "storageBucket": "iot-firebase-11286.appspot.com",
    "messagingSenderId": "548653079064",
    "appId": "1:548653079064:web:19b2abbacb59478c20416d"
    };
    conexion = ""
    baseRT = ""
    
    def __init__(self):
        self.conexion = pyrebase.initialize_app(self.datosConexion)
        self.baseRT = self.conexion.database()      
    
    def insertar_registro(self, rojo, verde, azul, color):
        registros = self.baseRT.child("detector").child("registros").order_by_child("idRegistro").get()
        id = len(registros.each()) + 1
        hoy = datetime.now()
        fecha = hoy.date()
        hora = hoy.strftime("%H:%M:%S")
        
        datos = {
        "idRegistro": id,
        "rojo": int(rojo),
        "verde": int(verde),
        "azul": int(azul),
        "color": color,
        "fecha": f"{fecha}",
        "hora": f"{hora}"
        }        
        self.baseRT.child("detector").child("registros").child(f"{fecha}:{hora}").set(datos)
        
        
    def consultar(self, opcion, color):        
        if opcion == "mas":
            registros = self.baseRT.child("detector").child("registros").order_by_child(color).limit_to_first(5).get()
        elif opcion == "menos":
            registros = self.baseRT.child("detector").child("registros").order_by_child(color).limit_to_last(5).get()
        elif opcion == "color":
            registros = self.baseRT.child("detector").child("registros").order_by_child("color").equal_to(color).get()  
        else:
            registros = self.baseRT.child("detector").child("registros").order_by_child("idRegistro").get()            
        data = []
        for registro in registros.each():
            data.append([registro.val()["idRegistro"], registro.val()["color"], registro.val()["rojo"], registro.val()["verde"], 
                         registro.val()["azul"], registro.val()["fecha"], registro.val()["hora"]])            
        return data
    
    