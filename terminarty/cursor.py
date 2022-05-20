from typing import Optional

CSI = '\033['


class Cursor:
    @staticmethod
    def setpos(x: Optional[int] = 1, y: Optional[int] = 1) -> None:
        print(f'{CSI}{y};{x}H', end='')

    @staticmethod
    def savepos() -> None:
        print(f'\0337', end='')

    @staticmethod
    def restorepos() -> None:
        print(f'\0338', end='')

    @staticmethod
    def up(n: Optional[int] = 1) -> None:
        print(f'{CSI}{n}A', end='')

    @staticmethod
    def down(n: Optional[int] = 1) -> None:
        print(f'{CSI}{n}B', end='')

    @staticmethod
    def right(n: Optional[int] = 1) -> None:
        print(f'{CSI}{n}C', end='')

    @staticmethod
    def left(n: Optional[int] = 1) -> None:
        print(f'{CSI}{n}D', end='')

    @staticmethod
    def hide() -> None:
        print(f'{CSI}?25l', end='')

    @staticmethod
    def show() -> None:
        print(f'{CSI}?25h', end='')

    @staticmethod
    def erase_line() -> None:
        print(f'{CSI}2K')
