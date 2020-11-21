import os
import pathlib
import shutil

def principal():
    # rutaTareas es la carpeta en donde se encuentran almacenadas todas las tareas de los alumnos y donde el programa los cogerá para luego ordenarlos
    rutaTareas = str(pathlib.Path().absolute()) + "/Nombre de la carpeta de las tareas"

    # rutaGrupos es los grupos separados en los cuales, dentro hay carpetas de alumnos
    rutaGrupos = str(pathlib.Path().absolute()) + "/Nombre de la carpeta de los grupos"

    # Esta variable nos servirá para al final almacenar la ruta de donde se encuentra la carpeta del alumno y de esta manera poder copiar el archivo dentro de esa carpeta
    rutaAlumno = ""

    # os.listdir nos ayuda a enlistar todos los elementos que estan dentro de una ruta, por ejemplo, si en la ruta actual tengo dos archivos de texto llamados: "Texto1" y "Texto2", listdir devolverá una lista con esos elementos de esta manera, ["Texto1", "Texto2"] y a su vez lo guardará el la variable en la que hayamos usado listdir
    EnlistadoTareas = os.listdir(rutaTareas)
    EnlistadoGrupos = os.listdir(rutaGrupos)

    # Todas estas variables nos ayudarán a determinar todos los datos del alumno
    contador = 0
    GrupoAlumno = ""
    nombreAlumno = ""

    for tarea in EnlistadoTareas:
        for nombre in tarea:
            
            # El formato del nombre deberá ser de esta manera: nombre_grupo_informacion adicional (opcional), por ejemplo: Juan Jose May Poot_1B_Actividad.
            if nombre != "_" and contador == 0:

                nombreAlumno += nombre
            
            elif nombre == "_":
                contador += 1
            
            elif contador != 2:
                GrupoAlumno += nombre

            else:
                break;

        # Sacamos la ruta del grupo del alumno, si es de 1B, 2B, 3C, aquí se guardará esa ruta
        rutaAlumno = rutaGrupos + r"\\" + EnlistadoGrupos[EnlistadoGrupos.index(GrupoAlumno)]

        # Con listdir enlistamos todos los elementos que se encuentran dentro de esa ubicación
        EnlistadoAlumnos = os.listdir(rutaAlumno)

        # Convetimos todos los elementos del arreglo a title() para que no tengamos problemas con las mayusculas y minusculas, esta funcion hace lo siguiente: jose david tuz may = Jose David Tuz May
        for i in range(len(EnlistadoAlumnos)):
            EnlistadoAlumnos[i].title()    

        # Encontramos el nombre del alumno dentro de la lista que anteriormente habiamos obtenido
        Alumno = EnlistadoAlumnos[EnlistadoAlumnos.index(nombreAlumno.title())]
        
        # Esta es la ruta original, la variable tarea toma el valor del alumno
        Ruta_original_tarea = rutaTareas + f"/{tarea}"

        # Ruta final en donde copiaremos el archivo del alumno
        Ruta_final = rutaAlumno + f"/{Alumno}" + f"/{tarea.title()}"

        shutil.copyfile(Ruta_original_tarea, Ruta_final)
        

        #Reiniciando el valor de todas las variables
        GrupoAlumno = ""
        nombreAlumno = ""
        contador = 0

principal()

# Notas importantes

# Los nombres de los alumnos en las carpetas deberan ser los mismos que en los archivos, si en la carpeta dice Juan Jose Bobadilla, el archivo debe llamarse de la misma manera, NOTA: No se distinguen entre letras mayusculas y minusculas, si la carpeta dice Juan Jose Bobadilla, y el archivo dice juan jose bobadilla, el programa funcionará con normalidad

# El programa esta diseñado para buscar dentro de una carpeta, en este caso usamos una carpeta llamada Grupos y dentro se encuentran todos los grupos, y dentro de esos grupos se encuentran carpetas de todos los alumnos, de esta manera
