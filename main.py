import pygame
import sys

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Definindo a câmera
camera = [0, 0, -5]  # Posição da câmera

# Definindo a esfera na cena
sphere_pos = [0, 0, 0]  # Posição da esfera
sphere_radius = 1  # Raio da esfera
sphere_color = (255, 255, 255)  # Cor da esfera           

def intersect_ray_sphere(origin, direction, sphere_center, sphere_radius):
    oc = [origin[0] - sphere_center[0], origin[1] - sphere_center[1], origin[2] - sphere_center[2]]
    a = direction[0] ** 2 + direction[1] ** 2 + direction[2] ** 2
    b = 2 * (oc[0] * direction[0] + oc[1] * direction[1] + oc[2] * direction[2])
    c = oc[0] ** 2 + oc[1] ** 2 + oc[2] ** 2 - sphere_radius ** 2

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return -1  # Não há interseção

    t1 = (-b - discriminant ** 0.5) / (2 * a)
    t2 = (-b + discriminant ** 0.5) / (2 * a)

    return min(t1, t2)  # Retorna o menor valor positivo de t


def ray_casting():
    for x in range(width):
        for y in range(height):
            # Transforma o x e y da tela em coordenadas entre -1 e 1
            normalized_x = (2 * x - width) / width
            normalized_y = (1 - 2 * y / height)

            # Direção do raio a partir da câmera para o pixel
            ray_direction = [normalized_x, normalized_y, 1]

            # Verifica a interseção do raio com a esfera
            t = intersect_ray_sphere(camera, ray_direction, sphere_pos, sphere_radius)
            ray_hits_sphere = t > 0

            # Se o raio atinge a esfera, pinte o pixel com a cor da esfera
            # Senão, pinte o pixel com a cor de fundo (preto)
            screen.set_at((x, y), sphere_color if ray_hits_sphere else (0, 0, 0))

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ray_casting()

    # Atualiza a tela
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
