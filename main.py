# import pygame
from sirius.sphere import Sphere
from sirius.plane import Plane
from sirius.vector import Vector
from sirius.color import Color
from sirius.camera import Camera
from sirius.scene import Scene
from sirius.ray import Ray

QUIT = 'q'

def main():
    # pygame.init()
    width, height = 800, 600
    location = Vector(0, 0, 0)
    focus = Vector(0, 0, 1)
    v_up = Vector(0, 1, 0)
    distance = 40
    # screen = pygame.display.set_mode((width, height))
    # pygame.display.set_caption('Ray Tracer')

    # clock = pygame.time.Clock()

    spheres = [
        Sphere(Vector(5, 5, 5), 5, Color(255, 0, 0)),  # Esfera vermelha
        Sphere(Vector(5, 2, 2), 5, Color(0, 255, 0))  # Esfera verde
    ]

    planes = [
        Plane(Vector(5, 0, 0), Vector(1, 1, 0), Color(255, 255, 255))
    ]

    scene = Scene()

    for sphere in spheres:
        scene.addSphere(sphere)
    
    for plane in planes:
        scene.addPlane(plane)

    camera = Camera(location, focus, v_up, distance, width, height)

    # Teste de intersecção de raio
    ray = Ray(Vector(0,0,0), Vector(1,1,0))

    instersect1_color, instersect1_distance, _ = spheres[0].intersect(ray).values()
    print(f'Intersecção da esfera vermelha com o raio - distancia: {instersect1_distance}, cor: {instersect1_color}')
    instersect2_color, instersect2_distance, _ = spheres[1].intersect(ray).values()
    print(f'Intersecção da esfera verde com o raio - distancia: {instersect2_distance}, cor: {instersect2_color}')
    instersect3_color, instersect3_distance, _ = planes[0].intersect(ray).values()
    print(f'Intersecção da esfera vermelha com o plano - distancia: {instersect3_distance}, cor: {instersect3_color}')
    

    # running = True
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == QUIT:
    #             running = False

    matrix = camera.take(scene)
        
    # Criando uma surface a partir da matriz
    # surface = pygame.surfarray.make_surface(matrix)

    # Redimensionando a surface para o tamanho da janela
    # surface = pygame.transform.scale(surface, (width, height))

    # Blit da surface na tela do Pygame
    # screen.blit(surface, (0, 0))

    # pygame.display.flip()
    # clock.tick(60)

    # pygame.quit()

if __name__ == "__main__":
    main()
