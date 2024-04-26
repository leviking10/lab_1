import math

def calc_distance(point1, point2):
    """
    Calcule la distance euclidienne entre deux points dans l'espace 3D.
    Args:
        point1 (list): Une liste contenant les coordonnées [x, y, z] du premier point.
        point2 (list): Une liste contenant les coordonnées [x, y, z] du deuxième point.
    Returns:
        float: La distance euclidienne entre les deux points.
    """
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distance

def main():
    # Exemple de points
    points1 = [[1.0, 1.0, 1.0], [2.0, 2.0, 2.0], [3.0, 3.0, 3.0]]
    points2 = [[4.0, 4.0, 4.0], [5.0, 5.0, 5.0], [6.0, 6.0, 6.0]]

    # Calcul des distances en utilisant la fonction calc_distance
    distances = [calc_distance(point1, point2) for point1, point2 in zip(points1, points2)]

    # Affichage des distances
    print(distances)

if __name__ == "__main__":
    main()
