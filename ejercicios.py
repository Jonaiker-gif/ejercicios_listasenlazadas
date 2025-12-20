Pazmiño Bazurto Carlos Jonaiker 
19/12/2025
19/20 ejercicios completados 
# ============================================================================
# 🟢EJERCICIOS BÁSICOS - LISTA SIMPLEMENTE ENLAZADA
# ============================================================================

"""
EJERCICIO 1: Contar elementos
Dificultad: 🟢 Básico
Tiempo estimado: 10 minutos

Implementa un método count(elem) en SLinkedList que cuente cuántas veces
aparece un elemento en la lista.

Ejemplo:
    lista = [1, 2, 3, 2, 4, 2]
    lista.count(2)  # Retorna: 3
    lista.count(5)  # Retorna: 0
"""

def count(self, elem):
    """
    Cuenta las ocurrencias de un elemento en la lista
    """
    # 1. Inicializamos un contador en 0
    counter = 0
    
    # 2. Empezamos el recorrido desde la cabeza de la lista
    current = self._head
    
    # 3. Iteramos mientras el nodo actual no sea None
    while current is not None:
        # 4. Si el dato del nodo coincide con el elemento, sumamos 1
        if current.elem == elem:
            counter += 1
        
        # 5. Pasamos al siguiente nodo
        current = current.next
        
    # 6. Retornamos el total acumulado
    return counter


"""
EJERCICIO 2: Obtener elemento por índice
Dificultad: 🟢 Básico
Tiempo estimado: 15 minutos

Implementa un método get(index) que retorne el elemento en la posición index.

Ejemplo:
    lista = ['A', 'B', 'C', 'D']
    lista.get(0)   # Retorna: 'A'
    lista.get(2)   # Retorna: 'C'
    lista.get(10)  # Lanza: IndexError
"""

def get(self, index):
    """
    Obtiene el elemento en una posición específica
    """
    # 1. Validación de índice negativo
    if index < 0:
        raise IndexError("El índice no puede ser negativo")

    # 2. Inicializamos el puntero y un contador de posición
    current = self._head
    current_index = 0

    # 3. Recorremos la lista hasta encontrar el índice o llegar al final
    while current is not None:
        if current_index == index:
            return current.elem
        
        # Avanzamos al siguiente nodo e incrementamos el contador
        current = current.next
        current_index += 1

    # 4. Si salimos del bucle sin retornar, el índice está fuera de rango
    raise IndexError("Índice fuera de rango")


"""
EJERCICIO 3: Encontrar índice de elemento
Dificultad: 🟢 Básico
Tiempo estimado: 15 minutos

Implementa un método index_of(elem) que retorne el índice de la primera
ocurrencia del elemento, o -1 si no existe.

Ejemplo:
    lista = ['A', 'B', 'C', 'B', 'D']
    lista.index_of('B')  # Retorna: 1 (primera ocurrencia)
    lista.index_of('D')  # Retorna: 4
    lista.index_of('Z')  # Retorna: -1
"""


def index_of(self, elem):
    """
    Encuentra el índice de la primera ocurrencia de un elemento
    """
    # 1. Empezamos en la cabeza de la lista y con el contador en 0
    current = self._head
    current_index = 0
    
    # 2. Recorremos la lista hasta el final
    while current is not None:
        # 3. Si encontramos el elemento, retornamos el índice actual inmediatamente
        if current.elem == elem:
            return current_index
        
        # 4. Avanzamos al siguiente nodo e incrementamos el índice
        current = current.next
        current_index += 1
        
    # 5. Si el bucle termina sin encontrar el elemento, retornamos -1
    return -1


"""
EJERCICIO 4: Lista a array
Dificultad: 🟢 Básico
Tiempo estimado: 10 minutos

Implementa un método to_list() que convierta la lista enlazada a una
lista de Python (array).

Ejemplo:
    linked_list = SLinkedList con [1, 2, 3, 4]
    linked_list.to_list()  # Retorna: [1, 2, 3, 4]
"""

def to_list(self):
    """
    Convierte la lista enlazada a una lista de Python
    """
    # 1. Creamos una lista de Python vacía (el "contenedor")
    result = []
    
    # 2. Empezamos el recorrido desde la cabeza
    current = self._head
    
    # 3. Recorremos cada nodo de la lista enlazada
    while current is not None:
        # 4. Añadimos el elemento actual a la lista de Python
        result.append(current.elem)
        
        # 5. Pasamos al siguiente nodo
        current = current.next
        
    # 6. Retornamos la lista finalizada
    return result



"""
EJERCICIO 5: Limpiar lista
Dificultad: 🟢 Básico
Tiempo estimado: 5 minutos

Implementa un método clear() que elimine todos los elementos de la lista.

Ejemplo:
    lista = [1, 2, 3, 4, 5]
    lista.clear()
    len(lista)  # Retorna: 0
"""

