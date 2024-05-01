import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir los colores
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Definir el tamaño de la pantalla
ANCHO = 600
ALTO = 400

# Definir el tamaño de la serpiente
TAMANO_CELDA = 20

# Definir la velocidad de la serpiente
VELOCIDAD = 10

# Crear la ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Snake Game")

# Reloj para controlar la velocidad de la serpiente
reloj = pygame.time.Clock()

# Función para mostrar el mensaje de texto
def mensaje_texto(texto, color, tamaño):
    fuente = pygame.font.SysFont(None, tamaño)
    mensaje = fuente.render(texto, True, color)
    pantalla.blit(mensaje, [ANCHO / 6, ALTO / 3])

# Función principal del juego
def juego():
    # Inicializar la posición y la longitud de la serpiente
    serpiente = [[ANCHO / 2, ALTO / 2]]
    longitud = 1

    # Posición aleatoria inicial de la comida
    comida = [random.randrange(0, ANCHO / TAMANO_CELDA) * TAMANO_CELDA,
              random.randrange(0, ALTO / TAMANO_CELDA) * TAMANO_CELDA]

    # Dirección inicial de la serpiente
    direccion = "DERECHA"

    # Variables para controlar la velocidad
    contador = 0
    cambio_x = TAMANO_CELDA
    cambio_y = 0

    # Bucle principal del juego
    juego_terminado = False
    while not juego_terminado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                juego_terminado = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and direccion != "DERECHA":
                    cambio_x = -TAMANO_CELDA
                    cambio_y = 0
                    direccion = "IZQUIERDA"
                elif evento.key == pygame.K_RIGHT and direccion != "IZQUIERDA":
                    cambio_x = TAMANO_CELDA
                    cambio_y = 0
                    direccion = "DERECHA"
                elif evento.key == pygame.K_UP and direccion != "ABAJO":
                    cambio_x = 0
                    cambio_y = -TAMANO_CELDA
                    direccion = "ARRIBA"
                elif evento.key == pygame.K_DOWN and direccion != "ARRIBA":
                    cambio_x = 0
                    cambio_y = TAMANO_CELDA
                    direccion = "ABAJO"

        # Mover la serpiente
        cabeza = []
        cabeza.append(serpiente[0][0] + cambio_x)
        cabeza.append(serpiente[0][1] + cambio_y)
        serpiente.insert(0, cabeza)

        # Si la serpiente come la comida
        if serpiente[0][0] == comida[0] and serpiente[0][1] == comida[1]:
            comida = [random.randrange(0, ANCHO / TAMANO_CELDA) * TAMANO_CELDA,
                      random.randrange(0, ALTO / TAMANO_CELDA) * TAMANO_CELDA]
            longitud += 1
        else:
            serpiente.pop()

        # Dibujar la pantalla
        pantalla.fill(BLANCO)
        pygame.draw.rect(pantalla, ROJO, [comida[0], comida[1], TAMANO_CELDA, TAMANO_CELDA])

        # Dibujar la serpiente
        for segmento in serpiente:
            pygame.draw.rect(pantalla, VERDE, [segmento[0], segmento[1], TAMANO_CELDA, TAMANO_CELDA])

        # Si la serpiente choca con los bordes
        if (serpiente[0][0] >= ANCHO or serpiente[0][0] < 0 or
            serpiente[0][1] >= ALTO or serpiente[0][1] < 0):
            juego_terminado = True

        # Si la serpiente choca consigo misma
        for segmento in serpiente[1:]:
            if serpiente[0][0] == segmento[0] and serpiente[0][1] == segmento[1]:
                juego_terminado = True

        # Actualizar la pantalla
        pygame.display.update()

        # Controlar la velocidad
        reloj.tick(VELOCIDAD)

# Ejecutar el juego
juego()

# Mostrar mensaje de juego terminado
pantalla.fill(BLANCO)
mensaje_texto("Juego Terminado", ROJO, 50)
pygame.display.update()

# Esperar un momento antes de cerrar la ventana
pygame.time.delay(2000)

# Salir de Pygame
pygame.quit()
