# TubeDown
## Descarga videos de YouTube con Python

### Modo De Uso:

                 TubeDown.py [-l URList.ext][-nr] | [-h]


         -l, --list              Se coloca el nombre del archivo
                                 para obtener la lista de URLs.

         -nr, --norepetir        Se añade este argumento después
                                 de seleccionar el archivo de URLs.

         -h, --help              Muestra el Modo De Uso.


- - -


 * ___Descargar videos de uno en uno:___
 
    - Solo se ejecuta el _Script_ ya sea directamente o desde consola.
        
        ```batch
        TubeDown.py
        ```
 * ___Descargar una lista de videos:___
 
    - Se ejecuta el _Script_ desde consola.
        
        ```batch
        TubeDown.py  -l  URList.txt
        ```
        
 * ___Descargar una lista de videos y no descargar los ya existentes:___
 
    - Se ejecuta el _Script_ desde consola.
        
        ```batch
        TubeDown.py  -l  URList.txt  -nr
        ```

- - -

### Ejemplo De Uso:

```batch
                      TubeDown.py  -l  xD.zion  -nr
```
