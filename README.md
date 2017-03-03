# TubeDown
## Descarga videos de YouTube con Python


    ████████╗██╗   ██╗██████╗ ███████╗██████╗  ██████╗ ██╗    ██╗███╗   ██╗
    ╚══██╔══╝██║   ██║██╔══██╗██╔════╝██╔══██╗██╔═══██╗██║    ██║████╗  ██║
       ██║   ██║   ██║██████╔╝█████╗  ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║
       ██║   ██║   ██║██╔══██╗██╔══╝  ██║  ██║██║   ██║██║███╗██║██║╚██╗██║
       ██║   ╚██████╔╝██████╔╝███████╗██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║
       ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝


                            ╦  ┌─┐┬ ┬┬  ┬┌─┐┌┬┐╦╦ ╦
                            ║  ├─┤││││  │├┤  │ ║╠═╣
                            ╩═╝┴ ┴└┴┘┴─┘┴└─┘ ┴╚╝╩ ╩


                                     v1.1.7

### Modo De Uso:

                 TubeDown.py [-l URList.ext][-nr] | [-v] | [-h] | [URL]


         -l,  --list             Se coloca el nombre del archivo
                                 para obtener la lista de URLs.

         -nr, --norepetir        Se añade este argumento después
                                 de seleccionar el archivo de URLs.

         -v,  --version          Muestra la versión y autor del Script.


         -h,  --help             Muestra el Modo De Uso.


    https://www.youtube.com/...  Se añade la URL como argumento y
                                 sólo se descargará ese video.

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
        
 * ___Descargar sólo un video:___
 
    - Se ejecuta el _Script_ desde consola.
        
        ```batch
        TubeDown.py  https://www.youtube.com/video_etc...
        ```

        
 * ___Ver el Modo de Uso:___
 
    - Se ejecuta el _Script_ desde consola.
        
        ```batch
        TubeDown.py  -h
        ```

        
 * ___Ver Versión y Autor del Script:___
 
    - Se ejecuta el _Script_ desde consola.
        
        ```batch
        TubeDown.py  -v
        ```

- - -

### Ejemplo De Uso:

```batch
Ejemplo 1 - Lista de URLs:          TubeDown.py  -l  xD.zion  -nr
                      
Ejemplo 2 - De a uno solo:          TubeDown.py  https://www.youtube.com/video_etc...
```
