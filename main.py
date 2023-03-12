import random
from typing import List, Dict

deck = [(color, rank) for color in ('R', 'G', 'B', 'W') for rank in range(1, 11)]
players_cards: Dict[int, List[str]] = {}


def start(n: int, c: int) -> None:
    global players_cards

    if n * c > len(deck):
        print("Ошибка: недостаточно карт в колоде для раздачи.")
        return

    players_cards.clear()
    random.shuffle(deck)
    for i in range(1, c + 1):
        players_cards[i] = [f"{color}{rank}" for color, rank in deck[(i - 1) * n:i * n]]


def get_cards(c: int) -> None:
    if c <= 0:
        print(f'Ошибка: Номер игрока не может быть отрицательным или равным нулю')
        return
    elif c not in players_cards:
        print(f"Ошибка: игрок {c} не найден.")
        return

    cards = " ".join(players_cards[c])
    print(f"{c} {cards}")


if __name__ == '__main__':
    print(f'Для раздачи карт используйте команду start N C, где N - количество случайных карт, C - количество игроков \n'
          f'Для просмотра карт игрока используйте команду get-cards C, где C - номер игрока \n' 
          f'Для выхода из програмы используйте команду exit')
    while True:
        input_msg = str(input())
        list_input_msg = input_msg.split(' ')
        if list_input_msg[0] == 'start':
            start(int(list_input_msg[1]), int(list_input_msg[2]))
        elif list_input_msg[0] == 'get-cards':
            get_cards(int(list_input_msg[1]))
        elif list_input_msg[0] == 'exit':
            break
        else:
            print(f'Команда {list_input_msg[0]} не найдена!')
