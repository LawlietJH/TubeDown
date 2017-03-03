# TubeDown
## Descarga videos de YouTube con Python

- - -

### Modo De Uso:

                 TubeDown.py [-l URList.ext][-nr] | [-h]


         -l, --list              Se coloca el nombre del archivo
                                 para obtener la lista de URLs.

         -nr, --norepetir        Se añade este argumento después
                                 de seleccionar el archivo de URLs.

         -h, --help              Muestra el Modo De Uso.



### Ejemplo De Uso:

                   TubeDown.py  -l  xD.zion  -nr

- - -


 * Descargar videos de uno en uno:
 
    - Solo se ejecuta el Script ya sea directamente o desde consola.
        
        ```batch
        TubeDown.py
        ```
 * Descargar una lista de videos:
 
    - Se ejecuta el Script desde consola.
        
        ```batch
        TubeDown.py  -l  URList.txt
        ```
        
 * Descargar una lista de videos y no descargar los ya existentes:
 
    - Se ejecuta el Script desde consola.
        
        ```batch
        TubeDown.py  -l  URList.txt  -nr
        ```
