class ManejadorCliente(object):



    def  agregar(self, nombre, telefono, nit):
        consulta = "INSERT INTO Cliente(nombre, telefono, nit) VALUES('"+nombre+"',"+telefono+","+nit+");"
        print(consulta)

print("hellos")