import random
import pygame

# 迷路をランダムに自動生成する
# - 迷路の壁は1、通路は0とする
# - 迷路のサイズはwidth * heightとする
# - 座標(1,1)をスタート地点とする
# - 座標(width-2,height-2)をゴール地点とする
# - 迷路の外側は壁とする
# 次の手順で迷路を生成する
# 1. 迷路サイズ(width,height)の全てを壁で埋める
# 2. 座標(1,1)を基点としてランダムに通路を掘っていく
# 3. 右下の座標(width-2,height-2)に到達したら終了する
# 4. 必ず基点から右下までの道が通るようにする


def make_maze(width, height):
    # 迷路を壁で埋める
    maze = [[1 for i in range(width)] for j in range(height)]
    # 基点を通路にする
    maze[1][1] = 0
    # 基点から右下までの道を掘る
    x = 1
    y = 1
    while x < width - 2 or y < height - 2:
        # 進む方向をランダムに決める
        direction = random.randint(0, 3)
        if direction == 0 and y < height - 2:
            # 下に進む
            y += 1
            maze[y][x] = 0
        elif direction == 1 and x < width - 2:
            # 右に進む
            x += 1
            maze[y][x] = 0
        elif direction == 2 and y > 1:
            # 上に進む
            y -= 1
            maze[y][x] = 0
        elif direction == 3 and x > 1:
            # 左に進む
            x -= 1
            maze[y][x] = 0
    # 迷路を返す
    return maze


def draw_maze(maze, player_x, player_y):
    # PyGameで迷路を表示する
    # - 迷路の壁は黒、通路は白
    # - ゴール地点は緑とする
    # 迷路の壁の色
    wall_color = (0, 0, 0)
    # 迷路の通路の色
    road_color = (255, 255, 255)
    # ゴール地点の色
    goal_color = (0, 255, 0)
    # プレイヤーの色
    player_color = (0, 0, 255)
    # プレイヤーの半径
    player_radius = 10
    # 迷路のサイズ
    width = len(maze[0])
    height = len(maze)
    wall_width = 600 // width
    wall_height = 600 // height
    # 迷路を描画する
    for y in range(height):
        for x in range(width):
            if maze[y][x] == 1:
                pygame.draw.rect(
                    screen, wall_color, (x * wall_width, y * wall_height, wall_width, wall_height))
            else:
                pygame.draw.rect(
                    screen, road_color, (x * wall_width, y * wall_height, wall_width, wall_height))
        # ゴール地点を描画する
        pygame.draw.rect(screen, goal_color, ((
            width - 2) * wall_width, (height - 2) * wall_height, wall_width, wall_height))
        # プレイヤーを描画する
        pygame.draw.circle(screen, player_color, (player_x * wall_width + wall_width //
                           2, player_y * wall_height + wall_height // 2), player_radius)
        # 画面を更新する
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Maze')
    # 迷路を生成する
    maze = make_maze(21, 21)
    # プレイヤーの座標
    player_x = 1
    player_y = 1
    # ウィンドウを閉じるまで繰り返す
    while True:
        # イベントを取得
        for event in pygame.event.get():
            # イベントが終了なら終了する
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # イベントがキーを押したなら
            if event.type == pygame.KEYDOWN:
                # キーが右なら
                if event.key == pygame.K_RIGHT:
                    # 右に移動できるなら
                    if player_x < len(maze[0]) - 2 and maze[player_y][player_x + 1] == 0:
                        # 右に移動する
                        player_x += 1
                # キーが左なら
                if event.key == pygame.K_LEFT:
                    # 左に移動できるなら
                    if player_x > 1 and maze[player_y][player_x - 1] == 0:
                        # 左に移動する
                        player_x -= 1
                # キーが下なら
                if event.key == pygame.K_DOWN:
                    # 下に移動できるなら
                    if player_y < len(maze) - 2 and maze[player_y + 1][player_x] == 0:
                        # 下に移動する
                        player_y += 1
                # キーが上なら
                if event.key == pygame.K_UP:
                    # 上に移動できるなら
                    if player_y > 1 and maze[player_y - 1][player_x] == 0:
                        # 上に移動する
                        player_y -= 1
        # 迷路を表示する
        draw_maze(maze, player_x, player_y)
        # ゴールに到達したら終了する
        if player_x == len(maze[0]) - 2 and player_y == len(maze) - 2:
            # 迷路を再生成する
            maze = make_maze(21, 21)
            # プレイヤーの座標を初期化する
            player_x = 1
            player_y = 1