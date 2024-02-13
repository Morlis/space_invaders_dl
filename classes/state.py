class State:
    PLAYER_Y = 382
    PLAYER_WITH = 30
    LIVES_POSITION = (20, 413)
    

    def __init__(self):
        self.points = 0
        self.player_X = None

    def reset(self):
        self.points = 0

    def process_image(self, image_bytes):
        self.__find_player_pos(image_bytes)

    def __find_player_pos(self, image_bytes):
        self.player_X = None

        current_x = None
        end = 0
        for i in range(end, image_bytes.shape[1]):
            if image_bytes[self.PLAYER_Y][i] != 0:
                current_x = i
                for end in range(i, image_bytes.shape[1]):
                    if image_bytes[self.PLAYER_Y][i] == 0:
                        if end - current_x >= self.PLAYER_WITH:
                            self.player_X = current_x
                            return
                        break
        