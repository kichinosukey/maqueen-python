# from maqueen import get_line
from microbit import display, sleep

def main():
    """ラインセンサーの値をLEDマトリックスに表示するテストプログラム"""
    while True:
        left, right = get_line()
        message = "L:{} R:{}".format(left, right)
        display.scroll(message)
        sleep(500)

if __name__ == '__main__':
    main()