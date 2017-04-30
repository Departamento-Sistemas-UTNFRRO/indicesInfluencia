# indicesInfluencia
Script Python para, dado un conjunto de tweets, obtener los más influyentes en base a las siguientes variables:

- Cantidad de retweets
- Cantidad de favoritos
- Cantidad de seguidores del usuario
- Cantidad de seguidos del usuario
- Cantidad de tweets del usuario

## Requisitos (Windows 64-bit)

- Python 3.6: descargar Python 3.6 desde el siguiente link: https://www.python.org/ftp/python/3.6.1/python-3.6.1-amd64.exe . Al finalizar, realizar la instalación siguiendo el asistente. **Seleccionar opción Add Python 3.6 to PATH.**. Para testear la instalación, abrir una consola de comandos y ejecutar *python --version*.
- Miniconda: descargar Minicoda desde el siguiente link: https://repo.continuum.io/miniconda/Miniconda3-latest-Windows-x86_64.exe . Al finalizar, realizar la instalación siguiendo el asistente. Para testear la instalación, abrir una consola de comandos y ejecutar *conda list*. (Más información en: https://conda.io/docs/install/quick.html)
- Librerías: abrir la consola de comandos y ejecutar los siguientes para instalar las librerías necesarias:
  - *conda install pandas*
  - *conda install numpy*
  - *conda install scikit-learn*
  
  ### Notas
  - Para abrir la consola de comandos: presionar tecla Windows + R, en el diálogo escribir *cmd* y hacer click en Aceptar.
  - Al instalar las librerías, cuando aparezca la pregunta *Proceed? (y/n)* deberá seleccionar *y*.
 
 ## Descargar y ejecutar
 
 - Descargar el programa como .zip ingresando al siguiente link: https://github.com/Departamento-Sistemas-UTNFRRO/indicesInfluencia , haciendo click en el botón Clone or download y luego seleccionando la opción Download ZIP.
 - Descomprimir en C:\ (se creará la carpeta indicesInfluencia-master).
 - Abrir consola de comandos y ejecutar *cd C:\indicesInfluencia-master*
 - Ejecutar *python indices_influencia.py*
  
 ## Datos de entrada y salida
 
 - Entrada: el programa toma como entrada un archivo csv, con un formato y nombres de columnas determinados. Se provee un archivo de muestra llamado **rosariosangra_muestra.csv** que se encuentra en la carpeta *data*. 
 - Cualquier archivo que se desee utilizar como entrada se debe almacenar en la carpeta *data*, debe ser csv y tener el formato adecuado.
 - Salida: los archivos de salida serán almacenados en la carpeta *results*.
 
 ## Utilización
 
 - Mediante la consola, el programa le pedirá ingresar el nombre del archivo a leer sin su extensión (por ejemplo: rosariosangra_muestra).
 - Luego le pedirá ingresar el nombre del archivo con los resultados (por ejemplo: resultados_rosariosangra)
 - Si el archivo fue almacenado con éxito, se mostrará un mensaje.  
 - El programa mostrará mensajes de error si se ingresa un nombre de archivo de entrada inválido o un nombre de archivo de salida que ya existe.