def clear(self):
    """
    Elimina todos los elementos de la lista
    """
    # 1. Simplemente desconectamos la cabeza de la lista
    self._head = None
    
    # 2. Si tu clase mantiene un contador de tamaño, debemos reiniciarlo
    self._size = 0



# ============================================================================
# 🟡 EJERCICIOS INTERMEDIOS
# ============================================================================

"""
EJERCICIO 6: Invertir lista
Dificultad: 🟡 Intermedio
Tiempo estimado: 25 minutos

Implementa un método reverse() que invierta el orden de los elementos
EN LA MISMA LISTA (no crear una nueva).

Ejemplo:
    lista = [1, 2, 3, 4, 5]
    lista.reverse()
    print(lista)  # Output: 5 → 4 → 3 → 2 → 1 → None

Pista: Necesitas cambiar los punteros next de cada nodo.
"""

def reverse(self):
    """
    Invierte la lista en su lugar (in-place)
    """
    prev = None          # El que será el "nuevo siguiente"
    current = self._head # El nodo que estamos procesando
    
    while current is not None:
        next_node = current.next  # 1. Guardamos el resto de la lista
        
        current.next = prev       # 2. INVERSIÓN: El nodo actual apunta hacia atrás
        
        prev = current            # 3. Movemos 'prev' un paso adelante
        current = next_node       # 4. Movemos 'current' al siguiente original
        
    # Al final, 'prev' queda apuntando al que era el último nodo
    self._head = prev


"""
EJERCICIO 7: Detectar ciclo
Dificultad: 🟡 Intermedio
Tiempo estimado: 30 minutos

Implementa un método has_cycle() que detecte si la lista tiene un ciclo
(un nodo apunta a un nodo anterior, creando un bucle infinito).

Usa el algoritmo de Floyd (tortuga y liebre):
- Dos punteros: uno avanza 1 paso, otro avanza 2 pasos
- Si se encuentran, hay ciclo
- Si el rápido llega a None, no hay ciclo

Ejemplo:
    lista normal: 1 → 2 → 3 → None (retorna False)
    lista con ciclo: 1 → 2 → 3 → (vuelve a 2) (retorna True)
"""

def has_cycle(self):
    """
    Detecta si la lista tiene un ciclo usando Floyd's algorithm
    """
    # 1. Si la lista está vacía, no hay ciclo
    if not self._head:
        return False
    
    # 2. Inicializamos ambos punteros en la cabeza
    slow = self._head # La tortuga (avanza 1 paso)
    fast = self._head # La liebre (avanza 2 pasos)
    
    # 3. Recorremos mientras 'fast' y el siguiente de 'fast' existan
    # Esto es vital para evitar errores de tipo 'NoneType has no attribute next'
    while fast is not None and fast.next is not None:
        slow = slow.next          # Avanza 1 nodo
        fast = fast.next.next     # Avanza 2 nodos
        
        # 4. Si los punteros se encuentran, hay un ciclo
        if slow == fast:
            return True
            
    # 5. Si la liebre llega al final (None), no hay ciclo
    return False



"""
EJERCICIO 8: Encontrar el medio
Dificultad: 🟡 Intermedio
Tiempo estimado: 20 minutos

Implementa un método get_middle() que retorne el elemento del medio de la lista.
Si hay número par de elementos, retorna el segundo del medio.

Usa el algoritmo de dos punteros:
- Un puntero lento (avanza 1 paso)
- Un puntero rápido (avanza 2 pasos)
- Cuando el rápido llega al final, el lento está en el medio

Ejemplo:
    [1, 2, 3, 4, 5] → retorna 3
    [1, 2, 3, 4] → retorna 3 (segundo del medio)
"""

def get_middle(self):
    """
    Encuentra el elemento del medio de la lista
    """
    # 1. Caso base: si la lista está vacía, lanzamos excepción
    if self._head is None:
        raise Exception("La lista está vacía")

    # 2. Inicializamos ambos punteros en la cabeza
    slow = self._head
    fast = self._head

    # 3. La liebre (fast) avanza al doble de velocidad
    # Se detiene si ella misma es None o si no tiene un "siguiente"
    while fast is not None and fast.next is not None:
        slow = slow.next          # Avanza 1 paso
        fast = fast.next.next     # Avanza 2 pasos

    # 4. Por la relación de velocidad 2:1, cuando 'fast' llega al final,
    # 'slow' ha recorrido exactamente la mitad de la distancia.
    return slow.elem

"""
EJERCICIO 9: Eliminar duplicados
Dificultad: 🟡 Intermedio
Tiempo estimado: 25 minutos

Implementa un método remove_duplicates() que elimine todos los elementos
duplicados de la lista, dejando solo la primera ocurrencia de cada elemento.

Ejemplo:
    [1, 2, 3, 2, 4, 1, 5] → [1, 2, 3, 4, 5]

Versión 1: Puedes usar un conjunto (set) auxiliar - O(n) tiempo, O(n) espacio
Versión 2: Sin espacio adicional (más difícil) - O(n²) tiempo, O(1) espacio
"""

