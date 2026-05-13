from node import Node
class City(Node):
    def __init__(self, id, name):
        super().__init__(id, name)

        self.lat = float(str(lat).replace(",", ".")) if lat else None
        self.lon = float(str(lon).replace(",", ".")) if lon else None