from shape import Shape

class Oval(Shape):
    def get_radius(self):
        return self.o_radius

    def set_radius(self, value):
        self.o_radius = value

    radius = property(get_radius, set_radius)

    def calculate_area(self):
        self.area = self.o_radius**2 * 3.14
        return float(self.area)

    def get_info(self):
        print(f'Shape {self.name}. Side = {self.o_radius}. Area = {self.area}')