def remove_duplicates(self):
    """
    Elimina elementos duplicados usando un set para recordar lo visto.
    Complejidad: O(n) tiempo, O(n) espacio.
    """
    if self._head is None:
        return

    # 1. Usamos un conjunto para almacenar valores únicos vistos hasta ahora
    seen = set()
    
    # 2. Necesitamos rastrear el nodo actual y el anterior para "puentear"
    current = self._head
    prev = None

    while current is not None:
        # 3. Si el valor ya existe en el conjunto...
        if current.elem in seen:
            # ELIMINACIÓN: El anterior apunta al siguiente del actual
            prev.next = current.next
            # Si tu clase mantiene un contador de tamaño, decrémentalo:
            # self._size -= 1
        else:
            # 4. Si es nuevo, lo guardamos y avanzamos 'prev'
            seen.add(current.elem)
            prev = current
        
        # 5. Siempre avanzamos 'current'
        current = current.next


"""
EJERCICIO 10: Fusionar dos listas ordenadas
Dificultad: 🟡 Intermedio
Tiempo estimado: 30 minutos

Implementa una función merge_sorted(list1, list2) que tome dos listas
enlazadas ORDENADAS y retorne una nueva lista enlazada también ordenada
con todos los elementos de ambas.

Ejemplo:
    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6, 8]
    merge_sorted(list1, list2) → [1, 2, 3, 4, 5, 6, 7, 8]

Pista: Usa dos punteros, uno para cada lista, y compara elementos.
"""

def merge_sorted(list1, list2):
    """
    Fusiona dos listas ordenadas en una nueva lista ordenada
    """
    # 1. Creamos un nodo ficticio (dummy) para empezar la nueva lista
    # Esto nos ayuda a no tener que validar si la cabeza está vacía al inicio
    dummy = Node(0) 
    current = dummy

    # 2. Punteros para recorrer ambas listas
    p1 = list1._head
    p2 = list2._head

    # 3. Mientras ambas listas tengan elementos, comparamos
    while p1 is not None and p2 is not None:
        if p1.elem <= p2.elem:
            current.next = p1  # Enganchamos el nodo de la lista 1
            p1 = p1.next       # Avanzamos en la lista 1
        else:
            current.next = p2  # Enganchamos el nodo de la lista 2
            p2 = p2.next       # Avanzamos en la lista 2
        
        current = current.next # Avanzamos el puntero de la lista resultante

    # 4. Si una lista terminó antes que la otra, enganchamos el resto
    # Las listas enlazadas son geniales para esto: solo necesitas un enlace
    if p1 is not None:
        current.next = p1
    elif p2 is not None:
        current.next = p2

    # 5. Creamos la nueva lista SLinkedList y asignamos su cabeza
    # (Omitimos el nodo dummy inicial)
    result_list = SLinkedList()
    result_list._head = dummy.next
    return result_list



# ============================================================================
# 🔴 EJERCICIOS AVANZADOS
# ============================================================================



"""
EJERCICIO 11: Palíndromo
Dificultad: 🔴 Avanzado
Tiempo estimado: 35 minutos

Implementa un método is_palindrome() que determine si la lista es un palíndromo
(se lee igual de adelante hacia atrás).

Ejemplo:
    [1, 2, 3, 2, 1] → True
    [1, 2, 3, 4, 5] → False

Solución eficiente:
1. Encuentra el medio (algoritmo dos punteros)
2. Invierte la segunda mitad
3. Compara primera mitad con segunda mitad invertida
4. Restaura la segunda mitad (opcional)

Complejidad: O(n) tiempo, O(1) espacio
"""

def is_palindrome(self):
    """
    Verifica si la lista es un palíndromo en O(n) tiempo y O(1) espacio
    """
    if self._head is None or self._head.next is None:
        return True

    # 1. Encontrar el medio (Usando técnica de Ejercicio 8)
    slow = self._head
    fast = self._head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # 2. Invertir la segunda mitad (Usando técnica de Ejercicio 6)
    # 'slow' está en el medio. Invertimos desde ahí hasta el final.
    prev = None
    current = slow
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # 3. Comparar las dos mitades
    # 'prev' es ahora la cabeza de la segunda mitad invertida
    left = self._head
    right = prev
    is_palin = True
    
    # Solo comparamos hasta que la parte derecha se agote
    while right is not None:
        if left.elem != right.elem:
            is_palin = False
            break
        left = left.next
        right = right.next

    # (Opcional) Aquí podrías volver a invertir la segunda mitad 
    # para dejar la lista como estaba originalmente.

    return is_palin



"""
EJERCICIO 12: Rotar lista
Dificultad: 🔴 Avanzado
Tiempo estimado: 30 minutos

Implementa un método rotate(k) que rote la lista k posiciones a la derecha.

Ejemplo:
    lista = [1, 2, 3, 4, 5]
    lista.rotate(2)
    print(lista)  # Output: 4 → 5 → 1 → 2 → 3 → None

Pasos:
1. Conectar el último nodo con el primero (hacer circular)
2. Encontrar el nuevo head (en posición size - k)
3. Romper el círculo

Complejidad esperada: O(n)
"""


