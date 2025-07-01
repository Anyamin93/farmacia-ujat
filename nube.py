from pyairtable.orm import Model
from pyairtable.orm import fields as F
# api = Api("patZ5sBuu9dTkmFIF.b3d039f74edf64dff74ba8584c30a35c0cb571c7a0b54dab7d6415de8437659c")#clave de acceso
# table = api.table("apptDDJ9LFD0VB3Jt", "receta")

# medicamento = {
#     "medicamento" : "Amlodipino",
#     "interacciones" : "Evitar picante y gaseosas"
# }

# table.create(medicamento)
# datos = table.all()

# for d in datos:
#     print(d['fields'])

class Receta(Model):
    medicamento = F.TextField("medicamento")
    interacciones = F.TextField("interacciones")
    class Meta:
        api_key = "patZ5sBuu9dTkmFIF.b3d039f74edf64dff74ba8584c30a35c0cb571c7a0b54dab7d6415de8437659c"
        base_id = "apptDDJ9LFD0VB3Jt"
        table_name = "receta"

