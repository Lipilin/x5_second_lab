"""Шаг 2. Переписываем на asyncio.

Задание 2а:
  1. Сделайте work корутиной (async def).
  2. Замените time.sleep на await asyncio.sleep.
  3. Сделайте main корутиной и вызовите в ней work через await в цикле.
  4. Запустите через asyncio.run.

Замерьте время. Изменилось ли оно по сравнению с шагом 1? Почему?

Задание 2б:
  Перепишите main так, чтобы все 10 задач ждали одновременно.
  Подсказка: asyncio.gather. Что изменилось в порядке вывода?
"""

import asyncio

from timer import print_time

N = 10

async def work(n: int) -> None:
    print(f'start {n}')
    await asyncio.sleep(1)
    print(f'done {n}')


async def main() -> None:
    for i in range(N):
      await work(i + 1)


if __name__ == "__main__":
    with print_time():
        asyncio.run(main())
