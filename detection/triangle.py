class Triangle:
    def __init__(self, start_x, end_x, start_high_y, start_low_y, end_high_y, end_low_y):
        self.start_x = start_x
        self.end_x = end_x

        self.start_high_y = start_high_y
        self.start_low_y = start_low_y
        
        self.end_high_y = end_high_y
        self.end_low_y = end_low_y

    def get_xs(self):
        return [self.start_x, self.end_x]
    
    def get_high_ys(self):
        return [self.start_high_y, self.end_high_y]
    
    def get_low_ys(self):
        return [self.start_low_y, self.end_low_y]
