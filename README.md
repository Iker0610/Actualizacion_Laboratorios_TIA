# Proyecto de Actualización

## Descripción

Este proyecto tiene como objetivo actualizar los laboratorios de la asignatura TIA con el fin de permitir realizarlos empleando las últimas versiones de Python.

También se espera mejorar varias estructuras de datos, el formato, y aplicar las guías y normas de programación que se emplean en Python. ~~(para que a los friki-pythons no nos de un mal)~~

## Objetivos

- Permitir emplear versiones de Python ≥ 3.6
- Eliminar ciertos anti-patherns existentes en el proyecto original
- Sustituir el formateo de strings por f-strings que son una alternativa mejor y más moderna.
- Optimizar imports
- Formatear el código
- Mejorar las estructuras de datos de **utils.py**
- [No definitivo] Mejorar la estructura de los directorios para que los alumnos tengan claro cuales son sus ficheros.

## Aclaraciones

* No se pretende ni alterar las funcionalidades, ni las evaluaciones (criterios, cálculos, etc.), ni completar el laboratorio.
* De primeras no se editará lo que hay en la carpeta _MACOSX del Labo 1 original.

## Mejora en las estructuras de datos de _utils.py_

Una parte importante es la mejora de las estructuras de datos, pues aunque las dadas son útiles, y se pueden emplear sin problema, son escasas en cuanto a funcionalidades.

### Clase Counter

Simplemente se ha refactorizado el código para que esté más limpio.


### Dunder Methods o Magic Methods

Se han implementado varios _dunder methods_ en las clases **_Queue_**, _**Stack**_ y **_PriorityQueue_** debido a que su implementación base era muy básica y no sacaba partido de las capacidades y diseño de Python:
- **\_\_bool\_\_:** Equivalente a isEmpty pero versión pythonic. Ejemplo de uso:
   ````python
  from utils import Queue
  
  queue = Queue()
  
  if queue:
      # Hay elementos en la lista
      pass
  
  elif not queue:
      # No hay elementos en la lista o la lista es null
      pass
  
  while queue:
    # Mientras haya elementos en la lista irá iterando
    pass
  ````  


- **\_\_len\_\_:** Permite consultar la longitud de la cola o pila:
  ````python
  from utils import Queue
  
  queue = Queue([1, 2, 3])
  len(queue)
  >>> 3  
  ````
  

- **\_\_getitem\_\_:** Permite obtener un objeto por su índice:
  ````python
  from utils import Queue
  
  queue = Queue([1, 2, 3])
  queue[1]
  >>> 2  
  ````

- **\_\_contains\_\_:** Permite consultar si un objeto está en la pila o cola:
  ````python
  from utils import Queue
  
  queue = Queue([1, 2, 3])
  
  1 in queue
  >>> True
  
  50 in queue
  >>> False 
  ````
  
- **\_\_iter\_\_:** Permite generar un iterador y emplearlo en un _for each_:
  - Está implementado tal que sea lazy (solo obtiene los items cuando se le piden).\
  - Por otro lado permite añadir nuevos objetos según se va iterando; si se añaden arbitrariamente puede dar lugar a error, por eso hay que emplear el método **_push_**.
  - Cuando el iterador devuelve un objeto lo hace como si se haría **_pop_**, por tanto, **EL OBJETO ES ELIMINADO DE LA ESTRUCTURA DE DATOS**
  
  ````python
  from utils import Queue
  
  # Forma común en PMOO:
  queue = Queue([1, 2, 3])
  
  while not queue.isEmpty(): # Otra forma sería: while queue: 
    item = queue.pop()
    print(item)
  
  >>> 1
  >>> 2
  >>> 3
  
  len(queue)
  >>> 0
  
  # Forma pythonica
  queue = Stack([1, 2, 3])
  
  for item in queue:
    print(item)
    # Prueba de la insercción de un elemento mientras se itera
    if item == 2:
        queue.push(4)
  
  >>> 3
  >>> 2
  >>> 4
  >>> 1
  
  len(queue)
  >>> 0
  ````

