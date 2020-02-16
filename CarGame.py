import Car_class
import pygame

#initiating pygame
pygame.init ()
#initiating font
pygame.font.init ()
screen_height = 750
screen_width = 1400
window = pygame.display.set_mode ((screen_width, screen_height))
pygame.display.set_caption ('Car Game')
#Frames per second
clock = pygame.time.Clock ()
bg = pygame.image.load ('parking_lot.jpg')
bg = pygame.transform.scale (bg, (screen_width, screen_height))

#drawing parked cars, platforms,background, and main car, and score font
def draw_window():
    window.blit (bg, (0, 0))
    cp_car1.draw_car (window)
    cp_car2.draw_car (window)
    cp_car3.draw_car (window)
    cp_car4.draw_car (window)
    cp_car5.draw_car (window)
    cp_car6.draw_car (window)
    cp_car7.draw_car (window)
    cp_car8.draw_car (window)
    cp_car9.draw_car (window)
    cp_car10.draw_car (window)
    cp_car11.draw_car (window)
    cp_car12.draw_car (window)
    cp_car13.draw_car (window)
    cp_car14.draw_car (window)
    cp_car15.draw_car (window)
    cp_car16.draw_car (window)
    cp_car17.draw_car (window)
    cp_car18.draw_car (window)
    cp_car19.draw_car (window)
    # cp_car20.draw_car (window)
    cp_car21.draw_car (window)
    cp_car22.draw_car (window)
    cp_car23.draw_car (window)
    # cp_car24.draw_car (window)
    cp_car25.draw_car (window)
    cp_car26.draw_car (window)
    # cp_car27.draw_car (window)
    # cp_car28.draw_car (window)
    cp_car29.draw_car (window)
    cp_car30.draw_car (window)
    cp_car31.draw_car (window)
    cp_car32.draw_car (window)
    cp_car33.draw_car (window)
    cp_car34.draw_car (window)
    cp_car35.draw_car (window)
    cp_car36.draw_car (window)
    cp_car37.draw_car (window)
    cp_car38.draw_car (window)
    cp_car39.draw_car (window)
    cp_car40.draw_car (window)
    cp_car41.draw_car (window)
    cp_car42.draw_car (window)
    cp_car43.draw_car (window)
    cp_car44.draw_car (window)
    cp_car45.draw_car (window)
    cp_car46.draw_car (window)
    cp_car47.draw_car (window)
    cp_car48.draw_car (window)
    cp_car49.draw_car (window)
    cp_car50.draw_car (window)
    cp_car51.draw_car (window)
    platform1.draw (window)
    platform2.draw (window)
    platform3.draw (window)
    park7.draw_spot (window)
    Main_car.draw_car(window)
    ##scoring###
    Main_car.scoring(window,park7,font)

    #collision#
    for plat in plat_list:
        for cp in cp_list:
            for ps in park_list:
                #Main_car.parking (ps)
                Main_car.hit (cp, plat)
                Main_car.hit (cp, plat)


    pygame.display.update ()

