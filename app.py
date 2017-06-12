#coding: utf-8
import pygame
from pygame.locals import *
import random
import sys
import invader
import function

START, PLAY, GAMEOVER = (0, 1, 2)  # ゲーム状態
SCR_RECT = Rect(0, 0, 640, 480)
WHITE = (255,255,255)

class InvaderGame:
    """メイン"""
    def __init__(self):
        pygame.init()
        #ウインドの設定
        screen = pygame.display.set_mode(SCR_RECT.size)
        pygame.display.set_caption(u"Oikos Invader Game")
        
        # 素材のロード（メンバ関数の呼び出し）
        self.load_images()
        self.load_sounds()
        
        # ゲームオブジェクトを初期化
        # ゲーム状態(インスタンス変数の生成)
        self.game_state = START
        # スプライトグループを作成して登録(属性の追加)
        self.all = pygame.sprite.RenderUpdates()
        self.shots = pygame.sprite.Group()   # ミサイルグループクラス

        # デフォルトスプライトグループを登録
        #各クラスのクラス属性containersを設定  
        invader.Tank.containers = self.all
        invader.TankMissile.containers = self.all, self.shots

        # 自機を作成
        self.player = invader.Tank()

        # メインループ開始
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            if self.game_state == PLAY:
                self.all.update()
            self.draw(screen)
            pygame.display.update()
            self.key_handler()


    #########################################
    #InvaderGameの関数
    def draw(self, screen):
        """描画"""
        screen.fill((0, 0, 0))
        if self.game_state == START:  # スタート画面
            # タイトルを描画
            title_font = pygame.font.SysFont(None, 80)
            title = title_font.render("INVADER GAME", False, (255,0,0))
            screen.blit(title, ((SCR_RECT.width-title.get_width())/2, 100))
            # エイリアンを描画
            alien_image = invader.Invader.images[0]
            screen.blit(alien_image, ((SCR_RECT.width-alien_image.get_width())/2, 200))
            # PUSH STARTを描画
            push_font = pygame.font.SysFont(None, 40)
            push_space = push_font.render("PUSH SPACE KEY", False, (255,255,255))
            screen.blit(push_space, ((SCR_RECT.width-push_space.get_width())/2, 300))
            # クレジットを描画
            credit_font = pygame.font.SysFont(None, 20)
            credit = credit_font.render(u"2017 OIKOS_INVADER_WORKSHOP", False, (255,255,255))
            screen.blit(credit, ((SCR_RECT.width-credit.get_width())/2, 380))

        elif self.game_state == PLAY:  # ゲームプレイ画面
            self.all.draw(screen)
   
    #########################################
    #InvaderGameの関数
    def key_handler(self):
        """キーハンドラー"""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_SPACE:
                if self.game_state == START:  # スタート画面でスペースを押したとき
                    self.game_state = PLAY
                elif self.game_state == GAMEOVER:  # ゲームオーバー画面でスペースを押したとき
                    self.init_game()  # ゲームを初期化して再開
                    self.game_state = PLAY



    #########################################
    #いじるべからず
    #InvaderGameの関数
    def load_images(self):
        """必要なイメージをロードする"""
        # 各クラスのクラス属性イメージに画像を登録する
        invader.Tank.image = function.load_image("player.png")
        invader.TankMissile.image = function.load_image("shot.png")
        invader.Invader.images = function.split_image(function.load_image("alien.png"), 2)
    
    #########################################
    #いじるべからず
    #InvaderGameの関数
    def load_sounds(self):
        """サウンドのロード"""
        #各クラスのクラス属性に音声を登録する
        invader.Tank.shot_sound = function.load_sound("shot.wav")

if __name__ == "__main__":
    InvaderGame()
