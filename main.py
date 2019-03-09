
# main game script controller:

# init
from scripts.__init__ import *

# matrix
from scripts.matrix import Matrix

# kelner
from scripts.waiter import Waiter

if __name__ == '__main__':
    mat = Matrix(N, N)
    mat.print_matrix()
    mat.insert_object('asdasd', 2, 4, debug=True)
    mat.insert_object(Matrix(2, 2, fill=5), 1, 1)
    mat.print_matrix()
    print(mat.objects_to_list('asdasd'))
    mat.delete_object(1, 1, debug=True)
    mat.print_matrix()

    # main game loop
    gamestate = 0

    pygame.mixer.init()
    pygame.mixer.music.load('sounds/over.mp3')

    olaf_sound = pygame.mixer.Sound('sounds/olaf.wav')

    while True:  # the main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                print(pygame.key.name(event.key))
                if event.key == K_RIGHT:
                    elsa.move_right()
                    hans.move()
                elif event.key == K_LEFT:
                    elsa.move_left()
                    hans.move()
                elif event.key == K_DOWN:
                    elsa.move_down()
                    hans.move()
                elif event.key == K_UP:
                    elsa.move_up()
                    hans.move()
                elif event.key == K_r:
                    gamestate = 0
                    pygame.mixer.music.stop()

                elif pygame.key.name(event.key) == "w":
                    elsa.move_up()

        all_sprites_list.update()

        if pygame.sprite.collide_rect(elsa, anna):
            gamestate = 1
            pygame.mixer.music.play(-1)
            elsa.reset()

        if pygame.sprite.collide_rect(elsa, hans):
            gamestate = 2
            elsa.reset()

        for olaf in olafs:
            if pygame.sprite.collide_rect(elsa, olaf):
                all_sprites_list.remove(olaf)
                olaf.rect.x = -1000
                olaf.rect.y = -1000
                olaf_sound.play()

        # game state control - win loose nothing
        if gamestate == 0:
            DISPLAYSURF.blit(background_image, (0, 0))
            all_sprites_list.draw(DISPLAYSURF)
        elif gamestate == 1:
            DISPLAYSURF.blit(gameover_image, (0, 0))
        elif gamestate == 2:
            DISPLAYSURF.blit(fail_image, (0, 0))

        # Refresh Screen
        pygame.display.flip()
        fpsClock.tick(FPS)