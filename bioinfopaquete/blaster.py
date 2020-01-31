# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:07:02 2020

@author: alech
"""


from subprocess import Popen, PIPE

from Bio import SeqIO

#--Generación de una archivo que sirva como subject a partir de un GeneBank--

def Conversor(input_genbank):

    with open(input_genbank, "r") as input_handle, open("subject.fasta", "w") as output_handle:
        for record in SeqIO.parse(input_handle, "genbank"):
            print()
        for feature in record.features:
            try:
                if feature.type == 'CDS':
                    output_handle.write(">"+feature.qualifiers['locus_tag'][0]+"\n"+feature.qualifiers['translation'][0]+"\n")
            except:
                try:
                    print("Hay un CDS sin secuencia:"+feature.qualifiers['locus_tag'][0])
                except:
                    print("Hay una Secuencia sin nombre del locus:"+feature.qualifiers['translation'][0])
    print("\nHa terminado de parsearse la base de datos \n")            
                
#--Realización del Blastp--

def blast(Contador):
    """Manda a la terminal el comando necesario para realizar el blast
    """    
    
    proceso = Popen(['blastp','-query',"query_paquete{}.fasta".format(Contador),'-subject',"subject.fasta",'-outfmt',"6" ], stdout=PIPE, stderr=PIPE)
    error_encontrado = proceso.stderr.read()
    listado = proceso.stdout.read()
    
    
    proceso.stderr.close()
    proceso.stdout.close()
    
    with open("blast_result{}".format(Contador),"w") as file:
        file.write("Sequence_ID\tSubject_ID\tpident\tlength\tmismatch\tgaps\tstart\tend\tStartinSubj\tEndinSubj\tevalue\tbitscore\n")
        file.write(listado.decode('utf-8'))
    
    if not error_encontrado: 
        pass 
    else: 
        print("Se produjo el siguiente error:\n%s" % error_encontrado)                
    
    print("Blastp finalizado")
                

                    
                    
                    