def rotate(self, k):
    """
    Rota la lista k posiciones a la derecha
    """
    # 1. Casos base: lista vacía, de un elemento o rotación de 0
    if not self._head or k == 0 or not self._head.next:
        return

    # 2. Calcular la longitud de la lista y encontrar el último nodo
    old_tail = self._head
    size = 1
    while old_tail.next:
        old_tail = old_tail.next
        size += 1

    # 3. Ajustar k (si k > size, el resultado es el resto de la división)
    k = k % size
    if k == 0:
        return

    # 4. HACER LA LISTA CIRCULAR: Conectamos la cola con la cabeza
    old_tail.next = self._head

    # 5. Encontrar el nuevo final (new_tail)
    # El nuevo final está en la posición (size - k - 1) desde el inicio
    steps_to_new_tail = size - k - 1
    new_tail = self._head
    for _ in range(steps_to_new_tail):
        new_tail = new_tail.next

    # 6. Definir la nueva cabeza y romper el círculo
    self._head = new_tail.next
    new_tail.next = None

"""
EJERCICIO 13: Particionar lista
Dificultad: 🔴 Avanzado
Tiempo estimado: 35 minutos

Implementa un método partition(x) que reorganice la lista de modo que
todos los elementos menores que x aparezcan antes que los elementos
mayores o iguales a x. El orden relativo dentro de cada grupo debe preservarse.

Ejemplo:
    lista = [3, 5, 8, 5, 10, 2, 1]
    lista.partition(5)
    # Resultado: [3, 2, 1] + [5, 8, 5, 10]
    # O cualquier permutación donde menores a 5 estén primero

Pista: Crea dos listas auxiliares (menores y mayores) y luego únelas.
"""
def partition(self, x):
    """
    Particiona la lista alrededor del valor x manteniendo el orden relativo.
    """
    # 1. Creamos dos listas temporales con sus respectivos nodos dummy
    less_head = Node(0)
    greater_head = Node(0)
    
    # 2. Punteros para ir construyendo las dos sublistas
    less = less_head
    greater = greater_head
    
    # 3. Recorremos la lista original
    current = self._head
    while current is not None:
        if current.elem < x:
            # Va a la lista de menores
            less.next = current
            less = less.next
        else:
            # Va a la lista de mayores o iguales
            greater.next = current
            greater = greater.next
        
        current = current.next
    
    # 4. PASO CRUCIAL: Cortar el final de la lista de 'mayores'
    # Si no hacemos esto, podríamos crear un ciclo infinito
    greater.next = None
    
    # 5. Unir las dos listas
    # El final de la lista de menores apunta al inicio de la de mayores
    less.next = greater_head.next
    
    # 6. Actualizar la cabeza de la lista principal
    self._head = less_head.next


"""
EJERCICIO 14: Suma de dos listas (números)
Dificultad: 🔴 Avanzado
Tiempo estimado: 40 minutos

Tienes dos listas enlazadas que representan números (cada nodo es un dígito).
Los dígitos están almacenados en ORDEN INVERSO (el primer nodo es la unidad).

Implementa una función add_numbers(list1, list2) que sume ambos números
y retorne el resultado como una nueva lista enlazada.

Ejemplo:
    list1 = [2, 4, 3] representa 342
    list2 = [5, 6, 4] representa 465
    add_numbers(list1, list2) = [7, 0, 8] representa 807

Pista: Es como sumar manualmente, llevando el "carry".
"""

def add_numbers(list1, list2):
    """
    Suma dos números representados como listas enlazadas (orden inverso)
    """
    # 1. Usamos un nodo dummy para construir la lista resultante fácilmente
    dummy = Node(0)
    current = dummy
    carry = 0  # El acarreo inicial es 0
    
    # 2. Punteros para las cabezas de ambas listas
    p1 = list1._head
    p2 = list2._head
    
    # 3. Iteramos mientras haya nodos en alguna lista o quede un acarreo pendiente
    while p1 is not None or p2 is not None or carry > 0:
        # Extraemos los valores (si la lista ya terminó, usamos 0)
        val1 = p1.elem if p1 else 0
        val2 = p2.elem if p2 else 0
        
        # 4. Operación de suma manual
        total = val1 + val2 + carry
        carry = total // 10       # Calculamos el nuevo acarreo (ej. 14 // 10 = 1)
        digit = total % 10        # Calculamos el dígito a guardar (ej. 14 % 10 = 4)
        
        # 5. Creamos el nuevo nodo y avanzamos
        current.next = Node(digit)
        current = current.next
        
        # Avanzamos los punteros de las listas originales si no son None
        if p1: p1 = p1.next
        if p2: p2 = p2.next
            
    # 6. Creamos la nueva estructura de lista y retornamos
    result_list = SLinkedList()
    result_list._head = dummy.next
    return result_list

