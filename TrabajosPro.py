### Librerias necesarias para el codigo
import os
import time

from U_Profile import C_Profile
from User import Client
from Location import Location

from Worker import Worker
from W_Profile import W_Profile
from Job_Title import Job_Title

from Ad import Ad
from Job_IP import Job_IP
from Browsing_Page import Browsing_Page

from Response import C_Response, W_Response
from Payment import Payment
from Score import Score ###FALTA!!!!!

from Records import C_Records, W_Records
from Help import Help
from Verification import C_Verification, W_Verification


def Modo_Usuario():
    print('Tipo de Usuario')
    print('1. Cliente')
    print('2. Trabajador')
    print('3. Administrador')
    print('0. FIN')

def Principal_Cliente():
    print('----Menú----')
    print('1. Perfil')
    print('2. Contratar Servicio')
    print('3. Trabajos en Proceso')
    print('4. Ayuda')
    print('0. FIN')
    
def Principal_Trabajador():
    print('----Menú----')
    print('1. Perfil')
    print('2. Explorar Solicitudes')
    print('3. Trabajos en Proceso')
    print('4. Historial')
    print('5. Ayuda')
    print('0. FIN')

def Menu_Actualizar():
    print('----Estado----')
    print('1. Estás en camino')
    print('2. Has llegado a destino')
    print('3. El trabajo está siendo realizado')
    print('4. Trabajo finalizado')

def Registro():
    print('---TrabajosPro---')
    print('1. Iniciar Sesión')
    print('2. Registrarse')
    print('0. Salir')

def Categorias_Menu():
    print('Áreas de trabajo')
    print('1. Fontanería')
    print('2. Carpintería')
    print('3. Electricidad')
    print('4. Jardinería')

def Certificaciones_Menu():
    print('¿Tiene una certificación en esta área?')
    print('1. Sí')
    print('2. No')

def Contratar_Menu():
    print('Contrata un servicio')
    print('1. Crear una solicitud')
    print('2. Gestionar respuestas')

def Administrador_Menu():
    print('1. Ver pagos realizados')
    print('2. Ganancia total')
    print('0. FIN')
    

    
### VARIABLES
op=opc=opr=oprt=opt=cs=cert=' '
t=False
loginT=loginC=False
active_ad=False

ClaveAdmin='trabajospro123'

while op!='0':
    os.system('cls')
    Modo_Usuario()
    op=input('Ingrese el tipo de usuario: ')
    opc=opr=opt=' '

