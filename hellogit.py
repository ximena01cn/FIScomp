## ya tenemos un fichero de codigo 
print('hola')
## con git checkout no me guarda los cambios realizados en los ficheros y se va a la ultima 
## versión guardada

## tamién tenemos un git reset

## para volver a guardar soolo ponemos git add

## para guardar comandos podemos usar alias, solo hay que poner
## git config alias.nombre del alias 'comando que queremos guardar'

## si yo se que nunca voy a guardar un fichero puedo usar git ignore para que me deje de aparcer en rojo
## con git diff podemos ver que cambios hicimos respecto a la ultima modificaión

## también con gitcheckout podemos movermos entre las 'ramas' del arbol y especificar a cual
## por ejemplo HEAD o bien al poner git log nos aparecen los codigos especiales para estos (hash)

## con git reset --hard podemos 'desaparecer' algunas cosas y volver a un punto antes de hacerlas
## para ello idual debemos contar con el ID de la ubicación de ese punto a donde queremos ir, además
## es como si hubieramos movido la cabecera de nuestro 'tree'

## con git reflog nos aparece todo el historial completo de modificaciones en caso de querer recuperar
## una versión 'borrada'

## podemos etiquetar commits con tags (puntos importantes), en este caso tenemos heaed ->main, tag:clase_1
## HEAD nos indica en donde estamos dentro del 'tree'

## hay un comando reverb para eliminar commits pero no se recomineda su uso, puede ser peligroso

## podemos hacer una ramificación, si queremos empezar a trabajar en una funcionalidad diferente podemos
## hacer uso de git branch nombre_de_la_rama para crear esta nueva rama

## para movernos de rama lo que tenemos que hacer es poner git switch nombre_de_la_rama y ya, y es una 
## rama que ya tiene todo lo que habiamos creado pero en 'otro' lugar

## cuando usamos switch siempre se va al ultimo fichero de la rama a la que vayamos, cuando cambiamos
## de rama 'desaparecen' los ficheros creados en otras ramas y solo aparcen los de esa

## con git merge podemos 'combinar' branches, combinado la rama main dentro de login,
## se mezclas las dos ultimas colas de las branches en la branch en la que estemos

## que pasa cuando no funcionan los merges, hay casos en donde si despues de hacer un merge se modifica
## la misma linea de codigo en las branches involucradas y guardamos esos cambios con commit
## git lo detecta y no salvara ese cambio hasta que se solucionepara poder sincronizar los cambios

## una vez se hallan solucionado los cambios se tiene que volver a añadir el fichero y luego realizar 
## commit


## si estoy en una rama y creo un fichero y no le hago add y commit, git me madara un aviso de que si
## estoy seguro de querer salir ya que sino 'guardo' se perdera lo que halla hecho, pero si tengo un 
## código todo feo lo mejor sera usar un stash que guarda el fichero localmente sin afectar todo el arbol
## ya que esta todo feo el codigo, ya cuando vuelva a donde tenia mi stash (que lo puedo ver con git
## stash list), solo pongo git stash pop y asi ya aparecera lo que tenia

## si guardo algo en el stash y luego considero que ya no me sirve lo puedo borrar con git stash drop


## tembien podemos usar git diff para ver las modificaciones de las ramas


## cuando ya no ocupamos unas ramas porque las hemos merged con la principal u otra más importante 
## utilizamos git branch -d nombre_de_la_rama y asi la borramos 

## aunque la borremos aun podemos acceder a donde se encuentran, 'existe' extraoficialmente