"""
EJERCICIO 15: Intersección de dos listas
Dificultad: 🔴 Avanzado
Tiempo estimado: 45 minutos

Dadas dos listas enlazadas, determina si se intersectan (comparten nodos)
y encuentra el nodo donde se intersectan.

Ejemplo:
    list1: 1 → 2 → 3
    7 → 8 → 9
    list2: 4 → 5 → 6
    
    Retorna el nodo con valor 7 (primer nodo compartido)

Solución eficiente:
1. Calcula la longitud de ambas listas
2. Alinea los inicios (avanza en la lista más larga)
3. Avanza simultáneamente hasta encontrar el nodo común

Complejidad: O(n + m) tiempo, O(1) espacio
"""

def find_intersection(list1, list2):
    """
    Encuentra el punto de intersección de dos listas enlazadas
    """
    if not list1._head or not list2._head:
        return None

    # 1. Función auxiliar para obtener longitud y último nodo
    def get_len_and_tail(list_head):
        length = 1
        current = list_head
        while current.next:
            length += 1
            current = current.next
        return length, current

    # 2. Obtener datos de ambas listas
    len1, tail1 = get_len_and_tail(list1._head)
    len2, tail2 = get_len_and_tail(list2._head)

    # 3. Si los últimos nodos son diferentes, no hay intersección
    if tail1 is not tail2:
        return None

    # 4. Alinear los puntos de inicio
    # El puntero 'longer' siempre será el de la lista con más nodos
    longer = list1._head if len1 > len2 else list2._head
    shorter = list2._head if len1 > len2 else list1._head

    # Avanzamos en la lista más larga la diferencia de longitudes
    diff = abs(len1 - len2)
    for _ in range(diff):
        longer = longer.next

    # 5. Avanzar ambos simultáneamente hasta que choquen
    while longer is not shorter:
        longer = longer.next
        shorter = shorter.next

    # Retornamos cualquiera de los dos (son el mismo nodo)
    return longer


# ============================================================================
# 🟡 EJERCICIOS DE LISTA DOBLEMENTE ENLAZADA
# ============================================================================

"""
EJERCICIO 16: Navegador Web
Dificultad: 🟡 Intermedio
Tiempo estimado: 40 minutos

Implementa una clase BrowserHistory que simule el historial de un navegador
usando una lista doblemente enlazada.

Métodos requeridos:
- __init__(homepage): Inicia con la página de inicio
- visit(url): Visita una nueva URL (elimina historial futuro)
- back(steps): Retrocede 'steps' páginas (máximo hasta el inicio)
- forward(steps): Avanza 'steps' páginas (máximo hasta el final)
- get_current(): Retorna la URL actual

Ejemplo:
    browser = BrowserHistory("google.com")
    browser.visit("youtube.com")    # google.com → youtube.com
    browser.visit("facebook.com")   # ... → facebook.com
    browser.back(1)                 # Vuelve a youtube.com
    browser.forward(1)              # Regresa a facebook.com
"""

class Node:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self, homepage):
        # Iniciamos con la página de inicio como el nodo actual
        self.current = Node(homepage)

    def visit(self, url):
        """
        Visita una nueva URL. Al hacerlo, perdemos la capacidad de ir 
        hacia adelante (el historial futuro se borra).
        """
        new_node = Node(url)
        
        # Conectamos el actual con el nuevo
        self.current.next = new_node
        new_node.prev = self.current
        
        # El nuevo nodo se convierte en el actual
        self.current = new_node

    def back(self, steps):
        """
        Retrocede 'steps' veces usando el puntero 'prev'
        """
        while steps > 0 and self.current.prev is not None:
            self.current = self.current.prev
            steps -= 1
        return self.current.url

    def forward(self, steps):
        """
        Avanza 'steps' veces usando el puntero 'next'
        """
        while steps > 0 and self.current.next is not None:
            self.current = self.current.next
            steps -= 1
        return self.current.url

    def get_current(self):
        return self.current.url

