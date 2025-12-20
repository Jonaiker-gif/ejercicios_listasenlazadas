1.Prueba para el EJERCICIO 8: get_middle()
Aquí vamos a praobar la lógica de los dos punteros tanto para listas de tamaño par como impar 
def test_get_middle():
    # Caso 1: Lista Impar [1, 2, 3, 4, 5]
    lista_impar = SLinkedList()
    for i in [1, 2, 3, 4, 5]: lista_impar.append(i)
    assert lista_impar.get_middle() == 3, "Error en lista impar: medio debería ser 3"

    # Caso 2: Lista Par [1, 2, 3, 4]
    lista_par = SLinkedList()
    for i in [1, 2, 3, 4]: lista_par.append(i)
    # Según el enunciado, debe retornar el segundo del medio
    assert lista_par.get_middle() == 3, "Error en lista par: medio debería ser 3"

    # Caso 3: Lista de un solo elemento
    lista_unica = SLinkedList()
    lista_unica.append(10)
    assert lista_unica.get_middle() == 10, "Error: El medio de un elemento es sí mismo"

    print("Test get_middle: PASADO")

2. Prueba para el EJERCICIO 11: is_palindrome()
Este es el más completo de las pruebas ya que verifica si la manipulación de punteros (invertir la mitad) y no rompe la lógica de comparación
def test_is_palindrome():
    # Caso 1: Es palíndromo (Impar)
    p1 = SLinkedList()
    for i in [1, 2, 3, 2, 1]: p1.append(i)
    assert p1.is_palindrome() is True, "Error: [1,2,3,2,1] es palíndromo"

    # Caso 2: No es palíndromo
    p2 = SLinkedList()
    for i in [1, 2, 3, 4, 5]: p2.append(i)
    assert p2.is_palindrome() is False, "Error: [1,2,3,4,5] NO es palíndromo"

    # Caso 3: Palíndromo Par y Lista Vacía
    p3 = SLinkedList()
    for i in [1, 2, 2, 1]: p3.append(i)
    assert p3.is_palindrome() is True, "Error: [1,2,2,1] es palíndromo"
    
    p4 = SLinkedList() # Vacía
    assert p4.is_palindrome() is True, "Error: Lista vacía se considera palíndromo"

    print("Test is_palindrome: PASADO")

3.Prueba para el EJERCICIO 3: index_of(elem)
Esta prueba verifica la búsqueda lineal y el manejo del caso "no encontrado"
def test_index_of():
    lista = SLinkedList()
    lista.append('A')
    lista.append('B')
    lista.append('C')

    # Caso 1: El elemento está en el medio
    assert lista.index_of('B') == 1, "Error: Debería retornar índice 1"

    # Caso 2: El elemento es la cabeza
    assert lista.index_of('A') == 0, "Error: Debería retornar índice 0"

    # Caso 3: El elemento no existe
    assert lista.index_of('Z') == -1, "Error: Debería retornar -1 si no existe"
    
    print("Test index_of: PASADO")


"""
Llamar a las pruebas para que todas funcionen correctamente
"""
if __name__ == "__main__":
    test_index_of()
    test_get_middle()
    test_is_palindrome()
    print("\n¡Todas las pruebas se ejecutaron con éxito")
  
