#El script consiste en que recibe como entradas eventos, de los cuales se obtienen el nombre de las maquinas
#Fechas de inicio de sesion y deslogueo de usuarios

def get_event_date(event):#Esta funcion ordena la lista de eventos por fechas
  return event.date

def current_users(events):
  events.sort(key=get_event_date)#Ordenamos los eventos 
  machines = {}#Creamos un diccionario donde se almacenaran los nombres de las maquinas, junto con los usuarios que se logiaron
  for event in events:
    if event.machine not in machines:#Iteramos la lista de eventos
      machines[event.machine] = set()#Combprobamos si la maquina afectada se encuentra en el evento, sino la agregamos al conjunto
    if event.type == "login":#Añadimos los usuarios a la lista
      machines[event.machine].add(event.user)
    elif event.type == "logout":#Los eliminamos si no estan
       if event.user in machines[event.machine]:
        machines[event.machine].remove(event.user)
      
  return machines#Creamos un diccionario que contiene los nombres de las maquinas como palabra clave y como valor el conjunto de usuarios
#Que estuvieron conectados a esa maquina
def generate_report(machines):#La funcion genera un reporte utilizando como parametro el diccionario que antes hemos creado.
  for machine, users in machines.items():#iteramos el diccionario tanto clave como valor
    if len(users) > 0:#Si la maquina no contiene ningun usuario, es decir ningun usuario conectado no se mostrara en el informe
      user_list = ", ".join(users)#Con los valores del diccionario se crea una lista de usuarios
      print("{}: {}".format(machine, user_list))

class Event:#Creamos una clase evento, que establece los atributos necesarios
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user
#Lista de eventos
events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]
#Se pasa la lista de eventos por la funcion para que los organize y luego se guarda en una variable usuario.
users = current_users(events)
print(users)
#Pasamos la variable usuario a la funcion "generar reporte", con esto obtenemos un reporte de los eventos organizados, por fechasy usuarios conectados
generate_report(users)
