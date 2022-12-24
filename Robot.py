class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, commands: str):
        new_x = self.x
        new_y = self.y
        for command in commands:
            match command:
                case  "N":
                    new_y += 1
                    if new_y not in range(0, 101):
                        return "Robot can't move this way!"
                case  "S":
                    new_y -= 1
                    if new_y not in range(0, 101):
                        return "Robot can't move this way!"
                case  "E":
                    new_x += 1
                    if new_x not in range(0, 101):
                        return "Robot can't move this way!"
                case  "W":
                    new_x -= 1
                    if new_x not in range(0, 101):
                         return "Robot can't move this way!"

        else:
            self.x = new_x
            self.y = new_y
            return self.x, self.y

robot = Robot(0, 0)
print(robot.move("NNNNW"))

