from shape import Shape

class Square(Shape):
    def get_side(self):
        return self.sq_side

    def set_side(self, value):
        self.sq_side = value

    side = property(get_side, set_side)

    def calculate_area(self):
        self.area = self.sq_side**2
        return float(self.area)

    def get_info(self):
        print(f'Shape {self.name}. Side = {self.sq_side}. Area = {self.area}')