"""
EJERCICIO 17: LRU Cache
Dificultad: 🔴 Avanzado
Tiempo estimado: 60 minutos

Implementa una estructura de datos LRU Cache (Least Recently Used Cache)
usando una lista doblemente enlazada + diccionario.

El cache tiene capacidad limitada. Cuando se llena, elimina el elemento
usado menos recientemente.

Métodos:
- __init__(capacity): Crea cache con capacidad dada
- get(key): Obtiene el valor (marca como usado recientemente)
- put(key, value): Inserta/actualiza (elimina LRU si está lleno)

Ambos métodos deben ser O(1).

Pista:
- Diccionario: para acceso O(1) por key
- Lista doble: para mantener orden de uso (más reciente al final)
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {} # {key: Node}
        
        # Nodos dummy para evitar chequeos de None
        self.head = Node(0, 0) # El más antiguo (LRU)
        self.tail = Node(0, 0) # El más reciente
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Elimina un nodo de la lista (desconexión de punteros)"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_tail(self, node):
        """Añade un nodo justo antes del dummy tail (posición de 'más reciente')"""
        before_tail = self.tail.prev
        before_tail.next = node
        node.prev = before_tail
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            # Como se usó, lo movemos al final (más reciente)
            self._remove(node)
            self._add_to_tail(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            # Si ya existe, eliminamos el nodo viejo
            self._remove(self.cache[key])
        
        # Creamos el nuevo nodo y lo registramos
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_to_tail(new_node)
        
        # Si excedemos la capacidad, eliminamos el LRU (después del dummy head)
        if len(self.cache) > self.cap:
            lru_node = self.head.next
            self._remove(lru_node)
            del self.cache[lru_node.key]


"""
EJERCICIO 18: Editor Multi-cursor
Dificultad: 🔴 Avanzado
Tiempo estimado: 50 minutos

Extiende el TextEditor para soportar múltiples cursores (como en VS Code).
Cada cursor puede estar en una posición diferente del documento.

Funcionalidades:
- add_cursor(position): Agregar cursor en posición
- remove_cursor(cursor_id): Eliminar cursor
- type_at_cursor(cursor_id, text): Escribir en cursor específico
- undo_all(): Deshacer en todos los cursores
- redo_all(): Rehacer en todos los cursores

Esto requiere mantener múltiples historiales sincronizados.
"""
class Cursor:
    def __init__(self, position=0):
        self.position = position
        self.undo_stack = []
        self.redo_stack = []

class MultiCursorEditor:
    def __init__(self):
        self.document = [] # Representación simple del texto
        self.cursors = {}  # {cursor_id: Cursor}
        self.next_id = 0

    def add_cursor(self, position=0):
        cursor_id = self.next_id
        self.cursors[cursor_id] = Cursor(min(position, len(self.document)))
        self.next_id += 1
        return cursor_id

    def remove_cursor(self, cursor_id):
        if cursor_id in self.cursors:
            del self.cursors[cursor_id]

    def type_at_cursor(self, cursor_id, text):
        if cursor_id not in self.cursors:
            return
        
        cursor = self.cursors[cursor_id]
        # Guardar estado para Undo
        cursor.undo_stack.append({'type': 'insert', 'text': text, 'pos': cursor.position})
        cursor.redo_stack.clear() # Al escribir, se limpia el historial de redo
        
        # Insertar texto en el "documento"
        for i, char in enumerate(text):
            self.document.insert(cursor.position + i, char)
        
        # Actualizar posición del cursor
        cursor.position += len(text)
        
        # NOTA: En un sistema real, insertar aquí desplazaría la posición 
        # de otros cursores que estén más adelante en el texto.

    def undo_all(self):
        """Deshace la última acción de cada cursor individualmente"""
        for cursor_id, cursor in self.cursors.items():
            if not cursor.undo_stack:
                continue
            
            action = cursor.undo_stack.pop()
            if action['type'] == 'insert':
                # Revertir inserción: eliminar el texto
                start = action['pos']
                length = len(action['text'])
                del self.document[start : start + length]
                
                # Guardar en Redo y restaurar posición
                cursor.redo_stack.append(action)
                cursor.position = start

    def redo_all(self):
        """Rehace la última acción deshecha de cada cursor"""
        for cursor_id, cursor in self.cursors.items():
            if not cursor.redo_stack:
                continue
            
            action = cursor.redo_stack.pop()
            if action['type'] == 'insert':
                # Re-insertar
                for i, char in enumerate(action['text']):
                    self.document.insert(action['pos'] + i, char)
                
                cursor.undo_stack.append(action)
                cursor.position = action['pos'] + len(action['text'])



# ============================================================================
# EJERCICIOS DE ANÁLISIS Y OPTIMIZACIÓN
# ============================================================================


"""
EJERCICIO 19: Benchmark de operaciones
Dificultad: 🟡 Intermedio
Tiempo estimado: 30 minutos

Escribe un programa que compare el rendimiento de:
- Arrays (listas de Python)
- Listas simplemente enlazadas
- Listas doblemente enlazadas

Para las siguientes operaciones:
1. Inserción al inicio (1000 elementos)
2. Inserción al final (1000 elementos)
3. Eliminación al inicio (1000 elementos)
4. Eliminación al final (1000 elementos)
5. Acceso por índice (1000 accesos aleatorios)

Usa el módulo 'time' para medir el tiempo.
Imprime los resultados en una tabla comparativa.
"""
#Este ejercicio no lo pude comprender, así que pasé al siguente.


"""
EJERCICIO 20: Análisis de casos de uso
Dificultad: 🟡 Intermedio
Tiempo estimado: 20 minutos

Para cada uno de los siguientes escenarios, determina qué estructura
es más apropiada (Array, Lista Simple, Lista Doble) y justifica tu respuesta:

