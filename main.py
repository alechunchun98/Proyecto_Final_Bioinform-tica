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

def movimiento_archivos():
    """Crea un directorio y mueve los archivos resultado a este directorio
    """
    nombre_directorio = input("Introduzca el nombre del directorio para guardar los archivos: ")
    try : 
        os.mkdir(nombre_directorio)
    except FileExistsError:
        print("El nombre del archivo ya existe")
        movimiento_archivos()
    except:
        print("Ha ocurrido un error crear el directorio para guardar los archivos")
    
    try:    
        shutil.move("query_paquete.fasta", nombre_directorio)
        shutil.move("subject.fasta", nombre_directorio)
        shutil.move("blast_result", nombre_directorio)
        shutil.move("blast_hits.fasta", nombre_directorio)
        shutil.move("allingment.fasta", nombre_directorio)
        shutil.move("Árbol.phy", nombre_directorio)
        shutil.move("domain_prosite", nombre_directorio)
    except:
        print("Ha ocurrido un error al mover los archivos")
        

def main():
    
    input_queries= input("Introduzca el archivo donde tiene las queries: ")
    
    with open(input_queries,"r") as input_handle:
        for record in SeqIO.parse(input_handle, "fasta"):
            nombre=str(record.name)
            sequence=str(record.seq)
            with open("query_paquete.fasta","w") as output_handle:
                output_handle.write(">"+nombre+"\n"+sequence+"\n")
    
            blaster.Conversor()
            
            blaster.blast()
            
            alligntree.pre_allign()
            
            alligntree.Muscle()
            
            alligntree.Filo()
            
            prositedoc.dataparse()
            
            movimiento_archivos()
            
            print("\n Se acaba de completar una query \n")
    
#------COMIENZO DE EJECUCIÓN -------

intro()

Actuar = input("""Elija la acción que quiere realizar: 
                 1 . Ayuda
                 2 . Funcionamiento
                 3 . Ejecutar el paquete
                 > """)   
if Actuar == "1":
    print("""El paquete usa un archivo fasta donde se encuentran las queries
          La base de Datos puede tener extensiones .gb .gbff .fasta
          Asegúrese de tener instalados los paquetes Bio , Bio.ExPASy , ete3
          """)
elif Actuar == "2":
    print(""" El paquete requiere de un archivo de Bases de Datos de proteínas y un archivo fasta con ls queries.
          Utiliza tres módulos llamados blaster, alligntree y prositedoc
          blaster: parsea la base de datos en busca de las secuencias y realiza un blastp
          alligntree: hace un alineamiento con los hits y luego un árbol filogenético
          prositedoc: Busca en las base de datos de prosite dominios de proteínas
          """)
    

elif Actuar == "3":    
    if __name__ == "__main__":
        main()
        print("Ha terminado la ejecución")
    else:
        print("No se encuentra ejecutando el paquete desde main")
else:
    print("Introduzca un número válido")