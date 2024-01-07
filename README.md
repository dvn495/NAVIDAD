# Ejercicios-navidad

# EJERICIO 1:

# 	Sumador de Números Enteros Positivos

​	        Este es un simple programa en Python que permite al usuario ingresar tres números enteros positivos y realiza la suma de los mismos. El 		programa utiliza un bucle "while" para mantenerse en ejecución mientras el usuario desee realizar más operaciones.

## Cómo utilizar el programa

1. ingresar tres números enteros positivos.
2. El programa mostrará la suma de los números ingresados.
3. Se le preguntará si desea realizar otra operación.
4. Si selecciona "S" (sí), se le pedirá que ingrese tres nuevos números.
5. Si selecciona "N" (no), el programa se cerrará.

## Notas

- El programa maneja errores para garantizar que el usuario ingrese números enteros positivos válidos.
- El comando "os.system("cls")" se utiliza para borrar la pantalla en sistemas Windows. Si está utilizando un sistema diferente, puede cambiarlo a "os.system("clear")".
- Si el usuario ingresa un valor no entero, se manejará la excepción "ValueError" y se le pedirá que ingrese los valores nuevamente.

# Desarrollo y Funcionalidad del Código

1. **Importación de la Librería os:**
   - Se importa la librería os para utilizar la función os.system más adelante. En este código, se utiliza para limpiar la pantalla en sistemas Windows (os.system("cls")).
2. **Inicialización de la Variable SumActive:**
   - Se inicializa la variable SumActive  como True. Esta variable controla la ejecución del bucle while. Mientras SumActive sea True, el programa seguirá pidiendo al usuario ingresar números y realizar sumas.
3. **Bucle while:**
   - Se utiliza un bucle `while` que se ejecuta mientras `SumActive` sea `True`.
4. **Manejo de Excepciones con `try` y `except`:**
   - Se envuelve el bloque de código dentro de un bloque `try-except` para manejar posibles excepciones, específicamente `ValueError`, que se produce si el usuario ingresa un valor no entero.
5. **Entrada de Números del Usuario:**
   - El programa solicita al usuario que ingrese tres números enteros (`num1`, `num2`, `num3`).
6. **Verificación de Números Positivos:**
   - Se verifica que los tres números ingresados (`num1`, `num2`, `num3`) sean mayores o iguales a cero.
7. **Suma de Números:**
   - Si los números son positivos, se realiza la suma de los tres números y se muestra el resultado al usuario.
8. **Solicitud de Otra Operación:**
   - Se le pregunta al usuario si desea realizar otra operación. La respuesta se almacena en la variable `Seleccion`.
9. **Control del Bucle y Cierre del Programa:**
   - Dependiendo de la respuesta del usuario, `SumActive` se establece en `True` para continuar ejecutando el bucle o en `False` para salir del bucle y cerrar el programa.
10. **Manejo de Errores:**

- Si se produce una excepción `ValueError` (cuando el usuario ingresa un valor no entero), se imprime un mensaje indicando que se debe ingresar un entero positivo y se le pide al usuario que presione una tecla para continuar.

**Variables:**

- **`SumActive`:** Controla la ejecución del bucle `while`. Si es `True`, el programa continuará solicitando y sumando números. Si es `False`, el programa se cerrará.
- **`num1`, `num2`, `num3`:** Almacenan los números ingresados por el usuario.
- **`Seleccion`:** Almacena la respuesta del usuario sobre si desea realizar otra operación.

# EJERICIO 2 Y 3:

# Calculadora de Índice de Masa Corporal (IMC)

Este es un programa en Python que permite a los usuarios ingresar datos sobre su peso, altura, nombre y edad, y calcula el Índice de Masa Corporal (IMC) clasificándolo en diferentes categorías. Además, realiza un conteo del número de estudiantes en cada categoría de IMC.

## Cómo Utilizar el Programa

