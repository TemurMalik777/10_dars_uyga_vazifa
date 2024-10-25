class Car:
    def __init__(self, brand: str, model: str, color: str):
        self.brand = brand
        self.model = model
        self.color = color

    def info(self) -> str:
        return f"""
BRAND: {self.brand}
MODEL: {self.model}
COLOR: {self.color}"""

class Chevrolet(Car):
    def __init__(self, model: str, color: str, price: float, generation: int):
        super().__init__(Chevrolet, model, color)

        self.price = price
        self.generation = generation

    def info(self):
        return super().info() + f"""    
PRICE:  {self.price}
GENERATION  {self.generation}"""

cobalt = Chevrolet("Cobalt", "oq", 12500, 4)
print(cobalt.info())