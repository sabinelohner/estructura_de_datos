import os
NOMBRE_ARCHIVO='job_ip.txt'

job=open(NOMBRE_ARCHIVO, 'w')
job.write("Aceptada 12:00 50 Bs. Cliente 000 Trabajador 111\n")
job.write("Denegado 13:50   -    Cliente 222 Trabajador 111\n")
job.write("Aceptado 14:33 60 Bs. Cliente 333 Trabajador 111\n")
job.write("Denegado 17:00   -    Cliente 555 Trabajador 111\n")
job.write("Aceptado 20:00 75 Bs. Cliente 777 Trabajador 111\n")

job.close()