#creating variables to call class instances
Main_car = Car_class.Car (1146, 644, 96, 96, 3)
cp_car1 = Car_class.CPU (26, 108, 96, 96, 1)
cp_car2 = Car_class.CPU (26, 180, 96, 96, 1)
cp_car3 = Car_class.CPU (26, 244, 96, 96, 1)
cp_car4 = Car_class.CPU (26, 308, 96, 96, 1)
cp_car5 = Car_class.CPU (26, 372, 96, 96, 1)
cp_car6 = Car_class.CPU (26, 436, 96, 96, 1)
cp_car7 = Car_class.CPU (26, 508, 96, 96, 1)
cp_car8 = Car_class.CPU (26, 572, 96, 96, 1)
cp_car9 = Car_class.CPU (1286, 182, 96, 96, 2)
cp_car10 = Car_class.CPU (1286, 238, 96, 96, 2)
cp_car11 = Car_class.CPU (1286, 301, 96, 96, 2)
cp_car12 = Car_class.CPU (1286, 364, 96, 96, 2)
cp_car13 = Car_class.CPU (1286, 427, 96, 96, 2)
cp_car14 = Car_class.CPU (1286, 497, 96, 96, 2)
cp_car15 = Car_class.CPU (1286, 301, 96, 96, 2)
cp_car16 = Car_class.CPU (250, 658, 96, 96, 4)
cp_car17 = Car_class.CPU (320, 658, 96, 96, 4)
cp_car18 = Car_class.CPU (390, 658, 96, 96, 4)
cp_car19 = Car_class.CPU (418, 441, 96, 96, 2)
cp_car20 = Car_class.CPU (411, 119, 96, 96, 2)
cp_car21 = Car_class.CPU (411, 182, 96, 96, 2)
cp_car22 = Car_class.CPU (411, 245, 96, 96, 2)
cp_car23 = Car_class.CPU (411, 308, 96, 96, 2)
cp_car24 = Car_class.CPU (411, 371, 96, 96, 2)
cp_car25 = Car_class.CPU (544, 371, 96, 96, 1)
cp_car26 = Car_class.CPU (544, 434, 96, 96, 1)
cp_car27 = Car_class.CPU (544, 308, 96, 96, 1)
cp_car28 = Car_class.CPU (544, 245, 96, 96, 1)
cp_car29 = Car_class.CPU (544, 182, 96, 96, 1)
cp_car30 = Car_class.CPU (544, 119, 96, 96, 1)
cp_car31 = Car_class.CPU (678, 14, 96, 96, 3)
cp_car32 = Car_class.CPU (732, 14, 96, 96, 3)
cp_car33 = Car_class.CPU (804, 14, 96, 96, 3)
cp_car34 = Car_class.CPU(876, 14, 96, 96, 3)
cp_car35 = Car_class.CPU (930, 14, 96, 96, 3)
cp_car36 = Car_class.CPU (1002, 14, 96, 96, 3)
cp_car37 = Car_class.CPU (1074, 14, 96, 96, 3)
cp_car38 = Car_class.CPU (1192, 14, 96, 96, 3)
cp_car39 = Car_class.CPU (602, 652, 96, 96, 4)
cp_car40 = Car_class.CPU (836, 238, 96, 96, 2)
cp_car41 = Car_class.CPU (836, 310, 96, 96, 2)
cp_car42 = Car_class.CPU (836, 364, 96, 96, 2)
cp_car43 = Car_class.CPU (836, 436, 96, 96, 2)
cp_car44 = Car_class.CPU (836, 634, 96, 96, 2)
cp_car45 = Car_class.CPU (998, 634, 96, 96, 1)
cp_car46 = Car_class.CPU (998, 490, 96, 96, 1)
cp_car47 = Car_class.CPU (998, 436, 96, 96, 1)
cp_car48 = Car_class.CPU (998, 364, 96, 96, 1)
cp_car49 = Car_class.CPU (998, 292, 96, 96, 1)
cp_car50 = Car_class.CPU (998, 238, 96, 96, 1)
cp_car51 = Car_class.CPU (1006, 554, 96, 96, 1)
platform1 = Car_class.Platform ((125, 125, 125), (527, 6, 134, 105), 0)
platform2 = Car_class.Platform ((125, 125, 125), (1263, 8, 134, 105), 0)
platform3 = Car_class.Platform ((125, 125, 125), (6, 635, 154, 145), 0)
platform4 = Car_class.Platform ((0, 0, 0), (504, 6, 134, 105), 0)
spot1 = Car_class.ParkSpot ((0, 255, 0), (924, 7, 63, 109), 2)
spot2 = Car_class.ParkSpot ((0, 255, 0), (544, 308, 109, 63), 2)
spot3 = Car_class.ParkSpot ((0, 255, 0), (411, 371, 109, 63), 2)
spot4 = Car_class.ParkSpot ((0, 255, 0), (662, 7, 63, 109), 2)
spot5 = Car_class.ParkSpot ((0, 255, 0), (537, 245, 109, 63), 2)
spot6 = Car_class.ParkSpot ((0, 255, 0), (852, 238, 109, 63), 2)
spot7 = Car_class.ParkSpot ((0, 255, 0), (418, 112, 109, 63), 2)
spot8 = Car_class.ParkSpot ((0, 255, 0), (1286, 119, 109, 63), 2)
spot9 = Car_class.ParkSpot ((0, 255, 0), (852, 623, 109, 63), 2)
park1 = Car_class.ParkSpot ((0, 255, 0), (934, 2, 54, 16), 1)
park2 = Car_class.ParkSpot ((0, 255, 0), (544, 308, 16, 54), 1)
park3 = Car_class.ParkSpot ((0, 255, 0), (500, 371, 16, 54), 1)
park4 = Car_class.ParkSpot ((0, 255, 0), (662, 7, 54, 16), 1)
park5 = Car_class.ParkSpot ((0, 255, 0), (537, 245, 16, 54), 1)
park6 = Car_class.ParkSpot ((0, 255, 0), (940, 238, 16, 54), 1)
park7 = Car_class.ParkSpot ((0, 255, 0), (490, 112, 16, 54), 1)
park8 = Car_class.ParkSpot ((0, 255, 0), (1356, 119, 16, 54), 1)
park9 = Car_class.ParkSpot ((0, 255, 0), (922, 623, 16, 54), 1)

