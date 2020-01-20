# Proyecto_Final_Bioinformatica
Paquete realizado como proyecto final de la asignatura de Bioinformática realizado por Alejandro Moreno Díaz, estudiante de la Universidad Politécnica de Madrid.

Este paquete realiza las siguientes tareas:
- BlastP frente a multitud de secuencias de proteínas obtenidas de genbanks que el
propio usuario aportará, el usuario podrá aportar una o varias proteínas query.
- Una vez obtenidos los hits, las secuencias (hits) serán alineadas y se generará un
árbol filogenético Neighbor-Joining (N-J) usando el programa MUSCLE.
- Búsqueda de dominios de proteínas presentes en la base de datos Prosite mediante
el uso del paquete RE en python, entre los hits de blast obtenidos. Para cada
proteína se indicará el dominio que tiene (name), su accession, descripción y patrón
encontrado según la base de datos de PROSITE.

El programa tiene que estar programado en forma de paquete. Con un script main.py
principal que llame a los diferentes módulos(blaster, alligntree, prositedoc).

El archivo utilizado como query puede tener una o varias secuencias queries.
El archivo utilizado como genebank puede tener las siguientes extensiones: .gb .gbff .fasta

Los resultados generados se almacenan en un directorio cuyo nombre elige el usuario
El paquete genera los siguientes archivos:
  - query_paquete.fasta  : Contiene sólo una query
  - subject.fasta : Contiene las secuencias del genebank
  - blast_result : Contiene los resultados del blast
  - blast_hits.fasta : Contiene las secuencias completas de los hits
  - allingment.fasta : Contiene el alineamiento de las secuencias completas de los hits
  - Árbol.phy: Contiene el árbol generado gracias al alineamiento creado previamente
  - domain_prosite: Contiene información de los dominios encontrados en la base de datos de prosite que corresponden con las secuencias de      los hits.