1. ingrese nombre, edad, peso en kg y altura en metros.
2. El programa calculará el IMC y mostrará la clasificación correspondiente.
3. Se le preguntará si desea registrar otra persona (S) o pasar a ver el conteo (N).
4. Después de registrar a 20 estudiantes, el programa mostrará un resumen del conteo de estudiantes en cada categoría de IMC.
5. Se le preguntará si desea ingresar más datos (S) o no (N).
6. El programa se cerrará cuando el usuario elija no ingresar más datos.

## Desarrollo del Código

1. **Importación de la Librería `os`:**
   - Se importa la librería `os` para utilizar la función `os.system` y limpiar la pantalla en sistemas Windows (`os.system("cls")`).
2. **Inicialización de Variables:**
   - Se inicializan las variables `isActive`, `estudiantes`, `NumEstudiantes`, `PesoNormal`, `Sobrepeso`, `ObesidadI`, `ObesisdadII` y `ObesidadIII`.
3. **Bucle Principal `while`:**
   - Se utiliza un bucle principal (`while isActive`) para controlar la ejecución del programa.
4. **Bucle `while` para Ingresar Datos de Estudiantes:**
   - Se utiliza un bucle `while` para solicitar datos de hasta 20 estudiantes. Se manejan excepciones en caso de errores en la entrada de datos.
5. **Cálculo del IMC y Clasificación:**
   - Se calcula el IMC para cada estudiante y se clasifica en diferentes categorías (normal, sobrepeso, obesidad I, obesidad II, obesidad III).
6. **Conteo de Estudiantes en Cada Categoría:**
   - Se utiliza un bucle `for` para contar el número de estudiantes en cada categoría y se almacenan en variables correspondientes.
7. **Impresión de Resumen:**
   - Se imprime un resumen del conteo de estudiantes en cada categoría de IMC.
8. **Pregunta al Usuario para Continuar o Salir:**
   - Se le pregunta al usuario si desea ingresar más datos. Si selecciona 'S', se continúa; si selecciona 'N', el programa se cierra.

# EJERCICIO 4:

#  Analizador de Números

Este programa en Python permite al usuario ingresar números y realiza varias estadísticas y análisis sobre ellos.

## Cómo Utilizar el Programa

1. ingrese los números. El programa acepta números enteros positivos.
2. Después de ingresar cada número, el programa proporcionará información sobre el tipo de número (par, impar), su rango (menor de 10, entre 20 y 50, mayor a 100), y contará la cantidad de números en cada categoría.
3. Ingrese un número negativo para finalizar la entrada de datos.
4. El programa mostrará un resumen con estadísticas sobre los números ingresados.

## Desarrollo del Código

1. **Importación de la Librería `os`:**
   - Se importa la librería `os` para utilizar la función `os.system` y limpiar la pantalla en sistemas Windows (`os.system("cls")`).
2. **Inicialización de Variables:**
   - Se inicializan las variables `n`, `par`, `menor10`, `entre20`, `mas100`, `impar`, `numerospar`, `numerosimpar` y `isActive`.
3. **Bucle Principal `while`:**
   - Se utiliza un bucle principal (`while isActive`) para controlar la entrada de números. El programa se detiene cuando se ingresa un número negativo.
4. **Manejo de Excepciones con `try` y `except`:**
   - Se envuelve el bloque de código dentro de un bloque `try-except` para manejar posibles excepciones, específicamente `ValueError`, que se produce si el usuario ingresa un valor no entero.
5. **Análisis de Números y Conteo:**
   - Se analiza cada número ingresado y se cuenta en las categorías correspondientes (par, impar, menor de 10, entre 20 y 50, mayor a 100).
6. **Impresión de Estadísticas:**
   - Después de que el usuario ingresa un número negativo, se imprime un resumen con estadísticas sobre los números ingresados, incluyendo el total, el total de pares, el promedio de números pares, el promedio de números impares, y la cantidad de números en cada categoría

# EJERCICIO INTERMEDIO 1:

