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

    vx = 5
    vy = 5
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        enn_rect.move_ip(vx, vy)
        
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        screen.blit(enn, enn_rect)

        pg.display.update()
        tmr += 1
        clock.tick(50)

        if enn_rect.left > WIDTH or enn_rect.top > HEIGHT:
            enn_rect = enn.get_rect(center=(random.randint(0, WIDTH), random.randint(0, HEIGHT)))

            

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()