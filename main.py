#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 01:58:53 2020

@author: alex
"""
import os
import shutil

from Bio import SeqIO

try:
    from bioinfopaquete import alligntree, blaster,  prositedoc
except:
    print("""NO se han importado correctamente los módulos, asegúrese que están los módulos
            y que los paquetes Bio y ete3 están instalados 
            """)

def intro():
    print("""Este paquete realiza un blastp, una alineamiento y busca información de los dominios de proteínas.
          Requiere de un archivo -query y un -genebank
          Ambos archivos se pedirán como inputs
          """)

def movimiento_archivos(Contador):
    """Crea un directorio y mueve los archivos resultado a este directorio
    """
    nombre_directorio = "Results/Query{}".format(Contador)
    try : 
        os.makedirs(nombre_directorio)
    except FileExistsError:
        print("El nombre del directorio Results ya existe, la ejecución se para")
        exit
    except:
        print("Ha ocurrido un error crear el directorio para guardar los archivos")
        
    try:    
        shutil.move("query_paquete{}.fasta".format(Contador), nombre_directorio)
        shutil.move("blast_result{}".format(Contador), nombre_directorio)
        shutil.move("blast_hits{}.fasta".format(Contador), nombre_directorio)
        shutil.move("allingment{}.fasta".format(Contador), nombre_directorio)
        shutil.move("Árbol{}.phy".format(Contador), nombre_directorio)
        shutil.move("domain_prosite{}".format(Contador), nombre_directorio)
    except:
        print("Ha ocurrido un error al mover los archivos")

def limpieza(input_queries, input_genbank):
    """Crea un directorio de datos donde dejar la query y el genbank, y mete el subject con los Results
    """ 
    try:
        os.mkdir("Data")
    except FileExistsError:
        print("El nombre del directorio ya existe")
        exit
    except:
        print("Ha ocurrido un error crear el directorio para guardar los archivos")
    try:
        shutil.move(input_queries, "Data")
        shutil.move(input_genbank, "Data")
    except:
        print("Ha ocurrido un error al mover la query y el genbank a la carpeta Data")
    try:
        shutil.move("subject.fasta", "Results")
    except:
        print("Ha ocurrido un error al mover el subject")
    
       

def main():
    
    input_queries= input("Introduzca el archivo donde tiene las queries: ")
    input_genbank= input("Introduzca el archivo donde tiene el genbank: ")
    Contador = 1                                        #Hay alguna función que sólo se ejecuta una vez, además sirve para numerar los archivos
    
    with open(input_queries,"r") as input_handle:
        for record in SeqIO.parse(input_handle, "fasta"):
            nombre=str(record.name)
            sequence=str(record.seq)
            with open("query_paquete{}.fasta".format(Contador),"w") as output_handle:
                output_handle.write(">"+nombre+"\n"+sequence+"\n")
            
            if Contador==1:              
                blaster.Conversor(input_genbank)
                
            else:
                pass
        
            blaster.blast(Contador)
            
            alligntree.pre_allign(Contador)
            
            alligntree.Muscle(Contador)
            
            alligntree.Filo(Contador)
            
            prositedoc.dataparse(Contador)
            
            movimiento_archivos(Contador)
                
            Contador +=1
            print("\n Se acaba de completar una query \n")
    limpieza(input_queries,input_genbank)
    
#------COMIENZO DE EJECUCIÓN -------

intro()

Actuar = input("""Elija la acción que quiere realizar: 
                 1 . Ayuda
                 2 . Funcionamiento
                 3 . Ejecutar el paquete
                 > """)   
if Actuar == "1":
    print("""El paquete usa un archivo fasta donde se encuentran las queries
          La base de Datos puede tener extensiones .gbk .gbff 
          Asegúrese de tener instalados los paquetes Bio , Bio.ExPASy , ete3
          Compruebe que el directorio desde donde ejecuta el paquete esté lo más limpio posible de archivos
          Tiene que tener instalado el blast del NCBI y el muscle para usar línea de comandos
          Los directorios creados se basan en Linux con esta barra /
          """)
elif Actuar == "2":
    print(""" El paquete requiere de un archivo de Bases de Datos de proteínas y un archivo fasta con las queries.
          Utiliza tres módulos llamados blaster, alligntree y prositedoc
          blaster: parsea la base de datos en busca de las secuencias y realiza un blastp
          alligntree: hace un alineamiento con los hits y luego un árbol filogenético
          prositedoc: Busca en las base de datos de prosite dominios de proteínas
          Para cada query se crea una carpeta dentro de los resultados
          
          """)
    

elif Actuar == "3":    
    if __name__ == "__main__":
        main()
        print("Ha terminado la ejecución")
    else:
        print("No se encuentra ejecutando el paquete desde main")
else:
    print("Introduzca un número válido")