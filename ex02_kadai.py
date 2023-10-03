import sys
import pygame as pg
import random


WIDTH, HEIGHT = 1600, 900

def check_bound(obj_rct: pg.Rect):
    """
    引数：こうかとんRectかばくだんRect
    戻り値：タプル（横方向判定結果，縦方向判定結果）
    画面内ならTrue，画面外ならFalse
    """
    yoko, tate = True, True
    if obj_rct.left < 0 or WIDTH < obj_rct.right: # 横方向判定
        yoko = False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom: # 縦方向判定
        tate = False
    return yoko, tate

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ProjExD2023/ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ProjExD2023/ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)

    # 加速度のリスト
    accs = [a for a in range(1, 11)]

    # 拡大爆弾Surfaceのリストを作成
    bb_imgs = []
    for r in range(1, 11):
        enn = pg.Surface((20 * r, 20 * r), pg.SRCALPHA)
        pg.draw.circle(enn, (255, 0, 0), (10 * r, 10 * r), 10 * r)
        bb_imgs.append(enn)

    enn.set_colorkey((0, 0, 0))
    
    clock = pg.time.Clock()

    tmr = 0

    # 現在の速度と大きさのインデックス
    current_speed_index = 0
    current_size_index = 0

    # 爆弾Rectを作成
    enn_rect = bb_imgs[current_size_index].get_rect(center=(100, 100))

    #こうかとんRectを作成
    kk_rect = kk_img.get_rect(center=(900, 400))


    vx = 5
    vy = 5
    
    font = pg.font.Font(None, 36)

    
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

        # 時間経過に応じて速度と大きさを更新
        tmr += 1
        current_speed_index = min(tmr // 500, 9)
        current_size_index = min(tmr // 500, 9)

        # 爆弾を速度に応じて移動
        avx, avy = vx * accs[current_speed_index], vy * accs[current_speed_index]
        enn_rect.move_ip(avx, avy)
        yoko, tate = check_bound(enn_rect)

        enn = bb_imgs[(current_size_index)]
        
        
        screen.blit(bg_img, [0, 0])

        #こうかとん画面内処理
        if check_bound(kk_rect) != (True, True):  # 練習４：はみだし判定
            kk_rect.move_ip(-total_movement[0], -total_movement[1]) 


        screen.blit(kk_img, kk_rect)


        if not yoko:  # 練習４：横方向にはみ出たら
            vx *= -1
        if not tate:  # 練習４：縦方向にはみ出たら
            vy *= -1
        
        #当たり判定
        if kk_rect.colliderect(enn_rect):
            kk_img2 = pg.image.load("ProjExD2023/ex02/fig/8.png")
            kk_img2 = pg.transform.rotozoom(kk_img2, 0, 2.0)
            screen.blit(kk_img2, kk_rect)
            pg.display.update()
            pg.time.wait(1000)
            return
           
        screen.blit(enn, enn_rect)

        time = tmr // 50
        text = font.render(f"Timer{time}", True, (255, 0, 0))
        screen.blit(text, (10,10))

        pg.display.update()
        
        clock.tick(50)

    

            

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()