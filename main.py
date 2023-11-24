import pygame
from sirius.sphere import Sphere
from sirius.plane import Plane
from sirius.vector import Vector
from sirius.color import Color
from sirius.camera import Camera
from sirius.scene import Scene

QUIT = 'q'

def main():
    pygame.init()
    width, height = 800, 600
    location = Vector(0, 0, 0)
    focus = Vector(0, 0, 1)
    v_up = Vector(0, 1, 0)
    distance = 40
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Ray Casting')

    clock = pygame.time.Clock()

    spheres = [
        Sphere(Vector(0, 0, 0), 100, Color(255, 0, 0)),  # Esfera vermelha
        Sphere(Vector(150, 100, 100), 50, Color(0, 255, 0))  # Esfera verde
    ]

    planes = [
        Plane(Vector(10, 75, 80), Vector(0, 1, 0), Color(255, 255, 255))
    ]

    scene = Scene()

    for sphere in spheres:
        scene.addSphere(sphere)
    
    for plane in planes:
        scene.addPlane(plane)

    camera = Camera(location, focus, v_up, distance, width, height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        matrix = camera.take(scene)
        
        # Criando uma surface a partir da matriz
        surface = pygame.surfarray.make_surface(matrix)

        # Redimensionando a surface para o tamanho da janela
        surface = pygame.transform.scale(surface, (width, height))

        # Blit da surface na tela do Pygame
        screen.blit(surface, (0, 0))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
