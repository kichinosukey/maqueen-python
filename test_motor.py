# from maqueen import (
#     activate_motor_driver,
#     move_forward,
#     move_backward,
#     turn_left,
#     turn_right,
#     stop_motors,
#     get_distance,
# )
from microbit import sleep

def test_move_forward():
    print("【テスト】前進")
    move_forward(150, 2000)
    sleep(500)

def test_move_backward():
    print("【テスト】後退")
    move_backward(150, 2000)
    sleep(500)

def test_turn_left():
    print("【テスト】左旋回")
    turn_left(150, 1500)
    sleep(500)

def test_turn_right():
    print("【テスト】右旋回")
    turn_right(150, 1500)
    sleep(500)

def main():
    # モータードライバの初期化
    activate_motor_driver()
    
    # 各動作のテスト実行
    test_move_forward()
    test_move_backward()
    test_turn_left()
    test_turn_right()

if __name__ == '__main__':
    main()