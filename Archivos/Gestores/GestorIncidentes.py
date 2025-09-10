import datetime
dicIncidentes = {}
idIncrement = 1


def ListarIncidentes():
    if dicIncidentes:
        for clave,valor in dicIncidentes.items():
            print(f'{clave} - Subject: {valor["subject"]} - Descripcion: {valor["descripcion"]} - User: {valor["user"]} - Fecha Creacion: {valor["fechaCreacion"]} ')   
    else:
        print('No hay incidentes creados')
        
def CrearIncidentes(subject, descripcion,user,fechaCreacion=datetime.datetime.now()):
    global idIncrement
    dicIncidentes[idIncrement] = {
        'subject': subject,
        'descripcion': descripcion,
        'user': user,
        'fechaCreacion': fechaCreacion
    }
    print(f'Incidente {idIncrement} del usuario {user} fue creado correctamente')
    idIncrement = idIncrement + 1
    
def ModificarIncidentes(id,tipoModificacion, valorModificado):
    if tipoModificacion == '1':
        dicIncidentes[id] = {
        'subject': valorModificado,
        'descripcion': dicIncidentes[id]['descripcion'],
        'user': dicIncidentes[id]['user'],
        'fechaCreacion': dicIncidentes[id]['fechaCreacion'],
        'fechaModificacion': datetime.datetime.now()
        }
        print(f'\nSubject del incidente {id} modificado correctamente\n')
    elif tipoModificacion == '2':
        dicIncidentes[id] = {
        'subject': dicIncidentes[id]['subject'],
        'descripcion': valorModificado,
        'user': dicIncidentes[id]['user'],
        'fechaCreacion': dicIncidentes[id]['fechaCreacion'],
        'fechaModificacion': datetime.datetime.now()
        }
        print(f'\nDescripcion del incidente {id} modificado correctamente\n')
    elif tipoModificacion == '3':
        dicIncidentes[id] = {
        'subject': dicIncidentes[id]['subject'],
        'descripcion': dicIncidentes[id]['descripcion'],
        'user': valorModificado,
        'fechaCreacion': dicIncidentes[id]['fechaCreacion'],
        'fechaModificacion': datetime.datetime.now()
        }
        print(f'\nUsuario del incidente {id} modificado correctamente\n')

def EliminarIncidentes(id):
    del dicIncidentes[id]
    print(f'El incidente {id} fue eliminado correctamente')

def ValidarIncidente(id):
    if id in dicIncidentes:
        return True
    else:
        return False