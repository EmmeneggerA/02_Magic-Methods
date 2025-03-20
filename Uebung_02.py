import math

class Vector3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector3(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector3):
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            raise TypeError("Multiplication not supported between instances of 'Vector3' and '{}'".format(type(other)))
    
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return self * other
        else:
            return NotImplemented
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        return Vector3(
        x = (self.y * other.z) - (self.z * other.y)
        y = (self.z * other.x) - (self.x * other.z)
        z = (self.x * other.y) - (self.y * other.x)
        return Vector3(x, y, z)
    
    def normalize(self):
        magnitude = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        if magnitude == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector3(self.x / magnitude, self.y / magnitude, self.z / magnitude)

# Beispielnutzung
a = Vector3(3, 4, 2)
b = Vector3(2, 1, 0)

print("Addition:", a + b)
print("Subtraktion:", a - b)
print("Komponentenweise Multiplikation:", a * b)
print("Skalarmultiplikation:", a * 2)
print("Skalarprodukt:", a.dot(b))
print("Kreuzprodukt:", a.cross(b))
print("Normalisierter Vektor:", a.normalize())
