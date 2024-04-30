import math


def euclideanDistance(tuple1, tuple2):
    """
    Bu fonksiyon, iki demet (her biri bir noktayı temsil eder) alır ve
    bu iki nokta arasındaki Öklid mesafesini döndürür.
    :param tuple1: (x1, y1)
    :param tuple2: (x2, y2)
    :return: float euclidean.
    """
    euclidean = math.sqrt((tuple2[0] - tuple1[0]) ** 2 + (tuple2[1] - tuple1[1]) ** 2)
    return euclidean


points = [(8, 5), (5, 9), (9, 9), (7, 6), (5, 2)]

# points listesinin ikili kombinasyonunu almalıyız.
kombinasyon_sayisi = math.factorial(len(points)) // (math.factorial(2) * math.factorial(len(points) - 2))
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        # distances listesindeki ikili kombinasyonlar ile mesafeleri hesaplayalım.
        distances.append(euclideanDistance(points[i], points[j]))

print(f"Verilen noktalar arasındaki min mesafe: {min(distances)}")
