# Binary Tree

# Un árbol binario es una estructura de datos jerárquica en la que cada nodo tiene como máximo dos hijos, 
# conocidos como el hijo izquierdo y el hijo derecho. Cada nodo puede tener cero, uno o dos hijos.

# En un árbol binario, el primer nodo se llama nodo raíz y no tiene ningún nodo padre. 
# Los nodos que no tienen hijos se llaman hojas. Todos los demás nodos se llaman nodos internos.

# La forma en que se organizan los nodos en un árbol binario es importante, 
# ya que permite una búsqueda eficiente. En un árbol binario de búsqueda, 
# por ejemplo, los valores se organizan de tal manera que cada nodo izquierdo 
# tiene un valor menor que el nodo padre, y cada nodo derecho tiene un valor mayor que el nodo padre.

# Los árboles binarios se utilizan comúnmente en la informática para almacenar y buscar datos, 
# ya que permiten una búsqueda rápida y eficiente de valores. También se utilizan en algoritmos 
# de clasificación, análisis sintáctico de lenguajes de programación y muchas otras aplicaciones.

# Primero, definimos una clase para los nodos del árbol binario:

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Luego, definimos una clase para el árbol binario en sí mismo, que tendrá una referencia al nodo raíz:
class ArbolBinario:
    def __init__(self):
        self.raiz = None
# Ahora, agregamos un método para insertar un nuevo nodo en el árbol. 
# Este método tomará un valor como argumento y buscará su lugar en el árbol. 
# Si el valor ya existe, lo ignorará:
    def insertar(self, valor):
            nuevo_nodo = Nodo(valor)
            if self.raiz is None:
                self.raiz = nuevo_nodo
            else:
                nodo_actual = self.raiz
                while True:
                    if valor < nodo_actual.valor:
                        if nodo_actual.izquierda is None:
                            nodo_actual.izquierda = nuevo_nodo
                            break
                        else:
                            nodo_actual = nodo_actual.izquierda
                    elif valor > nodo_actual.valor:
                        if nodo_actual.derecha is None:
                            nodo_actual.derecha = nuevo_nodo
                            break
                        else:
                            nodo_actual = nodo_actual.derecha
                    else:
                        break
    # Finalmente, agregamos un método para imprimir los valores del árbol en orden:
    def imprimir_en_orden(self, nodo_actual):
            if nodo_actual is not None:
                self.imprimir_en_orden(nodo_actual.izquierda)
                print(nodo_actual.valor)
                self.imprimir_en_orden(nodo_actual.derecha)
# Con esto, podemos crear y usar un árbol binario en Python de la siguiente manera:
arbol = ArbolBinario()
arbol.insertar(5)
arbol.insertar(2)
arbol.insertar(7)
arbol.insertar(1)
arbol.insertar(9)
arbol.imprimir_en_orden(arbol.raiz)