# # # APLICACION DEL CLIENTE # # # 
    if op=='1':
        os.system('cls')
        while loginC==False and opr!='0':
            Registro()
            opr=input('Ingrese una opción: ')
            if opr=='1':
                os.system('cls')
                print('--Iniciar Sesión--')
                mail=input('Correo electrónico: ')
                password=input('Contraseña: ')
                c_ver=C_Verification(mail,password)
                aux=c_ver.verificacion()
                c_prof=C_Profile(aux[0],aux[1],aux[2],aux[3],aux[4],aux[5],aux[6])
            if opr=='2':
                os.system('cls')
                print('--Registro--')
                user=Client('0','0','0','0','0','0')
                user.registro()
                nombre=user.get_Nombre
                password=user.get_Contrasena
                sexo=user.get_Sexo
                edad=user.get_Edad
                mail=user.get_Mail
                telf=user.get_Telefono
                c_prof=C_Profile(nombre,password,sexo,edad,mail,telf,'')
                c_prof.archivos()
                loginC=True
        
        while opc!='0' and loginC==True:
            
            os.system('cls')
            Principal_Cliente()
            opc=input('Ingrese una opción: ')

            if opc=='1':
                os.system('cls')
                c_prof.perfil()
                prof_C=' '
                while prof_C!='0':
                    print('1. Editar ubicaciones')
                    print('2. Cerrar sesión')
                    print('0. Salir')
                    prof_C=input('Ingrese una opción: ')
                    if prof_C=='1':
                        ubicacion=Location()
                        ubi=input('Ingrese la ubicación: ')
                        ubicacion.add_location(ubi)
                        ubi=ubicacion.get_location
                        c_prof.set_Ubicacion(ubi)
                    elif prof_C=='2':
                        loginC=False
                    else:
                        print('Ingrese una opción válida')

                
            elif opc=='2':
                os.system('cls')
                contract=' '
                while contract!='0':
                    Contratar_Menu()
                    contract=input('Ingrese una opción: ')
                    if contract=='1':
                        nombre=c_prof.get_Nombre()
                        ad=Ad('0',nombre,'0','0','0','0')
                        ad.generate_code()
                        ad.hire_menu()
                        x=ad.lista()
                        ad.archivo_ad(x)
                        active_ad=True
                    elif contract=='2':
                        if active_ad==True:
                            code=ad.get_code
                            responseC=C_Response(code)
                            respuestas=responseC.cargar_respuestas()
                            print('El siguiente trabajador respondió a su solicitud: ')
                            print(f'Nombre: {respuestas[0]} \nÁrea de especialidad: {respuestas[1]} \nCalificación: {respuestas[2]}')
                            t=True
                            name=c_prof.get_Nombre
                            job_ip=Job_IP(code,respuestas[1],name,respuestas[0],'0')
                    else:
                        print('Error: Ingrese una opción válida')
                

            elif opc=='3':
                os.system('cls')
                cs=' '
                print('Trabajos en proceso')
                if t==False:
                    print('No tiene ningún trabajo en proceso')
                else:
                    code=job_ip.get_code()
                    print(f'Trabajo #{code}')
                    type=job_ip.get_type()                    
                    print(type)
                    while cs!='0':
                        print('1. Ver estado')
                        print('0. Salir')
                        cs=input('Ingrese una opción: ')
                        if cs=='1':
                            trabajo=job_ip.comunicacion()
                            job_ip.set_state(trabajo[4])
                            print('\n')
                            job_ip.state_cliente()
                            print('\n')
                        else:
                            print('Ingrese una opción válida')
                    if job_ip.get_state()=='4':
                        name=job_ip.get_w_name()
                        print('--PAGO--')
                        print('Tarifa estándar: Bs 50')
                        print('Si hay un monto extra, ingrese su total a continuación')
                        p=input('Monto extra: ')
                        os.system('cls')
                        print('TOTAL A PAGAR')
                        print('Tarifa estándar: Bs. 50')
                        print(f'Extras: {p}')
                        p=50+int(p)
                        p=str(p)
                        print(f'Total: {p})')
                        pay=Payment(code,name,p)
                        pay.set_date()
                        pay.ganancia()
                        pay.archivos()
                        print('--Califique el trabajo--')
                        calificacion=input('Evalúe el trabajo realizado del 1 al 5: ')
                        score=Score(name,calificacion)
                        #####CALIFICACION!!!!!!! VER COMO COMUNICARLOS
                        code=job_ip.get_code()
                        type=job_ip.get_type()
                        c_name=job_ip.get_c_name()
                        w_name=job_ip.get_w_name()
                        payment=pay.get_pay()
                        s=score.get_score()
                        finished_job=C_Records(code,type,c_name,w_name,payment,s)
                        t=False
                            
            elif opc=='4':
                os.system('cls')
                print('---Ayuda---')
                name=c_prof.get_Nombre()
                text=input('Ingrese su problema o sugerencia')
                ayuda=Help(name,'cliente',text)
                ayuda.archivo()

            else:
                os.system('cls')
                print('Ingrese una opción válida')

 
