Conceptos

🔵 Fundamentos
- ¿Qué es programar?
- ¿Qué es Python y para qué sirve?
- ¿Qué es un programa y cómo se ejecuta?
- ¿Qué es una variable?
- Tipos de datos básicos: texto (str), número entero (int), número decimal (float), verdadero/falso (bool).
- Operaciones básicas con números (+, -, *, /).
- Mostrar información en pantalla: print().
- Pedir información al usuario: input().
- Convertir tipos de datos: int(), float(), str().
- ¿Qué es un error? Errores comunes para principiantes.


🔵 Lógica de programación
- Comparar datos: (==, !=, <, >, <=, >=).
- Tomar decisiones: if, else, elif.
- Combinar condiciones: and, or, not.
- Cómo escribir comentarios en el código (# comentario).
- Qué es la indentación y por qué es tan importante en Python.
- Buenas prácticas al nombrar variables (nombres claros, sin espacios).
- ¿Qué hacer cuando algo no funciona? (buscar, leer errores, no frustrarse).


🔵 Estructuras de control
- Repetir acciones con bucles: for y while.
- Salir de un bucle antes de tiempo: break y continue.
- Manejo básico de errores: try-except.


LECTURA

Introducción a Python
- Python es un lenguaje de programación de alto nivel, interpretado y de propósito general.
- Fue creado por Guido van Rossum y lanzado en 1991.
- Hoy en día es uno de los lenguajes más populares debido a su simplicidad, versatilidad y una enorme comunidad de desarrolladores.

¿Por qué aprender Python?
- Es fácil de leer y escribir, incluso para principiantes.
- Tiene una sintaxis limpia que favorece buenas prácticas de programación.
- Es ampliamente usado en áreas como desarrollo web, ciencia de datos, inteligencia artificial, automatización, y más.
  
CARACTERISTICAS PRINCIPALES:
- Sintaxis sencilla y similar al inglés.
- Multiparadigma: soporta programación orientada a objetos, funcional y procedural.
- Gran ecosistema de librerías y frameworks.
- Portabilidad: corre en Windows, Linux, MacOS y más.
- Extensibilidad: se puede integrar con otros lenguajes como C, C++ y Java.
- ¿Qué puedes hacer con Python?
- Desarrollo Web (con frameworks como Django, Flask)
- Análisis de Datos y Machine Learning (con Pandas, NumPy, TensorFlow)
- Automatización de tareas y scripts
- Videojuegos (con Pygame)
- Aplicaciones de escritorio
- Internet de las cosas (IoT)
- Mucho más...
  
CURIOSIDADES

El nombre Python no viene del animal 🐍, sino de un grupo de comedia británico llamado "Monty Python's Flying Circus".

Tu primer programa en Python

Veamos el clásico "¡Hola Mundo!":
print("¡Hola, mundo!")



Tipos de datos

![image](https://github.com/user-attachments/assets/97252244-4901-474b-9f8f-fc5b77ea8a16)


- Categoría	Tipo de Dato	Ejemplo	Descripción
- Primitivo	int	5, -10, 0	Números enteros
- Primitivo	float	3.14, -0.5, 0.0	Números decimales (reales)
- Primitivo	bool	True, False	Booleanos: verdadero o falso






Primitivo	str	"Hola", 'Python'	Cadenas de texto
Especial	NoneType	None	Representa ausencia de valor
Numérico	complex	1 + 2j, -3j	Números complejos
Colección	list	[1, 2, 3], ['a', 'b']	Lista ordenada y mutable
Colección	tuple	(1, 2), ('x', 'y')	Tupla ordenada e inmutable
Colección	set	{1, 2, 3}	Conjunto sin duplicados, no ordenado
Colección	frozenset	frozenset([1, 2, 3])	Conjunto inmutable
Colección	dict	{'a': 1, 'b': 2}	Diccionario (pares clave: valor)
Rango	range	range(5)	Secuencia de números (usado en bucles)
Binario	bytes	b'Hola'	Secuencia inmutable de bytes
Binario	bytearray	bytearray(5)	Array mutable de bytes
Binario	memoryview	memoryview(b'Hola')	Vista de un bloque de memoria

Primitivo
Los tipos primitivos son los datos más básicos que maneja Python. Incluyen los números enteros (int), números decimales (float), booleanos (bool) y cadenas de texto (str). Son la base para construir otros tipos de datos más complejos.

Especial
Los tipos especiales representan valores únicos o específicos en Python. Por ejemplo, NoneType representa la ausencia de valor con None, y complex permite trabajar con números complejos.

Colección
Las colecciones son tipos de datos que agrupan múltiples valores en una sola estructura. Ejemplos son list, tuple, set, frozenset y dict. Cada uno maneja los datos de forma distinta (ordenada, mutable, sin duplicados, etc.).

Numérico
Los tipos numéricos permiten trabajar con valores matemáticos. Python maneja int para enteros, float para decimales y complex para números complejos (con parte real e imaginaria).

Rango
El tipo range representa una secuencia de números, comúnmente usado en bucles for. Es muy eficiente porque no genera todos los números a la vez, sino que los produce a medida que se recorren.

Binario
Los tipos binarios (bytes, bytearray, memoryview) permiten trabajar con datos en formato binario. Son útiles para manipular archivos, imágenes, transmisiones de red y otros formatos de bajo nivel.
