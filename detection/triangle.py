class Triangle:
    def __init__(self, start_x, end_x, start_high_y, start_low_y, end_high_y, end_low_y, type, start_datetime):
        self.start_x = start_x
        self.end_x = end_x

        self.start_high_y = start_high_y
        self.start_low_y = start_low_y
        
        self.end_high_y = end_high_y
        self.end_low_y = end_low_y

        # type (ascending(1)/descending(-1)/symmetrical(0))
        if type not in [-1, 0, 1]:
            raise ValueError("Triangle type must be one of: -1, 0, 1 where -1: descending, 0: symmetrical, 1: ascending")
        
        self._type = type
        self._start_datetime = start_datetime

    @property
    def type(self):
        return self._type
    
    @property
    def type_string(self):
        if self.type == -1:
            return "descending"
        elif self.type == 0:
            return "symmetrical"
        else:
            return "ascending"
    
    @property
    def start_datetime(self):
        return self._start_datetime

    def get_xs(self):
        return [self.start_x, self.end_x]
    
    def get_high_ys(self):
        return [self.start_high_y, self.end_high_y]
    
    def get_low_ys(self):
        return [self.start_low_y, self.end_low_y]