#  Sistema de Registro de Ciudades y Sismos

Este es un sistema interactivo desarrollado en Python para registrar ciudades, sus sismos asociados y realizar análisis de riesgo.

## Estructura del Código

El sistema consta de tres módulos principales: `main`, `menus`, `sismos` y `ciudades`. A continuación, se describen brevemente cada uno de ellos.

### `intermedio1`

Este módulo controla la ejecución del programa principal y utiliza los otros módulos para realizar diversas acciones, como registrar ciudades, sismos, buscar información y generar informes de riesgo.

### `menusint1`

Contiene funciones para mostrar menús al usuario y manejar la entrada de datos. Incluye el menú principal y la función para registrar sismos.

### `sismosint1`

Maneja la información relacionada con los sismos, incluido el cálculo del riesgo y la generación de informes.

### `ciudadesint1`

Maneja la información relacionada con las ciudades, como su registro y búsqueda.

## Cómo Utilizar el Sistema

1. Siga las instrucciones del menú principal para realizar diferentes acciones, como registrar ciudades, sismos, buscar información y generar informes de riesgo.
2. Utilice las funciones proporcionadas en los diferentes menús para interactuar con el sistema.

## Detalles Adicionales

- Se han incorporado mensajes de error y manejo de excepciones para mejorar la robustez del sistema.
- El sistema permite registrar hasta 5 ciudades, cada una con la posibilidad de registrar hasta 5 sismos.
- Se proporciona un informe de riesgo que clasifica el riesgo de las ciudades según el promedio de los niveles de sismos registrados.

VARIABLES:

### En el módulo `intermedio1`:

- **`isActive` (boolean):**
  - Controla la ejecución del programa principal.
- **`opmenu` (int):**
  - Almacena la opción seleccionada por el usuario en el menú principal.
- **`conteociudades` (int):**
  - Contador de ciudades registradas.
- **`promedioriesgo` (list):**
  - Lista que almacena los promedios de riesgo de cada ciudad.
- **`listaciudades` (list):**
  - Lista que contiene información sobre las ciudades y sus sismos asociados.

### En el módulo `menusint1`:

- **`menu` (str):**
  - Menú principal que se muestra al usuario.
- **`hasError` (boolean):**
  - Indica si ha habido un error en la entrada del usuario.

### En el módulo `sismosint1`:

- **`nombre_ciudad` (str):**
  - Almacena el nombre de la ciudad para el informe de riesgo.
- **`lista_sismos` (list):**
  - Lista que contiene los niveles de sismos registrados para una ciudad.
- **`riesgo` (float):**
  - Almacena el riesgo calculado para una ciudad.
- **`promedio` (float):**
  - Almacena el promedio de riesgo de todas las ciudades.

### En el módulo `ciudadesint1`:

- **`conteociudades` (int):**
  - Contador de ciudades utilizado para limitar el número de ciudades que se pueden registrar.
- **`isActive` (boolean):**
  - Controla la ejecución del registro de ciudades.
- **`ciudad` (int):**
  - Contador de ciudades registrado durante el proceso de registro.
- **`rta` (str):**
  - Respuesta del usuario durante el registro de ciudades.
- **`citta` (list):**
  - Lista que contiene información sobre una ciudad y sus sismos asociados.
- **`buscarcity` (str):**
  - Almacena el nombre de la ciudad ingresado por el usuario para buscar información.

# EJERICICIO INTERMEDIO 2

# Sistema de Gestión de Consumo y CO2

Este proyecto implementa un sistema de gestión de consumo y emisiones de CO2 para dependencias. Proporciona funcionalidades como el registro de dependencias, el seguimiento del consumo eléctrico y de transporte, y la visualización de las emisiones de CO2. A continuación, se detallan los módulos principales del sistema:

### Módulo `main`

En este módulo, se encuentra la lógica principal del programa, que interactúa con los módulos de menús (`menusint2`), consumo (`consumoint2`), y CO2 (`co2int2`). El usuario puede registrar dependencias, ingresar el consumo eléctrico y de transporte, y obtener información sobre las emisiones de CO2.