# # # APLICACION DEL TRABAJADOR # # # 
    elif op=='2':
        os.system('cls')
        while loginT==False and opr!='0':
            Registro()
            opr=input('Ingrese una opción: ')
            if opr=='1':
                os.system('cls')
                print('--Iniciar Sesión--')
                mail=input('Correo electrónico: ')
                password=input('Contraseña: ')
                t_ver=W_Verification(mail,password)
                aux=t_ver.verificacion()
                t_prof=W_Profile(aux[0],aux[1],aux[2],aux[3],aux[4],aux[5],aux[6],aux[7],aux[8])
            if opr=='2':
                worker=Worker('0','0','0','0','0','0','0')
                worker.registro()
                os.system('cls')
                cert=' '
                titles=Job_Title('0','0')
                
                categoria='' 
                while categoria!='1' and categoria!='2' and categoria!='3' and categoria!='4':
                    Categorias_Menu()
                    categoria=input('Ingrese una opción: ')
                    if categoria!='1' and categoria!='2' and categoria!='3' and categoria!='4':
                        print('Ingresó una opción no válida, vuelva a intentarlo')
                titles.set_categoria(categoria)
                certificacion=' '
                while certificacion!='1' and certificacion!='2':
                    Certificaciones_Menu()
                    certificacion=input('Ingrese una opción: ')
                    if certificacion!='1' and certificacion!='2':
                        print('Ingresó una opción no válida, vuelva a intentarlo')
                titles.set_certificacion(certificacion)
                z=titles.lista()
                nombre=worker.get_nombre()
                password=worker.get_contrasena()
                sexo=worker.get_sexo()
                dni=worker.get_dni()
                edad=worker.get_edad()
                mail=worker.get_mail()
                telf=worker.get_telefono()
                type=titles.get_categoria()
                t_prof=W_Profile(nombre,password,sexo,dni,edad,mail,telf,type,'')
                t_prof.archivos()
                loginT=True

        while opt!='0' and loginT==True:
            os.system('cls')
            Principal_Trabajador()
            opt=input('Ingrese una opción: ')

            if opt=='1':
                os.system('cls')
                t_prof.perfil()
                prof_T=' '
                while prof_T!='0':
                    print('1. Cerrar sesión')
                    print('0. Salir')
                    prof_T=input('Ingrese una opción: ')
                    if prof_T=='1':
                        loginT=False
                    else:
                        print('Ingrese una opción válida')
                
            elif opt=='2':
                os.system('cls')
                type=t_prof.get_categoria()
                browse=Browsing_Page(type) 
                browse.import_ads()
                browse.show_ads()
                selection=browse.select_ad()
                os.system('cls')
                print('Solicitud seleccionada:',selection)
                name=t_prof.get_nombre()
                categoria=t_prof.get_categoria()
                score=t_prof.get_score()
                code=selection[0]
                cliente=selection[5]
                response=W_Response(name,categoria,score,code)
                W_Response.respuesta_archivo()
                job_T=Job_IP(code,type,cliente,name,'0')
                job_T.archivos()
                tw=True


            elif opt=='3':
                os.system('cls')
                cs=' '
                print('Trabajos en proceso')
                if tw==False:
                    print('No tiene ningún trabajo en proceso')
                else:
                    code=job_T.get_code()
                    type=job_T.get_type()
                    print(f'Trabajo #{code}')
                    print(type)
                    while cs!='0':
                        print('1. Actualizar estado')
                        print('0. Salir')
                        cs=input('Ingrese una opción: ')
                        if cs=='1':
                            Menu_Actualizar()
                            act=input('Ingrese una opción: ')
                            if act=='1' or act=='2' or act=='3' or act=='4':
                                job_T.set_state(act)
                                job_T.actualizar()
                            else:
                                print('ERROR: Ingresó una opción no válida')
                        else:
                            print('Ingrese una opción válida')


            elif opt=='4':
                os.system('cls')
                records=W_Records()
                name=t_prof.get_nombre()
                type=t_prof.get_categoria()
                records.historial(name,type)
                print('Historial de Trabajos')
            
            elif opt=='5':
                os.system('cls')
                print('---Ayuda---')
                name=t_prof.get_nombre()
                text=input('Ingrese su problema o sugerencia: ')
                ayuda=Help(name,'trabajador',text)
                ayuda.archivo()
            
            else:
                os.system('cls')
                print('Ingrese una opción válida')

    elif op=='3':
        os.system('cls')
        loginA=False
        cont=0
        while cont<3:
            clave=input('Ingrese la clave: ')
            cont=cont+1
            if clave==ClaveAdmin:
                loginA=True
                cont=3
        if loginA==True:
            g=Payment('','','')
            opA=''
            while opA!='0':
                os.system('cls')
                Administrador_Menu()
                opA=input('Ingrese una opción: ')
                if opA=='1':
                    g.importar()
                    time.sleep(20)
                elif opA=='2':
                    print('---Ganancia total---')
                    x=g.ganancia_total()
                    print(f'Ganancia={x}')
                    time.sleep(10)

        
    else:
        os.system('cls')
        print('Ingrese una opción válida')