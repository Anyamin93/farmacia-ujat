
import peewee as pw

# Conexión a la base de datos
farmacia_ujat = pw.SqliteDatabase('assets/farmacia_ujat.db')

# Definir la tabla 'farmaco'
class Farmaco(pw.Model):
    nombre = pw.CharField(max_length=255, primary_key=True)
    descripcion = pw.CharField(max_length=255)
    categoria = pw.CharField(max_length=255)
    interacciones = pw.CharField(max_length=5000, null=True)
    class Meta:
        database = farmacia_ujat

# Definir la tabla 'medicamento'
class Medicamento(pw.Model):
    id = pw.IntegerField(primary_key=True) 
    clave = pw.CharField(max_length=255)
    descripcion = pw.CharField(max_length=1000)
    presentacion = pw.CharField(max_length=255)
    clasificacion = pw.CharField(max_length=255)
    nivel_atencion = pw.CharField(max_length=255)
    nombre_farmaco = pw.ForeignKeyField(
        column_name="nombre_farmaco",
        model=Farmaco, 
        field= "nombre",
        null=True
        )
    
    class Meta:
        database = farmacia_ujat
farmacia_ujat.connect()
print("Conexión exitosa")

farmaco = Farmaco.get(Farmaco.nombre == "Acarbosa")
print("Farmaco encontrado:", farmaco.nombre, farmaco.descripcion)