### Clases _Queue_ y _Stack_

Estas son las dos clases que más cambios han sufrido, pues además de faltar métodos, se echaba de menos la opción de poder crearlas con unos valores inciales sin necesidad de insertarlos uno a uno.

- Se ha añadido la opción de inicializar la cola o pila con unos valores iniciales dados por parámetro en la constructora en forma de lista.
Siendo el orden esperado: [first, second, third, ...]
- Se ha añadido el método **head**.
- También se ha cambiado la estructura de datos base de una lista (**_list_**) a una lista doblemente ligada (**_deque_**). Las razones son las siguientes:
  - Los costes de inserción (push) y eliminación (pop) al inicio tienen coste _**O**(n)_ si se emplean las listas de Python.\ 
  - Las listas de Python somo como los array de Java y su reajuste de tamaño automático para insertar más elementos tiene un coste _**O**(n)_ cuando se llenan.
  - Por ello Python ofrece en su librería colections la clase **_deque_**, pues es consciente de que la lista no es la opción más eficiente para muchas cosas.
    - La clase **_deque_** (Doubly Ended Queue) permite costes _**O**(1)_ tanto para inserciones como extracciones por ambos extremos. Por lo que son la mejor opción a la hora de implementar colas y pilas.




## Ficheros identicos / comunes

Ficheros identicos en los laboratorios indicados, lo que implica que los cambios/actualizaciones en uno se pueden exportar directamente al otro.

Archivo | _Laboratorios_
--- | --- 
**autograder.py** | _Labo 1, Labo 2, Labo 3_
**game.py** | _Labo 1, Labo 2, Labo 3, Mini Concurso_
**ghostAgents.py** | _Labo 1, Labo 2, Labo 3_
**grading.py** | _Labo 1, Labo 2, Labo 3_
**graphicsDisplay.py** | _Labo 1, Labo 2, Labo 3_
**graphicsUtils.py** | _Labo 1, Labo 2, Labo 3_
**keyboardAgents.py** | _Labo 1, Labo 2, Labo 3_
**layout.py** | _Labo 1, Labo 2, Labo 3_
**pacman.py** | _Labo 1, Labo 2, Labo 3_
**pacmanAgents.py** | _Labo 1, Labo 2, Labo 3_
**testClasses.py** | _Labo 1, Labo 2, Labo 3_
**testParser.py** | _Labo 1, Labo 2, Labo 3_
**textDisplay.py** | _Labo 1, Labo 2, Labo 3_
**util.py** | _Labo 1, Labo 2, Labo 3, Mini Concurso, Rush Hour_

### Honorables menciones

- **_Fichero game.py:_** Este fichero contiene un atributo  **_\_directions_** que es importante:
  - El orden de creación de este diccionario es importante en el laboratorio 2.
    - El laboratorio 1 no depende del orden. 
    - Se desconoce si el laboratorio 3 es sensible a estos cambios.
  - Esto implica que es obligatorio emplear Python _**≥ 3.6**_ pues en versiones menores el orden de los diccionarios no está garantizado.


- **_Mini Contest:_**
    - Los únicos ficheros _100%_ identicos son **game.py** y **util.py**.
    - El resto son muy parecidos pero no identicos.
    - Excluyo **search.py** debido a que hay que copiar y pegarlo del Labo 1 al inicio del laboratorio.


- **_Rush Hour:_**
    - Obviamente únicamente **util.py**
    - Excluyo **search.py** debido a que hay que copiar y pegarlo del Labo 1 al inicio del laboratorio.

## TODOs

- Actualizar la estructura de ficheros
- Eliminar la libería **_imp_** y sustituirla por **_importlib_**
- Terminar los siguientes labos:
  - Mini Concurso
  - Rush Hour