#list with all parked cars
cp_list = [cp_car1, cp_car2, cp_car3, cp_car4, cp_car5, cp_car6, cp_car7, cp_car8, cp_car9, cp_car10, cp_car11,
           cp_car12, cp_car13, cp_car14, cp_car15, cp_car16, cp_car17, cp_car18, cp_car19, cp_car21, cp_car22,
           cp_car23, cp_car25, cp_car26, cp_car29, cp_car30,cp_car31, cp_car32, cp_car33, cp_car34, cp_car35, cp_car36, cp_car37, cp_car38, cp_car39, cp_car40, cp_car41,
           cp_car42, cp_car43, cp_car44, cp_car45, cp_car46, cp_car47, cp_car48, cp_car49, cp_car50,cp_car51]
#list for platform barriers
plat_list = [platform1, platform2, platform3]
#list for optional empty parking spot
park_list = [park1,park2,park3,park4,park5,park6,park7,park8,park9]

num = 2

font = pygame.font.SysFont ('comicansms', 70)
count = 0
dam_count = 0
cpmoveCount = []

#main loop
def main():
    run = True
    while run:

        scored = False
        Main_car.velocity = 18
        
        #initialing event key gets pressed
        keys = pygame.key.get_pressed ()
        clock.tick (36)
        # pygame.time.delay(10)
        
        #if you click exit at top right the game exits properly
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #when not initalizing a key prints car position for reference
            if event.type == pygame.KEYUP:
                print (Main_car.x, Main_car.y)
                Main_car.driveCount = 0
                Main_car.park = True

        #move left and use booleans to ensure the left image gets used
        if keys[pygame.K_LEFT] and Main_car.x > Main_car.velocity:
            Main_car.height = 50
            Main_car.width = 96
            Main_car.x -= Main_car.velocity
            Main_car.left = True
            Main_car.right = False
            Main_car.up = False
            Main_car.down = False

        #move left and use booleans to ensure the right image gets used
        elif keys[pygame.K_RIGHT] and Main_car.x < screen_width - Main_car.width - Main_car.velocity:
            Main_car.height = 51
            Main_car.width = 96
            Main_car.x += Main_car.velocity
            Main_car.left = False
            Main_car.right = True
            Main_car.up = False
            Main_car.down = False
            
        #move left and use booleans to ensure the up image gets used
        elif keys[pygame.K_UP] and Main_car.y > Main_car.velocity:
            Main_car.height = 93
            Main_car.width = 42
            Main_car.y -= Main_car.velocity
            Main_car.left = False
            Main_car.right = False
            Main_car.up = True
            Main_car.down = False

        #move left and use booleans to ensure the down image gets used
        elif keys[pygame.K_DOWN] and Main_car.y < screen_height - Main_car.height - Main_car.velocity:
            Main_car.height = 86
            Main_car.width = 46
            Main_car.y += Main_car.velocity
            Main_car.left = False
            Main_car.right = False
            Main_car.up = False
            Main_car.down = True

            
        draw_window ()
main()
