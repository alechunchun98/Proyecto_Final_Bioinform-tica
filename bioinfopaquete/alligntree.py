# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 22:16:39 2020

@author: alech
"""   

from subprocess import Popen, PIPE

from Bio import SeqIO
from ete3 import Tree

#--Extracción de las secuencias completas de los hits--

def pre_allign():
    """Coge los nombres de los hits y luego busca en el subject la secuencia completa
    """
    with open("blast_result") as file:  #Hacemos una lista con los Subject_ID de los Hits
        data=file.readlines()
        Hits=[]
        for line in data:
            words=line.split()
            Hits.append(words[1])
    
    Def_Hits=Hits[1:len(Hits)]         #El primer Hit es el encabezado Subject_Id
    
    
    with open("subject.fasta", "r") as inp, open("blast_hits.fasta", "w") as out:  #Con los Subject_ID de los Hits hacemos un fasta con las secuencias correspondientes
        for record in SeqIO.parse(inp, "fasta"):
            
            for Hit in Def_Hits:
                if record.name==Hit:
                    name=str(record.name)
                    sequence=str(record.seq)
                    out.write(">"+name+"\n"+sequence+"\n")
                else:
                    pass

#--Alineamineto de las secuencias hits --

def Muscle():
    """Manda a la terminal que realice un alineamiento por muscle con las secuencias completas de los hits
    """
    proceso = Popen(['muscle','-in',"blast_hits.fasta","-out","allingment.fasta"], stdout=PIPE, stderr=PIPE)
    error_encontrado = proceso.stderr.read()
    
    proceso.stderr.close()
    proceso.stdout.close()
  
    if not error_encontrado: 
        pass 
    else: 
        print("Es posible que se hata producido un error al crear el alineamineto")
        Comprobación_allign=input("""Quiere leer el archivo: 
            1. Sí
            2. No
            >""")
        if Comprobación_allign == "1" :
            with open("allingment.fasta") as file:
                for line in file:
                    print(line)
        else:
            pass
            
#--Creación del árbol filogenético--

def Filo():
    """A partir del alineamineto obtenido se crea un árbol por el método neighbor-joining
    """
    proceso = Popen(['muscle','-maketree',"-in","allingment.fasta","-out","Árbol.phy","-cluster","neighborjoining"], stdout=PIPE, stderr=PIPE)
    error_encontrado = proceso.stderr.read()
    
    proceso.stderr.close()
    proceso.stdout.close()
    
    Visualizar=input("""Quiere visualizar el árbol filogenético: 
        1. Sí
        2. No
        > """)
    if Visualizar == "1":
       t=Tree("Árbol.phy")
       print(t)
       
    else:
        pass
   
    if not error_encontrado: 
        pass 
    else: 
        print("\nEs posible que se haya producido un error al crear el árbol filogenético")
        Comprobación_tree=input("""Quiere leer el archivo: 
            1. Sí
            2. No
            >""")
        if Comprobación_tree == "1" :
            with open("Arbol.phy") as file:
                for line in file:
                    print(line)
        else:
            pass
 

        
    