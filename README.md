
# <h1 align=center> **PROYECTO DE `ETL+FASTAPI+DOCKER` EN SERVICIOS DE STREAMING** </h1>

<p align="center">
<img src="https://raw.githubusercontent.com/abhisheknaiidu/abhisheknaiidu/master/code.gif"  height=400>
</p>

<hr>

## **TABLA DE CONTENIDO**  
+ 1-Introducción.  
+ 2-Objetivo de trabajo.  
+ 3-Principales tecnologías utilizadas.  
+ 4-Plan de Acción.  
+ 5-Conclusiones.  

<hr>


## **Introducción**

Hola! 👋 mi nombre es Lucas Maximiliano Seidl y este repositorio contiene mi proyecto individual de Data Engineering de la carrera de Data Science en la academia Henry.

<hr>

## **Objetivo de trabajo**

El proyecto consiste en realizar una ingesta de datos desde diversas fuentes, posteriormente aplicar las transformaciones que consideren pertinentes, y luego disponibilizar los datos limpios para su consulta a través de una API. Esta API deberán construirla en un entorno virtual dockerizado.

Los datos serán provistos en archivos de diferentes extensiones, como *csv* o *json*. Se espera que realicen un EDA para cada dataset y corrijan los tipos de datos, valores nulos y duplicados, entre otras tareas. Posteriormente, tendrán que relacionar los datasets así pueden acceder a su información por medio de consultas a la API.

Las consultas a realizar son:

+ Máxima duración según tipo de film (película/serie), por plataforma y por año:
    El request debe ser: get_max_duration(año, plataforma, [min o season])

+ Cantidad de películas y series (separado) por plataforma
    El request debe ser: get_count_plataform(plataforma)  
  
+ Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.
    El request debe ser: get_listedin('genero')  
    Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 para la plataforma de amazon.

+ Actor que más se repite según plataforma y año.
  El request debe ser: get_actor(plataforma, año).  
  
 <hr>
 
 ## **Principales tecnologías utilizadas**  
 
 + **Python**  
   - Pandas  
   - Numpy  
   - Pathlib  
   - Chardet
   - SqlAlchemy
   - Pymysql  
     
 Python es un lenguaje de programación que te permite trabajar rápidamente e integrar sistemas de manera más efectiva.
  https://docs.python.org/3/   
  
 + **FastApi**  

 FastAPI es un marco web moderno, rápido (de alto rendimiento) para crear API con Python 3.7+ basado en sugerencias de tipo estándar de Python.  
 https://fastapi.tiangolo.com/  
 
 + **Uvicorn**
 
Uvicorn es una implementación de servidor web ASGI para Python.

Hasta hace poco, Python carecía de una interfaz mínima de servidor/aplicación de bajo nivel para marcos asíncronos. La especificación ASGI llena este vacío y significa que ahora podemos comenzar a crear un conjunto común de herramientas utilizables en todos los marcos asíncronos.    
https://www.uvicorn.org/   

+ **MySql**  

MySQL es un sistema de gestión de bases de datos relacional desarrollado bajo licencia dual: Licencia pública general/Licencia comercial por Oracle Corporation.  
https://www.mysql.com/  

<hr>

 ## **Plan de Acción**  
 
 + **Trabajo de ETL con Python y Mysql**  
 
 <p align="center">
<img src="https://miro.medium.com/max/720/1*Mkb6pMXJ7XeZY7fLonG9XA.gif"  height=300>
</p>   

1- *Analisis y carga*  
En la primera parte del ETL analize los distintos tipos de archivos que nos fueron brindados en formato "csv" y "json".  
Luego cree dos funciones para la extraccion de la ruta y para la transformacion de los archivos a df utilizando Pathlib para leer las rutas y 
Chardet para decifrar el encoding.  

2- *Transformacion*  
Cree una columna nueva con el nombre del origen de cada df para poder identificarlos.  
Una vez concatenados y habiendo dropeado el index antiguo y creado uno nuevo, se hicieron varios samples para ir verificando los datos, me encontre que datos que pertenecen a la columna"duration" se encuentran en la columna "ranting".   
Se procede a cambiarlos de ubicacion para no perderlos con una funcion lambda, con esto disminuyo en aproximadamente un 61.2% la cantidad de nulos de la columna "duration".    
  
