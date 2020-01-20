# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:07:02 2020

@author: alech
"""
import warnings

from subprocess import Popen, PIPE

from Bio import SeqIO
from Bio import BiopythonWarning

warnings.simplefilter('ignore', BiopythonWarning)     #Sale un aviso de que cómo hay secuencias que no son múltiplos de 3 puede dar a error, sin embargo tras comprobarlo no afecta

#--Generación de una archivo que sirva como subject a partir de un GeneBank--

def Conversor():
    """Extrae las secuencias de archivos fasta,gb y gbff y las convierte en un fasta para
    posteriormente hacer un blastp
    """
    user_genebank_input = input("Introduzca la base de datos a utilizar: ")
    
    with open(user_genebank_input, "r") as input_handle, open("subject.fasta", "w") as output_handle:
        Comprobación = input_handle.name
        if Comprobación[-5:]=="fasta":
             for record in SeqIO.parse(input_handle, "fasta"):
                 nombre=str(record.description)
                 sequence=str(record.seq)
                 output_handle.write(">"+nombre+"\n"+sequence+"\n")
        else:
                    
            for record in SeqIO.parse(input_handle, "genbank"):
                if Comprobación[-4:]=="gbff":
                
                    for feature in record.features:
                        if feature.type == "CDS" :
            
                               start = feature.location.start
                               end = feature.location.end
                               strand = feature.location.strand
                                                   
                               if strand < 0:
                                   sequence =  record.seq[start:end]
                                   locus = feature.qualifiers['locus_tag'][0]
                                   OC = sequence.reverse_complement()
                                   Cad = str(OC.translate())                        
                                   output_handle.write(">"+locus+"\n"+Cad+"\n")
                                                        
                               else:
                                   sequence =  record.seq[start:end]
                                   locus = feature.qualifiers['locus_tag'][0]
                                   Trad = sequence.translate()
                                   Cad= str(Trad)
                                   output_handle.write(">"+locus+"\n"+Cad+"\n")
                else:
                    nombre=str(record.name)
                    sequence=str(record.seq)
                    output_handle.write(">"+nombre+"\n"+sequence+"\n")
            print("Conversión del gbk a fasta para realizar el blastp finalizado")
            
                
#--Realización del Blastp--

def blast():
    """Manda a la terminal el comando necesario para realizar el blast
    """    
    
    proceso = Popen(['blastp','-query',"query_paquete.fasta",'-subject',"subject.fasta",'-outfmt',"6" ], stdout=PIPE, stderr=PIPE)
    error_encontrado = proceso.stderr.read()
    listado = proceso.stdout.read()
    
    
    proceso.stderr.close()
    proceso.stdout.close()
    
    with open("blast_result","w") as file:
        file.write("Sequence_ID\tSubject_ID\tpident\tlength\tmismatch\tgaps\tstart\tend\tevalue\tbitscore\n")
        file.write(listado.decode('utf-8'))
    
    if not error_encontrado: 
        pass 
    else: 
        print("Se produjo el siguiente error:\n%s" % error_encontrado)                
    
    print("Blastp finalizado")
                

                    
                    
                    
