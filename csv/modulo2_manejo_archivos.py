'''El Departamento de Recursos Humanos de tu empresa quería que averiguaras cuántas personas había en cada departamento.
 Necesitaba escribir un script en Python que leyera un archivo CSV que contuviera una lista de los empleados de la organización, 
 contara cuántas personas hay en cada departamento y, a continuación, generara un informe con esta información. La salida de este 
 script era un archivo de texto plano. '''


import csv

#Convert employee data to dictionary
def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list

#Process employee data
def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data

#Generate a report
def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
        f.close()