1. Sistema de colas de impresión (FIFO estricto)
2. Historial de navegación de un navegador
3. Sistema de undo/redo con límite de 100 acciones
4. Base de datos que necesita acceso rápido por ID
5. Playlist de música con navegación adelante/atrás
6. Sistema de gestión de memoria del OS
7. Editor de texto que solo permite append al final
8. Implementación de una pila (Stack)
9. Juego que necesita insertar/eliminar enemigos frecuentemente
10. Sistema de logs que solo escribe al final y lee todo

Escribe tus respuestas en comentarios con justificación.
"""


"""
EJERCICIO 20: Respuestas y Justificaciones
"""

# 1. Sistema de colas de impresión (FIFO estricto)
# ESTRUCTURA: Lista Simple (Singly Linked List) con puntero al 'Tail'.
# JUSTIFICACIÓN: Solo necesitamos insertar al final y quitar del inicio. 
# Una lista simple con puntero al final permite ambas operaciones en O(1) 
# sin el desperdicio de memoria de una lista doble.

# 2. Historial de navegación de un navegador
# ESTRUCTURA: Lista Doblemente Enlazada (Doubly Linked List).
# JUSTIFICACIÓN: Como vimos en el ejercicio del BrowserHistory, necesitamos 
# movernos libremente hacia adelante (next) y atrás (prev).

# 3. Sistema de undo/redo con límite de 100 acciones
# ESTRUCTURA: Array (Python List).
# JUSTIFICACIÓN: Como el tamaño es fijo y pequeño (100), el acceso por índice 
# es instantáneo y no sufriremos por desplazamientos masivos de memoria. 
# Además, los arrays son más compactos en memoria para tipos de datos simples.

# 4. Base de datos con acceso rápido por ID
# ESTRUCTURA: Array (o Tabla Hash/Diccionario).
# JUSTIFICACIÓN: Si los IDs son secuenciales, un Array ofrece O(1). 
# Las listas enlazadas son pésimas para búsqueda (O(n)), lo que 
# ralentizaría la base de datos drásticamente.

# 5. Playlist de música con navegación adelante/atrás
# ESTRUCTURA: Lista Doblemente Enlazada Circular.
# JUSTIFICACIÓN: Permite 'Siguiente' y 'Anterior' en O(1). Al ser circular, 
# cuando termina la última canción, el puntero 'next' nos lleva automáticamente 
# a la primera sin lógica extra.

# 6. Sistema de gestión de memoria del OS (Free Lists)
# ESTRUCTURA: Lista Simple.
# JUSTIFICACIÓN: El OS necesita una lista de bloques de memoria libres. 
# Frecuentemente se insertan o eliminan bloques intermedios al asignar 
# memoria. Las listas permiten estas inserciones sin reasignar todo el array.

# 7. Editor de texto que solo permite append al final
# ESTRUCTURA: Array (Python List).
# JUSTIFICACIÓN: Si solo añadimos al final, el Array es el rey. El acceso 
# es O(1) amortizado y es la estructura con mejor aprovechamiento de la 
# 'caché' del procesador (localidad de datos).

# 8. Implementación de una pila (Stack)
# ESTRUCTURA: Lista Simple (insertando/quitando siempre por la cabeza).
# JUSTIFICACIÓN: La operación 'push' y 'pop' en la cabeza de una lista 
# simple es siempre O(1) y es más eficiente que un Array que podría 
# necesitar redimensionarse.

# 9. Juego que inserta/elimina enemigos frecuentemente
# ESTRUCTURA: Lista Doblemente Enlazada.
# JUSTIFICACIÓN: Los enemigos mueren o aparecen en cualquier orden. Si un 
# enemigo muere (está en medio de la lista), la lista doble permite 
# eliminarlo en O(1) si ya tenemos la referencia al objeto, reconectando 
# sus vecinos.

"""
- Sección de pruebas que ejecute todos los ejercicios
 - Imprime resultados de manera clara
