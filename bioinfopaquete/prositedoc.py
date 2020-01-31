#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 12:38:39 2020

@author: alex
"""

import re

from Bio.ExPASy import Prosite
from Bio import SeqIO

#--Conversión patterns de Prosite en patterns reconocibles por re--
def correct_pattern(PrePattern):
    """
    Convierte el pattern de prosite para que pueda ser leído por el módulo Re
    """
    PostPattern=PrePattern
    Prosyte=["-",".","x","{","}","(",")","<",">",">]"]
    Re=["","",".","[^","]","{","}","^","$","?$"]
    
    for i in range(len(Re)):
        PostPattern=PostPattern.replace(Prosyte[i],Re[i])      
    
    return PostPattern

#--Parsear dominios de proteínas reconociendo los patterns

def dataparse(Contador):
    """
    Para cada secuencia de los hits, hace una búsqueda de dominios y escribe en domain 
    el nombre, accesion, description y pattern del dominio reconocido
    """
    print("\nEsta parte puede tardar un tiempo, por favor espere")
    
    with open("blast_hits{}.fasta".format(Contador),"r") as input_handle, open ("domain_prosite{}".format(Contador),"w") as output_handle:
        for record in SeqIO.parse(input_handle, "fasta"):
            sequence=str(record.seq)
            output_handle.write("\n" + record.name +"\n"+"\n")
            handle = open("prosite.dat","r")
            records = Prosite.parse(handle)
            for hey in records:
                ozo=str(hey.pattern)                               
                Final=correct_pattern(ozo)
                if re.search(Final, sequence) and Final != "":
                 	output_handle.write("name:"+hey.name+"\n")
                 	output_handle.write("accession:"+hey.accession+"\n")
                 	output_handle.write("description:"+hey.description+"\n")
                 	output_handle.write("pattern:"+Final+"\n"+"\n")
            

