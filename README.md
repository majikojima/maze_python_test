reference:
[https://news.mynavi.jp/techplus/article/zeropython-100/]

# Usage

```bash
$ python3 -m venv myvenv
$ . myvenv/bin/activate
```

```bash
$ python3 -m pip install pygame==2.1.2
$ python maze.py
```

# Q&A

## Segmentation fault

とりあえず、以下で解決した

```bash
pip install --upgrade pygame
```

## I asked chatGPT how to make it

PythonとPygameを使用した迷路ゲームの作成について説明します。以下に20ステップに分けて説明します。

1. まずPythonとPygameがインストールされていることを確認します。Pygameはインストールが必要で、コマンドプロンプトやターミナルで `pip install pygame` を実行することでインストールできます。

2. Pythonのスクリプトファイル（例えば `maze.py`）を作成します。

3. このスクリプトファイルの最初に、以下のようにPythonの `random` モジュールと `pygame` モジュールをインポートします。

```python
import random
import pygame
```

4. 次に、迷路を生成する関数 `make_maze(width, height)` を作成します。この関数は迷路の横幅と高さを引数として受け取ります。

```python
def make_maze(width, height):
```

5. `make_maze` 関数の中で、迷路を2次元リストとして表現します。全ての要素を壁（値：1）で初期化します。

```python
    maze = [[1 for i in range(width)] for j in range(height)]
```

6. スタート地点（1,1）を通路（値：0）にします。

```python
    maze[1][1] = 0
```

7. スタート地点からスタートし、ランダムに上下左右に進みながら通路を作っていきます。ゴール地点（右下）に到達するまで続けます。

```python
    x = 1
    y = 1
    while x < width - 2 or y < height - 2:
```

8. 進む方向をランダムに選びます。0は下、1は右、2は上、3は左を表します。

```python
        direction = random.randint(0, 3)
```

9. 選んだ方向によって、それぞれ進みます。ただし、迷路の外側には出ないようにします。

```python
        if direction == 0 and y < height - 2:  # 下に進む
            y += 1
            maze[y][x] = 0
        elif direction == 1 and x < width - 2:  # 右に進む
            x += 1
            maze[y][x] = 0
        elif direction == 2 and y > 1:  # 上に進む
            y -= 1
            maze[y][x] = 0
        elif direction == 3 and x > 1:  # 左に進む
            x -= 1
            maze[y][x] = 0
    return maze
```

10.  次に、迷路を描画するための `draw_maze(maze, player_x, player_y)` 関数を作成します。

```python
def draw_maze(maze, player_x, player_y):
```

11. まず、壁、道、ゴール、プレイヤーの色を設定します。

```python
    wall_color = (0, 0, 0)  # 黒
    road_color = (255, 255, 255)  # 白
    goal_color = (0, 255, 0)  # 緑
    player_color = (0, 0, 255)  # 青
    player_radius = 10  # プレイヤーの半径
```

12. 迷路の壁と道の幅を設定します。この例では600pxの正方形のスクリーンに迷路を描くものとします。

```python
    width = len(maze[0])
    height = len(maze)
    wall_width = 600 // width
    wall_height = 600 // height
```

13. `pygame.draw.rect` を使用して、迷路の全ての壁と道を描きます。

```python
    for y in range(height):
        for x in range(width):
            if maze[y][x] == 1:  # 壁
                pygame.draw.rect(screen, wall_color, (x * wall_width, y * wall_height, wall_width, wall_height))
            else:  # 道
                pygame.draw.rect(screen, road_color, (x * wall_width, y * wall_height, wall_width, wall_height))
```

14. ゴール地点とプレイヤーを描きます。プレイヤーは円で表します。

```python
    pygame.draw.rect(screen, goal_color, ((width - 2) * wall_width, (height - 2) * wall_height, wall_width, wall_height))  # ゴール
    pygame.draw.circle(screen, player_color, (player_x * wall_width + wall_width // 2, player_y * wall_height + wall_height // 2), player_radius)  # プレイヤー
    pygame.display.update()  # 描画更新
```

15. 次に、ゲームのメインループを書きます。まず、Pygameを初期化し、スクリーンを設定します。

```python
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
```

16. タイトルを設定し、迷路とプレイヤーの初期位置を設定します。

```python
    pygame.display.set_caption('Maze')
    maze = make_maze(21, 21)
    player_x = 1
    player_y = 1
```

17.  その後、ゲームループを始めます。このループは、ゲームが終了するかプレイヤーが迷路をクリアするまで続きます。

```python
    while True:
```

18. ここで、イベントループを開始します。これはプレイヤーの入力（キーボードの矢印キー）を処理します。プレイヤーのキー入力によってプレイヤーの位置を更新し、またゲームが終了された場合は適切にゲームを終了します。

```python
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # ゲーム終了
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:  # キーボードの入力
                if event.key == pygame.K_RIGHT:  # 右矢印キー
                    if player_x < len(maze[0]) - 2 and maze[player_y][player_x + 1] == 0:
                        player_x += 1
                elif event.key == pygame.K_LEFT:  # 左矢印キー
                    if player_x > 1 and maze[player_y][player_x - 1] == 0:
                        player_x -= 1
                elif event.key == pygame.K_DOWN:  # 下矢印キー
                    if player_y < len(maze) - 2 and maze[player_y + 1][player_x] == 0:
                        player_y += 1
                elif event.key == pygame.K_UP:  # 上矢印キー
                    if player_y > 1 and maze[player_y - 1][player_x] == 0:
                        player_y -= 1
```

19. 入力に基づいてプレイヤーを移動した後、迷路を再描画します。

```python
        draw_maze(maze, player_x, player_y)
```

20. プレイヤーがゴールに到達した場合、新たに迷路を生成し、プレイヤーを初期位置に戻します。

```python
        if player_x == len(maze[0]) - 2 and player_y == len(maze) - 2:
            maze = make_maze(21, 21)
            player_x = 1
            player_y = 1
```

以上でPythonとPygameを使用した基本的な迷路ゲームの作成は終了です。これはとても基本的な例であり、例えば迷路の生成アルゴリズムを改善したり、ゲームの見た目を改善したりするなど、改良の余地はまだまだあります。