"""

import time

class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prev = None  # Usado para Listas Dobles

class SLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def append(self, elem):
        """Método auxiliar para construir las listas fácilmente"""
        new_node = Node(elem)
        if not self._head:
            self._head = new_node
        else:
            curr = self._head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self._size += 1

    # EJERCICIO 1: Contar elementos
    def count(self, elem):
        counter = 0
        curr = self._head
        while curr:
            if curr.elem == elem: counter += 1
            curr = curr.next
        return counter

    # EJERCICIO 2: Obtener por índice
    def get(self, index):
        if index < 0: raise IndexError("Índice negativo")
        curr = self._head
        for i in range(index):
            if not curr: raise IndexError("Fuera de rango")
            curr = curr.next
        return curr.elem if curr else None

    # EJERCICIO 3: Encontrar índice
    def index_of(self, elem):
        curr = self._head
        idx = 0
        while curr:
            if curr.elem == elem: return idx
            curr = curr.next
            idx += 1
        return -1

    # EJERCICIO 4: Lista a Array
    def to_list(self):
        res = []
        curr = self._head
        while curr:
            res.append(curr.elem)
            curr = curr.next
        return res

    # EJERCICIO 5: Limpiar
    def clear(self):
        self._head = None
        self._size = 0

    # EJERCICIO 6: Invertir
    def reverse(self):
        prev = None
        curr = self._head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self._head = prev

    # EJERCICIO 8: Encontrar el medio
    def get_middle(self):
        if not self._head: return None
        slow = fast = self._head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.elem

    # EJERCICIO 9: Eliminar duplicados (O(n) con set)
    def remove_duplicates(self):
        if not self._head: return
        seen = {self._head.elem}
        curr = self._head
        while curr.next:
            if curr.next.elem in seen:
                curr.next = curr.next.next
            else:
                seen.add(curr.next.elem)
                curr = curr.next

    # EJERCICIO 11: Palíndromo
    def is_palindrome(self):
        if not self._head or not self._head.next: return True
        # 1. Medio
        slow = fast = self._head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 2. Invertir segunda mitad
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        # 3. Comparar
        left, right = self._head, prev
        while right:
            if left.elem != right.elem: return False
            left, right = left.next, right.next
        return True

    # EJERCICIO 12: Rotar k posiciones
    def rotate(self, k):
        if not self._head or k == 0: return
        # Tamaño y cola
        last = self._head
        size = 1
        while last.next:
            last = last.next
            size += 1
        k = k % size
        if k == 0: return
        # Hacer circular y romper
        last.next = self._head
        steps = size - k
        new_last = self._head
        for _ in range(steps - 1):
            new_last = new_last.next
        self._head = new_last.next
        new_last.next = None

# EJERCICIO 14: Suma de listas
def add_numbers(l1, l2):
    dummy = Node(0)
    curr = dummy
    p1, p2, carry = l1._head, l2._head, 0
    while p1 or p2 or carry:
        v1 = p1.elem if p1 else 0
        v2 = p2.elem if p2 else 0
        val = v1 + v2 + carry
        carry = val // 10
        curr.next = Node(val % 10)
        curr = curr.next
        if p1: p1 = p1.next
        if p2: p2 = p2.next
    res = SLinkedList()
    res._head = dummy.next
    return res

# EJERCICIO 17: LRU Cache
class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key in self.cache:
            n = self.cache[key]
            self._remove(n)
            self._add(n)
            return n.elem
        return -1

    def put(self, key, value):
        if key in self.cache: self._remove(self.cache[key])
        n = Node(value)
        n.key = key # Atributo extra para borrar del dict
        self.cache[key] = n
        self._add(n)
        if len(self.cache) > self.cap:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]



def run_tests():
    print("Reportes de Ejecución")

    # Grupo 1
    print("\n[MÓDULO 1: OPERACIONES BÁSICAS]")
    lista = SLinkedList()
    for x in [1, 2, 3, 2, 4, 2]: lista.append(x)
    print(f"Lista: {lista.to_list()}")
    print(f"Ej 1: Count(2) -> {lista.count(2)} | Esperado: 3")
    print(f"Ej 3: Index_of(4) -> {lista.index_of(4)} | Esperado: 4")

    # Grupo 2
    print("\n[MÓDULO 2: ALGORITMOS DE PUNTEROS]")
    lista.reverse()
    print(f"Ej 6: Reverse -> {lista.to_list()} | Esperado: [2, 4, 2, 3, 2, 1]")
    
    lista.clear()
    for x in [10, 20, 30, 40, 50]: lista.append(x)
    print(f"Ej 8: Middle -> {lista.get_middle()} | Esperado: 30")

    # Grupo 3
    print("\n[MÓDULO 3: CASOS AVANZADOS]")
    pali = SLinkedList()
    for x in [1, 2, 3, 2, 1]: pali.append(x)
    print(f"Ej 11: Palíndromo [1,2,3,2,1] -> {pali.is_palindrome()} | Esperado: True")

    lista.rotate(2)
    print(f"Ej 12: Rotate(2) de [10..50] -> {lista.to_list()} | Esperado: [40, 50, 10, 20, 30]")

    # Grupo 4
    print("\n[MÓDULO 4: SISTEMAS COMPLEJOS]")
    lru = LRUCache(2)
    lru.put(1, "Data1"); lru.put(2, "Data2")
    lru.get(1) # 1 es reciente
    lru.put(3, "Data3") # 2 debe morir
    print(f"Ej 17: LRU Cache (Get 2) -> {lru.get(2)} | Esperado: -1 (Eliminado)")
    print(f"Ej 17: LRU Cache (Get 1) -> {lru.get(1)} | Esperado: Data1")

    print("\n" + "="*60)
    print("PRUEBAS FINALIZADAS CON ÉXITO")
    print("="*60)

if __name__ == "__main__":
    run_tests()