### Módulo `co2int2`

Este módulo contiene funciones para visualizar las emisiones de CO2 de una dependencia específica (`VerCo2`) y encontrar la dependencia que produce la mayor cantidad de CO2 (`MayorCo2`).

### Módulo `consumoint2`

El módulo `consumoint2` se encarga de gestionar el registro del consumo eléctrico y de transporte para cada dependencia. También utiliza el módulo `anualmensualint2` para manejar el registro bimestral del consumo eléctrico.

### Módulo `menusint2`

En este módulo, se define el menú principal del sistema, proporcionando opciones para registrar dependencias, ingresar consumos, y visualizar datos relacionados con las emisiones de CO2.

### Módulo `anualmensualint2`

El módulo `anualmensualint2` contiene la función `consumobimestral`, que permite al usuario ingresar el consumo bimestral.

### Ejecución del Programa

1. **Registro de Dependencias:**
   - El usuario puede registrar dependencias con sus respectivos consumos eléctricos y de transporte.
2. **Registro de Consumo:**
   - Permite al usuario ingresar el consumo eléctrico y de transporte para una dependencia específica.
3. **Visualización de Emisiones de CO2:**
   - Proporciona la capacidad de ver las emisiones de CO2 de una dependencia seleccionada.
4. **Dependencia con Mayor CO2:**
   - Identifica la dependencia que produce la mayor cantidad de CO2.
5. **Salir:**
   - Finaliza la ejecución del programa.

### Uso del Programa

1. **Menú Principal:**
   - Selecciona la opción deseada ingresando el número correspondiente.
2. **Registro de Dependencias:**
   - Ingresa el nombre de la dependencia y su consumo eléctrico y de transporte.
3. **Registro de Consumo:**
   - Ingresa el tipo de consumo (eléctrico o de transporte) y la cantidad correspondiente.
4. **Visualización de Emisiones de CO2:**
   - Ingresa el nombre de la dependencia y visualiza las emisiones de CO2 asociadas.
5. **Dependencia con Mayor CO2:**
   - Identifica y muestra la dependencia que produce la mayor cantidad de CO2.
6. **Salir:**
   - Finaliza la ejecución del programa.

**Variables del Módulo `main`:**

- `isActive`: Booleano que indica si el programa está en ejecución.
- `dependencias`: Lista que almacena las dependencias registradas.
- `opmenu`: Entero que almacena la opción del menú seleccionada por el usuario.

**Variables del Módulo `co2int2`:**

- `dependenciamayor`: Cadena que almacena el nombre de la dependencia con mayor CO2.
- `aux`: Flotante que sirve como variable auxiliar en el cálculo de la dependencia con mayor CO2.
- `transporte`: Flotante que almacena las emisiones de CO2 por transporte de una dependencia.
- `electricidad`: Flotante que almacena las emisiones de CO2 por consumo eléctrico de una dependencia.

**Variables del Módulo `consumoint2`:**

- `is_dependencia`: Booleano que indica si se ha encontrado la dependencia especificada.
- `factoremisionelec`: Flotante que representa el factor de emisión para el consumo eléctrico.
- `factoremisiontransporte`: Flotante que representa el factor de emisión para el consumo de transporte.
- `isActive`: Booleano que controla la ejecución del registro de consumo.
- `buscar`: Cadena que almacena el nombre de la dependencia que se busca.

**Variables del Módulo `menusint2`:**

- `menu`: Cadena que contiene el menú principal del sistema.

**Variables del Módulo `anualmensualint2`:**

- `isBimestral`: Booleano que controla la ejecución del registro bimestral.
- `seleccion`: Entero que almacena la opción seleccionada por el usuario en el registro bimestral.
- `consumo`: Flotante que almacena el valor del consumo ingresado por el usuario en el registro bimestral.