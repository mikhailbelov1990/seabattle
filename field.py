# матрица кораблей противника (компьютера)
# 0 - море
# 1 - живой корабль
# 2 - подбитый корабль
field = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# метод drawField рисует пустое игровое поле 10х10
def drawField(canvas):
    for i in range(0, 10):
        for j in range(0, 10):
            canvas.create_rectangle(i*50+2, j*50+2, i*50+51, j*50+51,
                    outline='brown', fill='white')

def placeShips():
    # ToDo: реализовать алгоритм заполнения
    # матрицы field.
    # На поле должны быть установлены корабли:
    # 4-х-палубный - 1 шт
    # 3-х-палубный - 2 шт
    # 2-х-палубный - 3 шт
    # 1-х-палубный - 4 шт
    # таким образом, чтобы они не пересекались
    # и не касались друг друга (даже углами)
    global field
    field = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# обрабатывает выстрел
# возвращает True, если попал (или повторно попал)
# и False, если не попал
def shoot(x, y, canvas):
    global field
    if (field[y][x] == 0):
        canvas.create_rectangle(
            x*50+2, y*50+2, x*50+51, y*50+51,
            outline='brown', fill='blue')
        return False
    if (field[y][x] == 1):
        field[y][x] = 2
        canvas.create_rectangle(
            x*50+2, y*50+2, x*50+51, y*50+51,
            outline='brown', fill='red')
        return True
    if (field[y][x] == 2):
        return True

# Проверяет, есть ли еще неподбитые корабли
def isGameOver():
    return False

def showGameOver():
    print("Game over")
