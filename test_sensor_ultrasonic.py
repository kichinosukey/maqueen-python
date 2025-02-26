# from maqueen import get_distance
from microbit import display, sleep

while True:
    # 距離をcm単位で計測
    distance = get_distance()
    # 計測値を四捨五入して文字列に変換（小数第1位まで表示）
    display.scroll(str(round(distance, 1)) + "cm")
    sleep(500)