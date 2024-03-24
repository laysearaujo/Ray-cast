import cv2
import numpy as np

from src.graphic.camera import Camera
from src.graphic.scene import Scene
from src.geometry.vector import Vector
from src.geometry.triangularMesh import TriangularMesh
from src.data.SecondDeliveryTestData import vertices, triangles

def main():
    # Utilize os dados dos vértices e triângulos do seu módulo ou arquivo SecondDeliveryTestData
    width, height = 800, 600
    v_up = Vector(0, 1, 0)

    # Ajuste as dimensões do objeto para centralizá-lo na cena
    object_width = 100  # Largura do objeto na direção X
    object_height = 100  # Altura do objeto na direção Y
    object_depth = 100  # Profundidade do objeto na direção Z

    # Calcula o ponto de foco no centro do objeto
    focus = Vector(object_width / 2, object_height / 2, object_depth / 2)
    
    # Ajusta a posição da câmera para ficar na frente do objeto
    distance = max(object_width, object_height, object_depth) * 2  # Ajuste conforme necessário para melhor visualização
    location = focus.add(Vector(0, 0, distance))

    # Criar a malha triangular e adicionar os triângulos a ela
    mesh = TriangularMesh(vertices, triangles)

    # Criar a cena e adicionar a malha
    scene = Scene()
    scene.addMesh(mesh)

    # Configurar a câmera e gerar a imagem
    camera = Camera(location, focus, v_up, distance, width, height)
    matrix = camera.take(scene)

    # Converter a matriz de cores para uma imagem OpenCV
    img = np.zeros((height, width, 3), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            color = matrix[y][x]
            img[y][x] = [int(color.r), int(color.g), int(color.b)]

    cv2.imshow('Render', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
