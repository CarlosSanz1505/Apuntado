# Proyecto Apuntado

## Instructivo

El juego se puede ejecutar al correr el script `PYGAME/apuntado.py`.

Al ejecutar por primera vez se deberan ingresar datos para Crear una Nueva Cuenta (predispuesto), y en posteriores ejecuciones el script detectará el jugador guardado (en `PYGAME/jugador.txt`) y será incializado desde la Pantalla `Menu`.

## Backlog

### Mockup

- [x] Añadir advertencia de riesgos de apuestas en los Términos y Condiciones.

### Producto Final

- [x] ***CREAR CUENTA*** (una sola vez, no hay que volver a Iniciar Sesión).

- [x] ***MODO BOT*** (sin realizar cambios al modo, de lo contrario, tocaría programar también Multijugador):

    - [x] Se visualizan el **Jugador** y el **Bot** en la **Mesa** (inicialmente vacía), los botones **Tocar** y **Ganar** (NO funcionales), el **Temporizador** de jugada (preferiblemente animado para simular conteo de 30 segundos), y el botón de **Abandonar Partida**.

- [x] ***PERSONALIZAR***:
    
    - [x] Elegir un aspecto de personalización para hacer funcional en el aplicativo: El **Avatar** o el **Estilo de Cartas**. El que se elija, debe verse reflejado en todas sus instancias dentro del aplicativo.

- [x] ***TOKENS***:

    - [x] Solo se visualiza la primera pantalla emergente al hacer click (**Interfaz de Paquetes**), sin ninguna opción de compra funcional. Incluir un botón de salida más visible para esta Interfaz.

- [ ] ***INFORMACIÓN DE CUENTA (OPCIONAL)***.

- [x] ***INFORMACIÓN DEL JUEGO ("Reglas y demás que consideremos importante")***.

### Pantallas

- [x] Autenticación
- [x] Crear Cuenta
- [x] Términos y Condiciones
- [x] Menú
- [ ] Cuenta (OPCIONAL)
- [x] Tokens
- [x] Personalizar
- [x] Información: Reglas y Tutorial
- [x] Bot

## Tecnologías:

Se desarrolla el aplicativo como un script de *Python*, programado usando la librería `pygame`.

## Advertencia:

"Al participar en este juego de apuestas de cartas, el jugador acepta cumplir con todos los terminos y condiciones establecidos a continuación:

Edad Mínima: Solo se permite la participación de personas mayores de 18 años. Cualquier persona que no cumpla con este requisito no podrá participar en el juego.

Responsabilidad del Jugador: Cada jugador es responsable de su propia conducta y acciones durante el juego. El juego se basa en la honestidad y el fair play, por lo que cualquier intento de fraude o trampa resultará en la descalificación inmediata del jugador

Las apuestas conllevan riesgos financieros significativos y pueden resultar en adicción al juego, afectando negativamente la salud mental, las relaciones personales y el desempeño laboral. Se recomienda practicar el juego de manera responsable y buscar ayuda si se experimentan problemas."
