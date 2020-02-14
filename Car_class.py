import pygame, random


class Car (object):
    def __init__(self, x, y, width, height, start_pos):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.start_pos = start_pos
        self.driveCount = 0
        self.left = False
        self.right = False
        self.down = False
        self.up = False
        self.park = False
        self.velocity = 18

        # self.hit_box1 = (self.x + 7, self.y, 109, 63)
        # self.hit_box2 = (self.x + 2, self.y + 1, 107, 61)
        # self.hit_box3 = (self.x + 3, self.y + 2, 58, 103)
        # self.hit_box4 = (self.x - 4, self.y, 62, 100)

    def draw_car(self, window):

        drive_left = pygame.image.load ('car_left.jpg')
        drive_right = pygame.image.load ('car_right.jpg')
        drive_up = pygame.image.load ('car_up.jpg')
        drive_down = pygame.image.load ('car_down.jpg')
        drive_left = pygame.transform.scale (drive_left, (96, 50))
        drive_right = pygame.transform.scale (drive_right, (96, 51,))
        drive_up = pygame.transform.scale (drive_up, (42, 93))
        drive_down = pygame.transform.scale (drive_down, (46, 86))
        # self.hit_box1 = (self.x, self.y, 98, 54)
        # self.hit_box2 = (self.x, self.y + 1, 99, 56)
        # self.hit_box3 = (self.x - 3, self.y + 2, 50, 93)
        # self.hit_box4 = (self.x - 3, self.y, 54, 90)

        if self.driveCount == 0 and self.park == False:
            window.blit (drive_up, (self.x, self.y))
            # pygame.draw.rect (window, (255, 0, 0), self.hit_box, 2)

        if self.left:
            window.blit (drive_left, (self.x, self.y))
            # pygame.draw.rect (window, (255, 0, 0), self.hit_box1, 2)
            self.driveCount += 1

        if self.right:
            window.blit (drive_right, (self.x, self.y))
            # pygame.draw.rect (window, (255, 0, 0), self.hit_box2, 2)
            self.driveCount += 1

        if self.up:
            window.blit (drive_up, (self.x, self.y))
            # pygame.draw.rect (window, (255, 0, 0), self.hit_box3, 2)
            self.driveCount += 1

        if self.down:
            window.blit (drive_down, (self.x, self.y))
            # pygame.draw.rect (window, (255, 0, 0), self.hit_box4, 2)
            self.driveCount += 1

    def getRect(self):
        return pygame.Rect (self.x, self.y, self.width, self.height // 2)

    def hit(self, cp, plat):

        if cp.getRect ().colliderect (self.getRect ()):
            if self.right:
                self.x = self.x - 20
                cp.x = cp.x + 3

            if self.left:
                self.x = self.x + 20
                cp.x = cp.x - 3
            if self.down:
                self.y = self.y - 20
                cp.y = cp.y + 3
            if self.up:
                self.y = self.y + 20
                cp.y = cp.y - 3

        if plat.getRect ().colliderect (self.getRect ()):
            if self.right:
                self.x = self.x - 20

            if self.left:
                self.x = self.x + 20

            if self.down:
                self.y = self.y - 20

            if self.up:
                self.y = self.y + 20

    def parking(self, ps):

        parkingCountx = [934, 544, 500, 662, 537, 940, 490, 1356, 922]

        parkingCounty = [2, 308, 371, 7, 245, 238, 112, 119, 623]

        if ps.getRect ().colliderect (self.getRect ()):
            self.x = 1146
            self.y = 644
            num = random.randint (0, 8)
            ps.x = parkingCountx[num]
            ps.y = parkingCounty[num]
            print ('park')

    def scoring(self, window, ps, font):
        '''x_dif = self.x - ps.x
        y_dif = self.y - ps.y
        score = x_dif + 104, y_dif - 10'''
        x_dis = self.x - 490 + self.width
        y_dis = self.y - 112
        score = x_dis, y_dis

        '''if score[0] >= 0 and score[0] < 41 and score[1] <= 4 and score[1] > -19:
            print ('YOU WIN')'''
        # -8,10 y
        #
        if score[0] >= -8 and score[0] < 10 and score[1] >= 32 and score[1] > -4:
            print ('YOU WIN')


class CPU (object):
    def __init__(self, x, y, width, height, start_pos):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.start_pos = start_pos

    def draw_car(self, window):
        drive_left = pygame.image.load ('car_left.jpg')
        drive_right = pygame.image.load ('car_right.jpg')
        drive_up = pygame.image.load ('car_up.jpg')
        drive_down = pygame.image.load ('car_down.jpg')
        drive_left = pygame.transform.scale (drive_left, (96, 50))
        drive_right = pygame.transform.scale (drive_right, (96, 51,))
        drive_up = pygame.transform.scale (drive_up, (42, 93))
        drive_down = pygame.transform.scale (drive_down, (46, 86))

        if self.start_pos == 1:
            window.blit (drive_left, (self.x, self.y))
            # self.hit_box = self.hit_box1

        if self.start_pos == 2:
            window.blit (drive_right, (self.x, self.y))
            # self.hit_box = self.hit_box2

        if self.start_pos == 3:
            window.blit (drive_up, (self.x, self.y))
            # self.hit_box = self.hit_box3

        if self.start_pos == 4:
            window.blit (drive_down, (self.x, self.y))
            # self.hit_box = self.hit_box4

    def getRect(self):
        return pygame.Rect (self.x, self.y, self.width, self.height // 2)

    def hit(self):
        pass


class ParkSpot (object):
    def __init__(self, color, char, fill):
        self.x, self.y, self.height, self.width = char
        self.color = color
        self.fill = fill

    def draw_spot(self, window):
        pygame.draw.rect (window, self.color, (self.x, self.y, self.height, self.width), self.fill)

    def getRect(self):
        return pygame.Rect (self.x, self.y, self.width, self.height // 2)


class Platform (object):
    def __init__(self, color, char, fill):
        self.x, self.y, self.height, self.width = char
        self.color = color
        self.fill = fill

    def draw(self, window):
        pygame.draw.rect (window, self.color, (self.x, self.y, self.height, self.width), self.fill)

    def getRect(self):
        return pygame.Rect (self.x, self.y, self.width, self.height // 2)

    def hit(self):
        pass
        # reseting game window
