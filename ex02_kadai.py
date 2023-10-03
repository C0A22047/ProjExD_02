import sys
import pygame as pg
import random


WIDTH, HEIGHT = 1600, 900





def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ProjExD2023/ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ProjExD2023/ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)

    enn = pg.Surface((20, 20), pg.SRCALPHA)
    pg.draw.circle(enn, (255, 0, 0), (10, 10), 10)
    enn.set_colorkey((0, 0, 0))
    
    clock = pg.time.Clock()

    tmr = 0

   

    enn_rect = enn.get_rect(center=(random.randint(0, WIDTH), random.randint(0, HEIGHT)))
    kk_rect = kk_img.get_rect(center=(900, 400))

    vx = 5
    vy = 5
    
    

    def is_inside(rect):
        return screen.get_rect().contains(rect)
    
    movement_dict = {
        pg.K_UP: (0, -5),    # 上矢印
        pg.K_DOWN: (0, 5),  # 下矢印
        pg.K_LEFT: (-5, 0),  # 左矢印
        pg.K_RIGHT: (5, 0)   # 右矢印
    }

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        
        key_lst = pg.key.get_pressed()

        total_movement =[0,0]

        for key, movement in movement_dict.items():
            if key_lst[key]:
                total_movement[0] += movement[0]
                total_movement[1] += movement[1]


        kk_rect.move_ip(total_movement[0], total_movement[1])
        enn_rect.move_ip(vx, vy)
        
        
        screen.blit(bg_img, [0, 0])

        if not is_inside(kk_rect):
            kk_rect.clamp_ip(screen.get_rect())


        screen.blit(kk_img, kk_rect)


        if not is_inside(enn_rect):
            vx = -vx
            vy = -vy
        
        if kk_rect.colliderect(enn_rect):
            return
           
        screen.blit(enn, enn_rect)



        pg.display.update()
        tmr += 1
        clock.tick(50)

    

            

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()