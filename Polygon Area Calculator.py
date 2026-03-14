class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        pict = ''
        temp_Height = self.height
        while temp_Height > 0:
            pict += f"{'*' * self.width}\n"
            temp_Height -= 1
        return pict

    def get_amount_inside(self, other_shape):
        width_per = int(self.width / other_shape.width)
        height_per = int(self.height / other_shape.height)
        if width_per >= 1 and height_per >= 1:
            return width_per * height_per
        else:
            return 0

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_width(self, new_side):
        self.set_side(new_side)

    def set_height(self, new_side):
        self.set_side(new_side)

    def set_side(self, new_side):
        self.height = new_side
        self.width = new_side

    def __str__(self):
        return f'Square(side={self.width})'