*Analizando los datos se llego a las siguientes conclusiones:*
  
  

<p align="center">
<img src="https://user-images.githubusercontent.com/109487557/206541780-8f4fdb99-53a9-4a72-b942-3037b83ed1e5.png"  height=400>
</p>  




Para poder trabajar la columna "duration" tenemos que dividirla en dos, una parte numerica y otra parte str.  
Una vez tenemos las columnas con las que vamos a trabajar procedemos a cambiar los null por "sin dato" en el caso de columnas str y por 0 en columnas numericas.  
Usamos "strip" para sacar los espacios en blanco y reacomodamos el orden de las columnas con "reindex". 

Con las columnas "listed_in", "cast" que son dos columnas que tienen muchos valores en cada fila separados por comas vamos a crear dos nuevos df que mas adelante seran nuevas tablas en nuestra base de datos, conectadas por el index.  
Para realizar la separacion de palabras dentro de cada columna se uso "str.split" y "explode".  

Una vez tenemos nuestros datos limpios procedemos a subirlos a nuestra base de datos por medio de "SqlAlchemy".   
 
  
     

3- *Base de datos-modelo relacional*  
  
    
  
<p align="center">
<img src="https://user-images.githubusercontent.com/109487557/206522120-b6008e6e-03f4-4672-8fcd-482bc5f3cd1d.png"  height=400>
</p>   
  
    
    
    
    
+ **FastApi y Docker**  

*FastApi*  
  
1-Trabajamos en un entorno virtual en el cual instalamos todo lo necesario para realizar nuestra api y lo registramos con la funcion "pip freeze > requirements.txt".  
2-Creamos las carpetas para cada parte de nuestra api donde agregaremos el .py que corresponde:  
  + **main:** es un archivo de python que contiene el codigo principal de la API.Este archivo generalmente incluye la lógica de la aplicación y las funciones que se exponen a través de la API. Es responsable de establecer la conexión con otros componentes de la aplicación.  
  + **config:** va a tener nuestro engine para conectar con nuestra db.   
  + **models:** va a tener nuestros modelos de tablas (iguales a las que tenemos en nuestra db).   
  + **router:** es un archivo de Python que contiene la lógica de enrutamiento de la aplicación. Este archivo generalmente se encarga de gestionar las solicitudes entrantes a la API y enviarlas a las funciones correctas en el código de la aplicación.  
  + Luego de creamos un **"init.py"** en cada carpeta para que reconozca estas carpetas como modulos.    
                                                          
 

<p align="center">
<img src="https://user-images.githubusercontent.com/109487557/206532106-f5aa6ff2-4760-4aae-a4e1-879f40cd446b.png"  height=400>
</p>   
    


*Docker*  

Una vez la api esta lista y nuestro dockerfile esta en la carpeta de la api, nos posicionamos en el cmd de la terminal, donde se encuentra nuestra la ruta a la api y ejecutamos los siguientes comandos:  
  + **"docker build -t myimage ." :** nos va a crear una imagen de nuestra api.  
  + **"docker run -d --name mycontainer -p 80:80 myimage" :** nos va a crear un container en dockerdesktop.  


*docker container*
<p align="center">
<img src="https://user-images.githubusercontent.com/109487557/206547014-42f1efab-b309-4718-9e0c-63df66d5eed6.png"  >
</p>   

*FastApi corriendo con docker*

<p align="center">
<img src="https://user-images.githubusercontent.com/109487557/206548137-d8c71b68-61e7-4c41-a6e1-131935d0c0f6.png" >
</p> 

*Video demostración*
https://youtu.be/gyueOpqt4h0

<hr>


## **Conclusión**  

Fue un trabajo desafiante donde tuve que aprender desde el inicio a hacer una API y montarla en docker.  
Tambien me permitio fijar conocimientos de ETL en python y aprender a realizar querys en SqlAlchemy.   

Les dejo mi linkedin: https://www.linkedin.com/in/maxi-seidl/  

Un saludo a todos👋😁 y gracias por llegar hasta aca!




